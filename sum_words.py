# BROJ RECI U FOLDERU

import os
def broj_reci(dokument):

    folder_path = rf"C:\Users\ninas\Downloads\bag_of_words_test\chapters\{dokument}"
    total_words = 0

    for filename in os.listdir(folder_path): #os.listdir vraca listu svih fajlova i podfoldera unutar folder_path
        if filename.endswith(".txt"):  # računa samo txt fajlove
            file_path = os.path.join(folder_path, filename) #spajamo putanju foldera (romantizma) sa trenutnim .txt
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
                total_words += len(text.split())

    print(f"Ukupan broj reči u folderu {dokument}: {total_words}")
    return total_words
        
