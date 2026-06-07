# ⬡ MAXXKI Neural Studio

**AI-Powered Music Production System — 100% Local, Pharma-Grade Provenance**

[![Tests](https://img.shields.io/badge/tests-140%2B-green)](tests/)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://python.org)
[![PyTorch](https://img.shields.io/badge/pytorch-2.0%2B-orange)](https://pytorch.org)
[![License](https://img.shields.io/badge/license-MIT-purple)](LICENSE)

> *"The Produck meets Kingston — dark minimal meets neural synthesis"*

---

## 🎛️ Was ist MAXXKI?

MAXXKI ist ein **komplett lokales** Musikproduktionssystem, das KI-gestützte Generierung, Mastering und Provenance-Verfolgung in einer Pipeline vereint. Keine API-Keys, keine Cloud — 100% Offline-fähig.

### Kernkomponenten

| Modul | Zweck | Status |
|-------|-------|--------|
| 🧠 **Neural Engine** | Encoder-Transformer mit VAE-Bottlenecks für Bassline-Generierung | ✅ Produktiv |
| 🎹 **Beat Generator** | Multi-Track MIDI (Chords, Bass, Melody, Drums) | ✅ Produktiv |
| 🎵 **MIDI Generator** | GPT-2-basierte Token-Generierung (ai-guru/lakhclean) | ✅ Produktiv |
| 🎶 **Music Generator** | MusicGen Small (facebook/musicgen-small) | ✅ Produktiv |
| 👂 **Master-Ear** | GPT-2-basierte Mastering-Analyse + Post-Processing | ✅ Produktiv |
| 🎛️ **Orchestrator** | Koordiniert die gesamte Pipeline | ✅ Produktiv |
| 🔐 **Provenance** | Hash-Chain Registry + HMAC-Signatur (ALCOA+) | ✅ Produktiv |
| 🎹 **Kalado** | Dancehall-Style Presets (The Produck meets Kingston) | ✅ Produktiv |
| 💾 **MV-1 Export** | Roland Verselab MV-1 Optimierung (FAT32 8.3) | ✅ Produktiv |

---

## 🏗️ Architektur

```
maxxki/
├── core/                    # Orchestrator & Session-Management
│   ├── orchestrator.py      # Haupt-Pipeline
│   └── session.py           # Session-State
│
├── neural/                  # Neuronale Netzwerke
│   ├── encodertransformer.py    # Encoder-Transformer (Bach → Bass)
│   ├── transformer.py           # Encoder-Decoder Transformer
│   ├── basetransformer.py       # Abstrakte Basisklasse
│   ├── bottlenecks.py           # VAE-Bottlenecks (Linear/CNN)
│   ├── layers.py                # Attention, MLP, LayerNorm
│   ├── engine.py                # Neural Bass Engine
│   ├── euphonic.py              # Skalen-Quantisierung
│   ├── tokenizer.py             # Token-Vocabulary
│   ├── dataset.py               # HuggingFace Datasets Loader
│   ├── trainer.py               # Training Loop
│   ├── train.py                 # Legacy Training
│   ├── preprocess.py            # Dataset-Preprocessing
│   └── generate.py              # Autoregressive Generierung
│
├── generation/              # Musik-Generierung
│   ├── beat_gen.py          # Multi-Track MIDI Generator
│   ├── midi_gen.py          # GPT-2 MIDI Token Generator
│   ├── music_gen.py         # MusicGen Audio Generator
│   └── kalado.py            # Dancehall Style Presets
│
├── mastering/               # Mastering & Post-Processing
│   └── master_ear.py      # GPT-2 Analyse + scipy Processing
│
├── provenance/              # Audit-Trail & Signatur
│   ├── fingerprint.py       # SHA256 + HMAC-SHA256
│   ├── registry.py          # Append-only Hash-Chain
│   ├── registry_lock.py     # File-Lock (Singleton)
│   ├── sign_session.py      # Signier-Workflow
│   └── verify.py            # Verifikation
│
└── hardware/              # Hardware-Integration
    └── __init__.py          # Roland MV-1, etc.

scripts/                   # CLI-Tools
├── runtraining.py         # Training starten
├── runtraininggrid.py     # Grid-Search
├── generate_to_midi.py    # MIDI-Generierung
├── generate_to_mv1.py     # MV-1 Export
├── make_my_dataset.py     # Dataset aus MIDI erstellen
├── check_vocab.py         # Vokabular prüfen
└── quick_sign.py          # Batch-Signierung

tests/                     # Test-Suite (140+ Tests)
├── test_provenance.py
├── test_neural.py
├── test_generation.py
├── test_mastering_core.py
├── test_scripts.py
├── test_edge_cases.py
├── conftest.py
└── run_tests.py
```

---

## 🚀 Schnellstart

### 1. Installation

```bash
# Repository klonen
git clone https://github.com/maxxki/neural-studio.git
cd maxxki-neural-studio

# Virtuelle Umgebung
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Abhängigkeiten
pip install torch torchvision torchaudio
pip install transformers datasets accelerate
pip install numpy scipy soundfile
pip install midiutil note-seq
pip install wandb  # Optional für Logging
```

### 2. Training (Optional)

```bash
# Dataset vorbereiten
python scripts/make_my_dataset.py

# Training starten
python scripts/runtraining.py

# Grid-Search
python scripts/runtraininggrid.py
```

### 3. Generierung

```bash
# Beat generieren (interaktiv)
python -m maxxki.generation.beat_gen

# MIDI mit GPT-2
python -m maxxki.generation.midi_gen --instrument piano --density sparse --bpm 120

# Audio mit MusicGen
python -m maxxki.generation.music_gen "dark techno beat" --duration 15

# Kalado Dancehall
python -m maxxki.generation.kalado --preset dark_riddim
```

### 4. Mastering & Export

```bash
# Vollständige Pipeline
python -m maxxki.core.orchestrator

# MV-1 Export
python scripts/generate_to_mv1.py
```

---

## 🎛️ Module im Detail

### Neural Engine (`maxxki.neural`)

**Encoder-Transformer** mit **VAE-Bottleneck** für latente Bassline-Repräsentationen:

```python
from maxxki.neural import EncoderTransformer, EncoderTransformerConfig

config = EncoderTransformerConfig(
    vocab_size=320,
    n_layer=4,
    n_head=8,
    n_embd=256,
    block_size=512,
    bottleneck="VariationalCNNBottleneck",
    bottleneck_channels_list=[128, 256, 320]
)

model = EncoderTransformer(config)

# Generierung aus latenter Repräsentation
z = torch.randn(1, 4, 32, 64)  # Bottleneck-Shape
indices = model.generate(bottleneck_condition=z, temperature=0.85)
```

**Bottleneck-Varianten:**
- `Linear1DBottleneck` — Flatten + Linear
- `Linear2DBottleneck` — Per-Token Linear
- `CNNBottleneck` — Conv1D Encoder/Decoder
- `VariationalLinear1DBottleneck` — VAE mit KL-Loss
- `VariationalLinear2DBottleneck` — 2D VAE
- `VariationalCNNBottleneck` — CNN VAE

### Beat Generator (`maxxki.generation.beat_gen`)

Interaktiver Multi-Track MIDI Generator:

```bash
$ python -m maxxki.generation.beat_gen

MAXXKI Beat Generator
Multi-Track MIDI für LMMS/ZenBeats

Genre: dark
Tonart: C
BPM: 90
Takte: 16
...
✓ Fertig! → ~/projects/mk/music-output/midi/dark_C_90bpm_16bars.mid
```

**Features:**
- 11 Genres (Pop, Jazz, Blues, Lofi, Dark, Drill, Techno, ...)
- 7 Skalen (Major, Minor, Dorian, Phrygian, Mixolydian, Pentatonic, Blues)
- 8 Chord-Typen (Major, Minor, Maj7, Min7, Dom7, Sus2, Sus4, Dim)
- 6 Drum-Patterns (Basic, Trap, Lofi, Dancehall, Techno, Afrobeats)
- Humanized Velocity
- Configurable Density

### MIDI Generator (`maxxki.generation.midi_gen`)

GPT-2-basierte MIDI-Generierung mit `ai-guru/lakhclean_mmmtrack_4bars_d-2048`:

```python
from maxxki.generation.midi_gen import build_prompt, generate_tokens, tokens_to_midi

prompt = build_prompt("piano", "normal", bars=4)
tokens = generate_tokens(prompt, max_new_tokens=512)
tokens_to_midi(tokens, "output.mid", bpm=120)
```

**Fixes v1.1:**
- Multi-Track Parser (alle Tracks statt nur erster)
- Korrekte Channel-Zuweisung (CH9 für Drums)
- Keine BAR_END Timing-Drift
- FAT32 8.3-kompatible Filenames

### Music Generator (`maxxki.generation.music_gen`)

MusicGen Small mit Singleton-Pattern:

```python
from maxxki.generation.music_gen import MusicGenerator, MusicGeneratorConfig

gen = MusicGenerator.get_instance(MusicGeneratorConfig())
path = gen.generate("dark dancehall riddim, heavy 808", duration=15)
```

**Fixes v2:**
- `top_p=0.95` statt `0.0` (Nucleus Sampling)
- `guidance_scale=3.0` mit Prompt, `1.0` ohne
- Config-bewusste Singleton-Invalidierung
- Shared ThreadPoolExecutor

### Master-Ear (`maxxki.mastering.master_ear`)

GPT-2-basierte Mastering-Analyse (Rule-based Fallback):

```python
from maxxki.mastering.master_ear import GPT2MasterEar, PostProcessor

ear = GPT2MasterEar()
profile, musicgen_prompt, analysis = ear.analyze("dark minimal techno 140 bpm")

# Post-Processing
audio = scipy.io.wavfile.read("raw.wav")
processor = PostProcessor(profile)
mastered = processor.process(audio, 44100)
```

**Mastering Chain:**
1. Highpass (konfigurierbare Cutoff)
2. EQ (Sub-Boost, Mid-Scoop, High-Shelf)
3. Kompression (Ratio, Threshold, Attack/Release)
4. Sidechain (optional, konfigurierbar)
5. Reverb (Comb + Allpass)
6. Limiter (-0.5dB Ceiling)

### Provenance (`maxxki.provenance`)

Pharma-Grade Audit-Trail:

```python
from maxxki.provenance.fingerprint import create_manifest, verify_signature
from maxxki.provenance.registry import MAXXKIRegistry

# Manifest erstellen
manifest = create_manifest(
    session_id="mxk_20240101_120000",
    prompt="dark techno",
    generator="musicgen-small",
    duration_s=15.0,
    sample_rate=44100,
    raw_audio=audio_array,
    final_path=Path("output.wav")
)

# In Registry eintragen
reg = MAXXKIRegistry()
entry = reg.append(manifest)

# Chain verifizieren
ok, msg = reg.verify_chain()
# → True, "Chain OK — 42 Einträge verifiziert"
```

**ALCOA+ Features:**
- **Attributable**: Host, User, Timestamp in Provenance
- **Legible**: JSON-Formate, klare Struktur
- **Contemporaneous**: UTC-Timestamps
- **Original**: SHA256 über Roh- und Final-Audio
- **Accurate**: HMAC-SHA256 Signatur
- **Complete**: Hash-Chain verhindert Tampering
- **Consistent**: Deterministische Hash-Berechnung
- **Enduring**: Append-only Registry
- **Available**: Lokale Speicherung

---

## 🎹 Kalado Dancehall

Spezialmodul für Dancehall-Produktion im Stil von **Kalado** — *The Produck meets Kingston*:

```bash
python -m maxxki.generation.kalado --preset dark_riddim
```

**Style-Merkmale:**
- Heavy 808 Sub-Bass (+8dB, 40-60Hz Fokus)
- Sparse Percussion (Kick, Snare, minimal Hi-Hats)
- Dark Synth-Stabs (minor/Phrygian)
- Aggressive Sidechain-Pumpe (0.6)
- Maximal 3-4 Elemente gleichzeitig
- 100 BPM, lazy but heavy

**Presets:** `dark_riddim`, `produck_bashment`, `midnight_kingston`, `808_pressure`

---

## 💾 Roland Verselab MV-1 Export

Pharma-Grade MIDI-Optimierung für Hardware:

```bash
python scripts/generate_to_mv1.py
```

**Features:**
- FAT32 8.3-Filename-Konvertierung
- MV-1 Grid-Quantisierung (480 PPQN)
- Velocity-Steps (16, 48, 80, 112)
- Bass-Channel (CH6)
- Pattern-basierte Struktur
- SD-Karten-Verzeichnisstruktur (`ROLAND/SONGS/`, `ROLAND/EXPORT/`)
- Audit-Trail mit SHA256-Checksums

---

## 🧪 Test-Suite

140+ Tests mit Pytest:

```bash
# Alle Tests
pytest tests/ -v

# Spezifische Suite
pytest tests/test_neural.py -v
pytest tests/test_provenance.py -v

# Mit Coverage
pytest --cov=maxxki --cov-report=html

# Edge Cases & Stress Tests
pytest tests/test_edge_cases.py -v

# Ohne langsame Tests
pytest -m "not slow"
```

**Test-Kategorien:**
- Unit Tests (isolierte Komponenten)
- Integration Tests (End-to-End)
- Edge Cases (Boundary, Null, Extremwerte)
- Stress Tests (Concurrency, 10k+ Einträge)
- ALCOA+ Compliance Tests

---

## 📊 Performance

| Komponente | CPU (i3) | GPU (CUDA) | MPS (Apple) |
|-----------|----------|-----------|-------------|
| Training | ~2s/iter | ~0.1s/iter | ~0.3s/iter |
| Beat-Gen | <1s | <1s | <1s |
| MIDI-Gen | ~5s | ~2s | ~3s |
| MusicGen | ~30s/15s | ~3s/15s | ~8s/15s |
| Mastering | ~0.5s | N/A | N/A |

---

## 🔧 Konfiguration

### Umgebungsvariablen

```bash
export MAXXKI_OUTPUT_DIR="~/projects/mk/music-output"
export MAXXKI_MODEL_CACHE="~/projects/mk/models"
export WANDB_MODE="disabled"  # Optional
```

### Session-Konfiguration

```python
from maxxki.core.orchestrator import SessionConfig

config = SessionConfig(
    user_prompt="dark minimal techno",
    vibe_hint="the_produck",
    duration_seconds=60,
    bpm=130,
    key="C",
    genre="techno",
    use_beat_gen=True,
    use_midi_gen=True,
    use_music_gen=True,
    use_neural_bass=True,
    use_claude=False  # Kein API-Key nötig
)
```

---

## 🤝 Beitragen

1. Fork erstellen
2. Feature-Branch: `git checkout -b feature/neues-modul`
3. Tests schreiben: `pytest tests/test_neues_modul.py`
4. Commit: `git commit -am "Neues Modul hinzugefügt"`
5. Push: `git push origin feature/neues-modul`
6. Pull Request erstellen

**Anforderungen:**
- Alle Tests müssen passen
- Edge Cases müssen abgedeckt sein
- Provenance-Signatur für neue Generatoren
- FAT32-Kompatibilität für Hardware-Export

---

## 📜 Lizenz

MIT License — siehe [LICENSE](LICENSE)

---

## 🙏 Credits

- **Tristan Behrens** — Original MusicTransformer2023 & js-fakes Dataset
- **ai-guru** — lakhclean_mmmtrack GPT-2 Model
- **Facebook** — MusicGen (MIT License)
- **HuggingFace** — Transformers, Datasets
- **Google** — note-seq, magenta

---

## 📞 Kontakt

- Issues: [GitHub Issues](https://github.com/maxxki/neural-studio/issues)
- Discussions: [GitHub Discussions](https://github.com/maxxki/neural-studio/discussions)

---

> *"Kein Claude, kein API-Key, 100% lokal."* — MAXXKI Master-Ear v2.0

⬡ **MAXXKI Neural Studio** — *The Future of Local AI Music Production*
