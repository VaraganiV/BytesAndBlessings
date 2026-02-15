---
title: "JavaScript"
description: "A comprehensive JavaScript reference covering types, objects, functions, closures, prototypes, async patterns, and best practices."
date: 2016-07-22
draft: false
categories:
  - tech
ShowToc: true
TocOpen: false
tags:
  - javascript
  - web
  - programming
cover:
  image: "/images/covers/javascript-cover.svg"
  alt: "Cover image"
  relative: false
---

## Why JavaScript?

JavaScript is an important language because it is the language of the web browser. Its association with the browser makes it one of the most popular programming languages in the world.

## JavaScript Object System

JavaScript's object system is based around a Global Object which is created before the control enters any execution context. All the other features are its properties only. In JavaScript, Objects are hash maps which store properties. Strictly speaking these properties can be.

* Named data property
* Named accessor property
* Internal property

Data properties are used to store so called "value" and some boolean attributes , while accessor properties are functions which are used to access stored "value", while internal properties are only for specification purposes and can not be accessed from user code.The "value" is stored in [[value]] attribute of data property. [[get]] and [[set]] attribute stores the respective accessor functions in accessor properties

In JavaScript as functions can be called as both as a function as well as constructor thus they have different behaviour for both. for example if Object is called without "new" operator with a value passed. It will do type convertion. var x = Object("hello"); x gets the result of ToObject(value) function whereas if "new" operator is used it may create a new object as well, depending on the value passed var x = new Object("hello"); in the above both cases, same value gets stored in x as the value we supplied was a primitive string only.

## Execution Context

When code is run in JavaScript, the environment in which it is executed is very important, and is evaluated as 1 of the following:

Global code          – The default envionment where your code is executed for the first time.

Function code       – Whenever the flow of execution enters a function body.

Eval code              – Text to be executed inside the internal eval function.

<figure>
<a href="cid:5602b0192fdc52a0b29da94d4b603792" target="_blank">
<img src="cid:5602b0192fdc52a0b29da94d4b603792" alt="Blog image" loading="lazy" style="max-width:100%; width:480px; height:auto; border-radius:8px; cursor:zoom-in;" />
</a>
</figure>

We have 1 global context represented by the purple border and 3 different function contexts represented by the green, blue and orange border There can only ever be 1 global context, which can be accessed from any other context in your program. You can have any number of function contexts, and each function call creates a new context, which creates a private scope where anything declared inside of the function can not be directly accessed from outside the current function scope.

As we already know, when a browser first loads your script, it enters the global execution context by default. If, in your global code you call a function, the sequence flow of your program enters the function being called, creating a new execution context and pushing that context to the top of the execution stack. If you call another function inside this current function, the same thing happens. The execution flow of code enters the inner function, which creates a new execution context that is pushed to the top of the existing stack. The browser will always execute the current execution context that sits on top of the stack, and once the function completes executing the current execution context, it will be popped off the top of the stack, returning control to the context below in the current stack.

## Execution Stack Key Points

* Single threaded.
* Synchronous execution.
* 1 Global context.
* Infinite function contexts.
* Each function call creates a new execution context, even a call to itself.

## Execution Context in Detail

So we now know that everytime a function is called, a new execution context is created. However, inside the JavaScript interpreter, every call to an execution context has 2 stages:

* Creation Stage [when the function is called, but before it executes any code inside]:
  + Create the Scope Chain.
  + Create variables, functions and arguments.
  + Determine the value of "this".
* Activation / Code Execution Stage:
  + Assign values, references to functions and interpret / execute code.

## Interpreter Code Evaluation

* Find some code to invoke a function.
* Before executing the function code, create the execution context.
* Enter the creation stage:
* Initialize the Scope Chain.
* Create the variable object:
  + Create the arguments object, check the context for parameters, initialize the name and value and create a reference copy.
  + Scan the context for function declarations:
  + For each function found, create a property in the variable object that is the exact function name, which has a reference pointer to the function in memory.
  + If the function name exists already, the reference pointer value will be overwritten.
  + Scan the context for variable declarations:
  + For each variable declaration found, create a property in the variable object that is the variable name, and initialize the value as undefined.
  + If the variable name already exists in the variable object, do nothing and continue scanning.
* Determine the value of "this" inside the context.
* Activation / Code Execution Stage:
  + Run / interpret the function code in the context and assign variable values as the code is executed line by line.

## Hoisting

You can find many resources online defining the term hoisting in JavaScript, **explaining that variable and function declarations are hoisted to the top of their function scope**. However, none explain in detail why this happens, and armed with your new knowledge about how the interpreter creates the activation object, it is easy to see why. Take the following code example:

(function() {

console.log(typeof foo); // function pointer

console.log(typeof bar); // undefined

var foo = 'hello',

bar = function() {

return 'world';

};

function foo() {

return 'hello';

}

}());

### Why Can We Access Foo Before Declaration?

If we follow the creation stage, we know the variables have already been created before the activation / code execution stage. So as the function flow started executing, foo had already been defined in the activation object.

### Why Is Foo a Function?

Even though foo is declared twice, we know from the creation stage that functions are created on the activation object before variables, and if the property name already exists on the activation object, we simply bypass the decleration. Therefore, a reference to function foo() is first created on the activation object, and when we get interpreter gets to var foo, we already see the property name foo exists so the code does nothing and proceeds.

### Why Is Bar Undefined?

Bar is actually a variable that has a function assignment, and we know the variables are created in the creation stage but they are initialized with the value of undefined.

## Scope Chain and Closures

An important feature of JavaScript to note, is that the interpreter uses Lexical Scoping, as opposed to Dynamic Scoping. This is just a complicated way of saying all inner functions, are statically (lexically) bound to the parent context in which the inner function was physically defined in the program code. This lexical scope is the source of confusion for many developers. We know that every invocation of a function will create a new execution context and associated VO, which holds the values of variables evaluated in the current context.

When the interpreter executes line 14: alert(a + b + c), it resolves a first by looking into the scope chain and checking the first variable object, three's [VO]. It checks to see if a exists inside three's [VO] but can not find any property with that name, so moves on to check the next [VO].

The interpreter keeps checking each [VO] in sequence for the existence of the variable name, in which case the value will be returned to the original evaluated code, or the program will throw a ReferenceError if none is found. Therefore, given the example above, you can see that a, b and c are all resolvable given function three’s scope chain.

## How Closures Work

An inner function always has access to the vars and parameters of its outer function, even after the outer function has returned…

JavaScript is prototypal by nature and almost everything in the language, except for null and undefined, are objects. When trying to access a property on an object, the interpreter will try to resolve it by looking for the existence of the property in the object. If it can’t find the property, it will continue to look up the prototype chain, which is an inherited chain of objects, until it finds the property, or traversed to the end of the chain. This leads to an interesting question, does the interpreter resolve an object property using the scope chain or prototype chain first ? It uses both. When trying to resolve a property or identifier, the scope chain will be used first to locate the object. Once the object has been found, the prototype chain of that object will then be traversed looking for the property name.

## When to Use Closures

Closures are a powerful concept given to JavaScript and some of the most common situations to use them are:Encapsulation, Callbacks

## When Not to Use Closures

Although closures are powerful, they should be used sparingly due to some performance concerns: Large scope lengths, Garbage collection, Circular references

## Analyzing JavaScript

The very good ideas include functions, loose typing, dynamic objects, and an expressive object literal notation(In the object literal notation, an object description is a set of comma-separated name/value pairs inside curly braces. The names can be identifiers or strings followed by a colon). The bad ideas include a programming model based on global variables.

### IntegerJavaScript has a single number type. Internally, it is represented as 64-bit floating point, the same as Java’s double . Unlike most other programming languages, there is no separate integer type, so 1  and 1.0  are the same value. This is a significant convenience because problems of overflow in short integers are completely avoided, and all you need to know about a number is that it is a number. A large class of numeric type errors is avoided. The value NaN  is a number value that is the result of an operation that cannot produce a normal result. NaN  is not equal to any value, including itself. You can detect NaN  with the isNaN(number)  function.

### Strings A string literal can be wrapped in single quotes or double quotes. It can contain zero or more characters. The \ (backslash) is the escape character. JavaScript was built at a time when Unicode was a 16-bit character set, so all characters in JavaScript are 16 bits wide.   Strings are immutable. Once it is made, a string can never be changed.

### Objects The simple types of JavaScript are numbers, strings, booleans (true  and false ), null , and undefined. All other values are objects. Numbers, strings, and booleans are object-like in that they have methods, but they are immutable. Objects in JavaScript are mutable keyed collections. In JavaScript, arrays are objects, functions are objects, regular expressions are objects, and, of course, objects are objects. An object is a container of properties, where a property has a name and a value. A property name can be any string, including the empty string. A property value can be any JavaScript value except for undefined.

var flight = {

airline: "Oceanic",

number: 815,

departure: {

IATA: "SYD",

time: "2004-09-22 14:55",

city: "Sydney"

},

arrival: {

IATA: "LAX",

time: "2004-09-23 10:42",

city: "Los Angeles"

}

};  

### Function Objects Functions in JavaScript are objects. Objects are collections of name/value pairs having a hidden link to a prototype object. Objects produced from object literals are linked to Object.prototype. Function objects are linked to Function.prototype (which is itself linked to Object.prototype). Every function is also created with two additional hidden properties: the function’s context and the code that implements the function’s behavior.

A function always returns a value. If the return value is not specified, then **undefined** is returned. If the function was invoked with the new prefix and the return value is not an object, then this (the new object) is returned instead.

### CascadeSome methods do not have a return value. For example, it is typical for methods that set or change the state of an object to return nothing. If we have those methods return this instead of undefined, we can enable cascades. In a cascade, we can call many methods on the same object in sequence in a single statement. An Ajax library that enables cascades would allow us to write in a style like this:

### CurryThe curry  method works by creating a closure that holds that original function and the arguments to curry. It returns a function that, when invoked, returns the result of calling that original function, passing it all of the arguments from the invocation of

curry  and the current invocation. It uses the Array concat  method to concatenate the two arrays of arguments together. Unfortunately, as we saw earlier, the arguments  array is not an array, so it does not have the concat  method. To work around that, we will apply the array slice  method on both of the arguments  arrays. This produces arrays that behave correctly with the concat  method:

### MemorizationFunctions can use objects to remember the results of previous operations, making it possible to avoid unnecessary work. This optimization is called memorization. JavaScript’s objects and arrays are very convenient for this.

## JavaScript Inheritance Patterns

### Pseudoclassical Pattern The Pseudoclassical pattern tries to replicate inheritance in a way that is familiar to those who come from a Java or C like background. By using Pseudoclassical inheritance, we attempt to recreate classic programming language’s behavior by using class wide inheritance and where objects are instances of those classes. A pattern which uses a constructor function and the new operator, combined with a prototype added to the constructor is said to be Pseudoclassical.

### Functional Pattern Another pattern you can use to achieve inheritance in JavaScript is by Douglas Crockford, called Functional inheritance. This pattern allows one object to inherit from another, take the result and augment it at the child level to achieve inheritance. What this really means, is you create an object as your parent, pass the child object to the parent to inherit / apply its properties, and return the resulting object back to the child, who can then augment its own properties to the object returned from the parent.

### Prototypal Pattern  You can also implement inheritance in JavaScript using a pure prototypal approach which is more suited to the language. As of ECMAScript 5, it is possible to create an inherited object by simply doing the following:

var male = Object.create(human); However, support is not so good for older browsers, thankfully you can augment the Object with a create method should it not exist already, which will have the same behavior as that of ECMAScript 5.

## Futures and Promises

With JavaScript usage constantly on the increase, asynchronous event-driven applications are becoming more and more popular. However, a common issue many developers face is with result-dependent operations being used in an asynchronous environment. Since each step requires the previous steps result, you will regularly see a pattern where people start nesting the callback functions within each other’s callbacks. These nested callbacks become difficult to maintain, understand and follow in larger asynchronous applications. Simple async flow such as do (A + B + C) then do D becomes an increasingly complex task.

A solution to use in this situation is the Promise / Futures pattern, which represents the result of a callback that has not happened yet. The concept is quite simple, instead of a function blocking and waiting to complete before returning the result, it simply returns immediately when invoked with an object that promises the future computation / result. This results in a non-blocking behaviour:

doA()

.then(function() { return doB(); })

.then(function() { return doC(); })

.done(function() { /\* do finished stuff here \*/ });

Writing your code using the Promise / Future pattern gives you most of the benefits of using nested callbacks, along with a cleaner, more structured code that is easier to maintain, understand and follow in most asynchronous environments.

Promises / Futures are not the ultimate solution, and there are dozens upon dozens of other solutions that all have their own benefits and drawbacks, each which should be explored in their own right for different situations.

## JavaScript Object

JavaScript’s core—most often used and most fundamental—data type is the Object data type. JavaScript has one complex data type, the Object data type, and it has five simple data types: Number, String, Boolean, Undefined, and Null. Note that these simple (primitive) data types are immutable (cannot be changed), while objects are mutable (can be changed).

### What is an Object?

An object is an unordered list of primitive data types (and sometimes reference data types) that is stored as a series of name-value pairs. Each item in the list is called a property (functions are called methods). Think of an object as a list that contains items, and each item (a property or a method) in the list is stored by a name-value pair. The property names in the example above are firstName and favoriteAuthor. And the values are “Richard” and “Conrad.” Reference Data Type and Primitive Data Types

One of the main differences between reference data type and primitive data types is reference data type’s value is stored as a reference, it is not stored directly on the variable, as a value, as the primitive data types are.

### Object Data Properties

Each data property (object property that store data) has not only the name-value pair, but also 3 attributes (the three attributes are set to true by default):

* Configurable Attribute: Specifies whether the property can be deleted or changed.
* Enumerable: Specifies whether the property can be returned in a for/in loop.
* Writable: Specifies whether the property can be changed.

Own and Inherited Properties: Objects have inherited properties and own properties. The own properties are properties that were defined on the object, while the inherited properties were inherited from the object’s Prototype object.

To find out if a property exists on an object (either as an inherited or an own property), you use the in operator:

hasOwnProperty: To find out if an object has a specific property as one of its own property, you use the hasOwnProperty method. This method is very useful because from time to time you need to enumerate an object and you want only the own properties, not the inherited ones.

Accessing Inherited Properties: Properties inherited from Object.prototype are not enumerable, so the for/in loop does not show them. However, inherited properties that are enumerable are revealed in the for/in loop iteration.

Serialize and Deserialize Objects: To transfer your objects via HTTP or to otherwise convert it to a string, you will need to serialize it (convert it to a string); you can use the JSON.stringify function to serialize your objects. To Deserialize your object (convert it to an object from a string), you use the JSON.parse function from the same json2 library.

## Prototypes in JavaScript

First, every JavaScript function has a prototype property (this property is empty by default), and you attach properties and methods on this prototype property when you want to implement inheritance. This prototype property is not enumerable; that is, it isn’t accessible in a for/in loop. But Firefox and most versions of Safari and Chrome have a \_\_proto\_\_ “pseudo” property (an alternative syntax) that allows you to access an object’s prototype property. You will likely never use this \_\_proto\_\_ pseudo property, but you should know that it exists and it is simply a way to access an object’s prototype property in some browsers.

The prototype property is used primarily for inheritance; you add methods and properties on a function’s prototype property to make those methods and properties available to instances of that function.

Consider this simple example of inheritance with the prototype property (more on inheritance later):

function PrintStuff (myDocuments) {

this.documents = myDocuments;

}

// We add the print () method to PrintStuff prototype property so that other instances (objects) can inherit it:

PrintStuff.prototype.print = function () {

console.log(this.documents);

}

// Create a new object with the PrintStuff () constructor, thus allowing this new object to inherit PrintStuff's properties and methods.

var newObj = new PrintStuff ("I am a new Object and I can print.");

// newObj inherited all the properties and methods, including the print method, from the PrintStuff function. Now newObj can call print directly, even though we never created a print () method on it.

newObj.print (); //I am a new Object and I can print.

An object’s prototype attribute points to the object’s “parent”—the object it inherited its properties from. The prototype attribute is normally referred to as the prototype object, and it is set automatically when you create a new object.To expound on this: Every object inherits properties from some other object, and it is this other object that is the object’s prototype attribute or “parent.” (You can think of the prototype attribute as the lineage or the parent). In the example code above, newObj‘s prototype is PrintStuff.prototype.

### Note All objects have attributes just like object properties have attributes. And the object attributes are prototype, class, and extensible attributes. It is this prototype attribute that we are discussing in this second example.

## Variable Scope and Hoisting

Local Variables (Function-level scope)

Unlike most programming languages, JavaScript does not have block-level scope (variables scoped to surrounding curly brackets); instead, JavaScript has function-level scope. Variables declared within a function are local variables and are only accessible within that function or by functions inside that function.

Global Variables

All variables declared outside a function are in the global scope. In the browser, which is what we are concerned with as front-end developers, the global context or scope is the window object (or the entire HTML document).

If a variable is initialized (assigned a value) without first being declared with the var keyword, it is automatically added to the global context and it is thus a global variable:

Variable Hoisting

All variable declarations are hoisted (lifted and declared) to the top of the function, if defined in a function, or the top of the global context, if outside a function.

It is important to know that only variable declarations are hoisted to the top, not variable initialization or assignments (when the variable is assigned a value).

Function Declaration Overrides Variable Declaration When Hoisted Both function declaration and variable declarations are hoisted to the top of the containing scope. And function declaration takes precedence over variable declarations (but not over variable assignment).

## Understanding Closures

What is a closure?

A closure is an inner function that has access to the outer (enclosing) function’s variables—scope chain. The closure has three scope chains: it has access to its own scope (variables defined between its curly brackets), it has access to the outer function’s variables, and it has access to the global variables.

The inner function has access not only to the outer function’s variables, but also to the outer function’s parameters. Note that the inner function cannot call the outer function’s arguments object, however, even though it can call the outer function’s parameters directly.

Closures’ Rules and Side Effects

Closures have access to the outer function’s variable even after the outer function returns:

Closures store references to the outer function’s variables;

Closures Gone Awry, Because closures have access to the updated values of the outer function’s variables, they can also lead to bugs when the outer function’s variable changes with a for loop.

## Callback Functions

We can pass functions around like variables and return them in functions and use them in other functions. When we pass a callback function as an argument to another function, we are only passing the function definition. We are not executing the function in the parameter. In other words, we aren’t passing the function with the trailing pair of executing parenthesis () like we do when we are executing a function.

And since the containing function has the callback function in its parameter as a function definition, it can execute the callback anytime.

Note that the callback function is not executed immediately. It is “called back” (hence the name) at some specified point inside the containing function’s body. So, even though the first jQuery example looked like this:

//The anonymous function is not being executed there in the parameter.

//The item is a callback function

$("#btn\_1").click(function() {

alert("Btn 1 Clicked");

});

### Callback Functions as Closures

When we pass a callback function as an argument to another function, the callback is executed at some point inside the containing function’s body just as if the callback were defined in the containing function. This means the callback is a closure. Read my post, Understand JavaScript Closures With Ease for more on closures. As we know, closures have access to the containing function’s scope, so the callback function can access the containing functions’ variables, and even the variables from the global scopE.

JavaScript callback functions are wonderful and powerful to use and they provide great benefits to your web applications and code. You should use them when the need arises; look for ways to refactor your code for Abstraction, Maintainability, and Readability with callback functions.

**JavaScript’s this Keyword Basics**

First, know that all functions in JavaScript have properties, just as objects have properties. And when a function executes, it gets the this property—a variable with the value of the object that invokes the function where this is used.

The this reference ALWAYS refers to (and holds the value of) an object—a singular object—and it is usually used inside a function or a method, although it can be used outside a function in the global scope. Note that when we use strict mode, this holds the value of undefined in global functions and in anonymous functions that are not bound to any object. This is used inside a function (let’s say function A) and it contains the value of the object that invokes function A. We need this to access methods and properties of the object that invokes function A, especially since we don’t always know the name of the invoking object, and sometimes there is no name to use to refer to the invoking object. Indeed, this is really just a shortcut reference for the “antecedent object”—the invoking object.

**The Biggest Gotcha with JavaScript “this” keyword**

If you understand this one principle of JavaScript’s this, you will understand the “this” keyword with clarity: this is not assigned a value until an object invokes the function where this is defined. Let’s call the function where this is defined the “this Function.”

Even though it appears this refers to the object where it is defined, it is not until an object invokes the this Function that this is actually assigned a value. And the value it is assigned is based exclusively on the object that invokes the this Function. this has the value of the invoking object in most circumstances. However, there are a few scenarios where this does not have the value of the invoking object. I touch on those scenarios later.

## When this Is Misunderstood

The this keyword is most misunderstood when we borrow a method that uses this, when we assign a method that uses this to a variable, when a function that uses this is passed as a callback function, and when this is used inside a closure—an inner function. We will look at each scenario and the solutions for maintaining the proper value of this in each example.

## The bind() Method

In JavaScript, we can pass functions around, return them, borrow them, and the like. And the bind () method makes it super easy to borrow methods.

**JavaScript’s Bind Allows Us to Curry a Function**

Function Currying, also known as partial function application, is the use of a function (that accept one or more arguments) that returns a new function with some of the arguments already set. The function that is returned has access to the stored arguments and variables of the outer function.

The Call, Apply, and Bind methods are indeed workhorses and should be part of your JavaScript repertoire for setting the this value in functions, for creating and executing variadic functions, and for borrowing methods and functions. As a JavaScript developer, you will likely encounter and use these functions time and again. So be sure you understand them well.

## Object-Oriented Programming

The two important principles with OOP in JavaScript are Object Creation patterns (Encapsulation) and Code Reuse patterns (Inheritance). When building applications, you create many objects, and there exist many ways for creating these objects: you can use the ubiquitous object literal pattern, for example:

var myObj = {name: "Richard", profession: "Developer"};