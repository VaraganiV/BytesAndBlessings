---
title: "Service Oriented Architecture"
date: 2016-07-20
draft: false
categories:
  - tech
ShowToc: true
TocOpen: false
---

A **loosely-coupled architecture** designed to meet the business needs of the organization.

**Principles:**

* **Standardised service contract**: Services adhere to a communications agreement, as defined collectively by one or more service-description documents.
* **Service loose coupling**: Services maintain a relationship that minimizes dependencies and only requires that they maintain an awareness of each other.
* **Service abstraction**: Beyond descriptions in the service contract, services hide logic from the outside world.
* **Service reusability**: Logic is divided into services with the intention of promoting reuse.
* **Service autonomy**: Services have control over the logic they encapsulate, from a Design-time and a Run-time perspective.
* **Service statelessness**: Services minimize resource consumption by deferring the management of state information when necessary
* **Service discoverability**: Services are supplemented with communicative meta data by which they can be effectively discovered and interpreted.
* **Service composability**: Services are effective composition participants, regardless of the size and complexity of the composition.
* **Service granularity**: A design consideration to provide optimal scope and right granular level of the business functionality in a service operation.
* **Service normalization**: Services are decomposed or consolidated to a level of normal form to minimize redundancy. In some cases, services are denormalized for specific purposes, such as performance optimization, access, and aggregation.
* **Service optimization**: All else being equal, high-quality services are generally preferable to low-quality ones.
* **Service relevance**: Functionality is presented at a granularity recognized by the user as a meaningful service.
* **Service encapsulation:**Many services are consolidated for use under the SOA. Often such services were not planned to be under SOA.
* **Service location transparency**: This refers to the ability of a service consumer to invoke a service regardless of its actual location in the network. This also recognizes the discoverability property (one of the core principle of SOA) and the right of a consumer to access the service. Often, the idea of service virtualization also relates to location transparency. This is where the consumer simply calls a logical service while a suitable SOA-enabling runtime infrastructure component, commonly a service bus, maps this logical service call to a physical service.

</a>
</figure>

</a>
</figure>

***Microservice applications are composed of small, independently versioned, and scalable customer-focused services that communicate with each other over standard protocols with well-defined interfaces.***

The changing business needs are:

* The need to build and operate a service at scale to enable greater customer reach--into new geographical regions or without having to deploy at customer locations, for example.
* Faster delivery of features and capabilities to be able to respond to customer demands in an agile way.
* Improved resource utilization's to reduce costs.

These business needs are affecting *how* we build applications.

When companies talk about building for the cloud, the expectation is **growth and usage**. The issue is that growth and scale are unpredictable. We would like to be able to prototype quickly while also knowing that we are on a path to deal with future success. **This is the lean startup approach: build, measure, learn, iterate**.

The benefits of microservices are that each one typically encapsulates simpler business functionality, and they can be **scaled up or down, tested, deployed, and managed independently**. One important benefit of a microservice approach is that teams tend to be **more driven by business scenarios than by technology**, which the tiered approach encouraged. In practice, this means that smaller teams develop a microservice based on a customer scenario, by using any technologies they choose. In other words, the organization doesn’t need to standardize tech to maintain monoliths. Further, individual teams that own services can do what makes sense for them based on team expertise or what’s most appropriate for the problem that service is trying to solve.

The **downside of microservices comes in managing the increased number of separate entities; dealing with more complex deployments and versioning**; having more network traffic between the microservices; and the corresponding network latencies. Having lots of chatty, very granular services is a recipe for a performance nightmare.

</a>
</figure>

Ultimately, standards are what make the microservice approach work, by agreeing on how to communicate and being tolerant of only the things you need from a service, rather than rigid contracts. It is important to define these contacts up front in the design, since services are going to be updated independently of one another.

</a>
</figure>

To summarizes, **the microservice approach is to compose your application of many smaller services running in containers deployed across a cluster of machines. Each service is developed by a smaller team that focuses on a scenario, and each** **service is independently tested, versioned, deployed, and scaled****, so that the application as a whole can evolve**.

A microservices application is decomposed into independent components called “microservices,” that work in concert to deliver the application’s overall functionality. The term “microservice” emphasizes the fact that applications should be composed of services small enough to truly reflect independent concerns such that each microservice implements a single function. Moreover, each has well-defined contracts (API contracts) – typically RESTful - for other microservices to communicate and share data with it. Microservices must also be able to version and update independently of each other. This loose coupling is what supports the rapid and reliable evolution of an application. Figure 3 shows how a monolithic application might be broken into different microservices.

</a>
</figure>

The independent, distributed nature of microservice-based applications also enables rolling updates, where only a subset of the instances of a single microservice will update at any given time. If a problem is detected, a buggy update can be “rolled back,” or undone, before all instances update with the faulty code or configuration. If the update system is automated, integration with **Continuous Integration (CI) and Continuous Delivery (CD) pipelines allow developers to safely and frequently** evolve the application without fear of impacting availability.