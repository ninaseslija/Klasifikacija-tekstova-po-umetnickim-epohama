import os
import re
from gutenberg_cleaner import simple_cleaner   


def poglavlja():
    patterns = r"^(?:PART|CHAPTER|Chapter|X|V|I|L|Sonnet|ACT|Scene|CANTO|NOVEL|OF THEIR|BOOK|\[\s*\d+\s*\]).*"
    broj_poglavlja_po_epohi = {}

    folders = {
        "Realizam": "Realizam",
        "Romantizam": "Romantizam",
        "Renesansa" : "Renesansa",
        "Modernizam" : "Modernizam"
    }

    for label, folder_path in folders.items():
        broj_poglavlja = 0
        for filename in os.listdir(folder_path):
            
            if filename.endswith(".txt"):
                file_path = os.path.join(folder_path, filename)

                with open(file_path, "r", encoding="utf-8") as f:
                    text = f.read()
                text = simple_cleaner(text)

                lines = text.splitlines()
                lines = [line.strip() for line in lines if line.strip()]
                text = "\n".join(lines)

                chapters = re.split(patterns, text, flags=re.MULTILINE | re.IGNORECASE)
                chapters = [c.strip() for c in chapters if c.strip()]

                for i, ch in enumerate(chapters, start = 1):
                    output_dir = os.path.join("chapters", label, filename.replace(".txt", ""))
                    os.makedirs(output_dir, exist_ok=True)

                    chapter_filename = f"chapter_{i}.txt"
                
                    chapter_path = os.path.join(output_dir, chapter_filename)

                    with open(chapter_path, "w", encoding="utf-8") as out_f:
                        broj_poglavlja+=1
                        out_f.write(ch)
        broj_poglavlja_po_epohi[label] = broj_poglavlja
        print(f"broj poglavlja za: {broj_poglavlja_po_epohi}")
    return broj_poglavlja_po_epohi





    



