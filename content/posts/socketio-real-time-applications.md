---
title: "Socket.IO | Real Time Applications"
description: "Building real-time web applications with Socket.IO — WebSockets, event-driven architecture, and practical implementation patterns."
date: 2016-08-22
draft: false
categories:
  - tech
ShowToc: true
TocOpen: false
tags:
  - socketio
  - realtime
  - web
cover:
  image: "/images/covers/socketio-real-time-applications-cover.svg"
  alt: "Cover image"
  relative: false
---

The real-time web is a set of technologies and practices that enable users to receive information as soon as it is published, rather than requiring that they or their software check a source periodically for updates.  

The other specification which goes on to implement a full duplex communication protocol for the web applications is WebSockets. In WebSockets, the client initiates a socket connection with the server, which supports this protocol as well. The server and client will send and receive data on this socket connection.

### Socket.IO

Ever since the onset of web applications, developers have worked towards different ways of getting duplex communication between the server and the browser. Be it using Java, Flash, Comet, or many other workarounds, all aim to do the same. But for the first time, there is a specification to build a full-duplex communication system by using HTML5 WebSockets. WebSocket is a revolutionary, new communication feature in the HTML5 specification that defines a full-duplex communication channel

operating over the Web through a single socket. Although the WebSockets RFC is published, it is not, and will never be, available on older browsers that are still in use. Socket.io is an abstraction layer for WebSockets, with Flash, XHR, JSONP, and HTMLFile fallbacks. Socket.io provides an easy server

and client library for making real-time, streaming updates between a web server and a browser client.

### Handling events

Since the socket.io framework has components for both the server and the client, we will use these components to code our communication on both the sides. Events emitted on a socket on one side will be handled by the corresponding event handler on the other side. Socket.io is built so that both the sides can send messages or attach handlers to process the incoming messages.

It is important to remember that "messages" here are not the actual messages sent and received by users of the chat system, but the messages used for communication by the client and the server. There will be two types of messages, as follows:

* The system messages: These messages will be sent by our chat system to the client, like when the user is connected, when others connect, or when users disconnect. Let's identify it with serverMessage.
* The user messages: These messages will be sent by the client to the server and will actually carry the user's message content in the payload. We will probably want to differentiate between the messages we send and the messages other users send. So let's call them myMessage and userMessage respectively.

### The server

Now we will implement the server, which will perform the task of relaying the messages, as already mentioned. Create a file in the routes folder called sockets.js and insert the following code into it:

</a>
</figure>

In the first line of code (you must be familiar with this by now), we import the socket.io module; we will identify this module by the io variable. Since socket.io works with the communication layer, we need to set it up to listen to the HTTP server. The HTTP server can only be accessed from the main application module, so we have to pass server to our module before our module can do anything. Hence, we export a method called initialize from our module, which will set up the socket.io server and also bind all the message handlers:

On the first line of the method, we will pass the server to the socket.io module's listen method. The server is an instance of the node HTTP server module; socket. io will configure various handlers on this server. This is the only boilerplate code required to set up socket.io. Next, we need to set up our message handler for socket. io messages.

The first event that our server will receive is a new connection from a new client. This is identified by the connection event on the io.sockets object and notifies our application that a new client has opened a new connection and all the protocol negotiation (transparent to us) has been completed and now we have a socket to communicate with this client:

The connection event handler will be triggered, passing along the socket that was just established. The socket is an event emitter that can trigger different events based on the messages it gets, and we will use this socket also to communicate with the client for which it was created. There are several events exposed, such as the connection event to handle events on the server. Let's take a quick look at

these events:

* io.sockets.on('connection', function(socket) {}): Initial connection from a client. The socket argument should be used in further communication with the client.
* socket.on('message', function(message, callback) {}): The message handler is triggered when a message sent with socket.send is received. The message parameter is the message sent, and callback is an optional acknowledgment function.
* socket.on('anything', function(data) {}): The anything event can be any event except the reserved events.
* socket.on('disconnect', function() {}): This event is fired when the socket disconnects.

When we send the message using the broadcast object, it will be sent to all the clients that are connected, except to the one for which this socket was created. The syntax for sending the message here is the same; the difference is that it is called on the broadcast object, referred to as message flags in socket.io, instead of the socket itself.

### The client

</a>
</figure>

The first step in starting the chat is to connect to the server: var socket = io.connect('/');

The last thing to do on the client side is to send the messages from the user. This will be done when the user writes his/her message in the message box and clicks the Send button. So, let's add an event handler to the Send button.

Like the connection event and other predefined events on the server, we have some predefined events on the client too. These are as follows:

* socket.on('connect', function () {}): The connect event is emitted when the socket is connected successfully.
* socket.on('connecting', function () {}):The connecting event is emitted when the socket is attempting to connect with the server.
* socket.on('disconnect', function () {}): The disconnect event is emitted when the socket is disconnected.
* socket.on('connect\_failed', function () {}): The connect\_failed event is emitted when socket.io fails to establish a connection to the server and has no more transports to fall back to.
* socket.on('error', function () {}): The error event is emitted when an error occurs and it cannot be handled by the other event types.
* socket.on('message', function (message, callback) {}): The message event is emitted when a message sent by using socket.send is received. The message parameter is the sent message, and callback is an optional acknowledgment function.
* socket.on('anything', function(data, callback) {}): The anything event can be any event except the reserved events. The data parameter represents the data, and callback can be used to send a reply.
* socket.on('reconnect\_failed', function () {}): The reconnect\_ failed event is emitted when socket.io fails to reestablish a working connection after the connection was dropped.
* socket.on('reconnect', function () {}): The reconnect event is emitted when socket.io is successfully reconnected to the server.
* socket.on('reconnecting', function () {}): The reconnecting event is emitted when the socket is attempting to reconnect with the server.

### The Socket.IO Protocol

Socket.io provides a very simple API that is easy to use but exposes a lot of functionality. Moreover, this functionality works uniformly across browsers and the various transport mechanisms provided by socket.io. To achieve this, a socket.io client and server do a lot of work in the background.

### Why do we need another protocol?

The answer is twofold; socket.io works in a uniform manner across browsers (dating back to Internet Explorer 6), and socket.io provides a much richer API.

Another problem for WebSocket is firewalls and proxies. Most of the firewalls block any communication (apart from standard HTTP 1.0/1.1), and may not allow a WebSocket connection to be established. The same applies to most proxy servers.

Contrary to this, when we build our application using socket.io, the people who can use WebSocket will continue using it, but those who can't will fall back on the next best available transport mechanism and then the next and so on, until they find one that works in the browser, even through the firewalls and proxies, all the way down to iframes (which is rarely used). The default order:

* WebSocket
* FlashSocket
* XHR long polling
* XHR multipart streaming
* XHR polling
* JSONP polling
* iframe

### The Socket.IO socket

The socket.io socket emulates a network socket over different transport mechanisms. Just as any other socket, it has various stages in its lifecycle, depending on the status of the connection. These are as follows:

* connecting
* connected
* disconnected
* disconnecting

Once the handshake is complete, a connection is opened using the transport negotiated during the handshake, and the state of the socket is set to connected. To check the liveliness of the socket depending on the server configuration, the server may require heartbeat messages to be sent from the client to the server in regular intervals. In the absence of such a message, or the failure of the underlying transport, the socket will be disconnected. In this case, the client will initiate a reconnect. If the connection is restored within the connection termination time or the timeout agreed at the time of the handshake, the buffered messages are sent across. In case the connection is not restored, the client will start a new connection request, beginning with a new handshake. Also, optionally, to ensure message delivery over the socket, we can make it compulsory for the socket to acknowledge the message delivery. The socket is terminated when the close method is called on either the client or

the server.

### The Socket.IO connection

The socket.io connection begins with the handshake. This makes the handshake a special part of the protocol. Apart from the handshake, all the other events and messages in the protocol are transferred over the socket. Socket.io is intended for use with web applications, and therefore it is assumed that these applications will always be able to use HTTP. It is because of this reasoning that the socket.io handshake takes place over HTTP. To initiate the connection and hence perform the handshake, the client performs a POST request on the handshake URI. Let us take the same socket.io connection URI and try to understand its various parts.

### Socket.IO messages

Once the transport's connection is established, all the communication between the client and server happens using messaging over the socket. The messages need to be encoded in the format specified by socket.io. This format enables socket.io to determine the type of the message and the data sent in the message, and some metadata useful for operation. The message format

is [type] : [id ('+')] : [endpoint] (: [data]).

### Disconnect (0)

When the type is zero (0), the message is a disconnect signal. This will tell socket.io to close the connection and the mentioned socket. If the endpoint is not specified, the message will be sent to the default socket, which will cause the whole socket to be closed and all the endpoints on that socket will be terminated.

### Connect (1)

This message is only used for multiplexing, and is sent from the client to the server to open a new connection. Thus, this message must always have an endpoint. The first (default) socket connection is established by the handshake explained earlier. The endpoint may be followed by query parameters in a URL query format. If the connection is successful, the server will echo the same message, else the server can send an error message

### Socket.IO Quick Reference

**Instantiating socket** The socket.io module is instantiated, just like any other node module, by using

require to import the module: var io = require('socket.io');

**Starting Socket.IO**The socket.io server component is started by using the listen method, which

attaches the socket.io to the node HTTP server: var sio = io.listen(<server>)

**Listening to events**The event handlers are attached to socket using the on method. The on method takes the event name and the callback/handler function as parameters:

sio.on(<event>, function(eventData){

//DO SOMETHING

});

**Emitting an event**We use the emit method to trigger an event. This event will be handled on the client: socket.emit(<event>, <event\_data>, ack\_callback);

**Sending a message**

The send method is used to send a message to the client: socket.send(<message>, ack\_callback);

**Sending a JSON message**A JSON message can be sent by using the json flag before the send method: socket.json.send(<message>, ack\_callback);

**Broadcasting a message/event**A message or an event can be broadcasted to all the connected sockets using the broadcast flag: socket.broadcast.emit(<event>, <event\_data>);

**Sending a volatile message**

Sometimes the message being sent is not important and can be ignored if not delivered. So these methods need not be queued or attempted to be redelivered. This is done with the volatile flag:

socket.volatile.send(<message>);

**Storing socket data**

We can call the set method on the socket to store some data on the socket. This is an asynchronous method call and takes a key, value, and a callback function:

socket.set(<key>, <value>, function(){

//DO SOMETHING

});

**Getting the socket data**

We use the get method to fetch the value stored on a socket. This is an asynchronous method and takes a key and a callback function, which will get the value:

socket.get(<key>, function(value){

//DO SOMETHING

});

**Restricting to a namespace**

We can multiplex the socket and restrict messages/events to a namespace by using the of method. This method returns a socket, which can be used as any other socket, but the messages will be restricted to only the clients connected to this namespace: var namespace\_socket = socket.of(<namespace>);

**Joining a room**

We use the join method of socket to join a room. It will create a new room if one doesn't already exist: socket.join(<room>);

**Broadcasting messages/events in a room**

We can send messages to all the connected clients in the room by using the in flag with broadcast:

socket.broadcast.in(<room>).send(<message>);

socket.broadcast.in(<room>).emit(<event>, <event\_data>);

**Leaving a room**

The leave method is used to leave a room. We don't need to do this explicitly if the socket is exiting. Also, an empty room will automatically be destroyed:

socket.leave(<room>);

**connection**

This event is fired when an initial connection with a client is established: io.sockets.on('connection', function(socket) {})

**message**

The message event is emitted when a message sent with socket.send is received: socket.on('message', function(<message>, <ack\_callback>) {})

**disconnect**

This event is fired when the socket disconnects: socket.on('disconnect', function() {})

**Connecting to a socket**

We connect to a socket using the connect method on the io object in the client: var socket = io.connect(<uri>);

**Listening to events**

We can attach event handlers to a socket using the on method: socket.on(<event>, function(event\_data, ack\_callback){});

**Emitting an event**

We use the emit method to trigger an event. This event will be handled on the server:

socket.on(<event>, <event\_data>, ack\_callback);

**Sending a message**

The send method is used to send a message to the server: socket.send(<message>, ack\_callback);

**connect**

The connect event is emitted when the socket is connected successfully: socket.on('connect', function () {})

**connecting**

The connecting event is emitted when the socket is attempting to connect with the server: socket.on('connecting', function () {})

**disconnect**

The disconnect event is emitted when the socket is disconnected: socket.on('disconnect', function () {})

**connect\_failed**

The connect\_failed event is emitted when socket.io fails to establish a connection to the server for reasons such as when none of the transports work or authorization failed: socket.on('connect\_failed', function () {})

**message**

The message event is emitted when a message sent with socket.send is received: socket.on('message', function (<message>, <ack\_callback>) {})

**reconnect**

The reconnect event is emitted when socket.io successfully reconnects to the server: socket.on('reconnect', function () {})

**reconnecting**

The reconnecting event is emitted when the socket is attempting to reconnect with the server:

socket.on('reconnecting', function () {})

**reconnect\_failed**

The reconnect\_failed event is emitted when socket.io fails to reestablish a working connection after the connection was dropped: socket.on('reconnect\_failed', function () {})