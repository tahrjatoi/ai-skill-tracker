#!/usr/bin/env python3
"""AI Skill Tracker CLI"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List

SKILLS_FILE = Path("skills.json")
SESSIONS_FILE = Path("sessions.json")

def load_json(path: Path) -> Dict:
    if not path.exists():
        return {}
    with open(path) as f:
        return json.load(f)

def save_json(path: Path, data: Dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def show_status():
    data = load_json(SKILLS_FILE)
    skills = data.get("skills", [])
    
    print("\nAI Skill Tracker — Current Status")
    print("=" * 50)
    print(f"{'Skill':<28} {'Level':<14} {'Target'}")
    print("-" * 50)
    for s in skills:
        print(f"{s['name']:<28} {s['level']:<14} {s['target']}")
    print()

def log_session(skill_id: str, minutes: int, notes: str = ""):
    skills_data = load_json(SKILLS_FILE)
    sessions_data = load_json(SESSIONS_FILE)
    
    skill = next((s for s in skills_data.get("skills", []) if s["id"] == skill_id), None)
    if not skill:
        print(f"Skill '{skill_id}' not found.")
        return
    
    session = {
        "skill_id": skill_id,
        "skill_name": skill["name"],
        "minutes": minutes,
        "notes": notes,
        "date": datetime.now().isoformat(timespec="seconds"),
    }
    
    sessions_data.setdefault("sessions", []).append(session)
    save_json(SESSIONS_FILE, sessions_data)
    print(f"Logged {minutes} min on {skill['name']}")

def main():
    import sys
    if len(sys.argv) < 2 or sys.argv[1] == "status":
        show_status()
    elif sys.argv[1] == "log" and len(sys.argv) >= 4:
        skill_id = sys.argv[2]
        minutes = int(sys.argv[3])
        notes = " ".join(sys.argv[4:]) if len(sys.argv) > 4 else ""
        log_session(skill_id, minutes, notes)
    else:
        print("Usage:")
        print("  python tracker.py status")
        print("  python tracker.py log <skill_id> <minutes> [notes]")
        print("\nSkill IDs: rag, agents, finetuning, system-design, prompting, python-ai")

if __name__ == "__main__":
    main()
