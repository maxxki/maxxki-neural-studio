import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Wir importieren die echte MIDI-Bibliothek
try:
    import midiutil
except ImportError:
    print("Bitte installiere midiutil: pip install midiutil")
    sys.path.exit(1)

def build_real_techno_midi():
    # Erstellt eine MIDI-Datei mit 3 Spuren (Drums, Bass, Synth)
    midi = midiutil.MIDIFile(3)  
    midi.addTempo(track=0, time=0, tempo=135) # 135 BPM Industrial Techno
    
    # --- SPUR 0: TECHNO DRUMS (Kanal 9 ist Standard für Drums) ---
    # Wir bauen den klassischen "Four-to-the-Floor" Beat über 4 Takte (16 Schläge)
    track = 0
    channel = 9
    
    for bar in range(4):
        base_time = bar * 4
        # Kick Drum (Note 36) auf jede 1 (0, 1, 2, 3 im Takt)
        for beat in range(4):
            midi.addNote(track, channel, pitch=36, time=base_time + beat, duration=0.5, volume=120)
        
        # Offbeat Hi-Hat (Note 42) immer GENAU zwischen den Kicks (0.5, 1.5, 2.5, 3.5)
        for hhat in range(4):
            midi.addNote(track, channel, pitch=42, time=base_time + hhat + 0.5, duration=0.2, volume=90)

    # --- SPUR 1: REEL TECHNO BASS (A-Moll / Note 45) ---
    # Typischer treibender Offbeat-Bass, der den Techno-Rhythmus drückt
    track = 1
    channel = 0
    bass_pitch = 45 # A1 (Düsterer Bass)
    
    for bar in range(4):
        base_time = bar * 4
        # Der Bass spielt auf den Sechzehnteln zwischen den Kicks
        for step in [0.5, 0.75, 1.5, 1.75, 2.5, 2.75, 3.5, 3.75]:
            midi.addNote(track, channel, pitch=bass_pitch, time=base_time + step, duration=0.2, volume=100)

    # Datei auf die Festplatte schreiben
    output_fn = "real_techno_groove.mid"
    with open(output_fn, "wb") as output_file:
        midi.writeFile(output_file)
        
    print(f"[Erfolg] ECHTER Techno-Groove wurde als '{output_fn}' gespeichert!")
    print("Zieh diese Datei in deine DAW. Jetzt hast du die Kick auf der 1, die Hi-Hats im Offbeat und den rollenden Techno-Bass.")

if __name__ == "__main__":
    build_real_techno_midi()
