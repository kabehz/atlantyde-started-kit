# 📦 README - Empaquetado del entorno local

## Comandos útiles

- `make init-docs`: Genera estructura mínima
- `make generate-toc`: Construye índice automático
- `make validate-frontmatter-schema`: Verifica todos los campos semánticos

## Empaquetado

Para distribuir esta estructura en `.zip`:

```bash
zip -r atlantyde-docs-sdlc.zip docs astro-docs docusaurus-docs mkdocs.yml docusaurus.config.js Makefile README_*.md .github
```

Verifica la validez de `README_Makefile_local_dev.md` y `frontmatter-spec.md` tras generación automática.
