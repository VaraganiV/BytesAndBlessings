---
title: "Kubernetes Learning Path – ReplicaSet"
description: "Kubernetes ReplicaSets maintain a stable set of replica Pods. Learn how they ensure availability and handle pod failures automatically."
date: 2020-09-12
draft: false
categories:
  - tech
ShowToc: true
TocOpen: false
tags:
  - kubernetes
  - devops
  - replicaset
cover:
  image: "/images/covers/kubernetes-learning-path-replicaset-cover.svg"
  alt: "Cover image"
  relative: false
---

## What Is a ReplicaSet?

A ReplicaSet's purpose is to maintain a stable set of replica Pods running at any given time. It is often used to guarantee the availability of a specified number of identical Pods.

A ReplicaSet is defined with fields, which includes a selector that specifies how to identify Pods it can acquire, a number of replicas indicating how many Pods it should be maintaining, and a pod template specifying the data of new Pods it should create to meet the number of replicas criteria.

A ReplicaSet then fulfills its purpose by creating and deleting Pods as needed to reach the desired number. When a ReplicaSet needs to create new Pods, it uses its Pod template.

## When to Use a ReplicaSet

A ReplicaSet ensures that a specified number of pod replicas are running at any given time. However, a Deployment is a higher-level concept that manages ReplicaSets and provides declarative updates to Pods along with a lot of other useful features. Therefore, we recommend using Deployments instead of directly using ReplicaSets, unless you require custom update orchestration or don't require updates at all.

## Example

```
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: frontend
  labels:
    app: bookingapps
    tier: frontend
spec:
  # modify replicas according to your case
  replicas: 3
  selector:
    matchLabels:
      tier: frontend
  template:
    metadata:
      labels:
        tier: frontend
    spec:
      containers:
      - name: php-redis
```

You can get the current ReplicaSets:

`kubectl get rs`

You can check the state of the ReplicaSet:

`kubectl describe rs/<label>`

## Alternatives to ReplicaSet

Deployment **(recommended)** is a mechanism to orchestrate Pod creation, deletion and updates. When you use Deployments you don't have to worry about managing the ReplicaSets that they create. Deployments own and manage their ReplicaSets.

## ReplicationController

ReplicaSets are the successors to ReplicationControllers. ReplicationController does not support set-based selector requirements (The set-based label selector is a general form of equality since environment=production is equivalent to environment in (production)). As such, ReplicaSets are preferred over ReplicationControllers