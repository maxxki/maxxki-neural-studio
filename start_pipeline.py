import sys
import os

# Stellt sicher, dass das Hauptverzeichnis im Suchpfad ist, damit "maxxki" importiert werden kann
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Jetzt mit den korrekten Pfaden laut deiner Tree-Struktur:
from maxxki.core.orchestrator import SessionConfig, ProductionSession, StemMixer

def main():
    print("=== MAXXKI Musik-Pipeline wird gestartet ===")
    
    # 1. Konfiguration definieren
    config = SessionConfig(
        user_prompt="Industrial Dark Techno mit harten Drums",
        vibe_hint="dark_techno",
        duration_seconds=15,
        bpm=135,
        key="Am",
        genre="techno",
        use_beat_gen=True,
        use_midi_gen=True,
        use_music_gen=False,
        use_neural_bass=False
    )
    
    print(f"-> Konfiguration geladen: {config.genre.upper()} bei {config.bpm} BPM in {config.key}")

    # 2. Produktions-Session initialisieren
    session = ProductionSession(
        session_id="test_session_001",
        config=config
    )
    print(f"-> Session '{session.session_id}' erfolgreich instanziiert.")
    
    # 3. Den Mixer vorbereiten
    mixer = StemMixer(bpm=config.bpm)
    print("-> Mixer-Modul initialisiert.")
    
    print("\n[Erfolg] Die Grundstruktur steht!")

if __name__ == "__main__":
    main()
