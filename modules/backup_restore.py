import shutil
import datetime

class BackupRestore:
    def create_backup(self):
        time = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        shutil.copy(
            "Data/notes.json",
            f"Data/backups/notes_backup_{time}.json"
        )
        print("✅ Backup created")
