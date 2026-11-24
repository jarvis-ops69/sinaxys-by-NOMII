# Bitácora de trabajo

Una entrada por pull request. La rama identifica el trabajo y el enlace a la PR permite consultar si está en revisión, integrada o cerrada. Si la tarea continúa en otra sesión, el agente actualiza la misma fila. La fecha corresponde a la última actualización, en hora de Santiago.

| Fecha | Frente y autor | Rama y PR | Cambio y material | Verificación | Decisión para Edward |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Equipo · Codex | `equipo/protocolo-agentes-bitacora` · [PR #1](https://github.com/jarvis-ops69/sinaxys-by-NOMII/pull/1) | Propone las instrucciones comunes en [AGENTS.md](AGENTS.md), esta bitácora, el acceso desde el [README](README.md) y una [plantilla de PR](.github/pull_request_template.md). | Se comprobó el punto de partida en `main`, la correspondencia entre las instrucciones y la plantilla, y los enlaces relativos. | Validar el flujo y, si hay acuerdo, integrar personalmente la PR. Confirmar por separado la cuenta para la protección de `main`. |
| 2026-11-24 | Hermit · Sirius | `equipo/claude-presentation-blueprint` · [PR #43](https://github.com/jarvis-ops69/sinaxys-by-NOMII/pull/43) | Agrega el [Blueprint para Claude](presentacion/claude/CLAUDE_DECK_BLUEPRINT.md): contrato visual, narrativa de 52 slides y cuatro workflows de lifecycle email con cantidad, cadencia, CTA, exclusiones y salida. | Validación programática de las slides 01–52 y de los cuatro workflows; `git diff --check` sin errores. | Revisar el blueprint antes de entregarlo a Claude; validar PT-BR, claims sensibles, voceros y condiciones de configuración antes de activar cualquier sistema. |

**Punto de partida.** El PDF y el guion inicial de 18 láminas ya figuraban en `main` antes de esta propuesta. [Versión inicial del guion](https://github.com/jarvis-ops69/sinaxys-by-NOMII/commit/fde00d1001002ef59aa9d16e9f3446be556c0224).
