---
title: Especificación de Frontmatter
order: 99
section: guide
author: kabehz
date: 2025-05-13
---

# Especificación de Frontmatter

Todos los archivos `.md` dentro de `docs/` deben incluir el siguiente frontmatter YAML:

```yaml
---
title: Título visible del documento
order: Número para orden en navegación
section: Sección o categoría (general, labs, guide, index)
author: kabehz | loky | culebra
date: YYYY-MM-DD (no puede ser futura)
---
```

## Validaciones automáticas

- El campo `order:` debe ser un número.
- El campo `section:` debe estar en la lista permitida.
- El campo `author:` debe coincidir con una lista blanca.
- El campo `date:` debe estar en formato `YYYY-MM-DD` y no ser futura.
