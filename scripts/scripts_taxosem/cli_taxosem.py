
import json
import argparse
from pathlib import Path

TAXONOMY_FILE = "taxonomy_keywords_updated.json"

def load_taxonomy():
    with open(TAXONOMY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def list_categories(data):
    for cat, terms in data.get("taxonomy_map", {}).items():
        print(f"📁 {cat.upper()}:
  - " + "\n  - ".join(terms))

def list_keywords(data):
    print("🔑 Palabras clave semánticas:
" + ", ".join(data.get("semantic_keywords", [])))

def list_github_insights(data):
    print("\n🌐 Temas GitHub:", ", ".join(data.get("github_topics", [])))
    print("🏷️ Etiquetas:", ", ".join(data.get("github_labels", [])))
    if discussions := data.get("github_discussions"):
        print("💬 Discusiones:", "; ".join(discussions))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI Atl0s Taxonomía Semántica")
    parser.add_argument("--categories", action="store_true", help="Mostrar categorías semánticas")
    parser.add_argument("--keywords", action="store_true", help="Mostrar palabras clave")
    parser.add_argument("--github", action="store_true", help="Ver temas/discusiones/etiquetas desde GitHub")

    args = parser.parse_args()
    data = load_taxonomy()

    if args.categories:
        list_categories(data)
    if args.keywords:
        list_keywords(data)
    if args.github:
        list_github_insights(data)
    if not (args.categories or args.keywords or args.github):
        parser.print_help()
