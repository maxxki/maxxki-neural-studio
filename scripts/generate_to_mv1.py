"""Generate MV-1 compatible files."""
import os
import re
from pathlib import Path

MV1_BASS_CHANNEL = 6
MV1_VELOCITY_STEPS = [16, 48, 80, 112]
MV1_GRID_PPQN = 480

def to_fat83_filename(filename):
    """Convert filename to FAT32 8.3 format."""
    # Remove extension
    if '.' in filename:
        name, ext = filename.rsplit('.', 1)
    else:
        name, ext = filename, 'MID'

    # Clean name: replace special chars with _, keep alphanumeric
    clean = re.sub(r'[^a-zA-Z0-9]', '_', name)
    clean = clean.upper()

    # Truncate to 8 chars
    clean = clean[:8]

    # Clean extension
    ext = ext.upper()[:3]

    return f"{clean}.{ext}"

class MV1Optimizer:
    def __init__(self, checkpoint_path, config):
        self.checkpoint_hash = "no_checkpoint_found"

    def quantize_to_mv1_grid(self, note_time, bpm):
        """Quantize note time to MV-1 grid."""
        beat_duration = 60.0 / bpm
        grid_step = beat_duration / 4  # 16th note grid
        return round(note_time / grid_step) * grid_step

    def optimize_velocity(self, velocity):
        """Quantize velocity to MV-1 steps."""
        steps = MV1_VELOCITY_STEPS
        min_dist = min(abs(x - velocity) for x in steps)
        candidates = [x for x in steps if abs(x - velocity) == min_dist]
        return max(candidates)

def prepare_sd_card_structure(batch_name, midi_files):
    """Prepare SD card structure for MV-1."""
    base = Path(f"/tmp/sd_{batch_name}")
    (base / "ROLAND" / "SONGS").mkdir(parents=True, exist_ok=True)
    (base / "ROLAND" / "EXPORT").mkdir(parents=True, exist_ok=True)
    (base / "PROJECTS").mkdir(parents=True, exist_ok=True)

    # Create filename map
    import json
    (base / "FILENAME_MAP.json").write_text(json.dumps({}))

    return str(base)
