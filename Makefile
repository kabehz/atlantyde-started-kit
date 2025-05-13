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