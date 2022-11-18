---
title: HTML Fragments Hacks
description: Hacks for HTML Fragments (Week 2) 
toc: true
comments: true
layout: post
permalink: /week2/HTML_fragments
categories: [week 02]
tags: [markdown, HTML]
---

# Hacks
### Remote Theme
- Before remote theme:
![Before ss 1]({{site.baseurl}}/images/Fastpage before remote theme.jpg)
![Before ss 1]({{site.baseurl}}/images/Fastpage before remote theme 2.jpg)

- After remote theme:
![after ss 1]({{site.baseurl}}/images/Fastpage hacker theme 1.jpg)
![after ss 1]({{site.baseurl}}/images/Fastpage hacker theme 2.jpg)

Observations:
- One thing I am 100% confident in is that I like how the default "miniima" theme looks
- The dark mode makes it very hard to read most of the text in the "Hacker" remote theme
- The remote theme looks a lot more vintage
- Remote theme does not support "pages" layout like the default (the little tabs in the top right become links instead)
- Hacker theme lacked organization and sectioning
- Looked like it was from the dinosaur era

### Time Box

| Time box | example |
| -------- | ------- |
| Week 0 | Tool setup (install all required software) & build fastpage |
| Week 1 | Bash checks and Hello to python (Python Quiz) |
| Week 2 | Python lists & dictionaries and HTML Fragments |

### Tags
- I have made a category for hacks so that the user can navigate to the tags page and access all hacks that have been completed or are in progress.
![Tags screenshot]({{site.baseurl}}/images/tags.jpg)

### Search
- Searching on my site seems to work properly for me.
![Search screenshot]({{site.baseurl}}/images/Search.jpg)

### Making a table the Lazy Programmer's way

<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>HTML Hack</title>
    <style>
      /* The . with the boxed represents that it is a class */
      .boxed {
        background: transparent;
        color: white;
        border: 1px solid grey;
        margin: 0px auto;
        width: 456px;
        padding: 10px;
        border-radius: 0px;
      }
    </style>
  </head>
  <body>
    <div class="boxed">
    <b>Time Box Example (Lazy way)</b>
    <hr>
    Week 0 &nbsp; | &nbsp; Tool setup (install all required software) & build fastpage
    <hr>
    Week 1 &nbsp; | &nbsp; Bash checks and Hello to python (Python Quiz)
    <hr>
    Week 2 &nbsp; | &nbsp; Python lists & dictionaries and HTML Fragments
    <hr>
    </div>
  </body>
</html>