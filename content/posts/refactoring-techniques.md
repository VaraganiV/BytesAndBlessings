---
title: "Refactoring | techniques"
description: "Essential refactoring techniques — Extract Method, Inline Method, Replace Temp with Query, and more ways to clean up your codebase."
date: 2016-07-22
draft: false
categories:
  - tech
ShowToc: true
TocOpen: false
---

The refactoring techniques in this ***group streamline methods, remove code duplication, and pave the way for future improvements***.

|  |  |  |
| --- | --- | --- |
| Extract Method | You have a code fragment that can be grouped together. | Move this code to a separate new method (or function) and replace the old code with a call to the method. |
| Inline Method | When a method body is more obvious than the method itself, use this technique. | Replace calls to the method with the method's content and delete the method itself. |
| Extract Variable | You have an expression that is hard to understand. | Place the result of the expression or its parts in separate variables that are self-explanatory. |
| Inline Temp | You have a temporary variable that is assigned the result of a simple expression and nothing more. | Replace the references to the variable with the expression itself. |
| Replace Temp with Query | You place the result of an expression in a local variable for later use in your code. | Move the entire expression to a separate method and return the result from it. Query the method instead of using a variable. Incorporate the new method in other methods, if necessary. |
| [Split Temporary Variable](https://sourcemaking.com/refactoring/split-temporary-variable) | You have a local variable that is used to store various intermediate values inside a method (except for cycle variables). | Use different variables for different values. Each variable should be responsible for only one particular thing |
| [Remove Assignments to Parameters](https://sourcemaking.com/refactoring/remove-assignments-to-parameters) | Some value is assigned to a parameter inside method's body. | Use a local variable instead of a parameter. |
| [Replace Method with Method Object](https://sourcemaking.com/refactoring/replace-method-with-method-object) | You have a long method in which the local variables are so intertwined that you cannot apply [Extract Method](https://sourcemaking.com/refactoring/extract-method). | Transform the method into a separate class so that the local variables become fields of the class. Then you can split the method into several methods within the same class. |
| [Substitute Algorithm](https://sourcemaking.com/refactoring/substitute-algorithm) | You want to replace an existing algorithm with a new one? | Replace the body of the method that implements the algorithm with a new algorithm |

These refactoring techniques show **how to safely move functionality between classes, create new classes, and hide implementation details from public access.**

|  |  |  |
| --- | --- | --- |
| [Move Method](https://sourcemaking.com/refactoring/move-method) | A method is used more in another class than in its own class. | Create a new method in the class that uses the method the most, then move code from the old method to there. Turn the code of the original method into a reference to the new method in the other class or else remove it entirely. |
| [Move Field](https://sourcemaking.com/refactoring/move-field) | A field is used more in another class than in its own class. | Create a field in a new class and redirect all users of the old field to it. |
| [Extract Class](https://sourcemaking.com/refactoring/extract-class) | When one class does the work of two, awkwardness results. | Instead, create a new class and place the fields and methods responsible for the relevant functionality in it. |
| [Inline Class](https://sourcemaking.com/refactoring/inline-class) | A class does almost nothing and is not responsible for anything, and no additional responsibilities are planned for it. | Move all features from the class to another one. |
| [Hide Delegate](https://sourcemaking.com/refactoring/hide-delegate) | The client gets object B from a field or method of object А. Then the client calls a method of object B. | Create a new method in class A that delegates the call to object B. Now the client does not know about, or depend on, class B. |
| [Remove Middle Man](https://sourcemaking.com/refactoring/remove-middle-man) | A class has too many methods that simply delegate to other objects. | Delete these methods and force the client to call the end methods directly. |
| [Introduce Foreign Method](https://sourcemaking.com/refactoring/introduce-foreign-method) | A utility class does not contain the method that you need and you cannot add the method to the class. | Add the method to a client class and pass an object of the utility class to it as an argument. |
| [Introduce Local Extension](https://sourcemaking.com/refactoring/introduce-local-extension) | A utility class does not contain some methods that you need. But you cannot add these methods to the class. | Create a new class containing the methods and make it either the child or wrapper of the utility class. |

These refactoring techniques **help with data handling, replacing primitives with rich class functionality.** Another important result is untangling of class associations, which makes classes more portable and reusable.

|  |  |  |
| --- | --- | --- |
| [Self Encapsulate Field](https://sourcemaking.com/refactoring/self-encapsulate-field) | You use direct access to private fields inside a class. | Create a getter and setter for the field, and use only them for accessing the field. |
| [Replace Data Value with Object](https://sourcemaking.com/refactoring/replace-data-value-with-object) | A class (or group of classes) contains a data field. The field has its own behavior and associated data. | Create a new class, place the old field and its behavior in the class, and store the object of the class in the original class. |
| [Change Value to Reference](https://sourcemaking.com/refactoring/change-value-to-reference) | So you have many identical instances of a single class that you need to replace with a single object. | Convert the identical objects to a single reference object |
| [Change Reference to Value](https://sourcemaking.com/refactoring/change-reference-to-value) | You have a reference object that is too small and infrequently changed to justify managing its life cycle. | Turn it into a value object. |
| [Replace Array with Object](https://sourcemaking.com/refactoring/replace-array-with-object) | You have an array that contains various types of data. | Replace the array with an object that will have separate fields for each element. |
| [Duplicate Observed Data](https://sourcemaking.com/refactoring/duplicate-observed-data) | Is domain data stored in classes responsible for the GUI? | Then it is a good idea to separate the data into separate classes, ensuring connection and synchronization between the domain class and the GUI. |
| [Change Unidirectional Association to Bidirectional](https://sourcemaking.com/refactoring/change-unidirectional-association-to-bidirectional) | You have two classes that each need to use the features of the other, but the association between them is only unidirectional. | Add the missing association to the class that needs it. |
| [Change Bidirectional Association to Unidirectional](https://sourcemaking.com/refactoring/change-bidirectional-association-to-unidirectional) | You have a bidirectional association between classes, but one of the classes does not use the other's features. | Remove the unused association. |
| [Replace Magic Number with Symbolic Constant](https://sourcemaking.com/refactoring/replace-magic-number-with-symbolic-constant) | Your code uses a number that has a certain meaning to it. | Replace this number with a constant that has a human-readable name explaining the meaning of the number. |
| [Encapsulate Field](https://sourcemaking.com/refactoring/encapsulate-field) | You have a public field. | Make the field private and create access methods for it. |
| [Encapsulate Collection](https://sourcemaking.com/refactoring/encapsulate-collection) | A class contains a collection field and a simple getter and setter for working with the collection. | Make the getter-returned value read-only and create methods for adding/deleting elements of the collection. |
| [Replace Type Code with Class](https://sourcemaking.com/refactoring/replace-type-code-with-class) | A class has a field that contains type code. The values of this type are not used in operator conditions and do not affect the behavior of the program | Create a new class and use its objects instead of the type code values. |
| [Replace Type Code with Subclasses](https://sourcemaking.com/refactoring/replace-type-code-with-subclasses) | You have a coded type that directly affects program behavior (values of this field trigger various code in conditionals). | Create subclasses for each value of the coded type. Then extract the relevant behaviors from the original class to these subclasses. Replace the control flow code with polymorphism. |
| [Replace Type Code with State/Strategy](https://sourcemaking.com/refactoring/replace-type-code-with-state-strategy) | You have a coded type that affects behavior but you cannot use subclasses to get rid of it. | Replace type code with a state object. If it is necessary to replace a field value with type code, another state object is "plugged in". |
| [Replace Subclass with Fields](https://sourcemaking.com/refactoring/replace-subclass-with-fields) | You have subclasses differing only in their (constant-returning) methods. | Replace the methods with fields in the parent class and delete the subclasses |