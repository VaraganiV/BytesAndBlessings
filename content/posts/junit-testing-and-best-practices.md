---
title: "JUnit Testing And Best Practices"
description: "What is unit testing and why does it matter? Learn JUnit best practices, test structure, and how to write effective automated tests."
date: 2020-08-29
draft: false
categories:
  - tech
tags:
  - junit
  - unittesting
ShowToc: true
TocOpen: false
cover:
  image: "images/covers/junit-testing-and-best-practices-cover.svg"
  alt: "Cover image"
  relative: false
---

A “unit” is a method or function. **Unit test** is a piece of a code (usually a method) that invokes another piece of code and **checks the correctness of some assumptions afterward**.  If the assumptions turn out to be wrong, the unit test has failed.

Junit was developed by **Kent Beck** and **Erich Gamma**. Its first version was released in **1997**. JUnit is a unit testing framework for Java programming language. JUnit promotes the idea of "first testing then coding", which emphasizes on setting up the test data for a piece of code that can be tested first and then implemented. This approach is like "test a little, code a little, test a little, code a little."

Best Practices

Some best practices with the aim of providing reliable, extensible, fast and readable unit test cases.

Unit test runs completely in memory

Unit tests which access database or read from filesystems are slow and unreliable. They are better tested via functional tests.

Unit test method to perform exactly one assertion

With more assertions in a test method, determining the failure is difficult and if an unchecked exception occurs, the assertions after the exception do not happen

## Unit test should be independent to all the others

Dependent unit test cases will prevent from identifying the cause of failure.

## Unit test should have exact matching when mocking framework

Instead of using any, configure with exact parameters

Mock all external services and state

Relying on state date will impact / influence other tests and also add the dependency to run the tests in a defined order. It will also take time for debugging failure.

## Name unit tests appropriately

Use convention that includes the method and condition to be tested

## Don’t unit-test configuration settings

Configurations are bound to change with the environment.

With unit testing, it's possible to detect the changes that break the design contract, rerunning the entire suite after every build gives confidence that new code is not breaking the functionality. Following the best practices will explicitly express the intent, isolate, self-checking of the test cases implemented.