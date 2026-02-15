---
title: "Bad Code | Smells"
description: "Identify the five categories of bad code smells — Bloaters, Object-Orientation Abusers, Change Preventers, Dispensables, and Couplers."
date: 2016-07-22
draft: false
categories:
  - tech
ShowToc: true
TocOpen: false
---

## Bloaters

**Bloaters are code**, methods and classes that have increased to such gargantuan proportions that they are hard to work with.

* Long Method: A method contains too many lines of code. Generally, any method longer than ten lines should make you start asking questions.
* Large Class: A class contains many fields/methods/lines of code.
* Primitive Obsessions: Using primitives instead of small tasks like String Names as fields in Arrays
* Long Parameter list: More than 3 or 4 parameters to a function
* Data clumps: Different parts of the code contain identical group of variables [parameters for connecting to DB]

## Object-Oriented Abusers

**Object oriented Abusers**: All these smells are incomplete or incorrect application of object-oriented programming principles.

* *Switch Statements*: if you have complex switch statements As a rule of thumb, when you see `switch` you should think of polymorphism.
* Temporary fields get their values (and thus are needed by objects) only under certain circumstances. Outside of these circumstances, they are empty. Temporary fields and all code operating on them can be put in a separate class via [Extract Class](https://sourcemaking.com/refactoring/extract-class). In other words, you are creating a method object, achieving the same result as if you would perform [Replace Method with Method Object](https://sourcemaking.com/refactoring/replace-method-with-method-object).
* If a subclass uses only some of the methods and properties inherited from its parents, the hierarchy is off-kilter. The unneeded methods may simply go unused or be redefined and give off exceptions. If inheritance makes no sense and the subclass really does have nothing in common with the superclass, eliminate inheritance in favor of [Replace Inheritance with Delegation](https://sourcemaking.com/refactoring/replace-inheritance-with-delegation).

* Alternative classes with different behaviors: Two classes perform identical functions but have different method names.

## Change Preventers

**Change Preventers**: These smells mean that if you need to change something in one place in your code, you have to make many changes in other places too. Program development becomes much more complicated and expensive as a result.

* Divergent Change: Often these divergent modifications are due to poor program structure or "copypasta programming”. Split up the behavior of the class via [Extract Class](https://sourcemaking.com/refactoring/extract-class)
* Shotgun Surgery:Making any modifications requires that you make many small changes to many different classes. A single responsibility has been split up among a large number of classes.
* Parallel Inheritance Hierarchies: Whenever you create a subclass for a class, you find yourself needing to create a subclass for another class.

## Dispensables

**A dispensable** is something pointless and unneeded whose absence would make the code cleaner, more efficient and easier to understand.

* Comments are usually created with the best of intentions, when the author realizes that his or her code is not intuitive or obvious. In such cases, comments are like a deodorant masking the smell of fishy code that could be improved. The best comment is a good name for a method or class.
* Duplicate Code: If the same code is found in two or more methods in the same class: use [Extract Method](https://sourcemaking.com/refactoring/extract-method) and place calls for the new method in both places.
* Lazy classes: Understanding and maintaining classes always costs time and money. So if a class doesn't do enough to earn your attention, it should be deleted.
* A data class refers to a class that contains only fields and crude methods for accessing them (getters and setters). It's a normal thing when a newly created class contains only a few public fields (and maybe even a handful of getters/setters).
* Dead Code: A variable, parameter, field, method or class is no longer used (usually because it is obsolete)
* Speculative Generality: These are unused class, methods fields or parameters.

## Couplers

**Couplers**: All the smells in this group contribute to excessive coupling between classes or show what happens if coupling is replaced by excessive delegation.

* Feature Envoy: A method accesses the data of another object more than its own data.
* Inappropriate Intimacy: 

  One class uses the internal fields and methods of another class.
* Message Chains: a->b->c->D
* Middle main: if a class performs only task of delegation

## Incomplete Library

**Incomplete Library**: Sooner or later, [libraries](https://en.wikipedia.org/wiki/Library_(computing)) stop meeting user needs. The only solution to the problem – changing the library – is often impossible since the library is read-only.