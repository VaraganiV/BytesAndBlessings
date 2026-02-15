---
title: "Security | Attacks"
description: "Understanding common security attacks — DDoS, SQL Injection, XSS, CSRF, Man-in-the-Middle, and how to defend against them."
date: 2016-07-22
draft: false
categories:
  - tech
ShowToc: true
TocOpen: false
---

**DDoS Attack – Distributed Denial Of Service Attack**

DDoS, or Distributed Denial of Services, is where a server or a machine’s services are made unavailable to its users. And  when the system is offline, the hacker proceeds to either  compromise  the entire website or a specific function of a website to  their own  advantage. The usual agenda of a DDoS campaign is to temporarily interrupt or completely take down a successfully running system.  The  most common example of a DDoS attack could be sending tons of URL requests to a website or a webpage in a very small amount of time. This causes bottlenecking at the server side because the CPU just ran   out of resources. Denial-of-service  attacks are considered violations of the Internet  Architecture Board’s  Internet proper use policy, and also violate the  acceptable use  policies of virtually all Internet service providers.

**Remote Code Execution Attacks**

A Remote Code Execution attack is a result of either server side or client side security weaknesses. Vulnerable  components may include libraries, remote directories on a  server that  haven’t been monitored, frameworks, and other software  modules that run  on the basis of authenticated user access. Applications  that use these  components are always under attack through things like  scripts,  malware, and small command lines that extract information.  The following vulnerable components were downloaded 22 million times in 2011: Apache CXF Authentication Bypass (http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-3451) By failing to provide an identity token, attackers could invoke any web service with full permission.

**Cross Site Request Forgery Attacks**

*A Cross Site Request Forgery Attack happens when a user is logged  into a  session (or account) and a hacker uses this opportunity to send  them a  forged HTTP request to collect their cookie information.* In most cases, the cookie remains valid as long as the user or the attacker stays logged into the account.  This is why websites ask you  to  log out of your account when you’re finished – it will expire the   session immediately. In other cases,  once the user’s browser session is compromised, the  hacker can generate  requests to the application that will not be able to  differentiate  between a valid user and a hacker. A Cross Site Attack Examples Page on example.com <img src=”<span style=”color:  red;”>http://Example Domain/app/transferFunds?amount=1500&destinationAccount=attackersAcct#</span>”  width=”0″ height=”0″ />

**Symlinking – An Insider Attack**

A symlinking attack occurs when a hacker positions the symlink in such a way that the user or application that   access the endpoint thinks *they’re accessing the right file when  they’re  really not*. If the endpoint  file is an output, the consequence of the symlink  attack is that it  could be modified instead of the file at the intended  location.  Modifications to the endpoint file could include appending,   overwriting, corrupting, or even changing permissions. In  different variations of a symlinking attack a hacker may be able  to  control the changes to a file, grant themselves advanced access,  insert  false information, expose sensitive information or corrupt or  destroy  vital system or application files.

**Social Engineering Attacks**

A classic example of a social engineering attack is the “Microsoft tech support” scam. This  is when someone from a call center pretends to be a MS tech  support  member who says that your computer is slow and/or infected, and  can be  easily fixed – at a cost, of course. Here’s an article from Wired.com on how a security expert played along with so-called Microsoft tech support person.

**DNS Cache Poisoning**

DNS Cache Poisoning involves old cache data that you might think you no longer have on your computer, but is actually “toxic”. Also  known as DNS Spoofing, hackers can identify vulnerabilities in a   domain name system, which allows them to divert traffic from legit   servers to a fake website and/or server. This form of attack can spread and replicate itself from one DNS server to another DNS, “poisoning” everything in it’s path.

**Clickjacking Attacks**

Clickjacking,  also called a UI Redress Attack, is when a hacker uses  multiple opaque  layers to trick a user into clicking the top layer  without them  knowing. Thus the attacker is  “hijacking” clicks that are not meant for the  actual page, but for a  page where the attacker wants you to be. For example, using a carefully crafted combination of stylesheets,   iframes, and text boxes, a user can be led to believe they are typing  in  the password for their bank account, but are actually typing into  an  invisible frame controlled by the attacker. Clickjacking example: Here’s a live, but safe example of how clickjacking works: Alphabet Hero And here’s a video that shows how we helped Twitter defend against a Clickjacking attack:

**Broken Authentication and Session Management Attacks**

Authentication  systems involve passwords, key management, session  IDs, and cookies  that can allow a hacker to access your account from any  computer (as  long as they are valid). If a hacker exploits the authentication and session management system, they can assume the user’s identity. Scary indeed. Ask yourself these questions to find out if your website is vulnerable to a broken authentication and session management attack: Are user credentials weak (e.g. stored using hashing or encryption)? Can  credentials be guessed or  overwritten through weak account management  functions (e.g. account  creation, change password, recover password,  weak session IDs)? Are session IDs exposed in the URL (e.g. URL rewriting)? Are session IDs vulnerable to session fixation attacks? Do session IDs timeout and can users log out? If you answered “yes” to any of these questions, your site could be vulnerable to a hacker.

**Cross Site Scripting Attacks**

Cross  Site Scripting, also known as an XSS attack, occurs when an   application, url “get request”, or file packet is sent to the web   browser window and bypassing the validation process. Once an XSS script   is triggered, it’s deceptive property makes users believe that the   compromised page of a specific website is legitimate. For example, if www.example.com/abcd.html has XSS script in it, the user might see a popup window asking for their credit card info and other sensitive info.Technical Cross Site Scripting Example:

**Injection Attacks**

Injection  Attacking occurs when there are flaws in your SQL Database,  SQL  libraries, or even the operating system itself. Employees open   seemingly credible files with hidden commands, or “injections”,   unknowingly. In doing so, they’ve  allowed hackers to gain unauthorized access to  private data such as  social security numbers, credit card number or  other financial data  Technical Injection Attack Example: An Injection Attack could have this command line: String query = “SELECT \* FROM accounts WHERE custID='” + request.getParameter(“id”) +”‘”; The  hacker modifies the ‘id’ parameter in their browser to send: ‘ or   ‘1’=’1. This changes the meaning of the query to return all the records   from the accounts database to the hacker, instead of only the intended   customers.