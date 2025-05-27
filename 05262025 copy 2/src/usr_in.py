#!/usr/bin/env python3
import os
from pathlib import Path
from datetime import datetime

# Set correct path for external volume
desktop_path = Path.home() / "Desktop"

# Ask the user for a folder name
user_folder_name = input("Enter a name for the drum samples folder (or press Enter to use a timestamp): ").strip()

# If the user doesn't provide a name, use a timestamp
if not user_folder_name:
    user_folder_name = f"drum_samples_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

# Create the base folder
base_folder = desktop_path / user_folder_name
os.makedirs(base_folder, exist_ok=True)

# Create a single folder inside the user-defined folder
folder_paths = [base_folder]