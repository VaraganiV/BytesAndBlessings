---
title: "Kubernetes Learning Path - Pods"
description: "What are Kubernetes Pods? The smallest deployable units — understanding pod lifecycle, multi-container pods, networking, and storage."
date: 2020-09-05
draft: false
categories:
  - tech
ShowToc: true
TocOpen: false
tags:
  - kubernetes
  - devops
  - pods
cover:
  image: "/images/covers/kubernetes-learning-path-pods-cover.svg"
  alt: "Cover image"
  relative: false
---

## What Are Pods?

Pods are the smallest deployable units of computing that you can create and manage in Kubernetes. A pod can be a group of one or more containers with shared storage and network resources.

## Pod Template

Let's look at the POD template:

```
apiVersion: batch/v1
kind: Job
metadata:
  name: hello
spec:
  template:
    # This is the pod template
    spec:
      containers:
      - name: hello
        image: busybox
        command: ['sh', '-c', 'echo "Hello !" && sleep 3600']
      restartPolicy: OnFailure
    # The pod template ends here
```

## Pod Lifecycle

Following is the high level summary of pod lifecycle

|  |  |
| --- | --- |
| **Pending** | The Pod has been accepted by the Kubernetes cluster, but one or  more of the containers has not been set up and made ready to run |
| **Running** | The Pod has been bound to a node, and all of the containers  have been created. |
| **Succeded** | All containers in the Pod have terminated in success, and will not be restarted. |
| **Failed** | All containers in the Pod have terminated, and at least one  container has terminated in failure. |
| **Unknown** | For some reason the state of the Pod could not be obtained. |

## Container States

What about the state of the container in side POD, Yes Kubernetes tracks the state of each container inside a Pod. Once the scheduler assigns a Pod to a Node, the kubelet starts creating containers for that Pod using a container runtime. There are three possible container states:

**Waiting**

A container is in the waiting state, if its still running the operations in order to complete start up.

**Running**

The Running status indicates that a container is executing without issues.

**Terminated**

A container in the `Terminated` state began execution and then either ran to completion or failed for some reason.

## Container Restart Policy

The spec of a Pod has a restartPolicy field with possible values Always, OnFailure, and Never. The default value is Always. The restartPolicy applies to all containers in the Pod.

## Pod Condition

A Pod has a PodStatus, which has an array of PodConditions through which the Pod has or has not passed. Pod condition can be one of the: PodScheduled, ContainersReady, Initialized and Ready

## Pod Readiness

We can inject extra feedback or signals to get the pod status: Pod Readiness. To use this we need to set **readinessGates** in the spec

## Container Probe

To probe the health of a container, Kubelet periodically calls handler implemented by the container. There are three types of Handlers

* **ExecAction** - Execute a command inside the container. Diagnostic is successful if the return value 0.
* **PSocketAction** - Perform check against a port. Diagnostic is successful if the port is open
* **HttpGetAction** - Perform get request against a URL, Diagnostic is successful if the http code is 200

The kubelet can optionally perform and react to three kinds of probes on running containers:

* `livenessProbe`: Indicates whether the container is running. If the liveness probe fails, the kubelet kills the container. If a Container does not provide a liveness probe, the default state is `Success`.
* `readinessProbe`: Indicates whether the container is ready to respond to requests. If the readiness probe fails.. If a Container does not provide a readiness probe, the default state is `Success`.
* `startupProbe`: Indicates whether the application within the container is started. All other probes are disabled if a startup probe is provided, until it succeeds. If a Container does not provide a startup probe, the default state is `Success`.

**When to use liveness probe**  
If you'd like your container to be killed and restarted if a probe fails, then specify a liveness probe, and specify a `restartPolicy` of Always or OnFailure.

**When to use readiness probe**  
If you want your container to be able to take itself down for maintenance, you can specify a readiness probe that checks an endpoint specific to readiness that is different from the liveness probe.

**When to use startup probe**  
Startup probes are useful for Pods that have containers that take a long time to come into service. Rather than set a long liveness interval, you can configure a separate configuration for probing the container as it starts up, allowing a time longer than the liveness interval would allow.

## Termination of Pods

The container runtime sends a TERM signal to the main process in each container. Once the grace period has expired, the KILL signal is sent to any remaining processes, and the Pod is then deleted from the API Server. If the kubelet or the container runtime's management service is restarted while waiting for processes to terminate, the cluster retries from the start including the full original grace period.

## Forced Pod Termination

When a force deletion is performed, the API server does not wait for confirmation from the kubelet that the Pod has been terminated on the node it was running on. It removes the Pod in the API immediately so a new Pod can be created with the same name. On the node, Pods that are set to terminate immediately will still be given a small grace period before being force killed.

## Garbage Collection of Failed Pods

The control plane cleans up terminated Pods, when the number of Pods exceeds the configured threshold. This avoids a resource leak as Pods are created and terminated over time.

We will explore kubernetes Controllers in next post .....