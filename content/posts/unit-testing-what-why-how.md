---
title: "Unit Testing | What | Why | How"
description: "A complete guide to unit testing — what it is, why it matters, testing frameworks, best practices, and how to write tests that actually help."
date: 2016-07-20
draft: false
categories:
  - tech
ShowToc: true
TocOpen: false
---

## What is Unit Testing?

A unit test is a piece of a code (usually a method) that invokes another piece of code and **checks the correctness of some assumptions afterward**. If the assumptions turn out to be wrong, the unit test has failed. A “unit” is a method or function. Unit testing will be performed against a system under test (SUT). When we test something, we refer to the thing we’re testing as the SUT.  

## Properties of a Good Unit Test  
A unit test should have the following properties:  

* It should be automated and repeatable.
* It should be easy to implement.
* Once it’s written, it should remain for future use.
* Anyone should be able to run it.
* It should run at the push of a button.
* It should run quickly.

## Key Definitions  
**Unit test** is an automated piece of code that invokes the method or class being tested and then checks some assumptions about the logical behavior of that method or class. A unit test is almost always writtenusing a unit-testing framework. It can be written easily and runs quickly. It’s fully automated, trustworthy, readable, and maintainable.  

**Refactoring** means changing a piece of code without changing its functionality. If you’ve ever renamed a method, you’ve done refactoring. If you’ve ever split a large method into multiple smaller method calls, you’ve refactored your code. The code still does the same thing, but it becomes easier to maintain, read, debug, and change.  
An external dependency is an object in your system that your code under test interacts with, and over which you have no control. (Common examples are filesystems, threads, memory, time, and so on.)  
A stub is a controllable replacement for an existing dependency (or collaborator) in the system. By using a stub, you can test your code without dealing with the dependency directly.  

**Mock object is like a stub, but it also helps you to assert something in your test.** A stub, on the other hand, can never fail your test and is strictly there to simulate various situations. Combining stubs and mocks in the same test is a powerful technique, but you must take care to have no more than one mock in each test. The rest of the fake objects should be stubs that can’t break your test.  
Stubs that produce other stubs or mocks can be a powerful way to inject fake dependencies into code that uses other objects to get its data. It’s a great technique to use with factory classes and methods. You can even have stubs that return other stubs that return other stubs and so on, but at some point you’ll wonder if it’s all worth it.  
One of the most common problems encountered by people who write tests is using mocks too much in their tests. You should rarely verify calls to fake objects that are used both as mocks and as stubs in the same test. (This is quite a narrow corner case. You verify a function was called. Because it’s still a function, it must return some value, and because you’re faking that method, you’ll need to tell the test what that value will be. This value is the part in the test that’s a stub, because it has nothing to do with asserting whether the test passes or fails.) If you see “verify” and “stub” on the same variable in the same test, you most likely are over specifying your test, which will make it more brittle.  

## Qualities of Good Tests

No matter how you organize your tests, or how many you have, they’re worth very little if you can’t trust them, maintain them, or read them. The tests that you write should have three properties that together make them good:  

* **Trustworthiness**—Developers will want to run trustworthy tests, and they’ll accept the test results with confidence. Trustworthy tests don’t have bugs, and they test the right things.
* **Maintainability**—No maintainable tests are nightmares because they can ruin project schedules, or you risk losing the tests when the project is put on a more aggressive schedule. Developers will simply stop maintaining and fixing tests that take too long to change.
* **Readability**—This means not just being able to read a test but also figuring out the problem if the test seems to be wrong. Without readability, the other two pillars fall pretty quickly. Maintaining tests becomes harder, and you can’t trust them anymore.

## Testing One Thing

**If your test contains more than a single assert, it may be testing more than one thing**. That doesn’t sound so bad until you go to name your test or consider what happens if the first assert fails. Naming a test may seem like a simple task, but if you’re testing more than one thing, giving the test a good name that indicates what is being tested becomes almost impossible. When you test just one thing, naming the test is easy.  

## Code Coverage

To ensure good coverage for your new code, use one of the automated tools (for example, NCover or Visual Studio Team System Test Edition).  

## Adding Missing Tests

Check whether you’ve added the correct test with these steps:  

1. Comment out the production code you think isn’t being covered.
2. Run all the tests.
3. If all the tests pass, you’re missing a test or are testing the wrong thing. Otherwise there would have been a test somewhere that was expecting that line to be called, or some resulting consequence of that line of code to be true, and that missing test would now fail.
4. Once you’ve found a missing test, you’ll need to add it. Keep the code commented out and write a new test that fails, proving that the code you’ve commented is missing.
5. Uncomment the code you commented before.
6. The test you wrote should now pass. You’ve detected and added a missing test!
7. If the test still fails, it means the test may have a bug or is testing the wrong thing. Modify the test until it passes. Now you’ll want to see that the test is OK, making sure it fails when it should, and doesn’t just pass when it should. To make sure the test fails when it should, reintroduce the bug into your code (commenting out the line of production code) and see if the test indeed fails.
8. As an added confidence booster, you might also try replacing various parameters or internal variables in your method under test with constants (making a bool always true to see what happens, for example). The trick to all this testing is making sure it doesn’t take up too much time to make it worth your while. That’s what the next section is about: maintainability.

## Testing Private/Protected Methods  
Private or protected methods are usually private for a good reason in the developer’s mind. Sometimes it’s to hide implementation details, so that the implementation can change later without the end functionality changing. It could also be for security-related or IP-related reasons (obfuscation, for example).  

When you test a private method, you’re testing against a contract internal to the system, which may well change. Internal contracts are dynamic, and they can change when you refactor the system. When they change, your test could fail because some internal work is being done differently, even though the overall functionality of the system remains the same. For testing purposes, the public contract (the overall functionality) is all that you need to care about. Testing the functionality of private methods may lead to breaking tests, even though the overall functionality is correct.  

**If a method is worth testing, it might be worth making it public, static, or at least internal**, and defining a public contract against any user of it. In some cases, the design may be cleaner if you put the method in a different class altogether. We’ll look at these approaches in a moment.  
Does this mean there should eventually be no private methods in the code base? No. **With test-driven development, we usually write tests against methods that are public, and those public methods are later refactored into calling smaller, private methods**. All the while, the tests against the public methods continue to pass.  

**Making a method public isn’t necessarily a bad thing**. It may seem to go against the object-oriented principles you were raised on, but wanting to test a method means that the method has a known behavior or contract against the calling code. By making it public, you’re making this official. By keeping the method private, you tell all the developers who come after you that they can change the implementation of the method without worrying about unknown code that uses it, because it only serves as part of a larger group of things that together make up a contract to the calling code.  

## Extracting Methods

If your method contains a lot of logic that can stand on its own, or it uses state in the class that’s only relevant to the method in question, it may be a good idea to extract the method into a new class, with a specific role in the system. You can then test that class separately.  

## Making Methods Static

If your method doesn’t use any of its class’s variables, you might want to refactor the method by making it static. That makes it much more testable, but also states that this method is a sort of utility method that has a known public contract specified by its name.  

## Making Methods Internal

When all else fails, and you can’t afford to expose the method in an “official” way, you might want to make it internal, and then use the [InternalsVisibleTo("TestAssembly")] attribute on the production code assembly so that tests can still call that method. This is my least favorite approach, but sometimes there’s no choice (perhaps because of security reasons, lack of control over the code’s design, and so on).  

**Setting up mocks and fakes in the setup method** It’s not always a bad idea to use the setup method to create mocks and fake objects, but it’s important that only those mocks and fakes that are used in all the tests in the class are initialized in the setup method, or it will become hard to read and maintain.  

**My preference is to have each test create its own mocks and stubs by calling helper methods within the test, so that the reader of the test knows exactly what is going on, without needing to jump from test to setup to understand the full picture.**  

## Test Isolation

The lack of test isolation is the biggest single cause of test blockage I’ve seen while consulting and working on unit tests. The basic concept is that a test should always run in its own little world, isolated from even the knowledge that other tests out there may do similar or different things.  

## Readable Tests  
### Naming Conventions

Naming standards are important because they give us comfortable rules and templates that outline what we should explain about the test.  

### Test Name Structure

The name of the method being tested—This is essential, so that you can easily see where the tested logic is. Having this as the first part of the test name allows easy navigation and as-you-type intenseness (if your IDEsupports it) in the test class.  
The scenario under which it’s being tested—This part gives us the “with” part of the name: “When I call method X with a null value, then it should do Y.”  
The expected behavior when the scenario is invoked—This part specifies in plain English what the method should do or return, or how it should behave, based on the current scenario: “When I call method X with a null value, then it should do Y.”  
A common way to write these three parts of the test name is to separate them with underscores, like this: MethodUnderTest\_Scenario\_Behavior().  

## Why Tests Matter  
You may be sure your code works fine, but what about other people’s code? How do you know it works? How do they know your code works and that they haven’t broken anything when they make changes? Remember that coding is just the first step in the life of the code. Most of its life, the code will be in maintenance mode. You need to make sure it will tell people when it breaks, using unit tests.  

A study held by Curtis, Krasner, and Iscoe showed that most defects don’t come from the code itself, but **result from miscommunication between** people, requirements that keep changing, and a lack of application domain knowledge. Even if you’re the world’s greatest coder, chances are that, if someone tells you to code the wrong thing, you’ll do it. And when you need to change it, you’ll be glad you have tests for everything else to make sure you don’t break it.  

## Test-Driven Development

I personally see a lot of value in TDD, and many people find it productive and beneficial, but others find that writing the tests after the code is good enough for them. You can make your own choice.  

## Design for Testability

There are several design points that make code much more testable. Robert C. Martin has a nice list of design goals for object-oriented.  

* Make methods virtual by default
* Make classes no sealed by default
* Avoid instantiating concrete classes inside methods with logic
* If your method relies on a logger, for example, don’t instantiate the logger inside the method. Get it from a simple factory method, and make that factory method virtual so that you can override it later and control what logger your method works against. Or use constructor injection instead of a virtual method.
* Avoid direct calls to static methods
* Try to abstract any direct dependencies that would be hard to replace at runtime. Abstracting a static method away using the Extract and Override refactoring (shown in section 3.4.6 of chapter 3) is one way to deal with these situations.
* A more extreme approach is to avoid using any static methods whatsoever. That way, every piece of logic is part of an instance of a class that makes that piece of logic more easily replaceable. Lack of replace ability is one of the reasons some people who do unit testing or TDD dislike singletons; they act as a public shared resource that is static, and it’s hard to override them.
* Avoiding static methods altogether may be too difficult, but trying to minimize the number of singletons or static methods in your application will make things easier for you while testing.
* Avoid constructors and static constructors that do logic
* Things like configuration-based classes are often made static classes or singletons because so many parts of the application use them. That makes them hard to replace during a test
* If you’re planning to use a singleton in your design, separate the logic of the singleton class and the logic that makes it a singleton

**References**  

* <http://www.hanselman.com/blog/ListOfNETDependencyInjectionContainersIOC.aspx>
* <http://butunclebob.com/ArticleS>