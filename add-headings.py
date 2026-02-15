#!/usr/bin/env python3
"""
Script to add markdown H2 headings to blog posts based on content structure.
"""

import os
import re
from pathlib import Path


def get_posts_dir():
    """Get the posts directory path."""
    return Path(os.path.expanduser("~/Factory/BytesAndBlessings/site/content/posts"))


def read_file(filepath):
    """Read file content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(filepath, content):
    """Write content to file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def extract_frontmatter(content):
    """Extract frontmatter and body from markdown."""
    match = re.match(r'^(---\n.*?\n---\n)(.*)', content, re.DOTALL)
    if match:
        return match.group(1), match.group(2)
    return "", content


def add_headings_bad_code_smells(body):
    body = body.replace("**Bloaters are code**,", "## Bloaters\n\n**Bloaters are code**,")
    body = body.replace("**Object oriented Abusers**:", "## Object-Oriented Abusers\n\n**Object oriented Abusers**:")
    body = body.replace("**Change Preventers**:", "## Change Preventers\n\n**Change Preventers**:")
    body = body.replace("**A dispensable** is", "## Dispensables\n\n**A dispensable** is")
    body = body.replace("**Couplers**:", "## Couplers\n\n**Couplers**:")
    body = body.replace("**Incomplete Library**:", "## Incomplete Library\n\n**Incomplete Library**:")
    return body


def add_headings_burning_out(body):
    lines = body.split('\n')
    result = []
    h1 = h2 = False
    for line in lines:
        if not h1 and 'Are you burning out' in line:
            result.append("## Signs of Burnout\n")
            h1 = True
        elif not h2 and 'Try' in line and 'Try .....' in body[body.find(line):]:
            result.append("## Recovery Steps\n")
            h2 = True
        result.append(line)
    return '\n'.join(result)


def add_headings_career_sutras(body):
    body = body.replace("Do you feel, you're struggling", "## The Career Plateau\n\nDo you feel, you're struggling")
    body = body.replace("So, are some key sutras", "## Career Sutras\n\nSo, are some key sutras")
    return body


def add_headings_detox_your_thoughts(body):
    body = body.replace("**Detoxing your thoughts**", "## What Is Thought Detox?\n\n**Detoxing your thoughts**")
    body = body.replace("**Negative thoughts can be harmless**", "## Letting Go of Negative Thoughts\n\n**Negative thoughts can be harmless**")
    body = body.replace("**Get a paper and write down", "## A Practical Exercise\n\n**Get a paper and write down")
    return body


def add_headings_expanding_columns_in_wpf(body):
    body = body.replace("We were supposed to handle", "## The Problem\n\nWe were supposed to handle")
    body = body.replace("How did we achieve this", "## The Solution\n\nHow did we achieve this")
    return body


def add_headings_faster(body):
    lines = body.split('\n')
    result = []
    done = False
    for line in lines:
        if not done and line.startswith("1. Don't let"):
            result.append("## Learning Principles\n")
            done = True
        result.append(line)
    return '\n'.join(result)


def add_headings_javascript(body):
    replacements = [
        ("**Why JavaScript?**", "## Why JavaScript?"),
        ("**JavaScript : Object System**", "## JavaScript Object System"),
        ("**What is this Execution Context ? and why i need to know it?**", "## Execution Context"),
        ("**There are 5 key points to remember about the execution stack:**", "## Execution Stack Key Points"),
        ("**Execution Context in Detail**", "## Execution Context in Detail"),
        ("**Here is a pseudo-overview of how the interpreter evaluates the code:**", "## Interpreter Code Evaluation"),
        ("**A Word On Hoisting**", "## Hoisting"),
        ("**Why can we access foo before we have declared it?**", "### Why Can We Access Foo Before Declaration?"),
        ("**Foo is declared twice, why is foo shown to be function and not undefined or string?**", "### Why Is Foo a Function?"),
        ("**Why is bar undefined?**", "### Why Is Bar Undefined?"),
        ("**Identifier Resolution and Closures in the JavaScript Scope Chain**", "## Scope Chain and Closures"),
        ("**How does this work with closures?**", "## How Closures Work"),
        ("**When to use Closures?**", "## When to Use Closures"),
        ("**When not to use Closures ?**", "## When Not to Use Closures"),
        ("****Analyzing JavaScript****", "## Analyzing JavaScript"),
        ("**Integer:**", "### Integer"), ("**Strings:**", "### Strings"),
        ("**Objects:**", "### Objects"), ("**Function Objects:**", "### Function Objects"),
        ("****Cascade**:**", "### Cascade"), ("****Curry**:**", "### Curry"),
        ("**Memorization:**", "### Memorization"),
        ("**JavaScript Inheritance Patterns**", "## JavaScript Inheritance Patterns"),
        ("**Pseudoclassical pattern:**", "### Pseudoclassical Pattern"),
        ("**Functional pattern:**", "### Functional Pattern"),
        ("**Prototypal pattern:**", "### Prototypal Pattern"),
        ("**Futures and Promises in JavaScript**", "## Futures and Promises"),
        ("**JavaScript Object:**", "## JavaScript Object"),
        ("**What is an Object**", "### What is an Object?"),
        ("**Object Data Properties Have Attributes**", "### Object Data Properties"),
        ("**JavaScript Prototype in Plain Language**", "## Prototypes in JavaScript"),
        ("**Note:**", "### Note"),
        ("**JavaScript Variable Scope and Hoisting Explained**", "## Variable Scope and Hoisting"),
        ("**Understand JavaScript Closures With Ease**", "## Understanding Closures"),
        ("**Understand JavaScript Callback Functions and Use Them**", "## Callback Functions"),
        ("**Callback Functions Are Closures**", "### Callback Functions as Closures"),
        ("**JavaScript's this Keyword Basics**", "## The this Keyword"),
        ('**The Biggest Gotcha with JavaScript "this" keyword**', "## Understanding this Values"),
        ("**When this is most misunderstood and becomes tricky**", "## When this Is Misunderstood"),
        ("**Bind () Allows us to Borrow Methods**", "## The bind() Method"),
        ("**JavaScript's Bind Allows Us to Curry a Function**", "## Function Currying with bind()"),
        ("**OOP in JavaScript**", "## Object-Oriented Programming"),
    ]
    for old, new in replacements:
        body = body.replace(old, new)
    return body


def add_headings_kubernetes_learning_path(body):
    body = body.replace("Why Kubernetes\n", "## Why Kubernetes\n")
    body = body.replace("This learning path will focus on", "## Learning Path Overview\n\nThis learning path will focus on")
    return body


def add_headings_kuberneties_learning_path_components(body):
    body = body.replace("When we deploy Kubernetes, we get a cluster.", "## Kubernetes Cluster Overview\n\nWhen we deploy Kubernetes, we get a cluster.")
    body = body.replace("Lets understand some core components", "## Core Components\n\nLets understand some core components")
    body = body.replace("\nAPI Server\n", "\n## API Server\n")
    body = body.replace("\netcd\n", "\n## etcd\n")
    body = body.replace("\nScheduler\n", "\n## Scheduler\n")
    body = body.replace("\nController\n", "\n## Controller\n")
    body = body.replace("\nkubelet\n", "\n## kubelet\n")
    body = body.replace("\nkube-proxy\n", "\n## kube-proxy\n")
    body = body.replace("\nPOD\n", "\n## POD\n")
    return body


def add_headings_kuberneties_learning_path_deployments(body):
    body = body.replace("A Kubernetes deployment is a resource object", "## What Is a Deployment?\n\nA Kubernetes deployment is a resource object")
    body = body.replace("\nCreating a Deployment\n", "\n## Creating a Deployment\n")
    body = body.replace("\nUpdating a Deployment\n", "\n## Updating a Deployment\n")
    body = body.replace("\nRolling Back a Deployment\n", "\n## Rolling Back a Deployment\n")
    body = body.replace("\nScaling a Deployment\n", "\n## Scaling a Deployment\n")
    body = body.replace("\nPausing and Resuming a Deployment\n", "\n## Pausing and Resuming a Deployment\n")
    body = body.replace("\nDeployment status\n", "\n## Deployment Status\n")
    body = body.replace("\nFailed deployments\n", "\n## Failed Deployments\n")
    return body


def add_headings_kuberneties_learning_path_pods(body):
    body = body.replace("\nWhat are PODS\n", "\n## What Are Pods?\n")
    body = body.replace("\nPOD Template\n", "\n## Pod Template\n")
    body = body.replace("\nPOD Lifecycle\n", "\n## Pod Lifecycle\n")
    body = body.replace("\nContainer States\n", "\n## Container States\n")
    body = body.replace("\nContainer Restart Policy\n", "\n## Container Restart Policy\n")
    body = body.replace("\nPOD Condition\n", "\n## Pod Condition\n")
    body = body.replace("\nPOD Readiness\n", "\n## Pod Readiness\n")
    body = body.replace("\nContainer Probe\n", "\n## Container Probe\n")
    body = body.replace("\nTermination of Pods\n", "\n## Termination of Pods\n")
    body = body.replace("\nForced Pod termination\n", "\n## Forced Pod Termination\n")
    body = body.replace("\nGarbage collection of failed Pods\n", "\n## Garbage Collection of Failed Pods\n")
    return body


def add_headings_kuberneties_learning_path_replicaset(body):
    body = body.replace("A ReplicaSet's purpose is to maintain", "## What Is a ReplicaSet?\n\nA ReplicaSet's purpose is to maintain")
    body = body.replace("\nWhen to use a ReplicaSet\n", "\n## When to Use a ReplicaSet\n")
    body = body.replace("\nExample\n", "\n## Example\n")
    body = body.replace("\nAlternatives to ReplicaSet\n", "\n## Alternatives to ReplicaSet\n")
    body = body.replace("\nWhat is ReplicationController\n", "\n## ReplicationController\n")
    return body


def add_headings_mahalaya_paksham(body):
    body = body.replace("It is believed that after death,", "## The Journey of the Soul\n\nIt is believed that after death,")
    body = body.replace("Mahalaya Amavasai or Pithru Amavasai", "## Mahalaya Amavasai\n\nMahalaya Amavasai or Pithru Amavasai")
    body = body.replace("After Karna, the well-known donor", "## The Story of Karna\n\nAfter Karna, the well-known donor")
    body = body.replace("Great enlightened beings", "## Honoring Your Ancestors\n\nGreat enlightened beings")
    return body


def add_headings_ood_design_patterns(body):
    for old, new in [("**Creational Patterns**","## Creational Patterns"),("**Structural Patterns**","## Structural Patterns"),("**Behavioral Patterns**","## Behavioral Patterns"),("**Anti-Patterns**","## Anti-Patterns")]:
        if old in body: body = body.replace(old, new)
    if not body.strip().startswith("##"): body = "## Design Patterns Overview\n\n" + body
    return body


def add_headings_overthinking(body):
    body = body.replace("When we talk about overthinking, we're not talking", "## What Is Overthinking?\n\nWhen we talk about overthinking, we're not talking")
    body = body.replace("\nHabits to prevent overthinking\n", "\n## Habits to Prevent Overthinking\n")
    body = body.replace("\nShifting Mindset\n", "\n## Shifting Mindset\n")
    body = body.replace("\nAnalysis Paralysis\n", "\n## Analysis Paralysis\n")
    body = body.replace("\nChoose between options\n", "\n## Choosing Between Options\n")
    body = body.replace("\nWe can make only so many decisions in a day\n", "\n## Decision Fatigue\n")
    body = body.replace("\nWhen things are beyond our control\n", "\n## When Things Are Beyond Our Control\n")
    return body


def add_headings_power_of_four(body):
    body = body.replace("The best of life is the one", "## Living a Good Life\n\nThe best of life is the one")
    body = body.replace("P4 - the ultimate framework", "## The P4 Framework\n\nP4 - the ultimate framework")
    body = body.replace("Your body represents yourself", "## The Four Pillars\n\nYour body represents yourself")
    return body


def add_headings_power_of_subconscious_mind(body):
    body = body.replace("If you open your mental eyes", "## The Hidden Treasure Within\n\nIf you open your mental eyes")
    body = body.replace("Our minds have two distinct", "## Conscious vs Subconscious Mind\n\nOur minds have two distinct")
    return body


def add_headings_purpose_and_happiness(body):
    body = body.replace("Happiness is a positive emotional", "## What Is Happiness?\n\nHappiness is a positive emotional")
    body = body.replace("Providing answers to the following", "## Questions for Self-Reflection\n\nProviding answers to the following")
    return body


def add_headings_refactoring_techniques(body):
    body = body.replace("The refactoring techniques in this", "## Method Streamlining\n\nThe refactoring techniques in this")
    body = body.replace("These refactoring techniques show", "## Moving Functionality Between Classes\n\nThese refactoring techniques show")
    body = body.replace('These refactoring techniques **help with data handling**', "## Data Handling and Associations\n\nThese refactoring techniques **help with data handling**")
    return body


def add_headings_rest_details(body):
    for old, new in [("While REST stands for","## REST Principles\n\nWhile REST stands for"),("**Representations**","## Representations"),("**Messages**","## Messages"),("**HTTP Request**","## HTTP Request"),("**Listing Four: A GET request.**","### GET Request Example"),("**HTTP Response**","## HTTP Response"),("**HTTP response format.**","### Response Format")]:
        body = body.replace(old, new)
    return body


def add_headings_security_attacks(body):
    body = body.replace("**DDoS Attack", "## DDoS Attack\n\n**DDoS Attack")
    body = body.replace("**Remote Code Execution", "## Remote Code Execution\n\n**Remote Code Execution")
    body = body.replace("**Cross Site Request Forgery", "## Cross Site Request Forgery\n\n**Cross Site Request Forgery")
    body = body.replace("**Symlinking", "## Symlinking Attack\n\n**Symlinking")
    body = body.replace("**Social Engineering", "## Social Engineering\n\n**Social Engineering")
    return body


def add_headings_service_oriented_architecture(body):
    body = body.replace('A **loosely-coupled architecture**', '## SOA Principles\n\nA **loosely-coupled architecture**')
    body = body.replace('***Microservice applications are composed', '## Microservices\n\n***Microservice applications are composed')
    body = body.replace('The changing business needs are:', '## Business Drivers\n\nThe changing business needs are:')
    body = body.replace('When companies talk about building for the cloud', '## Building for the Cloud\n\nWhen companies talk about building for the cloud')
    body = body.replace('The benefits of microservices are that each one', '## Benefits of Microservices\n\nThe benefits of microservices are that each one')
    body = body.replace('The **downside of microservices comes', '## Challenges of Microservices\n\nThe **downside of microservices comes')
    body = body.replace('To summarizes, **the microservice approach', '## Summary\n\nTo summarizes, **the microservice approach')
    body = body.replace('The independent, distributed nature of microservice', '## Rolling Updates and CI/CD\n\nThe independent, distributed nature of microservice')
    return body


def add_headings_start_living(body):
    lines = body.split('\n')
    result = []
    done = False
    for line in lines:
        if not done and 'Life becomes' in line:
            result.append("## Living Fully\n")
            done = True
        result.append(line)
    return '\n'.join(result)


def add_headings_unfuck_yourself(body):
    body = body.replace("How willing are you to consider", "## The Weight of Self-Talk\n\nHow willing are you to consider")
    body = body.replace("Embrace your uncertainties", "## Embrace Uncertainty\n\nEmbrace your uncertainties")
    body = body.replace("You're not your thoughts", "## You Are Not Your Thoughts\n\nYou're not your thoughts")
    body = body.replace("**Expect nothing, accept everything", "## Expect Nothing, Accept Everything\n\n**Expect nothing, accept everything")
    return body


def add_headings_unit_testing(body):
    for old, new in [("A unit test is a piece of a code","## What is Unit Testing?\n\nA unit test is a piece of a code"),("**Properties of a good unit test**","## Properties of a Good Unit Test"),("**Definitions**","## Key Definitions"),("No matter how you organize","## Qualities of Good Tests\n\nNo matter how you organize"),("**Testing only one thing****If","## Testing One Thing\n\n**If"),("**Assuring code coverage** To","## Code Coverage\n\nTo"),("**When you add a new test that was missing**, check","## Adding Missing Tests\n\nCheck"),("**Testing private or protected methods**","## Testing Private/Protected Methods"),("**If a method is worth testing**","## Making Methods Testable"),("**Making a method public**","## When to Make Methods Public"),("**Extracting methods to new classes**If","## Extracting Methods\n\nIf"),("**Making methods static**If","## Making Methods Static\n\nIf"),("**Making methods internal**When","## Making Methods Internal\n\nWhen"),("**Setting up mocks and fakes in the setup method** It's","## Setup Methods and Mocks\n\nIt's"),("**My preference is to have each test**","## Test Organization Preference"),("**Enforcing test isolation** The lack","## Test Isolation\n\nThe lack"),("**Writing readable tests**","## Readable Tests"),("**Naming unit tests:** Naming","### Naming Conventions\n\nNaming"),("**The test name has three parts:** The name","### Test Name Structure\n\nThe name"),("**My debugger shows that my code works: why do I need tests?**","## Why Tests Matter"),("**A study held by Curtis**","## Common Defects"),("**TDD is a style choice**. I personally","## Test-Driven Development\n\nI personally"),("**Design goals for testability**There are","## Design for Testability\n\nThere are")]:
        body = body.replace(old, new)
    return body


def add_headings_win_arguments(body):
    lines = body.split('\n')
    result = []
    done = False
    for line in lines:
        if not done and line.strip() and 'argument' in line.lower():
            result.append("## Winning Arguments\n")
            done = True
        result.append(line)
    return '\n'.join(result)


def process_file(filepath):
    filename = filepath.name
    handlers = {
        'bad-code-smells.md': add_headings_bad_code_smells,
        'burning-out.md': add_headings_burning_out,
        'career-sutras.md': add_headings_career_sutras,
        'detox-your-thoughts.md': add_headings_detox_your_thoughts,
        'expanding-columns-in-wpf.md': add_headings_expanding_columns_in_wpf,
        'faster.md': add_headings_faster,
        'javascript.md': add_headings_javascript,
        'kubernetes-learning-path.md': add_headings_kubernetes_learning_path,
        'kubernetes-learning-path-components.md': add_headings_kuberneties_learning_path_components,
        'kubernetes-learning-path-deployments.md': add_headings_kuberneties_learning_path_deployments,
        'kubernetes-learning-path-pods.md': add_headings_kuberneties_learning_path_pods,
        'kubernetes-learning-path-replicaset.md': add_headings_kuberneties_learning_path_replicaset,
        'mahalaya-paksham.md': add_headings_mahalaya_paksham,
        'ood-design-patterns-and-anti-patterns.md': add_headings_ood_design_patterns,
        'overthinking.md': add_headings_overthinking,
        'power-of-four-for-good-life.md': add_headings_power_of_four,
        'power-of-subconscious-mind.md': add_headings_power_of_subconscious_mind,
        'purpose-and-happiness.md': add_headings_purpose_and_happiness,
        'refactoring-techniques.md': add_headings_refactoring_techniques,
        'rest-details.md': add_headings_rest_details,
        'security-attacks.md': add_headings_security_attacks,
        'service-oriented-architecture.md': add_headings_service_oriented_architecture,
        'start-living.md': add_headings_start_living,
        'unfuck-yourself.md': add_headings_unfuck_yourself,
        'unit-testing-what-why-how.md': add_headings_unit_testing,
        'win-arguments.md': add_headings_win_arguments,
    }
    if filename not in handlers:
        print(f"No handler for {filename}")
        return False
    try:
        content = read_file(filepath)
        frontmatter, body = extract_frontmatter(content)
        if re.search(r'^## ', body, re.MULTILINE):
            print(f"Skipping {filename} (already has headings)")
            return True
        new_body = handlers[filename](body)
        write_file(filepath, frontmatter + new_body)
        print(f"Processed {filename}")
        return True
    except Exception as e:
        print(f"Error processing {filename}: {e}")
        return False


def main():
    posts_dir = get_posts_dir()
    if not posts_dir.exists():
        print(f"Error: Posts directory not found at {posts_dir}")
        return
    files = ['bad-code-smells.md','burning-out.md','career-sutras.md','detox-your-thoughts.md','expanding-columns-in-wpf.md','faster.md','javascript.md','kubernetes-learning-path.md','kubernetes-learning-path-components.md','kubernetes-learning-path-deployments.md','kubernetes-learning-path-pods.md','kubernetes-learning-path-replicaset.md','mahalaya-paksham.md','ood-design-patterns-and-anti-patterns.md','overthinking.md','power-of-four-for-good-life.md','power-of-subconscious-mind.md','purpose-and-happiness.md','refactoring-techniques.md','rest-details.md','security-attacks.md','service-oriented-architecture.md','start-living.md','unfuck-yourself.md','unit-testing-what-why-how.md','win-arguments.md']
    print(f"Processing {len(files)} files from {posts_dir}\n")
    ok = 0
    for f in files:
        p = posts_dir / f
        if p.exists():
            if process_file(p): ok += 1
        else:
            print(f"File not found: {f}")
    print(f"\nSuccessfully processed {ok}/{len(files)} files")


if __name__ == "__main__":
    main()
