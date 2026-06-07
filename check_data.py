from datasets import load_from_disk
import os

# Pfad zu deinen Daten
data_dir = "data/jsfakes4bars/generation"

# Lade den Datensatz
ds = load_from_disk(data_dir)
train_ds = ds['train']

max_id = 0
for i in range(len(train_ds)):
    max_id = max(max_id, max(train_ds[i]['encoder_ids']))
    max_id = max(max_id, max(train_ds[i]['decoder_ids']))

print(f"Der höchste Token-ID im Datensatz ist: {max_id}")
print(f"Du benötigst eine vocab_size von mindestens: {max_id + 1}")
