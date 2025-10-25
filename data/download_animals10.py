"""
Download Animals-10 dataset from Kaggle and extract it into ./data directory.
This script can be committed to GitHub (without Kaggle API key).
"""

import os
import zipfile
import subprocess

# Ensure Kaggle is installed
subprocess.run(["pip", "install", "-q", "kaggle"], check=True)

# Create Kaggle folder and check for API key
os.makedirs(os.path.expanduser("~/.kaggle"), exist_ok=True)
api_path = os.path.expanduser("~/.kaggle/kaggle.json")

if not os.path.exists(api_path):
    raise FileNotFoundError(
        "Missing ~/.kaggle/kaggle.json. "
        "Go to https://www.kaggle.com/settings/account -> Create API Token "
        "and place it in ~/.kaggle/kaggle.json"
    )

# Set correct permissions
os.chmod(api_path, 0o600)

# Target folder
DATA_DIR = "./data"
os.makedirs(DATA_DIR, exist_ok=True)

# Download dataset
print("Downloading Animals-10 dataset from Kaggle...")
subprocess.run([
    "kaggle", "datasets", "download",
    "-d", "alessiocorrado99/animals10",
    "-p", DATA_DIR
], check=True)

# Unzip dataset
zip_path = os.path.join(DATA_DIR, "animals10.zip")
if os.path.exists(zip_path):
    print("Extracting ZIP file...")
    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(DATA_DIR)
    os.remove(zip_path)
    print("Done! Extracted to ./data/animals10")
else:
    print("ZIP file not found.")
