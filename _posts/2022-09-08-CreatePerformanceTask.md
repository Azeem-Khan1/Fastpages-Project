---
title: College Board Create Performance Task (Hacks)
description: Hacks for Create Performance Task (Week 3) 
toc: true
comments: true
layout: post
permalink: /week3/Create_Performance_Task
categories: [week 03]
tags: [markdown]
---

# Hacks
## The Idea
After racking my brain for design ideas, I came up with something interesting that is inspired by the video game "Aim Lab". It's essentially a game designed to practice the user's aim with their mouse.

## The Plan
### Creation of Design Elements
- First, I will make a start screen, which will display a title, the rules/instructions, and a button to start the game
- Next, I will create a "gameplay" page, which will have about 30 circles (or targets) scattered throughout the screen, along with a score counter at the top and a 3, 2, 1, GO countdown
- Then, I will create an end screen that will say "game over" and display the user's score, along with a button to *try again*, which will redirect them back to the start screen
- In case the user's speed is insanely good, I created a "win" page just in case, and it will simply say "congratulations, you beat the game" and will have an option to play again

### Writing the Code (Basic layout)
- Set the screen to the start screen
- Declare a variable: *score = 0*
- Define a function to hide all elements on the gameplay screen
- Call the function mentioned above when the "start game" button is clicked
- Use the setTimeout block to code a countdown before the targets appear
- Once the countdown is done, display the first target using the showElement block
- When that target is clicked,
    - hide that target
    - assign variable: *score = score + 1*
    - setText of score box to the variable *score*
    - display new target
- Copy and paste 29 times (I know there's probably a faster way to do this with a function but this seemed easier to me and it still works how I want it to)
- Use a setTimeout block to switch to the *end screen* after 15 seconds and setText to *"You scored" + score*
- After target #30 is clicked, redirect the user to the win screen
- If the "play again" button (on either the win or end screen) is clicked, redirect the user to the start screen

## The Product

Click [here](https://studio.code.org/projects/applab/h3hA8Qkx_rMF5kAi65xjePKOq6U5V-0_m-8bFrAyG9w) or use the embed below

<iframe width="392" height="620" style="border: 0px;" src="https://studio.code.org/projects/applab/h3hA8Qkx_rMF5kAi65xjePKOq6U5V-0_m-8bFrAyG9w/embed"></iframe>