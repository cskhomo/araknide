# Araknide

Automation pipeline for generating draft reports of KDE application activity from GitLab data.

Designed to support **This Week in KDE Apps (TWiKA)** by reducing the manual effort required to identify and structure meaningful updates across hundreds of repositories.

---

## Context

KDE publishes weekly updates summarizing notable changes across its applications.

This requires contributors to:
- Review large volumes of commits and merge requests  
- Identify changes relevant to users (features, UI improvements, major fixes)  
- Ignore low-signal technical noise  
- Rewrite technical content into user-friendly summaries  

This process is **time-intensive, inconsistent, and difficult to scale**.

---

## Problem

> “That’s the hard part.” — KDE Maintainers

Automatically identifying *meaningful* changes is non-trivial because:

- Most commits are not user-relevant  
- Commit quality and structure vary  
- Important changes are not always explicitly labeled  
- Human judgment is still required for final output  

---

## Approach

Araknide focuses on solving the **80% problem**:

Instead of fully automating reporting, it generates a **structured draft** that significantly reduces manual effort.

---

## What It Does

- Collects merged commits and merge requests from KDE repositories  
- Filters entries using known commit conventions:
  - `BUG:`
  - `FEATURE:`
  - `GUI:`
  - `CHANGELOG:`  
- Groups results by project  
- Outputs a structured Markdown draft  

---

## Key Idea

> Araknide is not a replacement for human editors — it is a **force multiplier**.

It:
- Surfaces potentially relevant changes  
- Reduces noise  
- Provides a starting point for editorial refinement  

---

## Pipeline

```
GitLab API
    ↓
Repository & Commit Collection
    ↓
Keyword Filtering + Heuristics
    ↓
Project Grouping
    ↓
Markdown Draft Generation
```

---

## Design Challenges

### 1. Signal vs Noise
Most commits are not meaningful to end users.

### 2. Inconsistent Annotations
Not all developers use keywords consistently (`FEATURE:`, `GUI:`).

### 3. Human-Centric Output
Raw commit messages are not suitable for publication without rewriting.

### 4. Scale
KDE spans hundreds of repositories and large datasets.

---

## Origin

This project was developed in response to a KDE task to:

> Automate the collection and structuring of weekly application updates for TWiKA

The goal is to make reporting:
- Sustainable  
- Scalable  
- Contributor-friendly  

---

## License

GPL-3.0
