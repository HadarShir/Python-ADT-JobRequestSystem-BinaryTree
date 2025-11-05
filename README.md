# Python ADT Project – Job Request System & Binary Tree

## Overview
Academic Python project implementing core **Abstract Data Types** and algorithms:
- **ADTs:** LinkedList, Stack, Queue (used as building blocks).
- **Job Request System:** rank-based scheduling over available CPU nodes with waiting/initialized containers and resource allocation/release logic.
- **Binary Tree:** root-to-leaf path discovery (recursive & iterative), printing same-level “neighbors”, and symmetry check.

This assignment follows strict academic constraints (no external libs, input validation, and clear docstrings).

## Structure
- `ADTs.py` – Generic linked list, stack, and queue implementations. :contentReference[oaicite:4]{index=4}
- `Job.py`, `CPUNodes.py`, `JobRequestSystem.py` – Job entity, CPU bundles list, and the ranked job scheduler. :contentReference[oaicite:5]{index=5}
- `BinaryTree.py` – Binary-tree utilities: paths (rec/iter), same-level neighbors, symmetry. :contentReference[oaicite:6]{index=6}
- `example_*.txt` – Example inputs/outputs for quick testing. :contentReference[oaicite:7]{index=7}

## Key Features
- Rank-based job scheduling with **waiting stack** and **initialized queue**; resource checks and graceful messages.
- CPU capacity model as a **linked list** of bundles; **occupy/free** semantics with correct invariants.
- Binary-tree algorithms: **paths root→leaf** (recursive & stack-based iterative), **neighbors at same depth**, **is_symmetric()**.

## How to Run
- Ensure Python 3.x is installed.
- Run the system and binary-tree demos using the provided example input files.
- No external dependencies are required.

## Notes
Code emphasizes **clean ADT usage**, **input validation**, and **academic clarity** (docstrings and exceptions).
