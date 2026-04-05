# 🧬 DNA Profiling (CS50)

This project is part of Harvard's CS50 course and focuses on DNA
identification using **Short Tandem Repeats (STRs)**.

## 📌 Overview

DNA is made up of sequences of nucleotides represented by the letters:

-   A (Adenine)
-   C (Cytosine)
-   G (Guanine)
-   T (Thymine)

Certain regions of DNA contain **Short Tandem Repeats (STRs)** --- short
sequences that repeat multiple times.\
The number of repetitions varies between individuals, making STRs useful
for identification.

------------------------------------------------------------------------

## 🎯 Objective

The goal of this program is to:

1.  Read a DNA sequence
2.  Analyze STR patterns
3.  Compare results with a database
4.  Identify the individual OR return `No match`

------------------------------------------------------------------------

## 📂 Project Structure

    .
    ├── dna.py
    ├── databases/
    │   ├── small.csv
    │   └── large.csv
    ├── sequences/
    │   ├── 1.txt
    │   ├── 2.txt
    │   ├── ... .txt
    │   └── 20.txt
    └── README.md

------------------------------------------------------------------------

## 🗃️ Database Format

The database is a CSV file structured like this:

``` csv
name,AGAT,AATG,TATC
Alice,28,42,14
Bob,17,22,19
Charlie,36,18,25
```

------------------------------------------------------------------------

## 🔍 How It Works

1.  The program scans the DNA sequence
2.  Finds the **longest consecutive run** of each STR
3.  Compares the counts with each person in the database
4.  Outputs the matching name

### Example:

If the sequence contains:

-   AGAT → 17 repeats\
-   AATG → 22 repeats\
-   TATC → 19 repeats

✅ Output:

    Bob

If no match is found:

❌ Output:

    No match

------------------------------------------------------------------------

## ▶️ How to Run

Make sure you have Python installed.

``` bash
python dna.py databases/small.csv sequences/sequence1.txt
```

------------------------------------------------------------------------

## 🧠 Key Concepts

-   String processing
-   Pattern matching
-   CSV file handling
-   Dictionaries and lists
-   Algorithms for sequence analysis

------------------------------------------------------------------------

## ⚠️ Academic Honesty

This repository contains my personal solutions to CS50 problem sets.

Please do not copy this code directly.\
Use it for learning and reference only.

------------------------------------------------------------------------

## 🚀 Future Improvements

-   Add visualization of STR matches
-   Optimize search performance
-   Build a simple UI for input/output

------------------------------------------------------------------------
