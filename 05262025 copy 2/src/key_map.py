#!/usr/bin/env python3
import src.key_map as key_map

# Constants
BARS = 32
TEMPO = 156
BEATS_PER_BAR = 4
TOTAL_BEATS = BARS * BEATS_PER_BAR  # 32 bars * 4 beats per bar = 128 beats

# MIDI note mappings
HIHAT_NOTE = 60  # Closed Hi-Hat
SNARE_NOTE = 60  # Acoustic Snare
KICK_NOTE = 60  # Bass Drum

CHORD_DURATION = 4  # One bar
CHORD_CHANNEL = 1 # MIDI channel for chords
