import sys

sys.path.insert(0, './local_lib')

from path import Path

# Crée un dossier nommé 'my_folder'
folder = Path("my_folder")
folder.makedirs_p()

# Crée un fichier 'Hello.txt' dans le dossier
file = folder / "Hello.txt"
file.write_text("Hello puta!")

# Affiche le contenu du fichier
print("Contenu du fichier :")
print(file.read_text())
