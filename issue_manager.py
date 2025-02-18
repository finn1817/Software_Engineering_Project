import json
import os

REPORTS_FILE = "reports.json"

def load_reports():
    """Load reports from file."""
    if os.path.exists(REPORTS_FILE):
        with open(REPORTS_FILE, "r") as file:
            return json.load(file)
    return []

def save_reports(reports):
    """Save reports to file."""
    with open(REPORTS_FILE, "w") as file:
        json.dump(reports, file, indent=4)

def report_issue(title, description):
    """Save a new issue."""
    reports = load_reports()
    reports.append({"title": title, "description": description, "status": "New"})
    save_reports(reports)

def delete_issue(index):
    """Delete an issue by index."""
    reports = load_reports()
    if 0 <= index < len(reports):
        reports.pop(index)
        save_reports(reports)

def list_issues():
    """Return list of issues."""
    return load_reports()
