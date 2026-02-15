---
title: "Java Architecture"
description: "Understanding Java's architecture — the JVM, class loader, bytecode, garbage collection, and how Java achieves platform independence."
date: 2016-07-22
draft: false
categories:
  - tech
ShowToc: true
TocOpen: false
tags:
  - java
  - architecture
  - jvm
cover:
  image: "images/covers/java-architecture-cover.svg"
  alt: "Cover image"
  relative: false
---

**Introduction to Java's Architecture**

Java's architecture arises out of four distinct but interrelated technologies:

* the Java programming language
* the Java class file format
* the Java Application Programming Interface
* the Java virtual machine

</a>
</figure>

# Architectural Tradeoffs

</a>
</figure>

* Performance
* The AWT attempts to give your program a user interface that adopts the native look on each platform. Nevertheless, you might find it difficult to design a user interface in which the components interact in a way that *feels* native on every platform, even though the individual components may have the native look
* One last tradeoff stems from the dynamically linked nature of Java programs combined with the close relationship between Java class files and the Java programming language. Because Java programs are dynamically linked, the references from one class file to another are symbolic. In a statically-linked executable, references between classes are direct pointers or offsets. Inside a Java class file, by contrast, a reference to another class spells out the name of the other class in a text string. If the reference is to a field, the field's name and *descriptor* (the field's type) are also specified. If the reference is to a method, the method's name and descriptor (the method's return type, number and types of its arguments) are specified. Moreover, not only do Java class files contain symbolic references to the fields and methods of other classes, they also contain symbolic references to their own fields and methods. Java class files also may contain optional debugging information that includes the names and types of local variables. A class file's symbolic information, and the close relationship between the bytecode instruction set and the Java language, make it quite easy to decompile Java class files back into Java source. This in turn makes it quite easy for your competitors to borrow heavily from your hard work.

Platform Independence  

  
Seven Steps to Platform Independence

Java's architecture allows you to choose between platform independence and other concerns. You make your choice by the way in which you write your program. If your goal is to take advantage of platform- specific features not available through the Java API, to interact with a legacy system, to use an existing library written not written in Java, or to maximize the execution speed of your program, you can use native methods to help you achieve that goal. In such cases, your programs will have reduced platform independence, and that will usually be acceptable. If, on the other hand, your goal is platform independence, then you should follow certain rules when writing your program. The following seven steps outline one path you can take to maximize your program's portability:

1. Choose a set of host computers and devices that you will claim your program runs on (your "target hosts").
2. Choose an edition and version of the Java Platform that you feel is well enough distributed among your target hosts. Write your program to run on this version of the Java Platform.
3. For each target host, choose a set of Java Platform implementations that you will claim your program runs on (your "target runtimes").
4. Write your program so that it accesses the host computer only through the standard runtime libraries of the Java API. (Don't invoke native methods, or use vendor-specific libraries that invoke native methods.)
5. Write your program so that it doesn't depend for correctness on timely finalization by the garbage collector or on thread prioritization.
6. Strive to design a user interface that works well on all of your target hosts.
7. Test your program on all of your target runtimes and all of your target hosts.

Security

Java's security model is focused on protecting users from hostile programs downloaded from untrusted sources across a network. To accomplish this goal, Java provides a customizable "sandbox" in which Java programs run. A Java program **must play only inside its sandbox**.The sandbox for untrusted Java applets,

* Reading or writing to the local disk

* Making a network connection to any host

* Creating a new process

* Loading a new dynamic library and directly calling a native method

**The sandbox is pervasive**

The fundamental components responsible for Java's sandbox are:

* Safety features built into the Java virtual machine (and the language)
* The class loader architecture
* The class file verifier
* The security manager and the Java API

**The sandbox is customizable**

To customize a sandbox, you write a class that descends from**java.lang.SecurityManager****.**

**Safety features built into the JVM**

Several built-in security mechanisms are operating as Java virtual machine bytecodes. The mechanisms are:

* Type-safe reference casting
* Structured memory access (no pointer arithmetic)
* Automatic garbage collection (can't explicitly free allocated memory)
* Array bounds checking
* Checking references for null

**Unspecified memory layout**

When a thread invokes a native method, that thread leaps outside the sandbox. The security model for native methods therefore is the same traditional approach to computer security described earlier: You have to trust a native method before you call it.

**Structured error handling**

Instead of crashing, the JVM can throw an exception or an error, which may result in the death of the offending thread but shouldn't crash the system.

**The class loader** concept, one of the cornerstones of the Java virtual machine, describes the behavior of converting a named class into the bits responsible for implementing that class. Because class loaders exist, the Java run time does not need to know anything about files and file systems when running Java programs. At its simplest, a class loader creates a flat name space of class bodies that are referenced by a string name. The method definition is:**Class r = loadClass(String className, boolean resolveIt);** All Java virtual machines include **one class loader** that is embedded in the virtual machine. This embedded loader is called the **primordial class loader**. It is somewhat special because the virtual machine assumes that it has access to a repository oftrusted classes which can be run by the VM without verification.

A non-primordial class loader: The Java virtual machine has hooks in it to allow a user-defined class loader to be used in place of the primordial one.

**Security considerations**

In our simple class loader, if the primordial class loader couldn't find the class, we loaded it from our private repository. What happens when that repository contains the class java.lang.FooBar ? There is no class named java.lang.FooBar, but we could install one by loading it from the class repository. This class, by virtue of the fact that it would have access to any package-protected variable in the java.lang package, can manipulate some sensitive variables so that later classes could subvert security measures. Therefore, one of the jobs of any class loader is to protect the system name space.

**Class loaders** provide the mechanism that allows Java applications, whether they are Web browsers or EMACs replacements, to be dynamically extended in a controlled way with additional Java code. The applications of class loaders are bounded only by your imagination.

**What is the Java Virtual Machine? Why is it here?**

The Java Virtual Machine, or JVM, is an **abstract computer** that runs compiled Java programs.

The JVM is lean because it is small when implemented in software. It was designed to be small so that it can fit in as many places as possible -- places like TV sets, cell phones, and personal computers. The JVM is mean because it of its ambition. "Ubiquity!" is its battle cry. It wants to be everywhere, and its success is indicated by the extent to which programs written in Java will run everywhere.

**Java bytecodes**

Java programs are compiled into a form called Java byte bytecodes  The Java compiler reads Java language source (.java) files, translates the source into Java bytecodes, and places the bytecodes into class (.class) files. The compiler generates one class file per class in the source.

A mnemonic is defined for each bytecode instruction. The mnemonics can be thought of as an assembly language for the JVM. For example, there is an instruction that will cause the JVM to push a zero onto the stack. The mnemonic for this instruction is iconst\_0, and its bytecode value is 60 hex. This instruction takes no operands. Another instruction causes program execution to unconditionally jump forward or backward in memory. This instruction requires one operand, a 16-bit signed offset from the current memory location. By adding the offset to the current memory location, the JVM can determine the memory location to jump to. The mnemonic for this instruction is goto, and its bytecode value is a7 hex.

**Virtual parts**

The "virtual hardware" of the Java Virtual Machine can be divided into four basic parts: **the registers, the stack, the garbage-collected heap, and the method area**. These parts are abstract, just like the machine they compose, but they must exist in some form in every JVM implementation. The size of an address in the JVM is 32 bits.The JVM can, therefore, address up to 4 gigabytes (2 to the power of 32) of memory, with each memory location containing one byte. Each register in the JVM stores one 32-bit address. The stack, the garbage-collected heap, and the method area reside somewhere within the 4 gigabytes of addressable memory. The exact location of these memory areas is a decision of the implementor of each particular JVM.  

References:  
<https://www.artima.com/insidejvm/ed2/index.html>