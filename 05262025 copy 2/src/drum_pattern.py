#!/usr/bin/env python3
import numpy as np

# MIDI note values for drum kit (fixed at 60)
DRUM = {
    "SNARE": np.array(60),
    "HIHAT": np.array(60),
    "KICK": np.array(60),
}

# Standard rhythmic durations in beats
DRUM_DURATIONS = {
    "quarter": 1.0,
    "eighth": 0.5,
    "sixteenth": 0.25,
    "triplet_eighth": 1.0 / 3,
    "triplet_sixteenth": 0.25 * 2 / 3,
    "dotted_eighth": 0.75,
    "dotted_sixteenth": 0.375,
}