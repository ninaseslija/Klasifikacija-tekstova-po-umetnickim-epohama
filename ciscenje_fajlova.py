import os
from gutenberg_cleaner import simple_cleaner

# Glavni folder sa svim epohama
input_root = "chapters"
output_root = "chapters_cleaned"

# Napravi output folder ako ne postoji
os.makedirs(output_root, exist_ok=True)

# Prođi rekurzivno kroz sve podfoldere
for root, dirs, files in os.walk(input_root):
    for file in files:
        if file.endswith(".txt"):
            input_path = os.path.join(root, file)

            # Napravi odgovarajući izlazni put
            relative_path = os.path.relpath(root, input_root)
            output_dir = os.path.join(output_root, relative_path)
            os.makedirs(output_dir, exist_ok=True)

            output_path = os.path.join(output_dir, file)

            # Pročitaj fajl
            with open(input_path, "r", encoding="utf-8") as f:
                text = f.read()

            # Očisti pomoću gutenberg_cleaner
            cleaned_text = simple_cleaner(text)

            # Sačuvaj očišćen fajl u novi folder
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(cleaned_text)

            print(f"Očišćen fajl: {input_path} → {output_path}")

print("\n Svi fajlovi su očišćeni i sačuvani u 'chapters_cleaned' folderu!")
