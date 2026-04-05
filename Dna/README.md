In a file called dna.py in a folder called dna, implement a program that identifies to whom a sequence of DNA belongs.

# DNA Profiling with STRs

## 🧬 What is DNA?

DNA is a sequence of molecules called **nucleotides**, arranged in a double helix structure.  
Each nucleotide contains one of four bases:

- Adenine (A)
- Cytosine (C)
- Guanine (G)
- Thymine (T)

Every human cell contains **billions of nucleotides** arranged in sequence.

Some parts of DNA are very similar across humans, while others vary significantly.

---

## 🔁 Short Tandem Repeats (STRs)

**Short Tandem Repeats (STRs)** are short sequences of DNA that repeat consecutively.

Example:
- STR: `AGAT`
- Alice: `AGAT` repeated 4 times
- Bob: `AGAT` repeated 5 times

The number of repeats varies between individuals, making STRs useful for identification.

---

## 🎯 Why Use Multiple STRs?

Using multiple STRs improves accuracy.

- Probability of matching 1 STR: ~5%
- Probability of matching 10 STRs: ~1 in 1 quadrillion

This assumes STRs are independent.

Real-world systems like **CODIS (FBI DNA database)** use **20 STRs**.

---

## 🗃️ DNA Database Format

A DNA database can be represented as a CSV file:

```csv
name,AGAT,AATG,TATC
Alice,28,42,14
Bob,17,22,19
Charlie,36,18,25
