
import requests
import json
from pathlib import Path

REPO = "kabehz/atlantyde-kit-adoption"  # Reemplazar con tu repo
TOKEN = "ghp_xxx"  # Sustituir por un token personal válido

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_topics(repo):
    r = requests.get(f"https://api.github.com/repos/{repo}/topics", headers={**headers, "Accept": "application/vnd.github.mercy-preview+json"})
    return r.json().get("names", [])

def get_labels(repo):
    r = requests.get(f"https://api.github.com/repos/{repo}/labels", headers=headers)
    return [label["name"] for label in r.json()]

def get_discussions(repo):
    r = requests.get(f"https://api.github.com/repos/{repo}/discussions", headers=headers)
    if r.status_code == 200:
        return [d["title"] for d in r.json()]
    return []

def update_taxonomy_file():
    base_path = Path("taxonomy_keywords.json")
    data = json.loads(base_path.read_text(encoding="utf-8"))

    data["github_topics"] = get_topics(REPO)
    data["github_labels"] = get_labels(REPO)
    data["github_discussions"] = get_discussions(REPO)

    with open("taxonomy_keywords_updated.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    update_taxonomy_file()
    print("📡 Taxonomía enriquecida con datos de GitHub.")
