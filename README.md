# SPIKELemonldap
# Is the community active?
Yes, the community is active on GitLab. However, there are'nt videos to serve as a guide or the documentation is very old in some cases like the Django's connector or the LemonLDAP::NG in Kubernetes.

https://gitlab.ow2.org/lemonldap-ng

# Can use authentication with google?
Yes, we can use authentication with Google

https://lemonldap-ng.org/documentation/2.0/authopenidconnect_google.html

# Has an authorization scheme?
Yes, it has an authorization scheme

https://lemonldap-ng.org/documentation/2.0/authcombination.html

# Can deploy it in a kubernetes cluster?
Yes, it can be deployed in Kubernetes, but the documentation on the official LemonLDAP page is 5 years ago and causes several incompatibility problems with the current versions, and although some initial problems can be solved, more and more errors appeared, which makes it difficult to deploy it in Kubernetes.

https://github.com/LemonLDAPNG/lemonldap-ng-docker

# Simple app
# Requirements
1. Python: 3.8.2
2. Django: 4.0.2
3. Docker
4. Kubernetes
5. Minikube
# Start Project
1. Create  and activate a virtual environment
```
python3 -m venv ‘name of virtual environment’
```
2. Activate a virtual environment:
```
source ‘name of virtual environment’/bin/activate
```
3. Clone the repository
```
git clone https://github.com/kjduy/SPIKELemonldap.git
```
4. Install the libraries
```
pip install django-lemonldap
pip install django-allauth
```
5. Create an admin
Go to the manage.py file and write:
```
python manage.py createsuperuser
```
And then you will have to type the username and password
6. Run the project
```
python manage.py migrate
python manage.py runserver
```
# Create the Social Application to use the Authentication with Google
Then you need to go to the following endpoint: 

http://127.0.0.1:8000/admin/ 

It is necessary to access the previously created user and once inside, a new Social Application must be created with the Google provider, for this it is necessary to create the OAuth credentials from the Google Cloud console to obtain the ‘client id’ and the ‘secret key’.

Once the new Social Application has been created, we must click on log out and go to the following endpoint: 

http://127.0.0.1:8000/accounts/login/

# Containerize the application 
Build a docker image to upload the Django application
```
docker build --tag ‘docker image name’ .
```
Run the docker image just created
```
docker run --publish 8000:8000 ‘docker image name’
```
Create another docker image to upload the LemonLDAP::NG
```
docker build --rm -t ‘yourname’/lemonldap-ng:’version’ .
```
And finally, to deploy the application in Kubernetes, it is necessary to perform the steps found on the next page before Create an Ingress:

https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/ 

It is important to follow the steps with the docker image LemonLDAP::NG that was previously created.
And when you get the minikube web service url you need to include the following ‘ALLOWED_HOSTS’ key with the minikube web service url inside the Django application's settings.py file.
