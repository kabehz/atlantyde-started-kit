import os
import argparse
import yaml
from pymdownx.emoji import twemoji, to_svg

def build_nav(base_dir="docs"):
    nav = []
    for root, _, files in os.walk(base_dir):
        section = os.path.relpath(root, base_dir)
        section_title = section.replace("_", " ").title()
        children = []
        for file in sorted(files):
            if file.lower().endswith(('.md', '.markdown')):
                label = os.path.splitext(file)[0].replace("_", " ").capitalize()
                path = os.path.join(section, file).replace("\\", "/")
                children.append({label: path})
        if section != "." and children:
            nav.append({section_title: children})
        elif children:
            nav.extend(children)
    return nav

def main():
    parser = argparse.ArgumentParser(description="Generate mkdocs.yml dynamically")
    parser.add_argument('--base-dir', type=str, default='docs', help='Base directory of docs')
    parser.add_argument('--output', type=str, default='mkdocs.yml', help='Output mkdocs.yml file path')
    args = parser.parse_args()

    config = {
        "site_name": "ATLANTYDE ACADEMY Foundation",
        "site_url": "https://kabehz.github.io/atl0s/",
        "site_description": "Infraestructura legal semántica para soberanía europea (NLP + DevSecOps).",
        "site_author": "Kabehz",
        "theme": {
            "name": "material",
            "logo": "assets/branding/header-main.png",
            "favicon": "assets/branding/favicon.ico",
            "palette": {
                "scheme": "default",
                "primary": "blue",
                "accent": "pink"
            },
            "features": [
                "navigation.tabs", "navigation.expand", "navigation.top",
                "toc.integrate", "search.highlight", "search.suggest"
            ],
            "font": {
                "text": "Roboto",
                "code": "Roboto Mono"
            },
            "language": "es"
        },
        "extra_css": [
            "assets/css/animations.css",
            "assets/branding/nav-style.css",
            "assets/css/markdown.css",
            "assets/css/mermaid.css"
        ],
        "extra_javascript": [
            "assets/js/intersection-observer.js",
            "assets/branding/scroll-effect.js",
            "https://cdnjs.cloudflare.com/ajax/libs/intro.js/7.0.1/intro.min.js"
        ],
        "extra": {
            "social": [
                {"icon": "fontawesome/brands/github", "link": "https://github.com/kabehz/atlantyde-kit-adoption"},
                {"icon": "fontawesome/brands/linkedin", "link": "https://linkedin.com/in/jaimesilvagonzalez"}
            ]
        },
        "markdown_extensions": [
            "toc", "tables", "attr_list", "admonition", "codehilite", "footnotes", "def_list",
            "pymdownx.highlight", "pymdownx.superfences", "pymdownx.inlinehilite",
            "pymdownx.tabbed", "pymdownx.details",
            {"pymdownx.emoji": {"emoji_index": twemoji, "emoji_generator": to_svg}}
        ],
        "plugins": [
            {"search": {"index": True}},
            {"minify": {"minify_html": True}},
            {"mermaid2": {"theme": "default"}}
        ],
        "nav": build_nav(args.base_dir)
    }

    with open(args.output, "w", encoding="utf-8") as f:
        yaml.dump(config, f, sort_keys=False, allow_unicode=True)

    print(f"✅ Archivo '{args.output}' generado automáticamente desde '{args.base_dir}'.")

if __name__ == "__main__":
    main()
