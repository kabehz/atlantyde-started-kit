
import csv
import requests
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = os.getenv("GITHUB_REPO")
OWNER = os.getenv("GITHUB_OWNER")

def crear_issue(title, body, labels):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    payload = {
        "title": title,
        "body": body,
        "labels": labels.split(",")
    }
    r = requests.post(url, json=payload, headers=headers)
    print(f"Issue creada: {title} | Status: {r.status_code}")

with open("ATLANTYDE_LABS_Issues.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        crear_issue(row['title'], row['body'], row['labels'])
