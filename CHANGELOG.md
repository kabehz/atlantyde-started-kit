# 📝 CHANGELOG - Atlantyde Docs SDLC Bundle

## Versión inicial consolidada - 2025-05-13

### 🆕 Estructura Unificada

- Fusión de `atl0s-sdk-main`, `atlantyde-kit-adoption-main`, y `atlantyde-started-kit-main`
- Todos los `.md` organizados en `docs/` con prefijo por repositorio de origen
- Añadido `_toc.md` raíz y por subcarpetas

### ✅ Validaciones CI

- Sintaxis Markdown (`markdownlint`)
- Enlaces rotos (`markdown-link-check`)
- Esquema `frontmatter` (`title`, `order`, `section`, `author`, `date`)
- Verificación de fechas futuras y autores autorizados
- Validación de referencias en `_toc.md`

### 🔁 Automatización Makefile

- `serve-*`, `build-*` para Astro, MkDocs y Docusaurus
- `generate-toc`, `generate-subtoc`, `validate-*` integrados en CI
- `init-docs` para creación de estructura mínima

### 📘 Documentación Agregada

- `README_Makefile_local_dev.md`
- `README_TOCs.md`
- `README_package.md`
- `docs/guide/frontmatter-spec.md`

### 📦 Distribución

- ZIP: `atlantyde-docs-sdlc-updated.zip` incluye todos los archivos actualizados y validados.
