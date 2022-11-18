---
title: Trimester 1 Final Blog
description: Corrections and blog on trimester 1 final
toc: true
comments: true
layout: post
permalink: /week12/tri1finalblog
categories: [week 12]
---

# Final Exam
## Results
I scored a 44/50, or 88%. This is high enough to earn a 3/3 in the grade book.

![Proof of Final]({{site.baseurl}}/images/tri1finalscore.jpg)

## Corrections

### Q6

In the following procedure, the parameter max is a positive integer.

    PROCEDURE printNums(max)
        {
            count ← 1
            REPEAT UNTIL(count > max)
            {
                DISPLAY(count)
                count ← count + 2
            }
        }

Which of the following is the most appropriate documentation to appear with the printNums procedure?

I answered: (A) Prints all positive even integers that are less than or equal to `max`

Correct answer: (B) Prints all positive odd integers that are less than or equal to `max`

### Q8

In the following procedure, the parameter numList is a list of numbers and the parameters j and k are integers.

    PROCEDURE swapListElements(numList, j, k)
    {
        newList ← numList
        newList[j] ← numList[k]
        newList[k] ← numList[j]
        RETURN(newList)
    }

Which of the following is the most appropriate documentation to appear with the swapListElements procedure?

I answered: (C) Interchanges the values of the parameters j and k. The value of j must be between 0 and the value of k, inclusive.

Correct answer: (B) Returns a copy of `numList` with elements at indices j and k interchanged. The values of j and k must both be between 1 and `LENGTH(numList)`, inclusive

### Q20

A video game character can face toward one of four directions: north, south, east, and west. Each direction is stored in memory as a sequence of four bits. A new version of the game is created in which the character can face toward one of eight directions, adding northwest, northeast, southwest, and southeast to the original four possibilities. Which of the following statements is true about how the eight directions must be stored in memory?

I answered: (C) Four bits are not enough to store the eight directions. Sixteen bits are needed for the new version of the game.

Correct answer: (D) Four bits are enough to store the eight directions.

### Q23

The position of a runner in a race is a type of analog data. The runner’s position is tracked using sensors. Which of the following best describes how the position of the runner is represented digitally?

I answered: (C) The position of the runner is predicted using a model based on performance data captured from previous races.

Correct answer: (D) The position of the runner is sampled at regular intervals to approximate the real-word position, and a sequence of bits is used to represent each sample.

### Q43

Consider the following code segment.

![]({{site.baseurl}}/images/Q43figure.jpg)

What is the value of `result` after the code segment is executed?

I answered: (A) 6

Correct answer: (C) 15

### Q50

Consider the following procedures for string manipulation.

| Procedure Call | Explanation |
| -------------- | ----------- |
| concat(str1, str2) | Returns a single string consisting of str1 followed by str2. For example, concat("key", "board") returns "keyboard". |
| prefix(str, length) | Returns the first length characters of str or str if length is greater than the number of characters in str. For example, prefix("delivery", 3) returns "del" and prefix("delivery", 100) returns "delivery". |


The variable `initials` is to be assigned a string consisting of the first letter of the string firstName followed by the first letter of the string lastName. Which of the following assigns the correct string to `initials`?

I answered: (B) `initials  ←  concat(prefix(firstName, 2), prefix(lastName, 2))`

Correct answer: (A) `initials  ←  concat(prefix(firstName, 1), prefix(lastName, 1))`


## Final Thoughts and Blogging

- Final exam was not as difficult as I had imagined
- There was some binary stuff on there that we were never taught
- Most of what was tested was simple math and following directions
    - follow along with what a program is doing
- I fail to recognize the importance of re-assigning variables to other various non-related variables multiples times, just to make the program complicated
