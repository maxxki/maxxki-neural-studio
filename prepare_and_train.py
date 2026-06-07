import sys
import os

# Suchpfad setzen
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from maxxki.neural.preprocess import peprocess

def main():
    print("=== SCHRITT 1: DATEN-PREPROCESSING ===")
    print("Konvertiere MIDI-Daten in KI-Tokens...")
    
    # Wir rufen deine preprocess.py auf.
    # Sie nimmt den Datensatz (Standard: TristanBehrens/js-fakes-4bars von HuggingFace)
    # und bereitet ihn in 'data/jsfakes4bars/generation/' für das Modell vor.
    peprocess(
        dataset_id="TristanBehrens/js-fakes-4bars",
        output_path="data/jsfakes4bars",
        padding_length=512,
        mode="generation"
    )
    
    print("\n[Erfolg] Daten wurden tokenisiert und unter 'data/jsfakes4bars' gespeichert!")
    print("\n=== SCHRITT 2: TRAINING STARTEN ===")
    print("Um das Training jetzt zu starten, führe folgenden Befehl im Terminal aus:")
    print("python maxxki/neural/train.py --data_dir data/jsfakes4bars/generation --epochs 5")

if __name__ == "__main__":
    main()
