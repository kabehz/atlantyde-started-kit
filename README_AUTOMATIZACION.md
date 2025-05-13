
// dynamic/VisualBanner.jsx
import { useSession } from "next-auth/react"
import MkdocsBanner from "@/components/visual/MkdocsBanner"
import DocusaurusBanner from "@/components/visual/DocusaurusBanner"
import AstroBanner from "@/components/visual/AstroBanner"
import RobotframeworkBanner from "@/components/visual/RobotframeworkBanner"

export default function VisualBanner({ lab, role }) {
  const { data: session } = useSession()
  const user = session?.user?.name || ""

  // Reglas personalizadas por usuario (extensible)
  if (user === "José Antonio López" || role === "DevSecOps Engineer") return <AstroBanner />
  if (user === "Ángel Cumbreño" || role === "Mentor") return <MkdocsBanner />

  if (lab === "LAB-000") return <MkdocsBanner />
  if (lab === "LAB-M00") return <DocusaurusBanner />
  if (lab === "LAB-021") return <AstroBanner />
  if (role === "QA" || role === "Infra") return <RobotframeworkBanner />

  return <AstroBanner />
}

// Uso:
// <VisualBanner lab="LAB-021" role="DevSecOps Engineer" />

// Esto refuerza el enfoque cognitivo adaptado y crea identidad visual por LAB

// ------------------------------------------------------------

// README_AUTOMATIZACION.md - Guía para contribuidores ATLANTYDE
// ------------------------------------------------------------

## 🤖 Automatización del flujo educativo con Makefile y seguridad

Este proyecto emplea un `Makefile` avanzado para orquestar tareas locales y de CI:

### ⚙️ Comandos principales:

- `make setup` → Instala hooks con Husky y copia workflows de forma segura
- `make deploy-workflows` → Copia temporal de `.github/.workflow_core/` a `.github/workflows/`
- `make github-ci` → Ejecuta preparación para GitHub Actions
- `make clean-workflows` → Limpia workflows visibles
- `make test` → Simulación de pruebas (extensible)
- `make help` → Ayuda interactiva

### 🔒 Seguridad e integridad:

- Prevenimos accidentalmente subir workflows reales con un hook `pre-push`
- Los workflows se mantienen en `.github/.workflow_core/` y se despliegan solo cuando se ejecuta `make`
- Compatible con GitHub Classroom, sparse-checkout y flujos educativos sensibles

### 🧠 Diseño pedagógico:

- Los banners se adaptan a tu rol/LAB mediante `VisualBanner`
- El sistema es modular, reutilizable y expandible para otros LABs

¡Contribuir aquí es también aprender buenas prácticas profesionales! 🚀
