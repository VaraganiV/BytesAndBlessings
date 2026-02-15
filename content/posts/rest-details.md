---
title: "REST | Details"
description: "A detailed guide to REST APIs — principles, HTTP methods, status codes, HATEOAS, versioning, and best practices for building web services."
date: 2016-07-22
draft: false
categories:
  - tech
ShowToc: true
TocOpen: false
tags:
  - rest
  - api
  - web
cover:
  image: "/images/covers/rest-details-cover.svg"
  alt: "Cover image"
  relative: false
---

## REST Principles

While REST stands for Representational State Transfer, which is an architectural style for networked hypermedia applications, it is primarily used to build Web services that are lightweight, maintainable, and scalable. A service based on REST is called a RESTful service. REST is not dependent on any protocol, but almost every RESTful service uses HTTP as its underlying protocol.

## Representations

A resource can consist of other resources. While designing a system, the first thing to do is identify the resources and determine how they are related to each other.

This is similar to the first step of designing a database: Identify entities and relations.

## Messages

The client and service talk to each other via messages. Clients send a request to the server, and the server replies with a response.

## HTTP Request

An HTTP request has the format shown in Figure 1:

<figure>
<a href="cid:1d2dc08cb7cdb27f0edf37e8032319f6 "REST"" target="_blank">

<figure>
<a href="cid:1d2dc08cb7cdb27f0edf37e8032319f6 " target="_blank">
<img src="cid:1d2dc08cb7cdb27f0edf37e8032319f6 " alt="REST" loading="lazy" style="max-width:100%; width:480px; height:auto; border-radius:8px; cursor:zoom-in;" />
</a>
</figure>

</a>
</figure>

### GET Request Example

`GET http://www.w3.org/Protocols/rfc2616/rfc2616.html HTTP/1.1`

`Host: www.w3.org`

`Accept: text/html,application/xhtml+xml,application/xml; …`

`User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 …`

`Accept-Encoding: gzip,deflate,sdch`

`Accept-Language: en-US,en;q=0.8,hi;q=0.6`

## HTTP Response

<figure>
<a href="cid:d19bd3f5cb5b6b022e96cc72d29034c0 "REST"" target="_blank">

<figure>
<a href="cid:d19bd3f5cb5b6b022e96cc72d29034c0 " target="_blank">
<img src="cid:d19bd3f5cb5b6b022e96cc72d29034c0 " alt="REST" loading="lazy" style="max-width:100%; width:480px; height:auto; border-radius:8px; cursor:zoom-in;" />
</a>
</figure>

</a>
</figure>

### Response Format

The server returns `<response code>`, which contains the status of the request. This response code is generally the [3-digit HTTP status code](http://en.wikipedia.org/wiki/List_of_HTTP_status_codes).

`<Response Header>`contains the metadata and settings about the response message.

`<Response Body>`contains the representation if the request was successful.

Listing Five is the actual response I received for the request cited in Listing Three:

An actual response to a GET request..

`HTTP/1.1 200 OK`

`Date: Sat, 23 Aug 2014 18:31:04 GMT`

`Server: Apache/2`

`Last-Modified: Wed, 01 Sep 2004 13:24:52 GMT`

`Accept-Ranges: bytes`

`Content-Length: 32859`

`Cache-Control: max-age=21600, must-revalidate`

`Expires: Sun, 24 Aug 2014 00:31:04 GMT`

`Content-Type: text/html; charset=iso-8859-1`

`<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">`

`<``html` `xmlns``=``'http://www.w3.org/1999/xhtml'``>`

`<``head``><``title``>Hypertext Transfer Protocol -- HTTP/1.1</``title``></``head``>`

`<``body``>`

REST requires each resource to have at least one URI. A RESTful service uses a directory hierarchy like human readable URIs to address its resources.

The job of a URI is to identify a resource or a collection of resources. The actual operation is determined by an HTTP verb. The URI should not say anything about the operation or action.

This enables us to call the same URI with different HTTP verbs to perform different operations.Suppose we have a database of persons and we wish to expose it to the outer world through a service.

A resource `person` can be addressed like this:

`http://MyService/Persons/1`

**Uniform Interface**

RESTful systems should have a uniform interface. HTTP 1.1 provides a set of methods, called verbs, for this purpose. Among these the more important verbs are:

|  |  |  |
| --- | --- | --- |
| **Method** | **Operation performed on server** | **Quality** |
| `GET` | Read a resource. | Safe |
| `PUT` | Insert a new resource or update if the resource already exists. | Idempotent |
| `POST` | Insert a new resource. Also can be used to update an existing resource. | N/A |
| `DELETE` | Delete a resource . | Idempotent |
| `OPTIONS` | List the allowed operations on a resource. | Safe |
| `HEAD` | Return only the response headers and no response body. | Safe |

A Safe operation is an operation that does not have any effect on the original value of the resource. For example, the mathematical operation "divide by 1" is a safe operation because no matter how many times you divide a number by 1, the original value will not change. An Idempotent operation is an operation that gives the same result no matter how many times you perform it. For example, the mathematical operation "multiply by zero" is idempotent because no matter how many times you multiply a number by zero, the result is always same. Similarly, a Safe HTTP method does not make any changes to the resource on the server. An Idempotent HTTP method has same effect no matter how many times it is performed. Classifying methods as Safe and Idempotent makes it easy to predict the results in the unreliable environment of the Web where the client may fire the same request again.

**Difference between PUT and POST**

The short descriptions of these two methods I provided above are almost the same. These two methods confuse a lot of developers. So let's discuss these separately.

The key difference between `PUT` and `POST` is that `PUT` is idempotent while `POST` is not. No matter how many times you send a `PUT` request, the results will be same. `POST` is not an idempotent method.

Making a `POST` multiple times may result in multiple resources getting created on the server.

Another difference is that, with `PUT`, you must always specify the complete URI of the resource. This implies that the client should be able to construct the URI of a resource even if it does not yet exist on the server. This is possible when it is the client's job to choose a unique name or ID for the resource, just like creating a user on the server requires the client to choose a user ID. If a client is not able to guess the complete URI of the resource, then you have no option but to use`POST`.

|  |  |
| --- | --- |
| **Request** | **Operation** |
| `PUT http://MyService/Persons/` | Won't work. `PUT` requires a complete URI |
| `PUT http://MyService/Persons/1` | Insert a new person with `PersonID=1` if it does not already exist, or else update the existing resource |
|  |
| `POST http://MyService/Persons/` | Insert a new person every time this request is made and generate a new `PersonID`. |
| `POST http://MyService/Persons/1` | Update the existing person where `PersonID=1` |

**Statelessness**

A RESTful service is stateless and does not maintain the application state for any client. A request cannot be dependent on a past request and a service treats each request independently. HTTP is a stateless protocol by design and you need to do something extra to implement a stateful service using HTTP. But it is really easy to implement stateful services with current technologies. We need a clear understanding of a stateless and stateful design so that we can avoid misinterpretation.

A stateless design looks like so:

Request1: `GET http://MyService/Persons/1 HTTP/1.1`

Request2: `GET http://MyService/Persons/2 HTTP/1.1`

Each of these requests can be treated separately.

A stateful design, on the other hand, looks like so:

Request1: `GET http://MyService/Persons/1 HTTP/1.1`

Request2: `GET http://MyService/NextPerson HTTP/1.1`

To process the second request, the server needs to remember the last `PersonID` that the client fetched. In other words, the server needs to remember the current state — otherwise Request2 cannot be processed. Design your service in a way that a request never refers to a previous request. Stateless services are easier to host, easy to maintain,

and more scalable. Plus, such services can provide better response time to requests, as it is much easier to load balance them.

**Query Parameters in URI**

The preceding URI is constructed with the help of a query parameter:

`http://MyService/Persons?id=1`

The query parameter approach works just fine and REST does not stop you from using query parameters.

**Caching**

Caching is the concept of storing the generated results and using the stored results instead of generating them repeatedly if the same request arrives in the near future.

This can be done on the client, the server, or on any other component between them, such as a proxy server. Caching is a great way of enhancing the service performance, but if not managed properly,

it can result in client being served stale results.

Caching can be controlled using these HTTP headers:

|  |  |
| --- | --- |
| **Header** | **Application** |
| `Date` | Date and time when this representation was generated. |
| `Last Modified` | Date and time when the server last modified this representation. |
| `Cache-Control` | The HTTP 1.1 header used to control caching. |
| `Expires` | Expiration date and time for this representation. To support HTTP 1.0 clients. |
| `Age` | Duration passed in seconds since this was fetched from the server. Can be inserted by an intermediary component. |

Values of these headers can be used in combination with the directives in a `Cache-Control`header to check if the cached results are still valid or not. The most common directives for`Cache-Control` header are:

**Documenting a RESTful Service**

This is a simple and short document that contains all the aspects of `MyService` and should be sufficient for developing a client.  
Service Name: MyService  
Address: [http://MyService/](http://myservice/)

|  |  |  |  |
| --- | --- | --- | --- |
| **Resource** | **Methods** | **URI** | **Description** |
| Person | `GET,POST,PUT, DELETE` | [http://MyService/Persons/{PersonID}](http://myservice/Persons/%7BPersonID%7D) | Contains information about a person  {`PersonID`} is optional  **Format:** text/xml |
| Club | `GET,POST,PUT` | [http://MyService/Clubs/{ClubID}](http://myservice/Clubs/%7BClubID%7D) | Contains information about a club. A club can be joined my multiple people  {`ClubID`} is optional  **Format:** text/xml |
| Search | `GET` | [http://MyService/Search](http://myservice/Search)? | Search a person or a club  **Format:** text/xml  **Query Parameters:**  Name: String, Name of a person or a club  Country: String, optional, Name of the country of a person or a club  Type**:**String, optional, Person or Club. If not provided then search will result in both Person and Cubs |

You may also like to document the representations of each resource and provide some sample representations.

Transport Layer Security (TLS) 1.0 / Secure Sockets Layer (SSL) 3.0, is the mechanism to provide private, secured and reliable communication over the internet. It is the most widely used protocols that provides secure *HTTPS*for internet communications between the client (web browsers) and web servers. It ensures that the transport of sensitive data are safe from cyber crimes which steals valuable client information. TLS/SSL enables server authentication, client authentication, data encryption, and data integrity over internet. Earlier most of the payment based web applications were involved in secured communication to prevent hacking and keep the critical payment information safe. The disadvantage of SSL is the performance hit. Since the data passed over the secured layer has to be encrypted by the server it uses more server resources than the unencrypted communication. However in recent days with faster internet most of the authentication based web applications prefer secured HTTPS. E.g. Google, Facebook, Twitter etc. and HTTPS is not limited to e-commerce or banking websites only.

What is the difference between TLS and SSL?

There are subtle differences between TLS and SSL. TLS is the successor to the SSL but TLS 1.2 cannot be interchangeable with SSL 3.0. TLS uses Hashing for Message Authentication Code (HMAC) algorithm over the SSL Message Authentication Code (MAC) algorithm.

HMAC is more secured than the standard SSL MAC algorithm

| No. | SOAP | REST |
| --- | --- | --- |
| 1) | SOAP is a **protocol**. | REST is an **architectural style**. |
| 2) | SOAP stands for **Simple Object Access Protocol**. | REST stands for **REpresentational State Transfer**. |
| 3) | SOAP **can't use REST** because it is a protocol. | REST **can use SOAP** web services because it is a concept and can use any protocol like HTTP, SOAP. |
| 4) | SOAP **uses services interfaces to expose the business logic**. | REST **uses URI to expose business logic**. |
| 5) | **JAX-WS** is the java API for SOAP web services. | **JAX-RS** is the java API for RESTful web services. |
| 6) | SOAP **defines standards**to be strictly followed. | REST does not define too much standards like SOAP. |
| 7) | SOAP **requires more bandwidth** and resource than REST. | REST **requires less bandwidth** and resource than SOAP. |
| 8) | SOAP **defines its own security**. | RESTful web services **inherits security measures** from the underlying transport. |
| 9) | SOAP **permits XML** data format only. | REST **permits different** data format such as Plain text, HTML, XML, JSON etc. |
| 10) | SOAP is **less preferred** than REST. | REST **more preferred** than SOAP. |

References:

<https://www.drdobbs.com/web-development/restful-web-services-a-tutorial/240169069>

<http://www.siteforinfotech.com/2012/11/secure-socket-layer-ssl.html>

<http://idiotechie.com/understanding-transport-layer-security-secure-socket-layer/>