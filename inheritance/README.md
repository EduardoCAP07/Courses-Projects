# 🧬 Blood Type Inheritance Simulation (CS50)

This project is part of Harvard's CS50 course and focuses on simulating
how blood types are inherited across generations using the C programming
language.

------------------------------------------------------------------------

## 📌 Overview

A person's blood type is determined by **two alleles** (different forms
of a gene):

-   A
-   B
-   O

Each individual inherits: - One allele from their mother - One allele
from their father

------------------------------------------------------------------------

## 🧬 Possible Blood Type Combinations

Each person has two alleles, leading to the following combinations:

-   OO
-   OA
-   OB
-   AO
-   AA
-   AB
-   BO
-   BA
-   BB

------------------------------------------------------------------------

## 👨‍👩‍👧 Inheritance Rules

Each parent randomly passes **one of their two alleles** to their child.

### Example 1

-   Parent 1: AO\
-   Parent 2: BB

Possible child blood types: - AB - OB

### Example 2

-   Parent 1: AO\
-   Parent 2: OB

Possible child blood types: - AO - OB - AB - OO

------------------------------------------------------------------------

## 🎯 Objective

Write a program in C that:

1.  Simulates a family tree of a given number of generations
2.  Assigns blood type alleles to each person
3.  Models inheritance from parents to children
4.  Uses dynamic memory allocation

------------------------------------------------------------------------

## 📂 Project Structure

    .
    └── inheritance/
        └── inheritance.c

------------------------------------------------------------------------

## ⚙️ Implementation Details

### 🔹 create_family Function

-   Takes an integer `generations` as input
-   Allocates memory for each person using `malloc`
-   Returns a pointer to the **youngest generation**

### 🔹 Family Structure

-   Each person has:
    -   Two alleles
    -   Two parents (pointers)

### 🔹 Oldest Generation

-   Alleles are assigned randomly using `random_allele`
-   Parents are set to `NULL`

### 🔹 Younger Generations

-   Each person:
    -   Inherits one allele randomly from each parent
    -   Has two parents (pointers to other `person` structs)

------------------------------------------------------------------------

## ▶️ How to Run

Compile the program:

``` bash
gcc inheritance.c -o inheritance
```

Run the program:

``` bash
./inheritance
```

------------------------------------------------------------------------

## 🧠 Key Concepts

-   Recursion (building family trees)
-   Dynamic memory allocation (`malloc`)
-   Pointers and structs in C
-   Random number generation
-   Simulation of real-world genetics

------------------------------------------------------------------------

## ⚠️ Academic Honesty

This repository contains my personal solution to a CS50 problem.

Do not copy this code directly.\
Use it for learning and reference only.

------------------------------------------------------------------------

## 🚀 Future Improvements

-   Visual representation of the family tree
-   Input-based generation size
-   Enhanced randomness control

------------------------------------------------------------------------
