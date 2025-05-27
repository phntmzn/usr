#!/usr/bin/env python3
import os
from pathlib import Path
from midiutil import MIDIFile
from chord_pattern import chords, inversions
import drum_pattern
import src.key_map as key_map
from src.key_map import create_drum_midi, create_chord_midi, drumpatterns, chordpatterns, BARS, BEATS_PER_BAR, TOTAL_BEATS, HIHAT_NOTE, SNARE_NOTE, KICK_NOTE, CHORD_DURATION, CHORD_CHANNEL, base_folder, TEMPO



#---- Drum MIDI creation ----
def create_drum_midi(filename, pattern, tempo=TEMPO, channel=1):
    """Creates a drum MIDI file with the given pattern on channel 1."""
    midi = MIDIFile(1)  # One track
    track = 0
    midi.addTrackName(track, 0, filename.stem)
    midi.addTempo(track, 0, tempo)

    for note, time in pattern:
        midi.addNote(track, channel=channel, pitch=note, time=time, duration=0.25, volume=100)

    with open(filename, "wb") as output_file:
        midi.writeFile(output_file)

# ---- Chord MIDI creation ----
def create_chord_midi(filename, chord_notes, interval_bars=4, bars=BARS, tempo=TEMPO, channel=CHORD_CHANNEL):
    """Creates a MIDI file that plays a chord every 'interval_bars' bars."""
    midi = MIDIFile(1)
    track = 0
    midi.addTrackName(track, 0, filename.stem)
    midi.addTempo(track, 0, tempo)

    beat_interval = interval_bars * BEATS_PER_BAR
    for bar in range(0, bars, interval_bars):
        time = bar * BEATS_PER_BAR
        for note in chord_notes:
            midi.addNote(track, channel=channel, pitch=note, time=time, duration=CHORD_DURATION, volume=90)

    with open(filename, "wb") as output_file:
        midi.writeFile(output_file)

drumpatterns()
chordpatterns()
print(f"Drum and chord MIDI files created in {base_folder}")
