---
title: CPT Project Blog
description: Tri 2 CPT Project blog
toc: true
comments: true
layout: post
permalink: /week20/projectblog
categories: [week 20]
---

# Pre-view

| Category | Expectation | Explanation/Response |
| :------: | ----------- | ----------- |
| Program Purpose and Function | Describes the purpose of the program, describes the program's functionality, and can take an input and return an output. | The purpose of this program is to provide the user with an entertaining and competitive experience through the gameplay of several virtual arcade games along with the exchange of digital currency, while being ranked based upon how much currency the user has. |
| Data Abstraction | Shows how data has been stored in a collection and shows data from that collection as it contributes to the overall purpose of the program. Identifies the name of a variable representing the collection being used and describes what the data contained in the collection represents in the program. | Our program abstracts data through the creation of records that are accessed in a backend database. The purpose of this database is to store crucial information about a user such as the number of tokens they have. This value can be used in our program to construct a leaderboard of players with the highest number of tokens in order to create a more competitive experience. We will also store a UserID, Name, and Password to identify users on the leaderboard and authenticate their account. |
| Managing Complexity | Shows a collection of data that manages complexity. Explains an alternative method that would have been more complex and explains why that method could not be used or how it would have to be written differently. | There will be many alternative ways to track currency or program each game, so we will show how we chose the simplest way to achieve the desired functionality and explain how it could have been done another way. |
| Procedural Abstraction | Shows a student-developed procedure with at least one parameter that has an effect on the functionality of the procedure, and shows where that procedure is called. Describes how the procedure contributes to the functionality of the program. | This will be found in each game that we develop, as all of our games are complex enough to require a function with a parameter. |
| Algorithm Implementation | Includes a student-developed algorithm that includes sequencing, selection, and iteration. Explains how the algorithm works in detail enough to where someone could recreate it. | The games that we develop for the virtual arcade will have sufficient algorithms to fit this criteria. |
| Testing | Describe two calls to the selected procedure in response 3c. Each call must pass a argument that causes different outputs. Describes conditions being tested by each call. Identifies the result of each call. | We will test two different features in each game, which test certain conditions and output different results. |

## Create Performance Task

Each person in our group is programming a game for the arcade, so each person's CPT will be focused on their respective game. This all will be incorporated into a larger N@TM project, which is the entire arcade itself with an account, currency, and leaderboard system.


# Code Plan

My game will be pretty simple to play and will be coded with HTML/CSS/JS.

1. The user pays 15 tokens to start the game
2. They are prompted with a basic overview of the game, as follows:
    1. Each round lasts 15 seconds
    2. You must click as many targets as possible before time ends
    3. The number of targets the user clicks is the number of tokens they earn
3. When the user clicks the button to begin, their score will be initialized to 0 and they are faced with a screen that displays the score at the top and a circular target somewhere inside a rectangle
4. When the user clicks the target, it will move to a different random location in the rectangle and will add 1 to the score at the top
5. This will repeat for as many targets clicked within 15 seconds of starting the game.
6. After 15 seconds, the user will be brought to a screen that shows the following:
    1. Their score, which is also the number of tokens they earned
    2. A button to view the leaderboard
    3. A button to try again for an additional 15 tokens

# Video Plan

I plan to show my game running for two rounds. One round will earn less than 15 points/tokens, which will show my overall balance go down, and vice versa for the second round.