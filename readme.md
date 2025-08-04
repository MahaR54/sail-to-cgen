**sail-to-cgen**
LFX Mentorship Coding Challenge Submission
A tool to convert structured YAML data into S-expression format, inspired by the instruction semantics work done in the SAIL ISA specification language and its CGEN backend transformations.

📝 Project Overview
This project implements a transformation pipeline that takes structured data in YAML format (representing nested trees and tabular data) and converts it into LISP-style S-expressions. This format mimics how ISA semantics might be represented or interpreted in compiler toolchains and formal models.
It is designed as a demonstration of understanding the SAIL to CGEN goal: automating the export of processor instruction set definitions from formal models (like Sail) to practical toolchain formats (like CGEN used by GCC).

✅ Features
Parse nested YAML structures
Convert values into S-expressions
Format special types like:
Dates → (make-date YYYY MM DD)
Symbols → 'A4786
Clean output matching the LISP syntax used in CGEN backends
Fully matches challenge example from Wikipedia YAML
