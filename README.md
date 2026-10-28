<div align="center">

# AI Skill Tracker

**Track, visualize, and deliberately improve your AI/ML skills over time.**

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

## Overview

What gets measured gets improved.  
This tool turns vague intentions like “I should get better at RAG” into concrete, trackable progress.

Designed for engineers who want deliberate practice and clear visibility into their growth in AI and machine learning.

---

## Features

- Define skills with progressive levels (Beginner → Intermediate → Advanced → Expert)
- Log practice sessions and projects against specific skills
- View progress over time
- Exportable JSON data
- Simple CLI that can later grow into a full dashboard

---

## Example Skills

| Skill                    | Current Level | Target       |
|--------------------------|---------------|--------------|
| RAG Systems              | Intermediate  | Advanced     |
| Multi-Agent Systems      | Beginner      | Intermediate |
| Fine-tuning LLMs         | Beginner      | Intermediate |
| System Design for AI     | Intermediate  | Advanced     |
| Prompt Engineering       | Advanced      | Expert       |

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/tahrjatoi/ai-skill-tracker.git
cd ai-skill-tracker

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start tracking
python tracker.py
```

### Common Commands

```bash
python tracker.py status     # View current skill levels
python tracker.py log        # Log a new practice session
```

---

## Project Structure

```text
ai-skill-tracker/
├── skills.json          # Your skill definitions & levels
├── sessions.json        # Logged practice sessions
├── tracker.py           # CLI interface
├── requirements.txt
└── README.md
```

---

## How to Use

1. Edit `skills.json` to match the skills that matter to you
2. Log sessions regularly with `python tracker.py log`
3. Review progress with `python tracker.py status`
4. Adjust targets as you grow

---

## Philosophy

Progress in AI is rarely linear.  
Having a simple system to track what you practice creates accountability and makes growth visible over weeks and months.

---

## Author

**Tahir Jatoi** — AI Engineer  
Building systems and continuously leveling up in the process.

- GitHub: [tahrjatoi](https://github.com/tahrjatoi)
- LinkedIn: [Tahir Jatoi](https://www.linkedin.com/in/tahrjatoi)

---

<div align="center">

*Deliberate practice beats random learning.*

</div>
