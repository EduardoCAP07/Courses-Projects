# 🔤 Speller (CS50)

This project is part of Harvard's CS50 course and focuses on building a
fast **spell-checker** using a hash table data structure implemented in C.

## 📌 Overview

The program reads a text file word by word and checks each one against a
loaded dictionary, reporting any misspellings along with performance
benchmarks for each operation.

The core challenge is implementing an efficient dictionary using:

-   A **hash table** for fast lookups
-   **Linked lists** to handle collisions
-   Manual **memory management** in C

---

## 🎯 Objective

The goal of this program is to:

1.  Load a dictionary of words into a hash table
2.  Read a text file word by word
3.  Check each word against the dictionary
4.  Report all misspelled words
5.  Benchmark the time spent in each operation

---

## 📂 Project Structure

    .
    ├── speller.c
    ├── dictionary.c
    ├── dictionary.h
    ├── Makefile
    ├── dictionaries/
    │   ├── small
    │   └── large
    ├── texts/
    │   ├── alice.txt
    │   ├── holmes.txt
    │   └── ...
    └── README.md

---

## 🗃️ Data Structure

Each word is stored in a `node` inside a hash table with `456,977` buckets:

```c
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;
```

Collisions are resolved with **chaining** — each bucket holds a linked list of nodes.

---

## 🔍 How It Works

1.  The program loads the dictionary into the hash table
2.  Each word in the text file is hashed to a bucket
3.  The linked list at that bucket is traversed for a match
4.  Misspelled words are printed to the console
5.  Benchmarks are reported for all four operations

### Example:

If the text contains the word `"speling"`:

-   It gets hashed to a bucket index
-   The linked list at that bucket is traversed
-   No match is found

❌ Output:

    speling

If the word `"spelling"` is checked:

-   It hashes to its bucket
-   `strcasecmp` finds a match in the linked list

✅ No output (word is correctly spelled)

---

## ▶️ How to Run

Make sure you have `clang` and `make` installed.

``` bash
make speller
```

``` bash
# Using the default large dictionary
./speller texts/alice.txt

# Using a custom dictionary
./speller dictionaries/small texts/alice.txt
```

### Example Output:

```
MISSPELLED WORDS

foo
baz

WORDS MISSPELLED:     2
WORDS IN DICTIONARY:  143091
WORDS IN TEXT:        17756
TIME IN load:         0.03
TIME IN check:        0.04
TIME IN size:         0.00
TIME IN unload:       0.02
TIME IN TOTAL:        0.09
```

---

## 🧠 Key Concepts

-   Hash tables and linked lists
-   Dynamic memory allocation (`malloc`, `free`)
-   File I/O in C
-   String manipulation and comparison
-   Recursive algorithms
-   Memory leak prevention with `valgrind`

---

## ⚠️ Academic Honesty

This repository contains my personal solution to a CS50 problem set.

Please do not copy this code directly.\
Use it for learning and reference only.

---

## 🚀 Future Improvements

-   Experiment with a better hash function to reduce collisions
-   Compare performance against a trie-based implementation
-   Add support for custom word lengths beyond 45 characters

---
