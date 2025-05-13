
# 📚 Documentación Técnica de Scripts Semánticos Atl0s

## 1. `update_taxonomy_from_github.py`
- **Función**: Consulta la API de GitHub para extraer `topics`, `labels`, y `discussions` de un repositorio.
- **Salida**: Crea o actualiza `taxonomy_keywords_updated.json` con estructura semántica extendida.
- **Uso**: Manual o dentro de workflows CI.

## 2. `cli_taxosem.py`
- **Función**: CLI educativa que permite explorar el contenido del mapa semántico.
- **Comandos**:
  - `--categories`: muestra categorías semánticas.
  - `--keywords`: muestra palabras clave.
  - `--github`: muestra temas, etiquetas y discusiones obtenidas del repositorio.

## 3. `update-taxonomy.yml`
- **Función**: Workflow GitHub Actions que ejecuta automáticamente `update_taxonomy_from_github.py` semanalmente o bajo demanda.
- **Ubicación**: `.github/workflows/`

## 4. `semantic_map_interactive.md`
- **Función**: Representación visual del mapa semántico, compatible con MkDocs y Docusaurus.
- **Uso**: Como página estática de documentación.

## 5. `docusaurus.config.js` y `sidebars.js`
- **Función**: Configuran la documentación visual en Docusaurus, incluyendo rutas y menús.
- **Recomendado**: Incluir en plantillas para auto-despliegue.

---

**Mantenimiento**: Todos los scripts están preparados para ambientes CI/CD educativos.
**Autor**: JaSiLez | Atl0s-AstroKit | 2025
