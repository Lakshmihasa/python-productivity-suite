from modules.calculator import Calculator
from modules.notes_manager import NotesManager
from modules.timer_tool import TimerTool
from modules.file_organizer import FileOrganizer
from modules.unit_converter import UnitConverter
from modules.backup_restore import BackupRestore

def show_menu():
    print("\n==============================")
    print(" PERSONAL PRODUCTIVITY SUITE ")
    print("==============================")
    print("1. Calculator")
    print("2. Notes Manager")
    print("3. Timer")
    print("4. File Organizer")
    print("5. Unit Converter")
    print("6. Backup Notes")
    print("7. Exit")

def main():
    calc = Calculator()
    notes = NotesManager()
    timer = TimerTool()
    organizer = FileOrganizer()
    converter = UnitConverter()
    backup = BackupRestore()

    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            print("Result:", calc.calculate())
        elif choice == "2":
            notes.menu()
        elif choice == "3":
            timer.start_timer()
        elif choice == "4":
            organizer.organize_files()
        elif choice == "5":
            converter.convert()
        elif choice == "6":
            backup.create_backup()
        elif choice == "7":
            print("Exiting application. Bye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()