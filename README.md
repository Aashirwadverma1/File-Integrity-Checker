Features

    File Integrity Monitoring: Automatically detects unauthorized modifications by hashing specified files.
    Baseline Creation: Generates and saves a baseline hash for all monitored files.
    Regular Integrity Checks: Compares current file hashes against the baseline to identify changes.
    Automated Logging: Logs each integrity check with a timestamp for easy review.
    Cron Job Support: Automates periodic integrity checks through cron on Linux-based systems.

Requirements

    Python 3.x
    Linux OS (for cron job setup)
    Python watchdog package for file monitoring

Installation
1. Clone the Repository

git clone https://github.com/Aashirwadverma1/file-integrity-checker.git
cd file-integrity-checker

2. Set Up a Virtual Environment (Recommended)

python3 -m venv venv
source venv/bin/activate  # Activate the virtual environment

3. Install Required Packages

pip install -r requirements.txt

Note: Ensure that requirements.txt includes watchdog or any other dependencies.
Usage
1. Configure the files_to_monitor List

    Open the config.py file and define the list of files you want to monitor.
    Example:

    files_to_monitor = [
        "/home/user/Documents/important_file.txt",
        "/home/user/Documents/another_file.txt"
    ]

2. Create Baseline Hashes

Run the following command to generate and save baseline hashes for the monitored files:

python3 integrity_checker.py

This will generate a file_hashes.json file containing the baseline hashes.
3. Perform Integrity Check

Run the following command to check if any monitored files have been modified:

python3 integrity_checker.py

4. Automating with Cron

To run the integrity check automatically at set intervals, you can set up a cron job:

    Open the crontab editor:

crontab -e

Add the following line to schedule the integrity check every minute (or customize as needed):

    * * * * * /usr/bin/python3 /path/to/integrity_checker.py >> /path/to/integrity_checker.log 2>&1

Replace /path/to/integrity_checker.py with the actual path of your script.
Example Output

If changes are detected in a monitored file, the script will output:

File modified: /home/user/Documents/important_file.txt

If no changes are detected:

File is intact: /home/user/Documents/important_file.txt

Logs and results will also be saved in integrity_checker.log if configured with cron.
Configuration

The main configuration file is config.py, where you specify which files to monitor. Modify the files_to_monitor list to include the paths of all critical files you want to track.

Example:

files_to_monitor = [
    "/home/user/Documents/important_file.txt",
    "/home/user/Documents/another_file.txt"
]

Example

    Creating Baseline:

python3 integrity_checker.py

Output: Baseline hashes created and saved to file_hashes.json.

Checking Files for Changes:

    python3 integrity_checker.py

    Output: File modified: /home/user/Documents/important_file.txt (if modified) or File is intact: /home/user/Documents/important_file.txt (if unchanged)

Contributing

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Commit your changes (git commit -m 'Add some feature').
    Push to the branch (git push origin feature-branch).
    Open a pull request.# File-Integrity-Checker
