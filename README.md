# MicroTask Orchestrator

## Overview
MicroTask Orchestrator is an AI-powered task planning agent that converts a set of user-defined tasks (or a high-level goal) into an optimized execution workflow. It structures tasks, removes redundancy, identifies dependencies, and organizes them into clear, phase-based steps.

---

## Features
- Task structuring and grouping
- Dependency detection
- Redundancy elimination
- Priority-based ordering
- Phase-wise execution planning
- Clean and readable output formatting

---

## Architecture
The system uses a multi-agent pipeline:

1. **Task Structurer**
   - Groups related tasks
   - Identifies dependencies
   - Removes duplicates

2. **Task Optimizer**
   - Creates execution phases
   - Prioritizes tasks
   - Improves workflow efficiency

3. **Formatter**
   - Presents output in a structured format
   - Organizes tasks into phases and ordered steps

---

## Workflow
1. User provides tasks or a goal
2. Tasks are stored in state (`TASKS`)
3. Agents process tasks sequentially:
   - Structuring → Optimization → Formatting
4. Final execution plan is generated

---

## Setup

### 1. Create Project Directory
```bash
cd ~ && mkdir -p microtask_orchestrator && cd microtask_orchestrator
