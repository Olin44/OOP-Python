from notatnik import Note, Notebook

class Menu:
    def __init__(self):
        self.options =  {"1": self.show_notes,
                         "2": self.search_notes,
                         "3": self.add_note,
                         "4": self.modify_note,
                         "5": self.quit}
        self.notebook = Notebook()
        note1 = Note("xxx", "xx")
        note2 = Note("xxx", "xc")
        self.notebook.new_note(note1)
        self.notebook.new_note(note2)
        self.run()
    def show_menu(self):
            print("\n"
                  "Opcje:\n"
                  "1. Pokaż notatki\n"
                  "2. Wyszukaj notatki z podaną frazą\n"
                  "3. Dodaj notatkę\n"
                  "4. Modyfikuj notatkę\n"
                  "5. Wyjdź z programu\n")
    def run(self):
        while True:
            self.show_menu()
            key = input("Wpisz klucz polecenia: ")
            self.options[key]()
        return 0

    def show_notes(self):
        for i in range(len(self.notebook.notes)):
            print(self.notebook.notes[i])

    def search_notes(self):
        key = input("Wpisz szukaną frazę: ")
        match = self.notebook.search(key)
        print("Notatki z podaną frazą: \n")
        for i in range(len(match)):
            print(match[i])

    def add_note(self):
        tag = input("Podaj tytuł notatki")
        text = input("\nPodaj tekst:")
        note = Note(tag, text)
        self.notebook.new_note(note)
        print("Notatka poprawnie dodana!\n" + str(self.notebook))

    def modify_note(self):
        chose = input("1. Edytuj tytuł. \n2 Edytuj tekst")
        id = 0
        if chose == "1":
            id = input("Podaj ID notatki do edycji: ")
            tag = input("Podaj nowy tytuł: ")
            self.notebook.modify_tag(int(id), tag)
        if chose == "2":
            id = input("Podaj ID notatki do edycji: ")
            tag = input("Podaj nowy tekst: ")
            self.notebook.modify_tag(int(id), tag)
        print(self.notebook)

    def quit(self):
        del Menu
        return False

menu1 = Menu()
