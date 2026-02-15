---
title: "How Browsers Work"
description: "A deep dive into how web browsers work — from parsing HTML and CSS to rendering the DOM tree, layout, and painting pixels on screen."
date: 2016-07-09
draft: false
categories:
  - tech
ShowToc: true
TocOpen: false
tags:
  - web
  - browsers
  - fundamentals
cover:
  image: "/images/covers/how-browsers-work-cover.svg"
  alt: "Cover image"
  relative: false
---

There are five major browsers used on desktop: Chrome, Internet Explorer, Firefox, Safari and Opera. On mobile the main browsers are Android Browser, iPhone, Opera Mini and Opera Mobile. All them expect Opera are based on **WebKit**.  

# Browsers Functionality:
</a>
</figure>

The main functionality of a browser is to present the web resources you choose, by requesting it from the server and displaying it in the browser window. The way browsers interpret and displays HTML files is specified in the HTML and CSS Specifications. These specifications are maintained by W3C organization.  

## Browser’s high level structure:

* **User Interface:** Includes address bar, back/forward buttons, bookmark menu, etc.
* **Browser Engine:** Marshals actions between the UI and the rendering engine
* **Rendering Engine:** Responsible for displaying the requested content.
* **Networking:** For network calls such as HTTP, FTP requests
* **UI Backend:** Used for drawing basic widgets like combo boxes, text boxes, windows. This backend exposes a generic interface that is not platform specific. Underneath it uses the operating system user interface methods.
* **JavaScript Interpreter:** Used to parse JavaScript code.
* **Data storage:** This is a persistence layer. Browser may need to save all sorts of data locally, such as cookies. Browsers also support language such as local storage, Indexed DB, WebSQL etc.

# Rendering Engine
</a>
</figure>

The responsibility of the rendering engine is well… Rendering, that is display of requested contents on the browser screen. Different browsers use different rendering engines: Internet Explorer uses **Trident**, Firefox users **Gecko**, Safari uses **WebKit**. Chrome and Opera use Blink, a fork of WebKit.  
The rendering engine will get the contents of the requested document from the networking layer. This is usually done in 8KB chunks. After this:  

### Parsing Algorithm:

Parsing can be separated into two sub processes: Lexical analysis and Syntax analysis.  Lexical analysis is process of breaking the input into tokens, which are  
</a>
</figure>
 language vocabulary. The parser is responsible for constructing the parse tree by  analyzing the document structure according to the language syntax rules.  

  
This algorithm consists two stages: **tokenization** and **tree construction**:  
The tokenization Algorithm: This algorithm’s output is an HTML token. The algorithm is expressed as state machine. Each state consumes one or more characters of the input stream and updates the next state according to those characters.  

Example:  

* The initial state is the “Data State”. When the < character is encountered, the state is changed to “Tag open state”. Consuming a-z character cause creation of a
</a>
</figure>
“Start tag token”, the state is changed to “Tag name state”.
* We stay in this state until the > character is consumed. When > tag is reached, the current token is emitted and the state changes back to the “Data State”.
* The `<body`> tag will be treated by the same steps.
* Consuming H character if Hello World will cause creation and emitting of a character token for each character of Hello World
* We are now back to the “Tag Open state”. Consuming the next input / will cause creation of an end tag token and a move to the “Tag name state”.
* We remain in the same state till we reach >. Then the new token will be emitted and we go back to the “Data state”.

### Tree construction algorithm

When the parser is created the Document object is created. During the tree construction stage the DOM tree with the Document in its root will be modified and elements will be added to it. The element is added to the DOM tree, and also the stack of open elements. The stack is used to correct nesting mismatches and unclosed tags. The algorithm is also described as a state machine.  

### Browser’s error tolerance

We never get an “Invalid Syntax” error on a HTML page. Browsers fix any invalid content and go on.  

### CSS Parsing

WebKit uses Flex and Bison parser generators to create parsers automatically from the CSS grammar files.  Bison creates a bottom up parser while Firefox uses top 
</a>
</figure>
down parser. In either cases CSS file is parsed into a Style Sheet object. Each object contains CSS rules.  
</a>
</figure>

  

  

  

  

  

  

  

### Scripts

The author expects scripts to be parsed and executed immediately when the parser reaches the `<Script`> tag. The document parsing is halted till script is executed. HTML5 adds an option of **marking the script as asynchronous** so it will be parsed and executed in a different thread.  

### Speculative parsing

Both Firefox and WebKit do this optimization while executing the scripts another threads parses the rest of the document and finds out what other resources need to be loaded from the network and loads them.  

### Style Sheet

Style sheets on the other hand have a different model. Conceptually it seems that since style sheets don't change the DOM tree, there is no reason to wait for them and stop the document parsing. There is an issue, though, of scripts asking for style information during the document parsing stage. If the style is not loaded and parsed yet, the script will get wrong answers and apparently this caused lots of problems. It seems to be an edge case but is quite common. Firefox blocks all scripts when there is a style sheet that is still being loaded and parsed. WebKit blocks scripts only when they try to access certain style properties that may be affected by unloaded style sheets.  

# Rendering Tree

While the DOM tree is being constructed, the browser constructs another tree, the render tree. This tree is of visual elements in the order in which they will be displayed. It is the visual representation of the document. The purpose of this tree is to enable painting the contents in their correct order. Firefox calls the elements in the render tree "frames". WebKit uses the term renderer or render object.  
The renderers correspond to DOM elements, but the relation is not one to one. Non-visual DOM elements will not be inserted in the render tree. An example is the "head" element. Also elements whose display value was assigned to "none" will not appear in the tree (whereas elements with "hidden" visibility will appear in the tree).  

# Layout

When the renderer is created and added to the tree, it does not have a position and size. Calculating these values is called layout or reflow. HTML uses a flow based layout model, meaning that most of the time it is possible to compute the geometry in a single pass. Elements later ``in the flow'' typically do not affect the geometry of elements that are earlier ``in the flow'', so layout can proceed left-to-right, top-to-bottom through the document. The coordinate system is relative to the root frame. Top and left coordinates are used. Layout is a recursive process. It begins at the root renderer, which corresponds to the `<html`> element of the HTML document. Layout continues recursively through some or all of the frame hierarchy, computing geometric information for each renderer that requires it. The position of the root renderer is 0,0 and its dimensions are the viewport–the visible part of the browser window. All renderers have a "layout" or "reflow" method, each renderer invokes the layout method of its children that need layout.  

## Dirty bit system

In order not to do a full layout for every small change, browsers use a "dirty bit" system. A renderer that is changed or added marks itself and its children as "dirty": needing layout. There are two flags: "dirty", and "children are dirty" which means that although the renderer itself may be OK, it has at least one child that needs a layout.  

## Global and incremental layout

Layout can be triggered on the entire render tree–this is "global" layout. This can happen as a result of:  

* A global style change that affects all renderers, like a font size change.
* As a result of a screen being resized

Layout can be incremental, only the dirty renderers will be laid out (this can cause some damage which will require extra layouts).  Incremental layout is triggered (asynchronously) when renderers are dirty. For example, when new renderers are appended to the render tree after extra content came from the network and was added to the DOM tree.  

## Asynchronous and Synchronous layout

Incremental layout is done asynchronously. Firefox queues "reflow commands" for incremental layouts and a scheduler triggers batch execution of these commands. WebKit also has a timer that executes an incremental layout–the tree is traversed and "dirty" renderers are layout out.  Scripts asking for style information, like "offsetHeight" can trigger incremental layout synchronously. Global layout will usually be triggered synchronously.  Sometimes layout is triggered as a callback after an initial layout because some attributes, like the scrolling position changed.  

## Optimizations

When a layout is triggered by a "resize" or a change in the renderer position (and not size), the renders sizes are taken from a cache and not recalculated...  In some cases, only a sub tree is modified and layout does not start from the root. This can happen in cases where the change is local and does not affect its surroundings–like text inserted into text fields (otherwise every keystroke would trigger a layout starting from the root).  

## The layout process

The layout usually has the following pattern:  

1. Parent renderer determines its own width.
2. Parent goes over children and:
   1. Place the child renderer (sets its x and y).
   2. Calls child layout if needed–they are dirty or we are in a global layout, or for some other reason–which calculates the child's height.
   3. Parent uses children's accumulative heights and the heights of margins and padding to set its own height–this will be used by the parent renderer's parent.
   4. Sets its dirty bit to false.

Firefox uses a "state" object(nsHTMLReflowState) as a parameter to layout (termed "reflow"). Among others the state includes the parent’s width.  The output of the Firefox layout is a "metrics" object(nsHTMLReflowMetrics). It will contain the renderer computed height.  

# The painting order

This order affects painting since the stacks are painted from back to front. The stacking order of a block renderer is:  

1. background color
2. background image
3. border
4. children
5. outline

Firefox goes over the render tree and builds a display list for the painted rectangular. It contains the renderers relevant for the rectangular, in the right painting order (backgrounds of the renderers, then borders etc). That way the tree needs to be traversed only once for a repaint instead of several times–painting all backgrounds, then all images, then all borders etc. Firefox optimizes the process by not adding elements that will be hidden, like elements completely beneath other opaque elements.  
Before repainting, WebKit saves the old rectangle as a bitmap. It then paints only the delta between the new and old rectangles.  
The browsers try to do the minimal possible actions in response to a change. So changes to an elements color will cause only repaint of the element. Changes to the element position will cause layout and repaint of the element, its children and possibly siblings. Adding a DOM node will cause layout and repaint of the node. Major changes, like increasing font size of the "html" element, will cause invalidation of caches, relayout and repaint of the entire tree.  
The rendering engine is single threaded. Almost everything, except network operations, happens in a single thread. In Firefox and Safari this is the main thread of the browser. In Chrome it's the tab process main thread.  
Network operations can be performed by several parallel threads. The number of parallel connections is limited (usually 2–6 connections).  
The browser main thread is an event loop. It's an infinite loop that keeps the process alive. It waits for events (like layout and paint events) and processes them.  
Ref: <http://www.html5rocks.com/en/tutorials/internals/howbrowserswork/#Render_tree_construction>