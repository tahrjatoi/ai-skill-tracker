# AI Skill Tracker

Track, visualize, and level up your AI/ML skills over time.

This is a simple but powerful tool for engineers who want deliberate practice and clear visibility into their growth.

## Features

- Define skills with levels (Beginner → Intermediate → Advanced → Expert)
- Log practice sessions and projects against skills
- See progress over time
- Exportable data (JSON)
- Ready to be extended into a web dashboard

## Quick Start

```bash
pip install -r requirements.txt
python tracker.py
```

## Example Skills

| Skill                    | Current Level | Target     |
|--------------------------|---------------|------------|
| RAG Systems              | Intermediate  | Advanced   |
| Multi-Agent Systems      | Beginner      | Intermediate |
| Fine-tuning LLMs         | Beginner      | Intermediate |
| System Design for AI     | Intermediate  | Advanced   |
| Prompt Engineering       | Advanced      | Expert     |

## How to Use

1. Edit `skills.json` to match the skills you care about
2. Log sessions with `python tracker.py log`
3. View progress with `python tracker.py status`

## Project Structure

```
ai-skill-tracker/
├── skills.json          # Your skill definitions
├── sessions.json        # Logged practice sessions
├── tracker.py           # CLI interface
└── requirements.txt
```

## Philosophy

What gets measured gets improved.  
This tool turns vague "I should learn X" into concrete tracking so you can see real progress.

---

Built by Tahir Jatoi · AI Engineer
