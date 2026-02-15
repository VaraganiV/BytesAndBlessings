---
title: "Kuberneties Learning Path - Components"
date: 2020-09-05
draft: false
categories:
  - tech
ShowToc: true
TocOpen: false
---

When we deploy Kubernetes, we get a cluster. A Kubernetes cluster consists of a set of worker machines Nodes, that run containerised applications

Kubernetes is configured on one or more Nodes. Node is a machine physical or virtual on which kubernetes is installed. A Node is a worker machine and this is where containers are hosted.

The Master is another node with Kubernetes installed in it, and is configured as a Master. The master watches over the nodes in the cluster and is responsible for the actual orchestration of containers on the worker nodes.

A cluster is a set of nodes grouped together. This way even if one Node fails you have  
your application still accessible from the other nodes.

[
<figure>
<a href="https://d33wubrfki0l68.cloudfront.net/2475489eaf20163ec0f54ddc1d92aa8d4c87c96b/e7c81/images/docs/components-of-kubernetes.svg" target="_blank">

<figure>
<a href="https://d33wubrfki0l68.cloudfront.net/2475489eaf20163ec0f54ddc1d92aa8d4c87c96b/e7c81/images/docs/components-of-kubernetes.svg" target="_blank">
<img src="https://d33wubrfki0l68.cloudfront.net/2475489eaf20163ec0f54ddc1d92aa8d4c87c96b/e7c81/images/docs/components-of-kubernetes.svg" alt="Components of Kubernetes" loading="lazy" style="max-width:100%; width:480px; height:auto; border-radius:8px; cursor:zoom-in;" />
</a>
</figure>

</a>
</figure>
](https://d33wubrfki0l68.cloudfront.net/2475489eaf20163ec0f54ddc1d92aa8d4c87c96b/e7c81/images/docs/components-of-kubernetes.svg)

Source

Lets understand some core components of the Kubernetes

API Server

API server acts as the front-end for kubernetes. The users, management devices,  
Command line interfaces all talk to the API server to interact with the kubernetes  
cluster

etcd

etcd is a distributed reliable key-value store used by kubernetes to store all data used to manage the cluster.

Scheduler

The scheduler is responsible for distributing work or containers across multiple nodes.

Controller

The controllers are the brain behind orchestration. They are responsible for noticing and responding when nodes, containers or endpoints goes down.

kubelet

kubelet is the agent that runs on each node in the cluster. The agent is responsible for making sure that the containers are running on the nodes as expected.

kube-proxy

kube-proxy is a network proxy that runs on each node in your cluster, It takes care of networking within Kubernetes.

POD

The containers are encapsulated into a Kubernetes object known as PODs. A POD is a single instance of an application. A POD is the smallest object, that you can create in kubernetes.

In the next post, we will explore kubernetes Pods