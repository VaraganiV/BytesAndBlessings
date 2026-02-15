---
title: "Kubernetes Learning Path – Deployments"
description: "Kubernetes Deployments explained — declarative updates, rolling deployments, rollbacks, and managing application lifecycle at scale."
date: 2020-09-18
draft: false
categories:
  - tech
ShowToc: true
TocOpen: false
---

## What Is a Deployment?

A Kubernetes deployment is a resource object in Kubernetes that provides declarative updates to applications. A deployment allows you to describe an application’s life cycle, such as which images to use for the app, the number of pods there should be, and the way in which they should be updated.

## Creating a Deployment

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

```
kubectl apply -f https://k8s.io/examples/controllers/nginx-deployment.yaml
kubectl get deployments
kubectl rollout status deployment.v1.apps/nginx-deployment
```

## Updating a Deployment

```
kubectl describe deployments
kubectl edit deployment.v1.apps/nginx-deployment
```

## Rolling Back a Deployment

Sometimes, you may want to rollback a Deployment

```
kubectl rollout status deployment.v1.apps/nginx-deployment
kubectl describe deployment
kubectl rollout history deployment.v1.apps/nginx-deployment
kubectl rollout undo deployment.v1.apps/nginx-deployment
```

## Scaling a Deployment

You can scale a Deployment by using the following command:

```
kubectl scale deployment.v1.apps/nginx-deployment --replicas=10
kubectl autoscale deployment.v1.apps/nginx-deployment --min=10 --max=15 --cpu-percent=80
```

## Pausing and Resuming a Deployment

```
kubectl rollout pause deployment.v1.apps/nginx-deployment
kubectl rollout history deployment.v1.apps/nginx-deployment
```

## Deployment Status

A Deployment enters various states during its lifecycle. It can be progressing while rolling out a new ReplicaSet, it can be complete, or it can fail to progress.

## Failed Deployments

* Insufficient quota
* Readiness probe failures
* Image pull errors
* Insufficient permissions
* Limit ranges
* Application runtime misconfiguration