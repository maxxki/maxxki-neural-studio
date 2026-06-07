import os
import json
from datasets import load_from_disk
from tqdm import tqdm

def main():
    # Pfade definieren (wie im Preprocessing)
    input_dir = "data/jsfakes4bars/generation"
    
    print(f"-> Lade Datensatz aus {input_dir}...")
    dataset = load_from_disk(input_dir)
    
    # Für jeden Split (train, test, validation, etc.) eine .jsonl Datei schreiben
    for split in dataset.keys():
        output_file = os.path.join(input_dir, f"{split}.jsonl")
        print(f"-> Schreibe {output_file}...")
        
        with open(output_file, "w", encoding="utf-8") as f:
            for row in tqdm(dataset[split]):
                # Zeile als JSON-String schreiben
                f.write(json.dumps(row) + "\n")
                
    print("\n[Erfolg] Die benötigten .jsonl Dateien wurden erfolgreich erstellt!")

if __name__ == "__main__":
    main()
