import json
from datetime import datetime

class NotesManager:
    def __init__(self):
        self.file = "Data/notes.json"
        self.load_notes()

    def load_notes(self):
        try:
            with open(self.file, "r") as f:
                self.notes = json.load(f)
        except:
            self.notes = []

    def save_notes(self):
        with open(self.file, "w") as f:
            json.dump(self.notes, f, indent=2)

    def add_note(self):
        title = input("Enter title: ")
        content = input("Enter content: ")

        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "content": content,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.notes.append(note)
        self.save_notes()
        print("✅ Note added successfully")

    def view_notes(self):
        for n in self.notes:
            print(n["id"], n["title"], "-", n["created"])

    def menu(self):
        print("\nNOTES MANAGER")
        print("1. View Notes")
        print("2. Add Note")

        choice = input("Choose: ")
        if choice == "1":
            self.view_notes()
        elif choice == "2":
            self.add_note()