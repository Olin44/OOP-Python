from datetime import date
import re

class Note:
    ID = 0
    def __init__(self, text, tag):
        self.text = text
        self.tag = tag
        self.date = date.today()
        Note.ID += 1
        self.ID = Note.ID

    def match(self, search):
        if (re.search(search, self.tag) or re.search(search, self.text)):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.ID}, {self.text}, {self.tag}, {self.date}"

class Notebook():
    def __init__(self):
        self.notes = []
        Note.ID = 0

    def new_note(self, note):
        self.notes.append(note)

    def modify_text(self, id, text):
        if self.notes:
            self.notes[int(id)-1].text = text
        else:
            print("Pusta lista")

    def modify_tag(self, id, tag):
        if self.notes:
            self.notes[int(id)-1].tag = tag
        else:
            print("Pusta lista")

    def search(self, phrase):
        match_notes = []
        if self.notes:
            for i in range(len(self.notes)):
                print("y")
                if self.notes[i].match(phrase):
                    print("x")
                    match_notes.append(self.notes[i])
        return match_notes

    def __str__(self):
        text = ""
        for i in range(len(self.notes)):
            text += f"{self.notes[i].ID}, {self.notes[i].text}, {self.notes[i].tag}, {self.notes[i].date}\n"
        return text




