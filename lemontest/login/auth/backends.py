from django.contrib.auth.backends import RemoteUserBackend
from django.contrib.auth import get_user_model


class LemonldapUserBackend(RemoteUserBackend):

    create_unknown_user = True

    def authenticate(self, request, lemonldap_user):
        if not lemonldap_user:
            return
        
        user = None
        username = self.clean_username(lemonldap_user['username'])
        
        UserModel = get_user_model()
        
        if self.create_unknown_user:
            user, created = UserModel.objects.get_or_create(**{UserModel.USERNAME_FIELD: username})
            if created:
                user = self.configure_user(user, lemonldap_user)
        else:
            try:
                user = UserModel.objects.get_by_natural_key(username)
            except UserModel.DoesNotExist:
                pass
        return user

    def clean_username(self, username):
        return username

    def configure_user(self, user, user_infos):
        if user_infos['mail']: user.email = user_infos['mail']
        if user_infos['firstname']: user.first_name = user_infos['firstname']
        if user_infos['lastname']: user.last_name = user_infos['lastname']
        user.is_superuser = 'true' == user_infos['is_superuser'] or user_infos['is_superuser'] is True
        user.is_staff = 'true' == user_infos['is_staff'] or user_infos['is_staff'] is True
        user.save()
        return user
