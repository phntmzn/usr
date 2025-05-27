import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import unittest
from src import drum_pattern, chord_pattern
from src.usr_in import run, base_folder
import os

class TestMIDIPatterns(unittest.TestCase):
    def setUp(self):
        run()  # initialize folder setup
        self.output_dir = base_folder
        self.assertTrue(self.output_dir.exists())

    def test_drum_midi_generation(self):
        drum_pattern.drumpatterns()
        files = list(self.output_dir.glob("*.mid"))
        self.assertTrue(any("drum" in f.name.lower() for f in files), "No drum MIDI file found.")

    def test_chord_midi_generation(self):
        chord_pattern.chordpatterns()
        files = list(self.output_dir.glob("*.mid"))
        self.assertTrue(any("chord" in f.name.lower() for f in files), "No chord MIDI file found.")

    def tearDown(self):
        for f in self.output_dir.glob("*.mid"):
            f.unlink()

# To run this test suite:
# python -m src.test
unittest.main()