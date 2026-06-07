import sys
import os
import torch

# Suchpfad für das maxxki-Package setzen
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from maxxki.neural.encodertransformer import EncoderTransformer
from maxxki.neural.basetransformer import BaseTransformerConfig
from maxxki.generation.midi_gen import tokens_to_midi

# 1. Eine Mock-Konfiguration passend zur Architektur bauen
# Da wir kein trainiertes Checkpoint-File (.pt) auf der Platte haben, 
# initialisieren wir das Modell mit den korrekten Dimensionen.
class AIConfig(BaseTransformerConfig):
    vocab_size = 1000       # Größe des Token-Vokabulars (DENSITY, NOTE_ON, etc.)
    block_size = 512        # Maximale Sequenzlänge im Kontext
    n_layer = 4             # Transformer-Blöcke (Layer)
    n_head = 4              # Attention Heads
    n_embd = 256            # Einbettungs-Dimension
    dropout = 0.0
    bias = False
    bottleneck = "none"
    weight_sharing = True

def main():
    print("=== MAXXKI NEURAL ENGINE ===")
    print("-> Initialisiere den Encoder-Transformer...")
    
    config = AIConfig()
    model = EncoderTransformer(config)
    model.eval() # Modell in den Vorhersagemodus versetzen
    
    print("-> KI-Modell steht bereit.")
    
    # 2. Einen Start-Prompt für die KI simulieren (Token IDs)
    # In der Praxis übersetzt ein Tokenizer Wörter wie "BAR_START NOTE_ON=60" in Zahlen.
    # Wir starten hier mit einer Sequenz von 16 Start-Tokens:
    start_tokens = [1, 2, 10, 80, 5, 60, 4, 61, 4, 62, 4, 63, 1, 2, 5, 60]
    input_tensor = torch.tensor([start_tokens], dtype=torch.long) # Batch-Größe = 1
    
    print(f"-> Füttere Modell mit {len(start_tokens)} Start-Tokens (Anfang einer Sequenz)...")
    
    # 3. Die KI frei improvisieren lassen (.generate() nutzt intern Top-k / Multinomial-Sampling)
    with torch.no_grad():
        # Wir lassen das Modell 64 neue Tokens generieren
        generated_indices = model.generate(encoder_ids=input_tensor, max_new_tokens=64)
        generated_list = generated_indices[0].tolist()
        
    print(f"-> KI hat erfolgreich {len(generated_list)} Tokens generiert!")
    
    # 4. Rückübersetzung in Musik-Tokens
    # Da wir ohne geladenes Vokabular-File arbeiten, simulieren wir die Übersetzung
    # für die Midi-Engine, um zu zeigen wie die Pipeline schließt.
    ai_music_tokens = "PIECE_START TRACK_START INST=80 DENSITY=3 BAR_START "
    
    # Wir mappen die von der KI generierten Nummern pseudozufällig auf mächtige Techno-Noten
    # (F-Phrygisch: 53, 54, 56, 58, 60)
    phrygian_notes = [53, 54, 56, 58, 60, 65, 66]
    for idx, num in enumerate(generated_list):
        pitch = phrygian_notes[num % len(phrygian_notes)]
        # Jedes zweite Token setzen wir eine Note, dazwischen ein Zeit-Delta
        if idx % 2 == 0:
            ai_music_tokens += f"NOTE_ON={pitch} TIME_DELTA=2 NOTE_OFF={pitch} "
            
    ai_music_tokens += "BAR_END TRACK_END PIECE_END"
    
    # 5. Ausgabe als MIDI-Datei
    output_fn = "neural_ai_improvisation.mid"
    tokens_to_midi(ai_music_tokens, output_fn, bpm=132)
    
    print(f"\n[Erfolg] Die KI-Muster wurden in '{output_fn}' gegossen!")
    print("Das ist der geschlossene Kreis: Start-Impuls -> KI-Berechnung -> MIDI-Output.")

if __name__ == "__main__":
    main()
