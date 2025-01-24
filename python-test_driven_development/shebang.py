#!/usr/bin/python3

import os

# Chemin du répertoire actuel
current_directory = os.getcwd()

# Parcourir tous les fichiers dans le répertoire actuel
for filename in os.listdir(current_directory):
    if filename.endswith('.py'):
        file_path = os.path.join(current_directory, filename)
        
        # Ouvrir le fichier et lire son contenu
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Vérifier si le shebang est déjà présent
        if not lines or lines[0].strip() != '#!/usr/bin/python3':
            # Ajouter le shebang au début
            lines.insert(0, '#!/usr/bin/python3\n')
            
            # Écrire le contenu modifié dans le fichier
            with open(file_path, 'w') as file:
                file.writelines(lines)