import hashlib
import json
import os
from config import files_to_monitor

# Generate SHA-256 hash for a file
def generate_file_hash(filepath):
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return None

# Load the existing hashes from a JSON file
def load_hashes():
    if os.path.exists("file_hashes.json"):
        with open("file_hashes.json", "r") as f:
            return json.load(f)
    return {}

# Save the generated hashes to a JSON file
def save_hashes(hashes):
    with open("file_hashes.json", "w") as f:
        json.dump(hashes, f, indent=4)

# Generate and save baseline hashes
def create_baseline():
    baseline_hashes = {file: generate_file_hash(file) for file in files_to_monitor}
    save_hashes(baseline_hashes)
    print("Baseline hashes created and saved to file_hashes.json.")

# Check if the monitored files have been modified
def check_files_for_changes():
    current_hashes = {}
    for file in files_to_monitor:
        file_hash = generate_file_hash(file)
        if file_hash:
            current_hashes[file] = file_hash

    # Load the stored hashes and compare
    stored_hashes = load_hashes()

    for file, current_hash in current_hashes.items():
        stored_hash = stored_hashes.get(file)
        if stored_hash != current_hash:
            print(f"File modified: {file}")
        else:
            print(f"File is intact: {file}")

    # Save the current hashes for future checks
    save_hashes(current_hashes)

# Example usage
# Uncomment one of the following lines to either create a baseline or check for changes

# create_baseline()  # Run this once to save the baseline
check_files_for_changes()  # Run this to check for modifications
