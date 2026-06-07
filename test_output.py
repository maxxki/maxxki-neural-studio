import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from maxxki.generation.midi_gen import build_prompt, tokens_to_midi

def main():
    print("Generiere Synth-Synthesizer-Spur über Tokens...")
    
    # 1. Wir bauen ein Token-Muster (So sieht die Musik für die KI aus)
    prompt_tokens = build_prompt(instrument="synth", density="dense", bars=4)
    print("\nSo sieht die 'Musik' im Speicher aus (KI-Sprache):")
    print(prompt_tokens[:150] + " ... [gekürzt]")
    
    # 2. Wir schreiben das in eine echte MIDI-Datei auf deine Festplatte
    output_fn = "techno_synth_output.mid"
    tokens_to_midi(prompt_tokens, output_fn, bpm=135)
    
    print(f"\n[Erfolg] Datei '{output_fn}' wurde im Hauptordner erstellt!")
    print("Du kannst diese Datei jetzt in FL Studio, Ableton oder VLC ziehen und anhören.")

if __name__ == "__main__":
    main()
