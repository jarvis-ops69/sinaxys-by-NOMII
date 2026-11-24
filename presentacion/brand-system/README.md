# Sinaxys

Sistema de diseño de Sinaxys, plataforma brasileña de recrutamento, credenciamento, pagamentos PJ e emissão de notas fiscais para instituciones y profesionales de salud. Reúne la identidad de sinaxys.com y las reglas de la alianza **Método ZAI by NOMII** para la campaña de médicos brasileños que evalúan ejercer en Alemania.

**Fuentes.** Colores, tipografía, radios, sombras y componentes: CSS en vivo de [sinaxys.com](https://sinaxys.com/) (23 de noviembre de 2026). Paleta y estilos de documento, pilares del manual y reglas de la alianza: `fuentes/Propuesta_preliminar_comercial_Metodo_ZAI_Sinaxys_Brasil.pdf` del repositorio `jarvis-ops69/sinaxys-by-NOMII`. Los dos coinciden en el violeta `#542aef` y el índigo `#20105b`.

## Cómo usar esta carpeta

| Archivo | Para qué |
| --- | --- |
| `tokens.json` | Fuente de los tokens: colores (claro y oscuro), tipografía, espaciado, radios y sombras, cada uno con su uso. |
| `tokens.css` | Los mismos tokens como variables CSS, clases de estilo tipográfico y `@font-face` de Sofia Sans. Generado desde `tokens.json`. |
| `components/bundle.css` | Estilos de los componentes (`sx-btn`, `sx-card`, `sx-eyebrow`, `sx-choice`, `sx-hero`, `sx-doc-table`). Requiere `tokens.css`. |
| `components/<Componente>/` | Guía de uso (`README.md`) y fragmento de ejemplo (`preview.html`; para verlo, cargar antes `tokens.css` y `bundle.css`). |
| `assets/Logos/` | Wordmarks, símbolo y firma provisoria «Sinaxys with nomii». Reglas en su README. |
| `fonts/` | Sofia Sans 400–700 (woff2) y su licencia SIL OFL. |

La versión navegable vive en el design system «Sinaxys» de Claude. Si se cambia un token, actualizar `tokens.json` y regenerar `tokens.css`.

## Contenido

### Voz

Sinaxys habla en portugués de Brasil, directo y de negocio: frases cortas, verbos de acción y beneficios concretos. Dos públicos, dos registros:

- **Instituições** — control, eficiencia y trazabilidad. «Mais agilidade e controle para sua operação.» «Uma operação de saúde precisa comprovar cada decisão.»
- **Profissionais** — autonomía y transparencia. «O profissional acompanha o próprio recebimento pelo celular.»
- Pares en paralelo para cerrar una idea: «Organização para a instituição. Transparência para quem atende.»
- Beneficios en pocas palabras: «Publicar vaga é grátis, sem limite».
- CTA en verbo + objeto, sin punto: «Agendar demo», «Ver vagas», «Publicar vaga», «Entrar na minha conta».
- Antetítulos (`eyebrow`) en MAYÚSCULAS para nombrar sección o público: «PLATAFORMA», «CLÍNICAS, HOSPITAIS, OSS E PROFISSIONAIS DE SAÚDE».

### Manual médico de la alianza (Método ZAI by NOMII)

La comunicación con médicos se apoya en cuatro pilares:

| Pilar | Aplicación |
| --- | --- |
| Claridad | La landing explica etapas, responsabilidades, costos y siguiente paso en lenguaje comprensible. |
| Preparación | El contenido muestra qué empieza en Brasil y qué exige el proyecto en idioma, documentación y tiempo. |
| Acompañamiento | En cada hito se identifica quién presta el apoyo y cómo puede contactarlo el médico. |
| Confianza respaldada | Casos y testimonios identifican programa, empresa que acompañó, etapa y permiso de uso. |

- Perfil de Instagram: «Sinaxys | Médicos na Alemanha». En la bio: «Preparação e acompanhamento com o Método ZAI by NOMII».
- En la landing, explicar el papel de ambas empresas. En un testimonio histórico, identificar al médico como participante acompañado por NOMII.
- NOMII define el mensaje y aprueba el contenido del programa; Sinaxys revisa que el portugués de Brasil sea correcto, claro y natural. Si una corrección cambia el sentido de una prestación o condición, NOMII confirma la formulación final.
- Un titular sobre una plaza de trabajo necesita alcance y condiciones confirmados antes de publicarse.

## Fundamentos visuales

### Color

- **Violeta `primary` (#542aef)** es la marca: botón primario, enlaces, eyebrows, símbolo. Hover del primario: `brand-pay`.
- **Índigo `primary-deep` (#20105b)** es la tinta: texto principal, wordmark, fondo del hero y del footer, cabeceras de tabla.
- **Acentos neón** — `brand-lime`, `brand-cyan`, `brand-mint`, `brand-yellow`, `brand-coral` — viven sobre `primary-deep` y llevan texto `primary-deep`. Lima para el CTA de campaña; cian para eyebrows del hero. Uno o dos por pantalla.
- **Neutros** zinc (`neutral-50`…`950`) para bordes (`border`), fondos suaves (`secondary`, `muted`) y texto secundario (`muted-foreground`).
- **Tema oscuro**: el fondo pasa a `primary-deep`, las tarjetas a `neutral-900`. `primary` ahí es solo fondo de botón (2.3:1 como texto); el texto de acento usa `primary-glow`.
- **Documentos NOMII × Sinaxys**: papel blanco, texto `doc-text`, cabeceras de tabla `primary-deep`, filas `doc-row`, filetes `doc-rule`, rótulos `primary`, pies `doc-caption`.
- Contraste: `success` (3.5:1) y `destructive` (4.4:1) con blanco solo para texto grande o semibold; `brand-chat` (verde WhatsApp) no admite texto blanco pequeño.
- El sitio declara gradientes, pero todos son planos salvo `gradient-pay` (135°, `brand-pay` → #582bee). Usa color sólido.

### Tipografía

- **Sofia Sans** (400, 500, 600, 700) es la tipografía del sistema, con licencia libre SIL OFL; los archivos están en `fonts/`. El sitio de Sinaxys usa Sofia Pro, que es de pago y no se usa aquí. Títulos con tracking −0.025em.
- Escala: `display` 40px → `heading-1` 36 → `heading-2` 24 → `heading-3` 18; `lead` 20, `body` 16, `body-sm` 14, `caption` 12; `eyebrow` 11px 700 tracking 0.18em; `stat` 48px con números tabulares.
- **Open Sans** (400, 600, 700) en propuestas y manuales de la alianza; los estilos `doc-*` están en pt sobre A4.

### Forma, espacio y profundidad

- Esquinas generosas: `radius-md` 8px en botones estándar, `radius-xl` 12px en CTA grandes y menús, `radius-2xl` 16px en tiles, `radius-3xl` 24px en tarjetas.
- Base de 4px (Tailwind): `space-3` 12 en ítems, `space-6` 24 en tarjetas, CTA grande 14 × 28.
- Sombras casi invisibles teñidas de índigo (`shadow-card`, `shadow-elev-2`); `shadow-elegant` para menús; `shadow-glow` solo en los CTA del hero.
- Bordes de 1px `border` en tarjetas, inputs y botones outline.
- Composición: hero índigo centrado; secciones blancas alternadas con bandas `muted`; mockups de producto (notebook y celular) como imagen principal.

### Iconografía

Íconos de línea simples, monocromos, en `primary` o `foreground` a 16–20px, siempre junto a texto. La flecha → acompaña a los CTA. No se encontró el set de íconos fuente; está pendiente de confirmar con Sinaxys.

## Logos

Grupo **Logos**: wordmark índigo, wordmark blanco, símbolo violeta y la firma provisoria de la alianza.

**Sinaxys with nomii.** Mientras se crea el logo de la alianza, la firma es el wordmark Sinaxys con una línea debajo, alineada a la derecha: «with» en Sofia Sans 500 y las letras originales del logo de nomii, sin su círculo. En la versión de color, «with» va en `primary-deep` y «nomii» en su azul original (#003f6b); en la versión blanca, todo en blanco. En textos corridos se sigue firmando «Método ZAI by NOMII».

## Pendientes

- Logo vectorial original de Sinaxys (los PNG salen del logo de 352 × 96 px).
- Logo definitivo de la alianza Sinaxys × nomii; «Sinaxys with nomii» es provisorio.
- Set de íconos y fotografía de voceros.
- Vocabulario PT-BR y tono por canal del manual, que la propuesta anuncia y aún no detalla.
