
# EXTENSIÓN: Manejo de múltiples badges y gamificación
BADGES = {
    "intro": "semantic_ci_badge.svg",
    "infra": "infra_ready.svg",
    "security": "code_secure.svg",
    "docs": "mkdocs_ready.svg",
}

def assign_badges(topics):
    return [BADGES[topic] for topic in topics if topic in BADGES]


# Disparador de misiones educativas
import requests
import json
import os
from github import Github
from datetime import datetime

# Configuraciones de acceso a la API de GitHub
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')  # Token de acceso personal para GitHub
REPO_NAME = os.getenv('REPO_NAME')  # Nombre del repositorio
GITHUB_ACTOR = os.getenv('GITHUB_ACTOR')  # El actor de GitHub (usuario que ejecuta el workflow)
LAB_NAME = os.getenv('LAB_NAME', 'Unknown')  # Nombre del Lab que se ha completado
BADGE_URL = os.getenv('BADGE_URL', 'http://example.com/badge.png')  # URL del badge

# Autenticación y acceso al repositorio de GitHub
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

# Crear un issue para registrar la finalización del Lab
def create_issue():
    issue_title = f"🚀 {LAB_NAME} completado por {GITHUB_ACTOR}"
    issue_body = f"""
    ## 🎉 ¡Felicidades! {GITHUB_ACTOR} ha completado el Lab `{LAB_NAME}`.
    
    **Badge Emitido**: [Ver Badge]({BADGE_URL})
    
    - El usuario ha completado todos los requisitos para este Lab.
    - ¡Sigue adelante y avanza al siguiente Lab!
    """
    labels = ['lab-completion', 'badge-issued', 'progress']
    
    issue = repo.create_issue(title=issue_title, body=issue_body, labels=labels)
    print(f"Issue creado: {issue.title}")
    return issue

# Emitir el Badge al usuario usando AtlantydeBot (simulación)
def issue_badge():
    # Puedes conectar esto con AtlantydeBot o un sistema de emisión de badges
    print(f"Emitiendo badge para {GITHUB_ACTOR} en el Lab {LAB_NAME}...")

# Disparar GitHub Actions Manualmente (usando la API de GitHub)
def trigger_github_action():
    url = f"https://api.github.com/repos/{REPO_NAME}/actions/workflows/dispatch_bot.yml/dispatches"
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    payload = {
        'ref': 'main',  # Nombre de la rama a la que se hace el dispatch
        'inputs': {
            'actor': GITHUB_ACTOR,
            'lab_name': LAB_NAME
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 201:
        print(f"Workflow de GitHub Actions disparado correctamente para {LAB_NAME}!")
    else:
        print(f"Error al disparar el workflow: {response.status_code}")
        print(response.text)

def main():
    print(f"Empezando el proceso para {GITHUB_ACTOR} en el Lab {LAB_NAME}...")
    
    # Crear un Issue que registre la finalización del Lab
    issue = create_issue()
    
    # Emitir el badge para el usuario
    issue_badge()
    
    # Disparar el workflow de GitHub Actions
    trigger_github_action()

if __name__ == "__main__":
    main()
    
# Este script se ejecuta como parte de un workflow de GitHub Actions
# y se encarga de crear un issue, emitir un badge y disparar otro workflow.
# Asegúrate de tener las variables de entorno configuradas correctamente
# para que funcione correctamente.
# Puedes ejecutar este script localmente para pruebas, pero asegúrate de
# tener las credenciales de GitHub configuradas en tu entorno.
# Recuerda que este script es un ejemplo y puede requerir ajustes
# dependiendo de tu configuración específica y de cómo quieras manejar
# la emisión de badges y la creación de issues.
# Asegúrate de tener la librería PyGithub instalada:
# pip install PyGithub
# También asegúrate de tener la librería requests instalada:
# pip install requests
# Este script es parte de un kit de inicio para la plataforma Atlantyde
# y está diseñado para facilitar la creación de misiones educativas
# y la gestión de badges. Puedes personalizarlo según tus necesidades
# y la estructura de tu repositorio.

# Simulación de uso extendido
if __name__ == '__main__':
    temas = ["intro", "security", "docs"]
    insignias = assign_badges(temas)
    print("Insignias generadas:", insignias)
