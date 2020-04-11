# DEVOPS-TREE-K8S
Deploy and run 'devops-tree-K8s' app in Kubernetes

## Docker
Build the images and spin up the containers:
```sh
$ docker-compose up -d --build
```
Run the migrations and seed the database:
```sh
$ docker-compose exec server python manage.py recreate_db
$ docker-compose exec server python manage.py seed_db
```
Test it out at:
1. http://localhost:8080/
1. http://localhost:5001/devops

## Kubernetes
### Minikube
Start the cluster:
```sh
$ minikube start --vm-driver=virtualbox
$ minikube dashboard
```
### Volume
Create the volume:
```sh
$ kubectl apply -f ./k8s/persistent-volume.yml
```
Create the volume claim:
```sh
$ kubectl apply -f ./kubernetes/persistent-volume-claim.yml
```
### Secrets
Create the secret object:
```sh
$ kubectl apply -f ./k8s/secret.yml
```
### Postgres
Create deployment:
```sh
$ kubectl create -f ./k8s/postgres-deployment.yml
```
Create the service:
```sh
$ kubectl create -f ./k8s/postgres-service.yml
```
Create the database:
```sh
$ kubectl get pods
$ kubectl exec postgres-<POD_IDENTIFIER> --stdin --tty -- createdb -U postgres devops
```
### Flask
Build and push the image to Docker Hub:
```sh
$ docker build -t vinaydhegde/flask-kubernetes ./services/server
$ docker push vinaydhegde/flask-kubernetes
```
>Make sure to replace 'vinaydhegde' with your Docker Hub namespace in the above commands as well as in *k8s/flask-deployment.yml*
Create the deployment:
```sh
$ kubectl create -f ./k8s/flask-deployment.yml
```
Create the service:
```sh
$ kubectl create -f ./k8s/flask-service.yml
```
Apply the migrations and seed the database:
```sh
$ kubectl get pods
$ kubectl exec flask-<POD_IDENTIFIER> --stdin --tty -- python manage.py recreate_db
$ kubectl exec flask-<POD_IDENTIFIER> --stdin --tty -- python manage.py seed_db
```
### Ingress
Enable and apply:
```sh
$ minikube addons enable ingress
$ kubectl apply -f ./k8s/minikube-ingress.yml
```
Add entry to /etc/hosts file:
```sh
<MINIKUBE_IP> devops-tree
```
Try it out: http://devops-tree/devops

### React
Build and push the image to Docker Hub:
```sh
$ docker build -t vinaydhegde/react-kubernetes ./services/client -f ./services/client/Dockerfile-minikube
$ docker push vinaydhegde/react-kubernetes
```
>Again, replace 'vinaydhegde' with your Docker Hub namespace in the above commands as well as in *k8s/react-deployment.yml*
Create the deployment:
```sh
$ kubectl create -f ./k8s/react-deployment.yml
```
Create the service:
```sh
$ kubectl create -f ./k8s/react-service.yml
```
Try it out at http://devops-tree






