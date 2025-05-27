#!/usr/bin/env python3

# Standard library imports
import json
import os
import multiprocessing
from multiprocessing import Pool
from threading import Thread
import queue
from datetime import datetime
import argparse
import tempfile
import shutil

# Project-specific module imports
from src import key_map, usr_in, chord_pattern, drum_pattern

# main.py: CLI entry point for MIDI generation and upload workflow
def main():
    """Main function to handle command-line arguments and execute MIDI generation tasks."""
    parser = argparse.ArgumentParser(description="main.py — Generate MIDI patterns and optionally upload them")
    parser.add_argument("--drums", action="store_true", help="Generate drum patterns")
    parser.add_argument("--chords", action="store_true", help="Generate chord patterns")
    parser.add_argument("--interactive", action="store_true", help="Run interactive mode")
    args = parser.parse_args()

    if args.interactive:
        usr_in.run()
        return

    if args.drums:
        print("[*] Generating drum patterns...")
        drum_pattern.drumpatterns()

    if args.chords:
        print("[*] Generating chord patterns...")
        chord_pattern.chordpatterns()

    if not (args.drums or args.chords or args.interactive):
        print("[!] No option specified. Use --help to view available commands.")

    if args.drums or args.chords:
        from src.key_map import base_folder, TEMPO
        print(f"[✓] Files written to {base_folder} at {TEMPO} BPM.")

if __name__ == "__main__":
    main()