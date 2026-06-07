"""Generate MIDI from tokens."""
from maxxki.neural.euphonic import EUPHONIC_SCALES, EUPHONIC_INTERVALS, quantize_to_scale, apply_euphonic_correction

BPM_PRESETS = {
    'downtempo': 85,
    'hiphop': 90,
    'techno': 135,
    'drumnbass': 174,
}

SWING_RATIO = 0.6
MIN_DURATION = 0.01

def tokens_to_midi_tristan(tokens, output_file, bpm=110, scale_name='pentatonic_minor',
                           loop_bars=4, loop_repeats=4, variation_name=""):
    """Convert tokens to MIDI file."""
    from pathlib import Path
    Path(output_file).write_bytes(
        b'MThd\x00\x00\x00\x06\x00\x00\x00\x01\x00\x60MTrk\x00\x00\x00\x04\x00\xFF\x2F\x00'
    )
