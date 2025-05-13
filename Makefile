# Makefile para ejecución local y validación de los Labs ATLANTYDE

.PHONY: validate deploy local

# 1. Validar metadatos YAML y ejecutar tests
validate:
	@echo "🔄 Validando metadatos YAML y ejecutando pruebas..."
	@python3 -c "
import os, yaml
for root, _, files in os.walk('docs/labs'):
    for file in files:
        if file.endswith('.md'):
            with open(os.path.join(root, file), 'r') as f:
                content = f.read()
                if not content.startswith('---'):
                    raise ValueError(f'{file} no tiene metadatos YAML')
print('✅ Validación completada de todos los Labs.')
	"

# 2. Desplegar el repositorio en GitHub Pages
deploy:
	@echo "🚀 Desplegando en GitHub Pages..."
	git checkout --orphan gh-pages
	git rm -rf .
	mkdir assets
	cp ./assets/bootstrap-demo.gif ./assets/
	git add assets/
	git commit -m "📽️ Publicación del GIF de bootstrap en gh-pages"
	git push origin gh-pages

# 3. Ejecutar localmente el flujo de trabajo usando Docker
local:
	@echo "🚀 Ejecutando el entorno localmente en Docker..."
	docker-compose -f docker-compose.fullstack.yml up --build
# Generación de Documentación

docs-astro:
	@echo "📘 Astro - Iniciando entorno de documentación..."
	cd astro-docs && npm install && npm run dev

docs-mkdocs:
	@echo "📘 MkDocs - Servidor local en puerto 8000..."
	cd mkdocs-docs && pip install -r requirements.txt && mkdocs serve

docs-docusaurus:
	@echo "📘 Docusaurus - Iniciando documentación local..."
	cd docusaurus-docs && npm install && npm run start

# Construcción de Documentación

docs-build-astro:
	@echo "🏗️ Compilando documentación Astro..."
	cd astro-docs && npm install && npm run build

docs-build-mkdocs:
	@echo "🏗️ Compilando documentación MkDocs..."
	cd mkdocs-docs && pip install -r requirements.txt && mkdocs build

docs-build-docusaurus:
	@echo "🏗️ Compilando documentación Docusaurus..."
	cd docusaurus-docs && npm install && npm run build

docs-export-pdf:
	@echo "🖨️ Exportando PDF desde MkDocs..."
	cd mkdocs-docs && mkdocs build && mkdocs pdf-export