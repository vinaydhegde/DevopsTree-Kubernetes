# Run a microservice in Kubernetes
Deploy and Run *DevopsTree* app in Kubernetes.
*DevopsTree* is a Flask based Microservice (along with Postgres & React.js) developed for demoing Kuberenetes.


Dependencies:
1. Docker Engine - CE: Client: v19.03.8, Server: v19.03.8
1. Kubectl: v1.18.0
1. Minikube: v1.9.2
1. Oracle VirtualBox: v6.1

Install all the above software on a physical machine or on a VM. 
This is tested on Ubuntu which was installed on a Virtual Machine. i.e.
1. Installed Ubuntu on a Windows physical host using Oracle Virtual Box.
1. On the Ubuntu VM, installed all the above software ('Oracle Virtual Box' for minikube to create a Node, Kubectl & minikube)

### Clone the software
```sh
$ git clone https://github.com/vinaydhegde/DevopsTree-Kubernetes ~/DevopsTree-Kubernetes
```

### Minikube
Start the cluster:
```sh
$ cd ~/DevopsTree-Kubernetes
$ minikube start --driver=docker
$ minikube dashboard
```
>Note: Since I have VirtualBox installed on a VirtaulBox, I am am using '--driver=docker'. If your minikube is directly installed on a physical machine & if you are going to create a minikube node on a Oracle VirtualBox, then use '--driver=virtualbox'

### Secrets
Create the secret object:
```sh
$ kubectl apply -f ./k8s/devopstree-secret.yml
```

### Volume
Create the volume:
```sh
$ kubectl apply -f ./k8s/devopstree-pv.yml
```

### Create the volume claim:
```sh
$ kubectl apply -f ./k8s/devopstree-pvc.yml
```
### Postgres (DB)
Create deployment:
```sh
$ kubectl create -f ./k8s/devopstree-deployment-postgres.yml
```
Create the service:
```sh
$ kubectl create -f ./k8s/devopstree-service-postgres.yml
```
Create the database:
```sh
$ kubectl get pods
$ kubectl exec devopstree-postgres<POD_IDENTIFIER> --stdin --tty -- createdb -U devopstree-demo devopstree
 ```
>Here, 
>*devopstree_demo*: is user name/login for the postgres DB 
>*devopstree*: is the DB name

### Flask (Server)
Build and push the image to Docker Hub:
```sh
$ docker build -t vinaydhegde/devopstree-flask ./services/server
$ docker push vinaydhegde/devopstree-flask
```
>Replace 'vinaydhegde' with your Docker Hub namespace in the above commands as well as in *k8s/devopstree-deployment-flask.yml*

Create the deployment:
```sh
$ kubectl create -f ./k8s/devopstree-deployment-flask.yml
```
Create the service:
```sh
$ kubectl create -f ./k8s/devopstree-service-flask.yml
```
Apply the migrations and bootsrap the database with initial content:
```sh
$ kubectl get pods
$ kubectl exec devopstree-flask-<POD_IDENTIFIER> --stdin --tty -- python manage.py recreate_db
$ kubectl exec devopstree-flask-<POD_IDENTIFIER> --stdin --tty -- python manage.py boostrap_db
```
### Ingress 
(An API object in Kubernetes to expose HTTP/HTTPs routes).

Enable and apply:
```sh
$ minikube addons enable ingress
$ kubectl apply -f ./k8s/devopstree-minikube-ingress.yml
```
Add entry to /etc/hosts file:
```sh
<MINIKUBE_IP> devops-tree
```
>Use the command *'minikube ip'* to get IP of the minikube cluster

Try it out: http://devops-tree/devopstree

### React (Client)
Build and push the image to Docker Hub:
```sh
$ docker build -t vinaydhegde/devopstree-react ./services/client -f ./services/client/Dockerfile-k8s
$ docker push vinaydhegde/devopstree-react
```
>Again, replace 'vinaydhegde' with your Docker Hub namespace in the above commands as well as in *k8s/devopstree-deployment-react.yml*
Create the deployment:
```sh
$ kubectl create -f ./k8s/devopstree-deployment-react.yml
```
Create the service:
```sh
$ kubectl create -f ./k8s/devopstree-service-react.yml
```
Try it out at http://devops-tree






