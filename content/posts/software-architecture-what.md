---
title: "Software Architecture | What"
description: "Software architecture fundamentals — defining structured solutions that balance technical requirements with quality attributes like performance and security."
date: 2016-07-22
draft: false
categories:
  - tech
ShowToc: true
TocOpen: false
tags:
  - architecture
  - software-design
cover:
  image: "/images/covers/software-architecture-what-cover.svg"
  alt: "Cover image"
  relative: false
---

Software application architecture is the process of defining
a structured solution that **meets all of
the technical and operational requirements, while optimizing common quality
attributes such as performance, security, and manageability**.

Systems should be designed with consideration for the user,
the system (the IT infrastructure), and the business goals. For each of these
areas, you should outline key scenarios and identify important quality
attributes (for example, reliability or scalability) and key areas of
satisfaction and dissatisfaction. Where possible, develop and consider metrics
that measure success in each of these areas.

### Consider the following high level concerns when thinking about software architecture:

·     
How will the users be using the application?

·     
How will the application be deployed into
production and managed?

·     
What are the quality attribute requirements for
the application, such as security, performance, concurrency,
internationalization, and configuration?

·     
How can the application be designed to be
flexible and maintainable over time?

·     
What are the architectural trends that might
impact your application now or after it has been deployed?

### The Goals of Architecture

·     
Application architecture seeks to build a **bridge between business requirements and
technical requirements** by understanding use cases, and then finding ways to
implement those use cases in the software.

·     
The goal of architecture is to identify the
requirements that affect the structure of the application.

·     
Good architecture reduces the **business risks associated** with building
a technical solution.

·     
A good design is sufficiently flexible to be
able to handle the natural drift that will occur over time in hardware and
software technology, as well as in user scenarios and requirements.

·     
An architect must consider the overall effect of
design decisions, the inherent tradeoffs between quality attributes (such as
performance and security), and the tradeoffs required to address user, system,
and business requirements

### The Principles of Architecture Design

Create your architecture with this evolution in mind so that
it will be able to adapt to requirements that are not fully known at the start
of the design process. Consider the following questions as you create an
architectural design

·     
What are **the
foundational parts of the architecture that represent the greatest risk** if
you get them wrong?

·     
What are the parts of the architecture that are
most **likely to change, or whose design**
you can delay until later with little impact?

·     
What are your **key assumptions**, and how will you test them?

·     
What conditions may require you to refactor the
design?

·     
Do not attempt to **over engineer** the
architecture, and do not make assumptions that you cannot verify. Instead, keep
your options open for future change. There will be aspects of your design that
you must fix early in the process, which may represent significant cost if
redesign is required. Identify these areas quickly and invest the time
necessary to get them right.

### Key Design Principles

When getting started with your design, keep in mind the key
principles that will help you to create an architecture that adheres to proven
principles, minimizes costs and maintenance requirements, and promotes
usability and extendibility. The key principles are:

·     
**Separation of concerns**. Divide your
application into distinct features with as little overlap in functionality as
possible.

·     
**Single Responsibility principle**. Each
component or module should be responsible for only a specific feature or
functionality, or aggregation of cohesive functionality.

·     
**Principle of Least Knowledge**(also
known as the Law of Demeter or LoD). A component or object should not know
about internal details of other components or objects.

·     
**Don’t repeat yourself (DRY)**. You should
only need to specify intent in one place. For example, in terms of application
design, specific functionality should be implemented in only one component; the
functionality should not be duplicated in any other component.

·     
**Minimize upfront design.**Only design
what is necessary. In some cases, you may require upfront comprehensive design
and testing if the cost of development or a failure in the design is very high.
In other cases, especially for agile development, you can avoid big design
upfront (BDUF). If your application requirements are unclear, or if there is a
possibility of the design evolving over time, avoid making a large design
effort prematurely. This principle is sometimes known as YAGNI ("You ain’t
gonna need it").

When designing an application or system, the goal of a
software architect is **to minimize the complexity by separating the design
into different areas of concern**. For example, the user interface (UI),
business processing, and data access all represent different areas of concern.
Within each area, the components you design should focus on that specific area
and should not mix code from other areas of concern. For example, UI processing
components should not include code that directly accesses a data source, but
instead should use either business components or data access components to
retrieve data. However, you must also make a cost/value determination on
the investment you make for an application. In some cases, you may need to
simplify the structure to allow, for example, UI data binding to a result set. In
general, try to consider the functional boundaries from a business viewpoint as
well. The following high level guidelines will help you to consider the wide
range of factors that can affect the ease of designing, implementing,
deploying, testing, and maintaining your application.

### Design Practices

·     
**Keep design patterns consistent within each
layer**. Within a logical layer, where possible, the design of components
should be consistent for a particular operation. For example, if you choose to
use the Table Data Gateway pattern to create an object that acts as a gateway
to tables or views in a database, you should not include another pattern such
as Repository, which uses a different paradigm for accessing data and
initializing business entities. However, you may need to use different patterns
for tasks in a layer that have a large variation in requirements, such as an
application that contains business transaction and reporting functionality.

·     
**Do not duplicate functionality within an
application**. There should be only one component providing a specific
functionality—this functionality should not be duplicated in any other
component.

·     
**Prefer composition to inheritance**. This
also reduces the inheritance hierarchies, which can become very difficult to
deal with.

·     
**Establish a coding style and naming
convention for development**.

·     
**Maintain system quality using automated QA
techniques during development**. Use unit testing and other automated Quality
Analysis techniques, such as dependency analysis and static code analysis,
during development.

·     
**Consider the operation of your application**.
Designing your application’s components and sub-systems with a clear
understanding of their individual operational requirements will significantly
ease overall deployment and operation. Use automated QA tools during
development to ensure that the correct operational data is provided by your
application’s components and sub-systems.

### Application Layers

·     
**Separate the areas of concern**. Break your
application into distinct features that overlap in functionality as little as
possible.

·     
**Be explicit about how layers communicate with
each other**. Allowing every layer in an application to communicate with or
have dependencies upon all of the other layers will result in a solution that
is more challenging to understand and manage. Make explicit decisions about the
dependencies between layers and the data flow between them.

·     
**Use abstraction to implement loose coupling
between layers**. This can be accomplished by defining interface components
such as a façade with well known inputs and outputs that translate requests
into a format understood by components within the layer.

·     
**Do not mix different types of components in
the same logical layer**. Start by identifying different areas of concern,
and then group components associated with each area of concern into logical
layers. For example, the UI layer should not contain business processing
components, but instead should contain components used to handle user input and
process user requests.

·     
**Keep the data format consistent within a
layer or component**. Mixing data formats will make the application more
difficult to implement, extend, and maintain. Every time you need to convert
data from one format to another, you are required to implement translation code
to perform the operation and incur a processing overhead.

### Components, Modules, and Functions

·     
**A component or an object should not rely on
internal details of other components or objects**. Each component or object
should call a method of another object or component, and that method should
have information about how to process the request and, if appropriate, how to
route it to appropriate subcomponents or other components. This helps to create
an application that is more maintainable and adaptable.

·     
**Do not overload the functionality of a
component**. For example, a UI processing component should not contain data
access code or attempt to provide additional functionality. Overloaded
components often have many functions and properties providing business
functionality mixed with crosscutting functionality such as logging and
exception handling. The result is a design that is very error prone and
difficult to maintain. Applying the single responsibility and separation of
concerns principles will help you to avoid this.

·     
**Understand how components will communicate
with each other**. This requires an understanding of the deployment scenarios
your application must support. You must determine if all components will run
within the same process, or if communication across physical or process
boundaries must be supported—perhaps by implementing message-based interfaces.

·     
**Keep crosscutting code abstracted from the
application business logic as far as possible**. Crosscutting code refers to
code related to security, communications, or operational management such as logging
and instrumentation. Mixing the code that implements these functions with the
business logic can lead to a design that is difficult to extend and maintain.
Changes to the crosscutting code require touching all of the business logic
code that is mixed with the crosscutting code. Consider using frameworks and
techniques (such as aspect oriented programming) that can help to manage
crosscutting concerns.

·     
**Define a clear contract for components**.
Components, modules, and functions should define a contract or interface
specification that describes their usage and behavior clearly. The contract
should describe how other components can access the internal functionality of
the component, module, or function; and the behavior of that functionality in
terms of pre-conditions, post-conditions, side effects, exceptions, performance
characteristics, and other factors.

## Key Design Considerations

### Determine the Application Type

·     
Choosing the appropriate application type is the
key part of the process of designing an application. Your choice is governed by
your specific requirements and infrastructure limitations. Many applications
must support multiple types of client, and may make use of more than one of the
basic archetypes.

·     
Applications designed for mobile devices.

·     
Rich client applications designed to run
primarily on a client PC.

·     
Rich Internet applications designed to be
deployed from the Internet, which support rich UI and media scenarios.

·     
Service applications designed to support
communication between loosely coupled components.

·     
Web applications designed to run primarily on
the server in fully connected scenarios.

·     
In addition, it provides information and
guidelines for some more specialist application types. These include the
following:

o  
Hosted and cloud-based applications and
services.

o  
Office Business Applications (OBAs) that
integrate Microsoft Office and Microsoft server technologies.

o  
SharePoint Line of Business (LOB) applications
that provide portal style access to business information and functions.

### Determine the Deployment Strategy

Your application may be deployed in a variety of
environments, each with its own specific set of constraints such as physical
separation of components across different servers, a limitation on networking
protocols, firewall and router configurations, and more. Several common
deployment patterns exist, which describe the benefits and considerations for a
range of distributed and non-distributed scenarios. You must balance the
requirements of the application with the appropriate patterns that the hardware
can support, and the constraints that the environment exerts on your deployment
options. These factors will influence your architecture design.

### Determine the Appropriate Technologies

When choosing technologies for your application, the key
factors to consider are the type of application you are developing and your
preferred options for application deployment topology and architectural styles.
Your choice of technologies will also be governed by organization policies,
infrastructure limitations, resource skills, and so on. You must compare the
capabilities of the technologies you choose against your application
requirements, taking into account all of these factors before making decisions.

### Determine the Quality Attributes

For example, every application design must consider security
and performance, but not every design needs to consider interoperability or
scalability. Understand your requirements and deployment scenarios first so
that you know which quality attributes are important for your design. Keep in
mind that quality attributes may conflict; for example, security often requires
a tradeoff against performance or usability.

### When designing to accommodate quality attributes, consider the following guidelines:

·     
Quality attributes are system properties that
are separate from the functionality of the system.

·     
From a technical perspective, implementing
quality attributes can differentiate a good system from a bad one.

·     
There are two types of quality attributes: those
that are measured at run time, and those that can only be estimated through
inspection.

·     
Analyze the tradeoffs between quality
attributes.

·     
Questions you should
ask when considering quality attributes include:

·     
What are the key quality attributes required for
your application? Identify them as part of the design process.

·     
What are the key requirements for addressing
these attributes? Are they actually quantifiable?

·     
What are the acceptance criteria that will indicate
that you have met the requirements?

### Determine the Crosscutting Concerns

·     
Crosscutting concerns represent key areas of
your design that are not related to a specific layer in your application. For
example, you should consider implementing centralized or common solutions for
the following:

·     
A logging mechanism that allows each layer to
log to a common store, or log to separate stores in such a way that the results
can be correlated afterwards.

·     
A mechanism for authentication and authorization
that passes identities across multiple layers to permit granting access to
resources.

·     
An exception management framework that will work
within each layer, and across the layers as exceptions are propagated to the
system boundaries.

·     
A communication approach that you can use to
communicate between the layers.

·     
A common caching infrastructure that allows you
to cache data in the presentation layer, the business layer, and the data
access layer.

# Architectural Styles and Patterns

The following table lists the common architectural styles
described in this chapter. It also contains a brief description of each style.
Later sections of this chapter contain more details of each style, as well as
guidance to help you choose the appropriate ones for your application.

|  |  |
| --- | --- |
| **Architecture style** | **Description** |
| *Client/Server* | Segregates the system into two applications, where the client makes requests to the server. In many cases, the server is a database with application logic represented as stored procedures. |
| *Component-Based Architecture* | Decomposes application design into reusable functional or logical components that expose well-defined communication interfaces. |
| *Domain Driven Design* | An object-oriented architectural style focused on modeling a business domain and defining business objects based on entities within the business domain. |
| *Layered Architecture* | Partitions the concerns of the application into stacked groups (layers). |
| *Message Bus* | An architecture style that prescribes use of a software system that can receive and send messages using one or more communication channels, so that applications can interact without needing to know specific details about each other. |
| *N-Tier / 3-Tier* | Segregates functionality into separate segments in much the same way as the layered style, but with each segment being a tier located on a physically separate computer. |
| *Object-Oriented* | A design paradigm based on division of responsibilities for an application or system into individual reusable and self-sufficient objects, each containing the data and the behavior relevant to the object. |
| *Service-Oriented Architecture (SOA)* | Refers to applications that expose and consume functionality as a service using contracts and messages. |

### Client/Server Architectural Style

Today, some examples of the client/server architectural style include Web
browser—based programs running on the Internet or an intranet; Microsoft
Windows® operating system—based applications that access networked data
services; applications that access remote data stores (such as e-mail readers,
FTP clients, and database query tools); and tools and utilities that manipulate
remote systems (such as system management tools and network monitoring tools).

Other variations on the client/server style include:

**Client-Queue-Client systems**. This approach allows
clients to communicate with other clients through a server-based queue. Clients
can read data from and send data to a server that acts simply as a queue to
store the data. This allows clients to distribute and synchronize files and
information. This is sometimes known as a *passive queue* architecture.

**Peer-to-Peer (P2P) applications**. Developed from the
Client-Queue-Client style, the P2P style allows the client and server to swap
their roles in order to distribute and synchronize files and information across
multiple clients. It extends the client/server style through multiple responses
to requests, shared data, resource discovery, and resilience to removal of
peers.

**Application servers**. A specialized architectural
style where the server hosts and executes applications and services that a thin
client accesses through a browser or specialized client installed software. An
example is a client executing an application that runs on the server through a
framework such as Terminal Services.

The main benefits of the client/server architectural style
are:

·     
**Higher security**. All data is stored on
the server, which generally offers a greater control of security than client
machines.

·     
**Centralized data access**. Because data is
stored only on the server, access and updates to the data are far easier to
administer than in other architectural styles.

·     
**Ease of maintenance**. Roles and
responsibilities of a computing system are distributed among several servers
that are known to each other through a network. This ensures that a client
remains unaware and unaffected by a server repair, upgrade, or relocation.

Consider the client/server
architectural style if your application is server based and will support many
clients, you are creating Web-based applications exposed through a Web browser,
you are implementing business processes that will be used by people throughout
the organization, or you are creating services for other applications to
consume. The client/server architectural style is also suitable, like many networked
styles, when you want to centralize data storage, backup, and management
functions, or when your application must support different client types and
different devices.

However, the traditional 2-Tier
client/server architectural style has numerous disadvantages, including the
tendency for application data and business logic to be closely combined on the
server, which can negatively impact system extensibility and scalability, and
its dependence on a central server, which can negatively impact system
reliability. To address these issues, the client-server architectural style has
evolved into the more general 3-Tier (or N-Tier) architectural style, described
below, which overcomes some of the disadvantages inherent in the 2-Tier
client-server architecture and provides additional benefits.

### Component-Based Architectural Style

Component-based architecture describes a software
engineering approach to system design and development. It focuses on the
decomposition of the design into individual functional or logical components
that expose well-defined communication interfaces containing methods, events,
and properties. This provides a higher level of abstraction than
object-oriented design principles, and does not focus on issues such as
communication protocols and shared state.

The key principle of the component-based style is the use of
components that are:

·     
**Reusable**. Components are usually designed
to be reused in different scenarios in different applications. However, some
components may be designed for a specific task.

·     
**Replaceable**. Components may be readily
substituted with other similar components.

·     
**Not context specific**. Components are
designed to operate in different environments and contexts. Specific
information, such as state data, should be passed to the component instead of
being included in or accessed by the component.

·     
**Extensible**. A component can be extended from
existing components to provide new behavior.

·     
**Encapsulated**. Components expose
interfaces that allow the caller to use its functionality, and do not reveal
details of the internal processes or any internal variables or state.

·     
**Independent**. Components are designed to
have minimal dependencies on other components. Therefore components can be
deployed into any appropriate environment without affecting other components or
systems.

The following are the main benefits of the component-based
architectural style:

·     
**Ease of deployment**. As new compatible
versions become available, you can replace existing versions with no impact on
the other components or the system as a whole.

·     
**Reduced cost**. The use of third-party
components allows you to spread the cost of development and maintenance.

·     
**Ease of development**. Components implement
well-known interfaces to provide defined functionality, allowing development
without impacting other parts of the system.

·     
**Reusable**. The use of reusable components
means that they can be used to spread the development and maintenance cost
across several applications or systems.

·     
**Mitigation of technical complexity**.
Components mitigate complexity through the use of a component container and its
services. Example component services include component activation, lifetime
management, method queuing, eventing, and transactions.

### Domain Driven Design Architectural Style

Domain Driven Design (DDD) is an object-oriented approach to
designing software based on the business domain, its elements and behaviors,
and the relationships between them. It aims to enable software systems that are
a realization of the underlying business domain by defining a domain model
expressed in the language of business domain experts. The domain model can be
viewed as a framework from which solutions can then be rationalized.

To apply Domain Driven Design, you must have a good
understanding of the business domain you want to model, or be skilled in
acquiring such business knowledge. The development team will often work with
business domain experts to model the domain. Architects, developers, and
subject matter experts have diverse backgrounds, and in many environments will
use different languages to describe their goals, designs and requirements.
However, within Domain Driven Design, the whole team agrees to only use a
single language that is focused on the business domain, and which excludes any
technical jargon.

As the core of the software is the domain model, which is a
direct projection of this shared language, it allows the team to quickly find
gaps in the software by analyzing the language around it. The creation of a
common language is not merely an exercise in accepting information from the
domain experts and applying it. Quite often, communication problems within
development teams are due not only to misunderstanding the language of the
domain, but also due to the fact that the domain's language is itself
ambiguous. The Domain Driven Design process holds the goal not only of
implementing the language being used, but also improving and refining the
language of the domain. This in turn benefits the software being built, since
the model is a direct projection of the domain language.

In order to help maintain the model as a pure and helpful
language construct, you must typically implement a great deal of isolation and
encapsulation within the domain model. Consequently, a system based on Domain
Driven Design can come at a relatively high cost. While Domain Driven Design
provides many technical benefits, such as maintainability, it should be applied
only to complex domains where the model and the linguistic processes provide
clear benefits in the communication of complex information, and in the
formulation of a common understanding of the domain.

The following are the main benefits of the Domain Driven
Design style:

·     
**Communication**. All parties within a
development team can use the domain model and the entities it defines to
communicate business knowledge and requirements using a common business domain
language, without requiring technical jargon.

·     
**Extensible**. The domain model is often
modular and flexible, making it easy to update and extend as conditions and
requirements change.

·     
**Testable**. The domain model objects are
loosely coupled and cohesive, allowing them to be more easily tested.

### Layered Architectural Style

Layered architecture focuses on the grouping of related
functionality within an application into distinct layers that are stacked
vertically on top of each other. Functionality within each layer is related by
a common role or responsibility. Communication between layers is explicit and
loosely coupled. Layering your application appropriately helps to support a
strong separation of concerns that, in turn, supports flexibility and
maintainability.

The layered architectural style has been described as
an *inverted pyramid of reuse* where each layer aggregates the
responsibilities and abstractions of the layer directly beneath it. With strict
layering, components in one layer can interact only with components in the same
layer or with components from the layer directly below it. More relaxed
layering allows components in a layer to interact with components in the same
layer or with components in any lower layer.

The layers of an application may reside on the same physical
computer (the same tier) or may be distributed over separate computers (*n*-tier),
and the components in each layer communicate with components in other layers
through well-defined interfaces. For example, a typical Web application design
consists of a presentation layer (functionality related to the UI), a business
layer (business rules processing), and a data layer (functionality related to
data access, often almost entirely implemented using high-level data access
frameworks). For details of the n-tier application architectural style,
see [N-Tier / 3-Tier
Architectural Style](https://msdn.microsoft.com/en-us/library/ee658117.aspx#NTier3TierStyle) later in this chapter.

Common principles for designs that use the layered
architectural style include:

·     
**Abstraction**. Layered architecture
abstracts the view of the system as whole while providing enough detail to
understand the roles and responsibilities of individual layers and the
relationship between them.

·     
**Encapsulation**. No assumptions need to be
made about data types, methods and properties, or implementation during design,
as these features are not exposed at layer boundaries.

·     
**Clearly defined functional layers**. The
separation between functionality in each layer is clear. Upper layers such as
the presentation layer send commands to lower layers, such as the business and
data layers, and may react to events in these layers, allowing data to flow
both up and down between the layers.

·     
**High cohesion**. Well-defined
responsibility boundaries for each layer, and ensuring that each layer contains
functionality directly related to the tasks of that layer, will help to
maximize cohesion within the layer.

·     
**Reusable**. Lower layers have no
dependencies on higher layers, potentially allowing them to be reusable in
other scenarios.

·     
**Loose coupling**. Communication between
layers is based on abstraction and events to provide loose coupling between
layers.

Examples of layered applications include line-of-business
(LOB) applications such as accounting and customer-management systems;
enterprise Web-based applications and Web sites, and enterprise desktop or
smart clients with centralized application servers for business logic.

The following are the key principles of the Separated
Presentation patterns:

·     
**Separation of concerns**. Separated
Presentation patterns divide UI processing concerns into distinct roles; for
example, MVC has three roles: the Model, the View, and the Controller. The
Model represents data (perhaps a domain model that includes business rules);
the View represents the UI; and the Controller handles requests, manipulates
the model, and performs other operations.

·     
**Event-based notification**. The Observer
pattern is commonly used to provide notifications to the View when data managed
by the Model changes.

·     
**Delegated event handling**. The controller
handles events triggered from the UI controls in the View.

Other examples of Separated Presentation patterns are the
Passive View pattern and the Supervising Presenter (or Supervising Controller)
pattern.

The main benefits of the layered architectural style, and
the use of a Separated Presentation pattern

·     
**Abstraction**. Layers allow changes to be
made at the abstract level. You can increase or decrease the level of
abstraction you use in each layer of the hierarchical stack.

·     
**Isolation**. Allows you to isolate
technology upgrades to individual layers in order to reduce risk and minimize
impact on the overall system.

·     
**Manageability**. Separation of core
concerns helps to identify dependencies, and organizes the code into more
manageable sections.

·     
**Performance**. Distributing the layers over
multiple physical tiers can improve scalability, fault tolerance, and
performance.

·     
**Reusability**. Roles promote reusability.
For example, in MVC, the Controller can often be reused with other compatible
Views in order to provide a role specific or a user-customized view on to the
same data and functionality.

·     
**Testability**. Increased testability arises
from having well-defined layer interfaces, as well as the ability to switch
between different implementations of the layer interfaces. Separated
Presentation patterns allow you to build mock objects that mimic the behavior
of concrete objects such as the Model, Controller, or View during testing.

Consider the layered architectural style if you have
existing layers that are suitable for reuse in other applications, you already
have applications that expose suitable business processes through service
interfaces, or your application is complex and the high-level design demands
separation so that teams can focus on different areas of functionality. The
layered architectural style is also appropriate if your application must
support different client types and different devices, or you want to implement
complex and/or configurable business rules and processes.

Consider a Separated Presentation pattern if you want
improved testability and simplified maintenance of UI functionality, or you
want to separate the task of designing the UI from the development of the logic
code that drives it. These patterns are also appropriate when your UI view does
not contain any request processing code, and does not implement any business
logic.

### Message Bus Architectural Style

Message bus architecture describes the principle of using a
software system that can receive and send messages using one or more
communication channels, so that applications can interact without needing to
know specific details about each other. It is a style for designing
applications where interaction between applications is accomplished by passing
messages (usually asynchronously) over a common bus. The most common
implementations of message bus architecture use either a messaging router or a
Publish/Subscribe pattern, and are often implemented using a messaging system
such as Message Queuing. Many implementations consist of individual
applications that communicate using common schemas and a shared infrastructure
for sending and receiving messages. A message bus provides the ability to
handle:

•       **Message-oriented
communications**. All communication between applications is based on messages
that use known schemas.

•       **Complex
processing logic**. Complex operations can be executed by combining a set of
smaller operations, each of which supports specific tasks, as part of a multistep
itinerary.

•       **Modifications
to processing logic**. Because interaction with the bus is based on common
schemas and commands, you can insert or remove applications on the bus to
change the logic that is used to process messages.

•       **Integration
with different environments**. By using a message-based communication model
based on common standards, you can interact with applications developed for
different environments, such as Microsoft .NET and Java.

•       **Enterprise
Service Bus (ESB)**. Based on message bus designs, an ESB uses services for
communication between the bus and components attached to the bus. An ESB will
usually provide services that transform messages from one format to another,
allowing clients that use incompatible message formats to communicate with each
other

•       **Internet
Service Bus (ISB)**. This is similar to an enterprise service bus, but with
applications hosted in the cloud instead of on an enterprise network. A core
concept of ISB is the use of Uniform Resource Identifiers (URIs) and policies
to control the routing of logic through applications and services in the cloud.

The main benefits of the message-bus architectural style
are:

•       **Extensibility**.
Applications can be added to or removed from the bus without having an impact
on the existing applications.

•       **Low
complexity**. Application complexity is reduced because each application only
needs to know how to communicate with the bus.

•       **Flexibility**.
The set of applications that make up a complex process, or the communication
patterns between applications, can be changed easily to match changes in
business or user requirements, simply through changes to the configuration or
parameters that control routing.

•       **Loose
coupling**. As long as applications expose a suitable interface for
communication with the message bus, there is no dependency on the application
itself, allowing changes, updates, and replacements that expose the same
interface.

•       **Scalability**.
Multiple instances of the same application can be attached to the bus in order
to handle multiple requests at the same time.

•       **Application
simplicity**. Although a message bus implementation adds complexity to the
infrastructure, each application needs to support only a single connection to
the message bus instead of multiple connections to other applications.

Consider the message bus architectural style if you have
existing applications that interoperate with each other to perform tasks, or
you want to combine multiple tasks into a single operation. This style is also
appropriate if you are implementing a task that requires interaction with
external applications, or applications hosted in different environments.

### N-Tier / 3-Tier Architectural Style

N-tier and 3-tier are architectural deployment styles that
describe the separation of functionality into segments in much the same way as
the layered style, but with each segment being a tier that can be located on a
physically separate computer. They evolved through the component-oriented
approach, generally using platform specific methods for communication instead
of a message-based approach.

N-tier application architecture is characterized by the
functional decomposition of applications, service components, and their
distributed deployment, providing improved scalability, availability,
manageability, and resource utilization. Each tier is completely independent
from all other tiers, except for those immediately above and below it. The nth
tier only has to know how to handle a request from the n+1th tier, how to
forward that request on to the n-1th tier (if there is one), and how to handle
the results of the request. Communication between tiers is typically
asynchronous in order to support better scalability.

N-tier architectures usually have at least three separate
logical parts, each located on a separate physical server. Each part is
responsible for specific functionality. When using a layered design approach, a
layer is deployed on a tier if more than one service or application is
dependent on the functionality exposed by the layer.

An example of the N-tier/3-tier architectural style is a
typical financial Web application where security is important. The business
layer must be deployed behind a firewall, which forces the deployment of the
presentation layer on a separate tier in the perimeter network. Another example
is a typical rich client connected application, where the presentation layer is
deployed on client machines and the business layer and data access layer are
deployed on one or more server tiers.

The main benefits of the N-tier/3-tier architectural style
are:

•       **Maintainability**.
Because each tier is independent of the other tiers, updates or changes can be
carried out without affecting the application as a whole.

•       **Scalability**.
Because tiers are based on the deployment of layers, scaling out an application
is reasonably straightforward.

•       **Flexibility**.
Because each tier can be managed or scaled independently, flexibility is
increased.

•       **Availability**.
Applications can exploit the modular architecture of enabling systems using
easily scalable components, which increases availability.

### Object-Oriented Architectural Style

An object-oriented design views a system as a series of
cooperating objects, instead of a set of routines or procedural instructions.
Objects are discrete, independent, and loosely coupled; they communicate
through interfaces, by calling methods or accessing properties in other
objects, and by sending and receiving messages.

The key principles of the object-oriented architectural
style are:

•       **Abstraction**.
This allows you to reduce a complex operation into a generalization that
retains the base characteristics of the operation. For example, an abstract
interface can be a well-known definition that supports data access operations
using simple methods such as **Get** and **Update**.
Another form of abstraction could be metadata used to provide a mapping between
two formats that hold structured data.

•       **Composition**.
Objects can be assembled from other objects, and can choose to hide these
internal objects from other classes or expose them as simple interfaces.

•       **Inheritance**.
Objects can inherit from other objects, and use functionality in the base
object or override it to implement new behavior. Moreover, inheritance makes
maintenance and updates easier, as changes to the base object are propagated
automatically to the inheriting objects.

•       **Encapsulation**.
Objects expose functionality only through methods, properties, and events, and
hide the internal details such as state and variables from other objects. This
makes it easier to update or replace objects, as long as their interfaces are
compatible, without affecting other objects and code.

•       **Polymorphism**.
This allows you to override the behavior of a base type that supports
operations in your application by implementing new types that are
interchangeable with the existing object.

•       **Decoupling**.
Objects can be decoupled from the consumer by defining an abstract interface
that the object implements and the consumer can understand. This allows you to
provide alternative implementations without affecting consumers of the
interface.

The main benefits of the object-oriented architectural style
are that it is:

·     
**Understandable**. It maps the application
more closely to the real world objects, making it more understandable.

·     
**Reusable**. It provides for reusability
through polymorphism and abstraction.

·     
**Testable**. It provides for improved
testability through encapsulation.

·     
**Extensible**. Encapsulation, polymorphism,
and abstraction ensure that a change in the representation of data does not
affect the interfaces that the object exposes, which would limit the capability
to communicate and interact with other objects.

·     
**Highly Cohesive**. By locating only related
methods and features in an object, and using different objects for different sets
of features, you can achieve a high level of cohesion.

Consider the object-oriented
architectural style if you want to model your application based on real world
objects and actions, or you already have suitable objects and classes that
match the design and operational requirements. The object-oriented style is
also suitable if you must encapsulate logic and data together in reusable
components or you have complex business logic that requires abstraction and
dynamic behavior.

**Service-Oriented Architectural Style**

Service-oriented architecture (SOA) enables application
functionality to be provided as a set of services, and the creation of
applications that make use of software services. Services are loosely coupled
because they use standards-based interfaces that can be invoked, published, and
discovered. Services in SOA are focused on providing a schema and message-based
interaction with an application through interfaces that are application scoped,
and not component or object-based. An SOA service should not be treated as a
component-based service provider.

The SOA style can package business processes into
interoperable services, using a range of protocols and data formats to
communicate information. Clients and other services can access local services
running on the same tier, or access remote services over a connecting network.

The key principles of the SOA architectural style are:

·     
**Services are autonomous**. Each service is
maintained, developed, deployed, and versioned independently.

·     
**Services are distributable**. Services can
be located anywhere on a network, locally or remotely, as long as the network
supports the required communication protocols.

·     
**Services are loosely coupled**. Each
service is independent of others, and can be replaced or updated without
breaking applications that use it as long as the interface is still compatible.

·     
**Services share schema and contract, not class**.
Services share contracts and schemas when they communicate, not internal
classes.

·     
**Compatibility is based on policy**. Policy
in this case means definition of features such as transport, protocol, and
security.

Common examples of
service-oriented applications include sharing information, handling multistep
processes such as reservation systems and online stores, exposing industry
specific data or services over an extranet, and creating mashups that combine
information from multiple sources.

The main benefits of the SOA architectural style are:

·     
**Domain alignment**. Reuse of common
services with standard interfaces increases business and technology
opportunities and reduces cost.

·     
**Abstraction**. Services are autonomous and
accessed through a formal contract, which provides loose coupling and
abstraction.

·     
**Discoverability**. Services can expose
descriptions that allow other applications and services to locate them and
automatically determine the interface.

·     
**Interoperability**. Because the protocols
and data formats are based on industry standards, the provider and consumer of
the service can be built and deployed on different platforms.

·     
**Rationalization**. Services can be granular
in order to provide specific functionality, rather than duplicating the
functionality in number of applications, which removes duplication.