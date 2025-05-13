# 🧪 README: Automatización local con Makefile

Este repositorio incluye un `Makefile` con flujos de trabajo para:

## 🧭 Documentación y Desarrollo

- `make serve-astro`: Copia desde `/docs` y lanza servidor Astro
- `make build-astro`: Build estático del sitio Astro
- `make serve-mkdocs`: Servidor local de MkDocs
- `make serve-docusaurus`: Servidor local de Docusaurus

## 📋 Validaciones

- `make lint-md`: Lint de sintaxis Markdown
- `make check-links-frontmatter`: Validación de enlaces + campos clave YAML
- `make validate-frontmatter-schema`: Valida `order`, `section`, `author`, `date`

## 🧰 Utilidades

- `make generate-toc`: Genera índice de archivos Markdown
- `make init-docs`: Genera estructura y archivos base
