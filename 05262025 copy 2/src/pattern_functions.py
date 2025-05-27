#!/usr/bin/env python3
import chord_pattern
import os
from pathlib import Path
from src.key_map import BARS, BEATS_PER_BAR, TOTAL_BEATS, base_folder, HIHAT_NOTE, SNARE_NOTE, KICK_NOTE, CHORD_DURATION, TEMPO

from chord_pattern import chords, inversions
import os
from datetime import datetime


# Set correct path for external volume
desktop_path = Path.home() / "Desktop"

# Function to create a folder for drum midi
def drumpatterns():
    """Generates and saves MIDI drum patterns in the base folder."""
    folder = base_folder
    # Generate patterns
    hihat_pattern = [(HIHAT_NOTE, t * 0.5) for t in range(TOTAL_BEATS * 2)]  # 8th notes
    snare_pattern = [(SNARE_NOTE, t * BEATS_PER_BAR + 2) for t in range(BARS)]  # Beat 3 of every bar
    kick_pattern = [(KICK_NOTE, t * BEATS_PER_BAR + offset) for t in range(0, BARS, 2) for offset in [0, 3]]


    # Create MIDI files inside the respective folder
    create_drum_midi(folder / "hihat.mid", hihat_pattern, channel=1)
    create_drum_midi(folder / "snare.mid", snare_pattern, channel=1)
    create_drum_midi(folder / "kick.mid", kick_pattern, channel=1)

# Generate the drum patterns in the folder
drumpatterns()

# Function to create base folder for chord patterns
def chordpatterns():
    folder = base_folder
    chord_pattern = []
    chord_progression = ["F#minor", "C#minor", "F#minor", "Gmajor"]
    for t in range(0, BARS, 2):
        chord = chord_progression[(t // 2) % len(chord_progression)]
        notes = inversions.get(chord, chords.get("C", [60, 64, 67]))
        for note in notes:
            chord_pattern.append((note, t * BEATS_PER_BAR))

    create_chord_midi(folder / "chord_pattern.mid", chord_pattern, channel=1)

chordpatterns()


base_folder = desktop_path / "drum_samples_" + datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
os.makedirs(base_folder, exist_ok=True)

print(f"Folder with hi-hat, snare, and kick patterns at {TEMPO} BPM created in {base_folder}.")