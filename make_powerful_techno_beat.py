import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import midiutil
except ImportError:
    print("Bitte installiere midiutil: pip install midiutil")
    sys.path.exit(1)

def build_powerful_techno():
    # 4 Spuren: 1. Core-Kick, 2. Bass-Rumble, 3. Hi-Hats/Percussion, 4. Wall-of-Sound Synth
    midi = midiutil.MIDIFile(4)  
    midi.addTempo(track=0, time=0, tempo=132) # Perfekte Geschwindigkeit für schwere Rhythmen

    # --- SPUR 0: DIE KICK (Fundament) ---
    track_kick = 0
    channel_kick = 9 # Drum Channel
    for bar in range(4):
        base_time = bar * 4
        for beat in range(4):
            # Akzentuierte, brutale Kicks auf die Viertel
            midi.addNote(track_kick, channel_kick, pitch=36, time=base_time + beat, duration=0.4, volume=127)

    # --- SPUR 1: DER RUMBLE BASS (Die Wand im Low-End) ---
    # Techno-Rumble entsteht durch Echos auf den Sechzehnteln direkt NACH der Kick
    track_bass = 1
    channel_bass = 0
    bass_pitch = 41 # F1 - extrem tiefer, physischer Bass
    for bar in range(4):
        base_time = bar * 4
        for beat in range(4):
            # Die Sechzehntel-Noten, die das Fundament zum Rollen bringen
            midi.addNote(track_bass, channel_bass, pitch=bass_pitch, time=base_time + beat + 0.5, duration=0.2, volume=100)
            midi.addNote(track_bass, channel_bass, pitch=bass_pitch, time=base_time + beat + 0.75, duration=0.2, volume=90)

    # --- SPUR 2: HIGHS (Der Treiber) ---
    track_hats = 2
    channel_hats = 9
    for bar in range(4):
        base_time = bar * 4
        for beat in range(4):
            # Offbeat Open Hat (Klassiker)
            midi.addNote(track_hats, channel_hats, pitch=46, time=base_time + beat + 0.5, duration=0.3, volume=105)
            # Treibende 16tel Closed Hats für die Energie
            for step in [0.25, 0.75]:
                midi.addNote(track_hats, channel_hats, pitch=42, time=base_time + beat + step, duration=0.1, volume=80)

    # --- SPUR 3: MÄCHTIGER SYNTH-LEAD (Phrygische Wand) ---
    # Hier nutzen wir das Phrygisch-Intervall aus beat_gen.py für maximale Wucht
    track_synth = 3
    channel_synth = 1
    
    # Repetitives, marschierendes Muster auf F2 und F#2
    root_note = 53  # F2
    tension_note = 54 # F#2 (Das phrygische Halbton-Intervall)
    
    pattern = [
        (0.0, root_note),  (0.25, root_note), 
        (1.0, tension_note), (1.25, tension_note),
        (2.0, root_note),  (2.5, root_note),
        (3.0, tension_note), (3.75, root_note)
    ]
    
    for bar in range(4):
        base_time = bar * 4
        for step, pitch in pattern:
            # Volle Velocity (127) für maximalen Druck
            midi.addNote(track_synth, channel_synth, pitch=pitch, time=base_time + step, duration=0.2, volume=120)

    output_fn = "powerful_industrial_groove.mid"
    with open(output_fn, "wb") as output_file:
        midi.writeFile(output_file)
        
    print(f"[Erfolg] Mächtiger Techno-Groove als '{output_fn}' gespeichert!")

if __name__ == "__main__":
    build_powerful_techno()
