# Sinaxys × NOMII — Blueprint de presentación para Claude

> **Propósito:** especificar una presentación visual, editable y fiel a la narrativa de Sinaxys Brasil, con contenido que debe validarse antes de publicar o configurar. Este archivo es el contrato de construcción para diseño: conserva el hilo de las láminas existentes, integra el funnel Lead-to-Client y expande el bloque de lifecycle email en cuatro workflows concretos.
>
> **Resultado esperado:** una presentación propuesta de **58 slides**, 16:9, visual-first. La capa estratégica se presenta en español; los guiones, CTA y mockups dirigidos al médico brasileño se conservan en **portugués brasileño (PT-BR)**. No crear una presentación corporativa genérica: debe sentirse como una ruta clara y humana para médicos brasileños que evalúan Alemania.

---

## 1. Límites de contenido

### Lo que esta presentación sí debe comunicar

- Sinaxys y NOMII construyen una ruta de preparación, selección y acompañamiento para médicos.
- La comunicación despierta interés, el sistema orienta y el equipo humano de Sinaxys opera la relación comercial.
- La captación se mide hasta la señal de negocio: primer pago / Customer, no sólo formularios o leads.
- La tecnología preserva contexto entre campaña, postulación, agenda, selección, venta, pago y onboarding.

### Lo que NO se debe afirmar ni prometer

- Empleo garantizado, admisión garantizada, homologación garantizada, plazos asegurados, ingresos asegurados o resultados migratorios.
- Cifras, acuerdos laborales, requisitos legales o condiciones comerciales que no estén identificadas como referencias por validar.
- Que NOMII atiende leads como Setter o Closer: NOMII diseña, configura, capacita y mide; **Sinaxys ejecuta la atención humana, venta, cobro y onboarding**.

### Principio de copy

- **Mostrar una posibilidad y explicar el siguiente paso.**
- Titulares breves y editoriales; explicación mínima; diagramas, cronologías, cards y UI mockups como cuerpo de la slide.
- Las frases en PT-BR son propuestas editables. Mantener tono humano, preciso y sobrio.

---

## 2. Dirección visual

### Sistema gráfico

- Fondo marfil/blanco cálido: `#F7F6F2` o equivalente.
- Violeta Sinaxys como color estructural: `#5A2488` / acento claro `#8D56B9`.
- Negro grafito para texto: `#1A1820`; gris cálido para notas: `#817B85`.
- Un acento verde suave sólo para estados positivos o avance verificado; nunca como color dominante.
- Mucho espacio negativo. Bordes finos, esquinas redondeadas amplias (18–28 px), líneas de flujo y círculos numerados.
- Titulares serif/editorial de alto contraste; información/UI en sans-serif limpia. No usar más de dos familias tipográficas.
- Logo **Sinaxys × NOMII** discreto y consistente; no en el centro de cada slide.

### Lenguaje de composición

1. **Una idea por slide.**
2. Titular máximo dos líneas. Bajada máximo dos líneas.
3. Usar fotografías documentales de médicos, Alemania, estudio o conversación humana; no bancos de imágenes clínicos genéricos.
4. Cuando se explique una configuración, representar una interfaz plausible: formulario, bandeja, calendar, pipeline o dashboard. No capturas reales con datos personales.
5. No usar iconos decorativos repetidos. Cada diagrama debe explicar una relación: movimiento, decisión, traspaso o medición.

### Reglas para Claude


### Idioma definitivo — esta regla tiene precedencia

- **La presentación de estrategia se diseña y se expone en español.** Títulos, subtítulos, explicaciones, diagramas, métricas, organigrama, etiquetas de proceso y notas de decisión van en español.
- **PT-BR queda reservado para guiones y muestras dirigidas al público brasileño:** anuncios, carruseles, guiones de video, CTAs, emails, WhatsApp, formularios y mockups de landing. Siempre deben llevar un rótulo en español: `Ejemplo de guion / mensaje al médico (PT-BR)`.
- No traducir el deck completo al portugués. Tampoco traducir al español un CTA o copy de campaña que deba evaluarse como experiencia final del médico brasileño.
- Las menciones anteriores de `Titular PT-BR` en este documento son referencias de copy de campaña; el diseñador debe componer su equivalente explicativo en español en la capa estratégica del deck.

### Assets de Notion — uso obligatorio

- **43 imágenes descargadas** desde la página estratégica están versionadas en [`presentacion/Assets/slides/`](../Assets/slides/).
- Usar [`README.md`](../Assets/slides/README.md) para la regla de uso y [`asset-manifest.json`](../Assets/slides/asset-manifest.json) para mapear asset, contexto de slide, hash y tamaño.
- Los assets son referencias de composición y marca. No son una autorización para reutilizar testimonios, rostros, logos o claims fuera del deck aprobado.

- Construir componentes reutilizables: `eyebrow`, `headline`, `body`, `status pill`, `card`, `step`, `CTA button`, `funnel node`, `email card`, `calendar slot`, `pipeline stage`, `metric chip`.
- Todas las imágenes deben quedar reemplazables y no contener texto rasterizado esencial.
- Usar animación sólo si la plataforma lo permite y no es requerida para entender la lámina. La presentación debe funcionar estática.
- Si hay una tensión entre estética y legibilidad, gana la legibilidad.

---

## 3. Arquitectura narrativa

```text
Posibilidad
→ estrategia
→ lanzamiento y contenido
→ hipótesis de audiencia
→ canales y paid media
→ web
→ postulación
→ selección
→ lifecycle email
→ venta
→ Customer
→ medición
→ operación compartida
→ roadmap e inversión
→ decisiones de dirección
```

La presentación se organiza en seis movimientos:

| Movimiento | Slides | Pregunta que responde |
|---|---:|---|
| I. Abrir la posibilidad | 01–05 | ¿Por qué esta alianza y qué futuro permite imaginar? |
| II. Construir demanda | 06–27 | ¿Qué contamos, a quién y en qué canales? |
| III. Convertir interés en caso | 28–39 | ¿Qué ocurre desde el anuncio hasta la conversación de selección? |
| IV. Email con intención | 40–45 | ¿Qué workflow acompaña cada nivel de decisión? |
| V. Venta, Customer y aprendizaje | 46–51 | ¿Cómo se preserva el contexto hasta el pago y la mejora? |
| VI. Escala, capacidad y decisión | 52–58 | ¿Qué evidencia, capacidad y decisiones sostienen la operación? |

---

## 4. Mapa maestro de slides

### I. Abrir la posibilidad

### 01 — Portada
- **Titular PT-BR:** `Sua carreira médica na Alemanha começa antes da viagem.`
- **Bajada:** `Sinaxys × Método ZAI by NOMII`.
- **Visual:** retrato editorial de médica brasileña en primer plano; una línea violeta inicia en Brasil y se proyecta hacia una ciudad alemana abstracta. Logo pequeño arriba a la derecha.
- **Objetivo:** abrir con posibilidad, no con una explicación de servicios.

### 02 — El camino imaginable
- **Titular PT-BR:** `A Alemanha pode despertar o interesse. Um caminho claro permite se imaginar lá.`
- **Bajada:** `Sinaxys e NOMII conectam possibilidade, preparação e acompanhamento.`
- **Visual:** una composición de dos planos: “desejo” (Alemania) y “próximo passo” (ruta). Evitar mapa literal como recurso principal.

### 03 — La estrategia convierte intención en decisiones
- **Titular PT-BR:** `Crescer começa com escolhas.`
- **Bajada:** `Investigar, testar, aprender e ajustar.`
- **Visual:** choice cascade de cinco preguntas: onde jogar / como vencer / capacidades / sistemas / métrica. Que parezca un marco de trabajo, no un consultory slide.

### 04 — Lanzamiento: tres semanas, una conversación
- **Eyebrow:** `LANÇAMENTO · 3 SEMANAS`
- **Titular PT-BR:** `Uma nova etapa. Um caminho mais claro.`
- **Visual:** timeline de tres semanas con tres momentos: alianza, método, personas. Cada momento se expresa mediante una pieza principal de contenido.

### 05 — Una grabación, varias piezas
- **Titular PT-BR:** `A aliança começa com uma conversa.`
- **Bajada:** `Uma gravação principal gera versões para YouTube, Reels, TikTok e mídia paga.`
- **Visual:** reproductor de video grande + cuatro derivados pequeños. Marcar capítulos: por que nos unimos / o que cada equipe aporta / o que é se preparar / como acompanhamos.

### II. Construir demanda

### 06 — Distribución: una conversación, varios ritmos
- **Titular PT-BR:** `Três semanas. Uma mesma conversa.`
- **Visual:** calendario editorial con Instagram como eje y ramificaciones a Facebook, TikTok, Shorts y YouTube.
- **Dato de composición:** `2 reels + 2 carrosséis + 2 stories` como referencia semanal inicial.

### 07 — Campaña conectada
- **Titular PT-BR:** `Cada ponto de contato tem uma função.`
- **Visual:** flujo horizontal contenido → anúncio → landing → candidatura → agenda. Agregar micro-etiquetas: despertar / orientar / selecionar / avançar.

### 08 — Ritmo de producción
- **Titular PT-BR:** `Produzir para aprender, não apenas para publicar.`
- **Visual:** tablero semanal con dos columnas: produção e distribuição. Mostrar versiones y aprendizajes; no una lista de tareas.

### 09 — Ejemplo de carrusel de apertura
- **Titular PT-BR:** `O que começa no Brasil?`
- **Visual:** cinco cards verticales como carrusel de Instagram: 01 intenção, 02 idioma, 03 documentação, 04 preparação, 05 próximo passo. Mockup de smartphone a escala amplia.

### 10 — La experiencia se entiende mejor cuando alguien la cuenta
- **Titular PT-BR:** `O acompanhamento ganha sentido quando alguém conta a própria experiência.`
- **Visual:** frame de testimonio con una cita corta; a un costado, módulos de corte para Reel, story y anuncio.
- **Nota:** no atribuir testimonios reales sin aprobación y derecho de uso.

### 11 — Marco visual de la alianza
- **Eyebrow:** `MANUAL DE MARCA · LINHA MÉDICA`
- **Titular PT-BR:** `Uma aliança. Um marco comum para comunicar.`
- **Visual:** mini design-system con foto, grid, tipografía, tonos, CTA y tratamiento de logos. Debe servir para alinear a producción audiovisual y paid media.

### 12 — Investigación propia: la motivación no es igual a decisión
- **Titular PT-BR:** `Cada decisão começa por uma motivação diferente.`
- **Visual:** matriz 2×2: motivação profissional / projeto de vida × descobrindo / decidindo. Dos o tres insights, no porcentajes no confirmados.

### 13 — Hipótesis: carrera médica
- **Titular PT-BR:** `Especializar-se também é construir uma direção.`
- **Visual:** perfil editorial “Carreira” con dolor, aspiración, pregunta y pieza de contenido idónea. No convertir una hipótesis en hecho.
- **CTA asociado:** `Entenda as etapas da preparação.`

### 14 — Hipótesis: proyecto de vida
- **Titular PT-BR:** `Mudar de país é uma decisão profissional e pessoal.`
- **Visual:** perfil editorial “Projeto de vida” con motivadores, dudas y contenido adecuado.
- **CTA asociado:** `Veja como o caminho pode se organizar.`

### 15 — Cinco pilares de contenido
- **Titular PT-BR:** `Imaginar o futuro. Entender o caminho.`
- **Visual:** cinco columnas o pétalos: carreira médica / vida na Alemanha / preparação e homologação / experiências e pessoas / metodologia e acompanhamento.

### 16 — Pilar 1: carrera médica en Alemania
- **Titular PT-BR:** `Carreira médica na Alemanha.`
- **Visual:** ruta conceptual de práctica, formación y especialización. Incluir tag `condições e exigências` para evitar simplificación.

### 17 — Pilar 2: vida en Alemania
- **Titular PT-BR:** `Vida na Alemanha também é parte da decisão.`
- **Visual:** mosaico humano de ciudad, familia, idioma, cotidianeidad y adaptación; no un catálogo turístico.

### 18 — Pilar 3: preparación y homologación
- **Titular PT-BR:** `Entender as etapas reduz a incerteza.`
- **Visual:** escalera de proceso con hitos genéricos y marcas `a validar por caso`. No prometer duración ni resultado.

### 19 — Pilar 4: experiencias y personas
- **Titular PT-BR:** `Histórias reais tornam o caminho mais concreto.`
- **Visual:** wall editorial de tres testimonios/formatos: médico, equipo, pregunta frecuente.

### 20 — Pilar 5: metodología y acompañamiento
- **Titular PT-BR:** `Método não é um discurso. É como o acompanhamento se organiza.`
- **Visual:** módulos del Método ZAI conectados; mantener una vista de proceso, no una lista de beneficios.

### 21 — Instagram: base semanal
- **Titular PT-BR:** `O perfil também explica a proposta.`
- **Visual:** perfil de Instagram con grid de seis piezas: dos Reels, dos carrosséis, dos stories. Subrayar que las piezas siguen los cinco pilares.

### 22 — Perfil diferenciado por audiencia
- **Titular PT-BR:** `Cada público precisa reconhecer sua própria pergunta.`
- **Visual:** comparación simple entre entrada para médicos, enfermería e instituciones, con la opción médica resaltada para este deck.

### 23 — Del descubrimiento al siguiente paso
- **Titular PT-BR:** `Descobrir a Alemanha é só o começo.`
- **Visual:** funnel TOFU → MOFU → BOFU con piezas, preguntas y CTA por etapa. Este es el puente a paid media.

### 24 — Paid media como sistema de aprendizaje
- **Titular PT-BR:** `Criativos não são peças isoladas. São hipóteses em teste.`
- **Visual:** biblioteca de cinco creativos por semana con variación de hook, propuesta y formato. Include “manter / iterar / pausar”.

### 25 — TOFU: descubrimiento
- **Titular PT-BR:** `TOFU · Fazer a possibilidade aparecer.`
- **Visual:** ejemplos de anuncios educacionales y de reconocimiento. CTA base: `Conheça o caminho.`

### 26 — MOFU: consideración
- **Titular PT-BR:** `MOFU · Transformar curiosidade em clareza.`
- **Visual:** tarjetas de preguntas: requisitos, idioma, etapas, acompañamiento, momento de vida. CTA base: `Entenda se este caminho faz sentido para você.`

### 27 — BOFU: candidatura
- **Titular PT-BR:** `BOFU · Convidar para uma candidatura informada.`
- **Visual:** anuncio con CTA visible: `Candidate-se ao programa.` Una nota pequeña: candidatura no equivale a admisión.

### III. Convertir interés en caso

### 28 — Del paid media a la web
- **Titular PT-BR:** `O anúncio desperta interesse. A web transforma curiosidade em próximo passo.`
- **Visual:** transición de anuncio vertical a landing desktop/mobile, conectada por una línea continua.

### 29 — La web necesita orientar, no sólo explicar
- **Titular PT-BR:** `Cada visita precisa de um caminho claro.`
- **Visual:** wireframe de landing con tres zonas: para quem é / como funciona / candidate-se. Usar resaltados de navegación, no párrafos densos.

### 30 — El recorrido empieza por el perfil
- **Titular PT-BR:** `O percurso começa pelo seu perfil.`
- **Visual:** tres tarjetas de entrada: Médicos / Enfermagem / Instituições. La tarjeta de médicos activa el flujo de esta presentación.

### 31 — El diferencial debe ser verificable
- **Titular PT-BR:** `O diferencial precisa vir acompanhado de evidência.`
- **Visual:** layout de “claim → fonte / documento → o que precisa validar”. No publicar afirmaciones de contrato, plaza o condiciones sin revisión jurídica/comercial.

### 32 — Ruta compartida
- **Titular PT-BR:** `Preparação no Brasil. Integração na Alemanha.`
- **Visual:** dos territorios en una misma línea de ruta con estaciones; usar lenguaje de acompañamiento, no garantía.

### 33 — Cifras: separar referencia, proyección y validación
- **Titular PT-BR:** `Dados claros também constroem confiança.`
- **Visual:** tres columnas: dado vigente con fuente / hipótese de negócio / dado a validar. Evitar usar cifras salariales como promesa.

### 34 — Lead-to-Client: transición
- **Titular PT-BR:** `O interesse abre uma porta. O sistema acompanha o próximo passo.`
- **Bajada:** `Do clique ao início do programa, uma rota contínua.`
- **Visual:** mapa panorámico de 10 nodos: campanha → web → candidatura → seleção → venda → pagamento → onboarding.

### 35 — Postulación: del clic al caso trazable
- **Titular PT-BR:** `Cada candidatura abre um caso, não apenas um formulário.`
- **Visual:** UI de formulario que se desdobla en Contacto, origem/UTM, Ticket y agenda Setter. Las cuatro entidades se conectan por líneas sutiles.

### 36 — Formulario: criterio y conversación
- **Titular PT-BR:** `O formulário orienta. A seleção confirma.`
- **Visual:** cinco campos de criterio: idade, formação, país, horizonte e capacidade de poupança. Un panel humano “avaliar contexto” decide: avançar / nutrir / não apto.
- **Nota:** el formulario no automatiza una promesa ni sustituye criterio humano.

### 37 — Cal: agenda y routing
- **Titular PT-BR:** `A agenda distribui oportunidade, não só horários.`
- **Visual:** calendar con disponibilidad sincronizada, distribución de agenda a Setter (round-robin sólo si Sinaxys lo valida), recordatorio y un único reagendamento. Capa inferior: `Cal booking ID → HubSpot`.

### 38 — Selección: conversación con criterio
- **Titular PT-BR:** `A chamada transforma interesse em informação útil.`
- **Visual:** llamada Setter de 30 min como hipótesis inicial medible, con cuatro tarjetas: contexto / motivação / barreiras / próximo passo. Resultados: `MQL`, `nutrição`, `não apto`. Un letrero claro: `Setter não apresenta preço.`

### 39 — Lifecycle email: no es newsletter
- **Titular PT-BR:** `Cada mensagem aparece quando ajuda a avançar.`
- **Visual:** orquestador central HubSpot con cuatro carriles de color violeta en distintas intensidades: Descarga de guía, TOFU Lead Gen, MOFU Agenda, BOFU Testimonios. Mostrar reglas de exclusión entre carriles.
- **Copy pequeño:** `Uma pessoa deve receber a sequência que corresponde ao seu momento — nunca todas ao mesmo tempo.`

---

## 5. Bloque expandido de email: cuatro workflows a construir

> **Estructura:** una revisión de solo lectura identificó workflows HubSpot con estas escalas de emails; la traducción a Sinaxys Brasil y su configuración futura siguen siendo una propuesta de deck, no una automatización aprobada. Antes de publicar, cada asunto, consentimiento, idioma, remitente, timing y condición de salida debe pasar revisión comercial, legal y operativa.

### 40 — Workflow 1: Descarga de guía
- **Eyebrow:** `EMAIL LIFECYCLE · 01 / 04`
- **Titular PT-BR:** `Entregue valor primeiro. Convide para o próximo passo depois.`
- **Finalidad:** activar un lead que pidió una guía y verificar si existe interés real en continuar.
- **Configuración propuesta:** **5 emails** + WhatsApp sólo con consentimiento explícito.
- **Cadencia:** `D0 · D2 · D5 · D8 · D12`.
- **Secuencia visual:** cinco sobres conectados por una línea de 12 días.
- **Contenido por envío:**
  1. `D0 — Aqui está o seu guia` → entrega del recurso; CTA: `Abrir o guia`.
  2. `D2 — O que esse caminho exige na prática` → contexto; CTA: `Entender as etapas`.
  3. `D5 — Uma dúvida comum antes de começar` → objeción frecuente; CTA: `Ver respostas`.
  4. `D8 — Como outras pessoas organizaram a decisão` → evidencia/testimonio aprobado; CTA: `Conhecer uma experiência`.
  5. `D12 — Quer entender o seu próximo passo?` → invitación selectiva; CTA: `Candidate-se ao processo de seleção`.
- **Reglas de salida:** candidatura enviada, reunión reservada, baja de suscripción, no elegible confirmado o entrada a MOFU/BOFU.
- **Visual:** rail de 5 cards email + una landing resource card. El CTA final debe ser el único violeta lleno.

### 41 — Workflow 2: TOFU Lead Gen
- **Eyebrow:** `EMAIL LIFECYCLE · 02 / 04`
- **Titular PT-BR:** `Fazer a possibilidade amadurecer antes de pedir uma decisão.`
- **Finalidad:** educar y construir confianza con personas que mostraron interés inicial, pero no han expresado intención de postular.
- **Configuración propuesta:** **12 emails** en una ventana de **65 días**.
- **Cadencia:** `D0 · D3 · D7 · D14 · D21 · D23 · D30 · D37 · D44 · D51 · D58 · D65`.
- **Arquitectura de mensajes:**
  - **01–03 / Descobrir:** carreira, vida y pregunta inicial. CTA: `Explorar o caminho`.
  - **04–06 / Entender:** idioma, etapas y preparación. CTA: `Ver como funciona`.
  - **07–09 / Confiar:** método, equipo, experiencia aprobada. CTA: `Conhecer a metodologia`.
  - **10–12 / Avançar:** autoevaluación, selección y candidatura. CTA: `Candidate-se ao programa`.
- **Reglas de salida:** candidatura, reserva Setter, interacción que eleva intención, baja, contacto ya gestionado por ventas.
- **Visual:** línea de 12 puntos agrupada en cuatro capítulos; no dibujar doce sobres idénticos. Cada capítulo tiene un color/tono, pregunta y CTA.

### 42 — Workflow 3: MOFU Agenda / consideración
- **Eyebrow:** `EMAIL LIFECYCLE · 03 / 04`
- **Titular PT-BR:** `Clareza antes da conversa. Contexto antes da agenda.`
- **Finalidad:** acompañar a la persona que ya explora activamente el programa y necesita claridad para postular o agendar una conversación inicial.
- **Configuración propuesta:** **8 emails** en una ventana de **42 días**.
- **Cadencia:** `D0 · D3 · D7 · D12 · D18 · D25 · D32 · D42`.
- **Contenido por envío:**
  1. `O que acontece depois da candidatura?` → CTA: `Conhecer as etapas`.
  2. `Como funciona a conversa de seleção?` → CTA: `Ver como se preparar`.
  3. `Que informações ajudam a avaliar seu caso?` → CTA: `Revisar meu perfil`.
  4. `O que significa se preparar com método?` → CTA: `Conhecer o Método ZAI`.
  5. `Perguntas que vale levar para a conversa` → CTA: `Organizar minhas dúvidas`.
  6. `Uma experiência que ajuda a dimensionar o caminho` → CTA: `Assistir ao relato`.
  7. `Se este é o seu momento, dê o próximo passo` → CTA: `Candidate-se ao processo`.
  8. `Ainda avaliando? Salve este caminho para retomar depois` → CTA: `Retomar quando fizer sentido`.
- **Reglas de salida:** candidatura, Setter booking, clasificación en maduración, baja.
- **Visual:** calendario de seis semanas + dos CTAs progresivos: primero “entender”, luego “candidatar-se”.

### 43 — Workflow 4: BOFU Testimonios / agenda
- **Eyebrow:** `EMAIL LIFECYCLE · 04 / 04`
- **Titular PT-BR:** `Quando a decisão está próxima, cada mensagem deve reduzir fricção.`
- **Finalidad:** convertir intención alta en una candidatura o reunión de selección con expectativas claras.
- **Configuración propuesta:** **9 emails** en una ventana máxima de **50 días**; el workflow se detiene al reservar.
- **Cadencia:** `D0 · D2 · D5 · D9 · D14 · D21 · D30 · D40 · D50`.
- **Contenido por envío:**
  1. `Você não precisa decidir tudo hoje` → CTA: `Entender meu próximo passo`.
  2. `O que a seleção avalia — e o que ela não promete` → CTA: `Conhecer os critérios`.
  3. `História aprovada: como outra médica organizou sua decisão` → CTA: `Ver a experiência`.
  4. `Como chegar preparado para a conversa` → CTA: `Agendar conversa de seleção`.
  5. `Dúvidas frequentes antes de se candidatar` → CTA: `Ver perguntas frequentes`.
  6. `O que levar para uma conversa mais útil` → CTA: `Reservar meu horário`.
  7. `Seu contexto importa` → CTA: `Compartilhar meu perfil`.
  8. `Ainda faz sentido avançar agora?` → CTA: `Agendar conversa`.
  9. `Quando estiver pronto, retomamos daqui` → CTA: `Retomar minha candidatura`.
- **Reglas de salida:** agenda Setter/Closer según diseño aprobado, candidatura, conversión Customer, baja, exclusión por no aptitud.
- **Visual:** nueve pasos comprimidos en tres actos: reduzir incerteza / criar confiança / reservar conversa. Mostrar la reserva como destino, no como presión.

### 44 — Orquestación y exclusiones
- **Titular PT-BR:** `Quatro workflows. Uma única pessoa. Uma única verdade de contexto.`
- **Visual:** diagrama de ruteo con cuatro lanes y una ficha Contacto central. Reglas visuales:
  - no superponer secuencias TOFU, MOFU y BOFU;
  - priorizar la señal de mayor intención;
  - detener nurturing al reservar o cuando Sinaxys toma la conversación;
  - preservar origen, UTM, consentimiento y motivo de salida;
  - separar comunicaciones de marketing de confirmaciones transaccionales.
- **Capa transaccional adicional:** confirmación agenda, recordatorio, cancelación/reagendamiento y no-show. No contarlos dentro de los cuatro workflows de marketing.

### IV. Venta, Customer y aprendizaje

### 45 — Traspaso a ventas: el contexto viaja
- **Titular PT-BR:** `O Closer recebe uma oportunidade, não um lead frio.`
- **Visual:** dossier/memoria de conversación pasa del Setter al Closer. Campos visibles: origem, motivação, barreiras, idioma, horizonte, minuta y próximo passo.
- **Regla:** agenda Closer creada durante/desde Setter = SQL y Deal. Ningún prospecto salta directamente desde formulario a Closer.

### 46 — Venta: decisión y seguimiento
- **Titular PT-BR:** `A venda continua um processo que já tem contexto.`
- **Visual:** pipeline Sinaxys Brasil en cards: Reunião Closer agendada → Seguimento <15 dias → >15 dias → 1 mês → Oportunidade → Contrato enviado → Assinado / pagamento pendente → pagamento parcial → cliente → perdido/descartado.
- **Nota visual:** price/payment only appears in the Closer stage.

### 47 — Customer: evidencia de compromiso
- **Titular PT-BR:** `Cliente não é intenção. É um compromisso verificável.`
- **Visual:** dos llaves que activan el estado: contrato firmado + primer pago recibido (monto acordado según política comercial). De ahí salen onboarding, accesos y tareas internas.

### 48 — Onboarding: una nueva etapa, no el final del funnel
- **Titular PT-BR:** `Depois do pagamento, começa a experiência que sustenta a confiança.`
- **Visual:** workflow de onboarding con owner Sinaxys: bienvenida, documentos/accesos, plan inicial, calendario, confirmación de próximo hito. Separar claramente tareas internas y comunicaciones al cliente.

### 49 — Medición: aprender hasta Customer
- **Titular PT-BR:** `Não otimizamos formulários. Otimizamos clientes.`
- **Visual:** una trayectoria de cohortes: fonte → candidatura → MQL → SQL/Deal → pagamento inicial → Customer. Mostrar un gráfico de velocidad/conversión y filtros: campanha, coorte, país, responsável.

### 50 — Identidad de datos: una cadena verificable
- **Titular PT-BR:** `Cada etapa deixa uma evidência conectada.`
- **Visual:** modelo de identidad horizontal: email normalizado + HubSpot Contact ID + UTM/fonte + formulário + Cal booking ID + meeting/ticket + Deal + contrato + Stripe customer/payment ID (o identificador del proveedor de pago que Sinaxys confirme).
- **Regla:** el dashboard no debe inventar relaciones; debe usar claves persistentes y estados verificables.

### 51 — Operación: una arquitectura compartida
- **Titular PT-BR:** `Um mesmo fluxo. Responsabilidades claras.`
- **Visual:** swimlanes de dos equipos.
  - **NOMII:** estrategia, campañas, copy, configuración CRM/Cal, automatizaciones, capacitación, instrumentación y análisis.
  - **Sinaxys:** atención humana, Setter, Closer, propuesta, contrato, cobro y onboarding.
- **Pie:** `Tecnologia coordena; pessoas decidem.`

### V. Escala, capacidad y decisión

### 52 — Roadmap de instalación y aprendizaje
- **Titular de slide (ES):** `Instalar, probar, aprender y ajustar.`
- **Contenido visible:** diciembre semana 1–4, enero y febrero como cronología operativa. Incluir la evidencia esperada en cada corte: postulación trazable, MQL, reuniones, propuestas y primeros pagos.
- **Visual:** timeline horizontal de tres meses con evidencias bajo cada hito.

### 53 — Medios: qué sabemos y qué debe validarse
- **Titular de slide (ES):** `Una referencia no es todavía una proyección.`
- **Contenido visible:** 70–80 leads mensuales como referencia histórica discutida; aproximadamente 100 leads clasificados para enero y aspiración de 10 clientes como escenario de mesa, no como meta comprometida.
- **Visual:** tres bloques `referencia histórica / hipótesis de escenario / dato pendiente de validar` con una banda de fuentes Chile–regional–Brasil.

### 54 — Métricas y ecuación de capacidad
- **Titular de slide (ES):** `Cada mejora debe verse en la cohorte, no sólo en el volumen.`
- **Contenido visible:** `MQL × tasa de agenda × tasa de asistencia × tasa de cierre sobre reuniones asistidas`; escenario ilustrativo 100 MQL → 10 clientes = 10 % MQL a Customer.
- **Visual:** ecuación grande + funnel medible + chips de tiempo: postulación → primer contacto → reunión → primer pago.

### 55 — Inversión: prueba de diciembre, captación sostenida en enero
- **Titular de slide (ES):** `Invertir más sólo cuando la señal justifica escalar.`
- **Contenido visible:** tres objetivos: adquirir audiencia, adquirir leads y convertir interés en reuniones. Para cada uno mostrar objetivo diciembre, foco enero y métrica de decisión. Los montos quedan `Por dimensionar / Por acordar` hasta revisión de Edward.
- **Visual:** matriz de tres filas × cuatro columnas, con celdas editables de inversión y moneda.

### 56 — Organigrama de trabajo y capacidad
- **Titular de slide (ES):** `Una estrategia sólo funciona si cada responsabilidad tiene capacidad real.`
- **Contenido visible:** equipo de implementación NOMII: Natalia comunicación 20 h/semana; Edward growth y medios 16 h; Elías datos e integración 16 h; diseño gráfico 20 h. Base = 72 h/semana. La tabla histórica de Notion agregaba Setter de selección 20 h y totalizaba 92 h, pero esa capacidad debe reasignarse a Sinaxys según la decisión vigente de ownership.
- **Visual:** organigrama con dos columnas: NOMII (estrategia, contenido, medios, datos, diseño, capacitación) y Sinaxys (Setter, Closer, ventas, contratos, cobros, onboarding). Mostrar una línea de coordinación, no jerarquía entre compañías.

### 57 — Dependencias y decisiones operativas
- **Titular de slide (ES):** `La operación se bloquea donde faltan dueño, permiso o capacidad.`
- **Contenido visible:** PT-BR reviewer, voceros, video, cuenta de Instagram, cambios web, cobertura, presupuesto, capacidad comercial, dominio/remitente, consentimientos, cupos/licencias y dueños de cuentas.
- **Visual:** tablero de decisión con columnas `decisión / qué destraba / owner / estado`.

### 58 — Cierre de dirección
- **Titular de slide (ES):** `No se trata sólo de generar leads. Se trata de construir un camino claro para la persona correcta.`
- **Contenido visible:** volver al primer anuncio, explicar público, mensaje, señal de avance y responsable que actúa sobre ella.
- **Visual:** loop que conecta primer anuncio → datos → conversación → Customer → aprendizaje → siguiente pieza.
- **Cierre oral PT-BR — guion, no texto del deck:** `A pergunta não é apenas quantos leads vamos gerar. É qual caminho vamos construir para que a pessoa certa avance com clareza.`

---

## 6. Contrato funcional para diseño y desarrollo

### Datos que Claude debe mantener editables

- Todos los textos PT-BR.
- Número de emails, cadencias, CTAs y reglas de salida por workflow.
- Nombres de owners/roles; no incrustar personas reales.
- Cifras, costos, estimaciones y logos de partners.
- Imágenes, testimonios y fuentes documentales.

### Componentes que deben existir en el archivo final

- Portadas y separadores de sección.
- Timelines editables.
- Fichas de workflow con `objetivo / cantidad / cadencia / CTA / salida`.
- Funnel, swím-lanes y pipeline editables.
- Mockups de interfaz no dependientes de capturas reales.
- Sistema de notas o speaker notes donde se documenten supuestos y elementos `A VALIDAR`.

### Validación antes de presentar

- [ ] Copy final revisado por nativo PT-BR de Sinaxys.
- [ ] Cada claim sensible tiene fuente/aprobación o se elimina.
- [ ] Ninguna slide promete resultado laboral, migratorio o comercial.
- [ ] Los cuatro workflows muestran cantidad, cadencia, CTA y condición de salida.
- [ ] El rol humano de Sinaxys es explícito en selección, venta, cobro y onboarding.
- [ ] NOMII aparece como diseñador/configurador/medidor, no como operador comercial diario.
- [ ] La secuencia no supera dos ideas por slide y privilegia visuales sobre texto.

---

## 7. Fuentes de construcción

- Página estratégica Sinaxys en Notion: secuencia de slides 01–44 y referencias visuales existentes.
- Revisión de solo lectura de workflows HubSpot: escalas de referencia identificadas para el bloque de marketing automation; la configuración futura de Sinaxys requiere aprobación:
  - Descarga de guía: 5 emails.
  - TOFU Lead Gen: 12 emails.
  - MOFU Agenda: 8 emails.
  - BOFU Testimonios / Agenda: 9 emails.
- Arquitectura operativa del funnel Lead-to-Client documentada para Sinaxys Brasil.
- Propuesta comercial preliminar del Método ZAI para frecuencia de canales, inversión y roadmap.

> **Nota de implementación:** este blueprint describe una propuesta de presentación y configuración futura. No activa envíos, automatizaciones, calendar routing, pipelines, cobros ni comunicaciones.

## 8. Contrato literal de textos provenientes de Notion

> **Uso obligatorio.** Los textos de este anexo son los textos propuestos que ya existen en Notion. Claude debe incorporarlos como copy visible en la slide indicada, no degradarlos a notas de speaker. Si un texto es un guion, anuncio, CTA, correo o mensaje dirigido al médico, se conserva en **PT-BR** dentro del mockup/asset. Si explica la estrategia a Sinaxys, se compone en **español**.

> **Precedencia de ownership.** Esta exportación conserva textos históricos tal como fueron redactados. La decisión más reciente de Sirius tiene precedencia: NOMII no atiende leads como Setter ni Closer; Sinaxys ejecuta la atención humana, selección, venta, cobro y onboarding. Cuando aparezca un texto anterior que atribuya ejecución humana a NOMII, debe representarse como antecedente y ajustarse a la arquitectura vigente, no implementarse literalmente.

### Fuente Notion · Slide 1: Portada

_No había copy textual adicional en el bloque; usar el título y el asset asociado como dirección visual._

### Fuente Notion · Slide 2:

[este txt más pequeño] Alemania puede despertar el interés.
[este txt en grande] Un camino claro
permite imaginarse ahí.
[Y debajo, más pequeño:]
Sinaxys y NOMII se unen para conectar esa posibilidad con una ruta de preparación y acompañamiento basada en el Método ZAI.

[Referencia o idea visual de la slide]

### Fuente Notion · Slide 3:

El crecimiento empieza con decisiones.
Para la bajada metodológica de esta estrategia, tomamos como referencia Strategy Choice Cascade, utilizado por IDEO U. Este marco conecta las decisiones esenciales del negocio y permite visualizar y compartir una dirección común para la comunicación y la operación.
| Decisión | Aplicación a Sinaxys |
| ¿Qué queremos lograr? | Convertir el interés en postulaciones calificadas y clientes. |
| ¿Dónde vamos a competir? | Brasil: médicos que exploran, evalúan o deciden su carrera en Alemania. |
| ¿Cómo nos diferenciaremos? | El vínculo local de Sinaxys junto al Método ZAI y la experiencia de NOMII. |
| ¿Qué necesitamos hacer bien? | Contenido en portugués, captación, selección y venta consultiva. |
| ¿Cómo sostendremos la operación? | HubSpot y Notion: responsables, seguimiento, medición y aprendizaje. |
Investigar, probar, aprender y ajustar.
Idea visual de la slide:

### Fuente Notion · Slide 4:

Antetítulo
LANZAMIENTO · 3 SEMANAS
Título
Una nueva etapa.
Un camino más claro.
Bajada
Presentar la alianza, explicar el Método ZAI y mostrar a las personas que acompañan el proceso.
Focos
Nueva etapa · Método ZAI · Personas
Concepto comunicacional
Sua carreira médica na Alemanha começa antes da viagem.
[referencia visual de la slide]

### Fuente Notion · Slide 5

Antetítulo
PIEZA DE APERTURA · PROPUESTA
Título
La alianza empieza con una conversación.
Bajada
Nicolás Orbenes y Luca, juntos en Alemania.
Texto dentro del reproductor
Sinaxys + Método ZAI by NOMII
Capítulos dentro del reproductor
01 · Por qué nos unimos
02 · Qué aporta cada equipo
03 · Qué significa prepararse
04 · Cómo acompañamos el camino
Título lateral
Una grabación, varias piezas
Distribución
YouTube · Conversación principal
Instagram y TikTok · Corte breve
Meta Ads · Versiones con hooks propios
Frase inferior
Uma nova etapa na Sinaxys. Um caminho construído com a experiência da NOMII.
Nota pequeña
Duración orientativa: YouTube 6–8 min · Versión breve 45–60 s.
[referencia visual de la slide]

### Fuente Notion · Slide 6:

Título
Tres semanas. Una misma conversación.
Bajada
Instagram como eje. Distribución y adaptación según el formato.
| Formato | Semana 1 | Semana 2 | Semana 3 |
| Reel | Por que nos unimos? | O que significa ser acompanhado? | As dúvidas que queremos responder |
| Carrusel | O que muda nesta nova etapa? | Quem faz o quê no seu caminho? | Do Brasil à Alemanha: as etapas |
| Reel | Preparar-se vai além do idioma | Alemão médico na prática | Uma experiência real da NOMII |
| Carrusel | Alemanha além do hospital | Sua vida também faz parte do plano | Onde você quer construir sua carreira? |
Distribución — texto inferior
Instagram + Facebook · Reels adaptados a TikTok y Shorts · Versiones extensas en YouTube.
Frecuencias — texto pequeño
Feed: 2 reels + 2 carruseles por semana.
Stories: 2 entregas por semana.
[referencia visual de la slide]

### Fuente Notion · Slide 7A:

Título
Una campaña conectada.
Bajada
Del contenido al seguimiento, cada punto de contacto tiene una función.
Textos del framework
| Bloque | Descripción |
| Orgánico | Comprender y confiar. |
| Meta Ads | Explorar y postular. |
| Web / landing médica | Alianza · Etapas · Requisitos. |
| Formulario + HubSpot | Perfil · Origen · Siguiente paso. |
| Selección y seguimiento | Email y WhatsApp según el estado del contacto. |
Frase inferior
Cada contacto conserva su origen, su contexto y su siguiente paso.
Nota pequeña
Pauta activa con formulario, CRM y atención operativos.
[referencia visual de la slide]

### Fuente Notion · Slide 7B

Título
El ritmo de producción del lanzamiento.
Bajada
Tres semanas · Las réplicas aprovechan el material principal.
Columna izquierda: CONTENIDO Y DISTRIBUCIÓN
Instagram
2 reels + 2 carruseles por semana.
12 publicaciones de feed en total.
Facebook
Réplica del feed: 12 publicaciones.
Stories de Instagram
2 entregas semanales · 6 en total.
TikTok
2 reels reutilizados por semana · 6 en total.
Columna derecha: PROFUNDIDAD Y CAPTACIÓN
YouTube
2 videos principales + 6 shorts en total.
Meta Ads
Mínimo 5 creativos nuevos por semana.
15 en total · Distribución inicial semanal: 2 TOFU + 2 MOFU + 1 BOFU.
Web, email y WhatsApp
1 landing médica y flujos según el estado del contacto.
Nota pequeña
Los flujos de email y WhatsApp se dimensionan por disparador, no como publicaciones semanales.
[referencia visual de la slide]

### Fuente Notion · Slide 8:

Título
Cómo entender esta nueva etapa
Bajada
Ejemplo de carrusel · Instagram y Facebook · Semana 1.
Pieza 1
O que muda nesta nova etapa?
Sinaxys + Método ZAI by NOMII.
Pieza 2
Duas experiências.
Um caminho conectado.
Sinaxys no Brasil.
Método ZAI da NOMII.
Pieza 3
Antes da viagem,
existe preparação.
Idioma. Documentação.
Preparação para o reconhecimento profissional.
Pieza 4
O próximo passo
é entender o caminho.
Acompanhe esta nova etapa.
Caption propuesto
Uma nova etapa começa na Sinaxys International. Em parceria com a NOMII, incorporamos o Método ZAI, criado pelo Dr. Nicolás Orbenes, ao nosso programa médico. Nas próximas semanas, vamos mostrar a preparação, as pessoas e as exigências desse caminho.
[referencia visual de slide]
Slide 9:
Título
El acompañamiento se entiende mejor cuando alguien lo cuenta.
Bajada
Experiencia real de NOMII · Adaptación para el lanzamiento de Sinaxys.
Texto de referencia dentro del video
Eu queria alguém que me orientasse.
Identificación
Marisol · Médica equatoriana.
Experiência de acompanhamento da NOMII.
Nota bajo el video
Subtitulación propuesta en portugués.
Título lateral
Lo que esta pieza debe mostrar.
Puntos
- La preocupación antes de comenzar.
- El apoyo concreto durante la preparación.
- La persona detrás del proyecto profesional.
Caption propuesto
Antes de começar, Marisol tinha uma preocupação: como organizar tudo sem enfrentar o processo sozinha? Ela compartilha sua experiência com a NOMII, empresa que desenvolveu o Método ZAI e agora se une à Sinaxys no Brasil. Uma história para conhecer o lado humano dessa preparação.
Aclaración
El caso conserva su origen: NOMII.
Distribución — texto pequeño
Instagram + Facebook · TikTok · Fragmentos para YouTube Shorts.
[refernecia visual de la slide]

### Fuente Notion · Slide 10:

Antetítulo
MANUAL DE MARCA · LÍNEA MÉDICA
Título
Una alianza.
Un marco común para comunicar.
Bajada
Toda comunicación sobre el Método ZAI, el proceso y la experiencia de NOMII debe seguir el manual de la alianza.
Autoría reconocible
El Método ZAI se identifica como metodología de NOMII.
Testimonios con contexto
Los casos de NOMII conservan su origen, contexto y etapa real.
Mensajes consistentes y respaldados
Proceso, servicios y condiciones deben coincidir con la oferta vigente.
Texto pequeño
Mismo criterio en redes, web, anuncios, mailings y materiales comerciales.
Enlace discreto al pie
Consultar manual completo en Notion ↗
[referencia visual]
Slide 11:
Investigación propia NOMII
Cada decisión tiene una motivación
Nuestro estudio interno explora qué buscan los clientes, qué les preocupa y qué necesitan para confiar.
Ambicioso profesional
Busca especializarse, crecer y superar límites en su trayectoria.
Proyecta en familia
Evalúa el bienestar y la viabilidad del proyecto familiar.
Migrante por seguridad
Busca ejercer y vivir con mayor tranquilidad.
Un aprendizaje transversal: claridad, acompañamiento y respaldo verificable.
Estos aprendizajes orientan el punto de partida; no representan una segmentación validada de Brasil.
[Referencia visual slide[

### Fuente Notion · Slide 12

Los perfiles se afinan con personas reales.
Durante los primeros meses, contrastaremos las hipótesis con postulaciones, conversaciones y decisiones de clientes de Sinaxys.
Probar mensajes
Motivaciones y objeciones.
Escuchar en selección
Interés, requisitos y disposición para comenzar.
Contrastar con clientes
Qué influyó en su decisión y qué necesitaron resolver.
Ajustar la comunicación
Actualizar perfiles, mensajes y contenidos con lo aprendido.
HubSpot conectará el origen del contacto con su motivación y avance comercial.
Evaluaremos postulaciones calificadas, reuniones realizadas y avance hacia clientes.
[referencia visual de slide]

### Fuente Notion · Lámina de transición

Cómo llevamos todo lo que hemos revisado hasta ahora a la comunicación concreta por canal

### Fuente Notion · Slide 15

Imaginar el futuro.Entender el camino.
Cinco pilares para despertar interés, orientar y construir confianza.
Carrera médica en Alemania
Ejercicio profesional, especialización y oportunidades, con sus condiciones y exigencias.
Vida en Alemania
Adaptación, vivienda, costo de vida, cultura y familia.
Preparación y homologación
Idioma, documentación, etapas y exámenes explicados con claridad.
Experiencias y personas
Vivencias, dificultades, aprendizajes y avances de médicos y equipos.
Metodología y acompañamiento
Cómo se organiza la preparación con Sinaxys y el Método ZAI de NOMII.
[referencia visual de la slide]

### Fuente Notion · Slide 16

Carrera médica en Alemania
Objetivo del pilar
Explorar el ejercicio profesional, la formación especializada y las oportunidades en Alemania, con sus condiciones y exigencias.
Qué comunicaremos
Especialización y desarrollo · Rutina y entorno clínico · Remuneración y condiciones laborales · Oportunidades y requisitos.
[referencia visual slide]

### Fuente Notion · Slide 17

Vida en Alemania
Objetivo del pilar
Acercar la vida cotidiana en Alemania, mostrando las posibilidades y los desafíos de adaptarse y construir un proyecto personal o familiar.
Qué comunicaremos
Vivienda y costo de vida · Cultura y adaptación
Vida cotidiana y tiempo libre · Pareja y familia
[referencia visual slide]

### Fuente Notion · Slide 18

Preparación y homologación
Objetivo del pilar
Explicar el camino para ejercer en Alemania, haciendo comprensibles sus etapas, requisitos y exigencias de preparación.
Qué comunicaremos
Alemán general y médico · Documentación y trámites
Etapas y exámenes · Preparación y planificación
[referencia visual slide]

### Fuente Notion · SLIDE 19

Experiencias y personas
Objetivo del pilar
Mostrar el lado humano del proceso a través de vivencias, dificultades, aprendizajes y avances reales de médicos y equipos.
Qué comunicaremos
Testimonios con contexto · Desafíos y aprendizajes
Avances del proceso · Personas detrás del acompañamiento
[referencia visual slide]
SLIDE 20
Metodología y acompañamiento
Objetivo del pilar
Hacer visible cómo se organiza la preparación con el Método ZAI de NOMII y cómo se articula el acompañamiento junto a Sinaxys.
Qué comunicaremos
Método ZAI y etapas de preparación · Equipos y responsabilidades
Acompañamiento en origen y destino · Alcances y límites del programa
[referencia visual slide]

### Fuente Notion · SLIDE 21:

Instagram · Base semanal
2 reels + 2 carruseles + 2 historias.
Distribución del contenido
- Facebook: espejo de Instagram.
- TikTok + YouTube Shorts: los mismos 2 videos cortos por semana.
- YouTube largo: 1 testimonio largo de NOMII al mes. En los próximos meses se evaluará producir contenido largo recurrente.
- LinkedIn: mantener su enfoque y alinear descripción e idioma.
[referencia visual slide]

### Fuente Notion · Slide 22

El perfil también explica la propuesta.
Instagram
Perfil médico diferenciado de enfermería.
Bio clara · Fijados de orientación · Destacados del proceso.
YouTube
Descripción centrada en médicos brasileños y el Método ZAI de NOMII.
Palabras clave en portugués · Listas por tema · Testimonios con contexto.
LinkedIn
Mantener el enfoque corporativo y explicar la alianza en la descripción.
Portugués como base · Alemán con traducción cuando el destinatario lo requiera.
[referencia visual slide]
[Slide de transición]
DE ORGÁNICO A PAID MEDIA
La confianza abre la conversación.
La pauta invita
a dar el siguiente paso.
Meta Ads · De la atención a la postulación calificada.

### Fuente Notion · Slide 23

De descubrir Alemania a dar el siguiente paso.
TOFU · Descubrimiento
Dar a conocer Sinaxys y abrir la posibilidad.
Acercar Alemania a quienes aún no la consideran, con información de valor sobre carrera y vida en el país.
MOFU · Consideración
Construir comprensión y confianza.
Explicar el Método ZAI de NOMII, el proceso y el alcance del acompañamiento.
BOFU · Conversión
Generar postulaciones calificadas.
Aclarar requisitos y facilitar la evaluación del perfil y su disposición para comenzar con CTAs que dirigen directamente a la postulación del programa.

### Fuente Notion · Slide 23A · Momentos de decisión

Antetítulo · VIAJE DEL MÉDICO · BRASIL
Título · ¿Cómo decide un médico si Alemania encaja en su proyecto de vida?
Bajada · En Brasil, cada médico puede entrar en un momento distinto. Sinaxys adapta el mensaje del Método ZAI a la pregunta que trae.
| Momento | Pregunta del médico | Punto de contacto | Qué muestra Sinaxys | CTA en PT-BR |
| Descubrir | Será que eu me imagino trabalhando na Alemanha? | Reel de Instagram o anuncio de Meta | Un médico cuenta cómo es su rutina en Alemania y qué le hizo dar el primer paso. | Conhecer a rotina médica |
| Explorar | O que preciso preparar ainda no Brasil? | Carrusel o YouTube → web médica | El Método ZAI de NOMII ordena el idioma, la documentación y las etapas de preparación. | Ver etapas e requisitos |
| Evaluar | Esse caminho faz sentido para mim e para a minha família? | Testimonio de NOMII + requisitos en la landing | Un caso real muestra qué apoyo recibió la médica, qué resolvió ella y cómo afectó a su familia. | Conhecer uma experiência real |
| Decidir | Quero começar. Meu perfil se encaixa no programa? | Remarketing o visita directa → formulario | Sinaxys explica los criterios y qué ocurrirá al enviar la postulación. | Candidate-se ao programa |
Cómo leer el mapa · La consideración tiene dos movimientos: explorar posibilidades y evaluar si encajan. Una médica puede consultar los requisitos, conversar con su familia y volver a un testimonio antes de decidir. Quien ya tomó la decisión puede ir directo al formulario.
Referencia visual de la slide
Base metodológica · The Messy Middle · Google · Journey Mapping 101 · Nielsen Norman Group. Adaptación a la postulación médica, con carrera profesional y proyecto familiar como hipótesis de partida para Brasil.

### Fuente Notion · Slide 24

Producir para aprender
Mínimo 5 creativos nuevos por semana, probando variaciones de hook, propuesta y formato. La distribución entre etapas se ajustará según los resultados.

### Fuente Notion · Slide 25

TOFU — Descubrimiento
Reconocimiento de Sinaxys e información de valor para descubrir Alemania.
- Reel: “E se a Alemanha entrasse nos seus planos?”
- Carrusel: “O salário é só uma parte da conta.”
- Video: “5 coisas que você precisa saber se quer se especializar como médico na Alemanha”

### Fuente Notion · Slide 26

MOFU — Consideración
Dar claridad sobre el programa y construir confianza en el acompañamiento.
- Video: “Antes da passagem, existe um plano.”
- Carrusel: “O que o programa faz. E o que depende de você.”
- Testimonio NOMII: “O que eu gostaria de ter sabido antes de começar.”

### Fuente Notion · Slide 27·

BOFU — Conversión
Invitar a postular al programa y evaluar el encaje del médico.
- Video: “Quer começar nos próximos três meses? Vamos avaliar seu perfil.”
- Carrusel: “Seu plano combina com o programa?”
- Pieza estática: “O próximo passo é apresentar o seu projeto.”
CTA de BOFU: “Candidate-se ao programa.”
Destino directo: formulario de postulación.

### Fuente Notion · Slide 28 ·

De paid media a la web
El anuncio despierta el interés.
La web convierte esa curiosidad
en una decisión informada.
Una experiencia clara para entender la propuesta y dar el siguiente paso.

### Fuente Notion · Slide 29 ·

Cada visita necesita un camino claro.
La web debe orientar al público correcto, explicar el programa y facilitar una postulación informada.
Orientar · Una entrada por perfil
Médicos, enfermería e instituciones con recorridos diferenciados.
Explicar · Una oferta médica clara
Método ZAI de NOMII, etapas, requisitos y alcance del acompañamiento.
Conectar · Un siguiente paso coherente
Postulación, evaluación y seguimiento comercial.
Actualizaremos la experiencia existente para alinearla con la alianza.

### Fuente Notion · Slide 30

El recorrido empieza por su perfil.
Subir las tarjetas existentes al primer bloque de la portada.
Médicos · Enfermería · Instituciones
Los anuncios médicos llegan directamente a la página médica.
Textos del mockup
> Conectamos profissionais de saúde e instituições entre Brasil e Alemanha.
Encontre as informações para o seu perfil.
| Tarjeta | Descripción | CTA |
| Sou médico(a) | Preparação para sua carreira na Alemanha. | Conhecer o programa médico |
| Sou profissional de enfermagem | Um caminho dedicado à sua profissão. | Conhecer o programa de enfermagem |
| Represento uma instituição | Conexões para equipes de saúde. | Conhecer as soluções |

### Fuente Notion · Slide 31

El diferencial, desde el inicio.
Contrato de trabajo asegurado desde el primer día en Alemania.
Respaldo documental del ministerio alemán — BMAS.
La comunicación debe reflejar el alcance de la documentación institucional.
Textos del mockup
> SINAXYS × NOMII
Prepare sua carreira médica. Chegue à Alemanha com contrato de trabalho.
Com o Método ZAI da NOMII, sua preparação conecta idioma, reconhecimento do diploma e inserção profissional.
✓ Contrato desde o primeiro dia na Alemanha
✓ Base institucional documentada · BMAS
Enlace: Conheça a documentação
CTA: Candidate-se ao programa
A candidatura inicia uma avaliação do seu perfil.

### Fuente Notion · Slide 32

Una ruta compartida con NOMII.
Preparación en Brasil.
Integración en Alemania.
Mismos hitos del Método ZAI, adaptados al público brasileño.
Sin plazos fijos ni una ruta paralela al programa.
Textos del mockup
> MÉTODO ZAI DA NOMII
Um caminho que começa no Brasil e continua na Alemanha.
Preparação e integração em duas fases conectadas.
FASE BRASIL · Preparação antes da viagem
- Alemão A1–B2: Lingoda + especialistas NOMII.
- Documentos para reconhecimento do diploma e visto.
- Gestão do contrato de trabalho.
- Preparação de moradia, seguros e viagem.
FASE ALEMANHA · Integração e reconhecimento profissional
- Chegada com contrato de trabalho.
- Preparação e aprovação na FSP.
- Atuação clínica com Berufserlaubnis.
- Preparação e aprovação na KP.
- Approbation e acesso à especialização.
> O avanço depende da preparação individual, das aprovações exigidas e dos trâmites aplicáveis.
CTA: Conheça os requisitos do programa.

### Fuente Notion · Slide 33

Cifras que debemos corregir o validar.
La web debe distinguir datos actuales, proyecciones e ingresos según etapa.
| Dato publicado | Qué falta precisar | Fuente de contraste |
| 50.000 médicos faltantes | La proyección del Zi contempla un déficit acumulado hasta 2040; no equivale a vacantes actuales. | Zi · Proyección 2024 |
| 10.997 médicos de familia | Sin fuente identificada: confirmar indicador y fecha antes de mantenerlo. | KBV · Por verificar |
| 50% se jubila en diez años | Validar población, año base y horizonte temporal. | KBV / Bundesärztekammer |
| Salarios hospitalarios | Usar categoría, antigüedad y salario base bruto del convenio vigente. | TV-Ärzte/VKA · Marburger Bund |
| 20.000–30.000 € en consulta propia | No presentarlo como salario de convenio; distinguir ingresos, gastos y beneficio. | Zi-Praxis-Panel |
Referencia VKA: Arzt, 5.722,05–7.355,29 € brutos mensuales, según antigüedad. Vigencia: junio–diciembre de 2026.

### Fuente Notion · Slide 34 · Lead to Client Funnel · transición

El interés abre una puerta. El sistema acompaña el siguiente paso.
Del clic al inicio del programa: una ruta continua, con contexto y una decisión posible en cada etapa.

### Fuente Notion · Slide 35 · Postulación · del clic al caso trazable

Cada postulación abre un caso, no solo un formulario.
Origen de campaña, perfil, Contacto, Ticket y agenda Setter quedan conectados desde el primer paso.

### Fuente Notion · Slide 36 · Postulación · criterio y conversación

El formulario orienta. La selección confirma.
Edad, formación, país, horizonte y capacidad de ahorro preparan la conversación; el criterio humano define la ruta.

### Fuente Notion · Slide 37 · Cal · agenda y routing

La agenda distribuye oportunidad, no solo horarios.
Disponibilidad sincronizada, round-robin de Setters y un reagendamiento permitido conservan trazabilidad y flexibilidad.

### Fuente Notion · Slide 38 · Selección · conversación con criterio

La llamada convierte interés en información útil.
La asistencia marca MQL. El Setter perfila, explica el camino y define SQL, nutrición o no aptitud; no comunica precio.

### Fuente Notion · Slide 39 · Email · lifecycle, no newsletter

Cada mensaje aparece cuando ayuda a avanzar.
HubSpot coordina CTAs, secuencias y exclusiones según la etapa; no se superponen TOFU, MOFU y BOFU.

### Fuente Notion · Slide 40 · Traspaso a ventas · contexto preservado

El Closer recibe una oportunidad, no un lead frío.
La agenda de Closer crea SQL y Deal; origen, motivación, barreras, notas y próximo paso viajan con la minuta.

### Fuente Notion · Slide 41 · Venta · decisión y seguimiento

La venta continúa un proceso que ya tiene contexto.
El pipeline de Sinaxys Brasil ordena conversación, seguimiento, contrato, firma, pago y motivo de pausa o pérdida.

### Fuente Notion · Slide 42 · Customer · evidencia de compromiso

Cliente no es una intención. Es un compromiso verificable.
Contrato firmado más primer pago recibido activa Customer en HubSpot y el onboarding correspondiente.

### Fuente Notion · Slide 43 · Medición · aprender hasta Customer

No optimizamos formularios. Optimizamos clientes.
Cada cohorte conecta fuente, postulación, MQL, Deal y primer pago para decidir qué mejorar y dónde intervenir.


## 9. Métricas, medios y contenido que debe quedar visible

### Métricas de negocio y atribución

| Pregunta de dirección | Definición que debe aparecer en el deck | Fórmula / evidencia |
|---|---|---|
| ¿Cuántos médicos postulan? | Primeras postulaciones únicas atribuibles a pauta. | Total de postulaciones únicas; promedio mensual = total ÷ seis. |
| ¿Cuánto cuesta cada postulación? | Costo por postulación atribuible a Meta. | Inversión Meta ÷ postulaciones únicas atribuibles a Meta. |
| ¿Cuánto cuesta un ticket de selección? | Costo por postulante que alcanza etapa de selección. | Inversión Meta ÷ postulantes únicos atribuibles a Meta que alcanzaron selección. |
| ¿Cuántos llegan a Customer? | Médicos con contrato firmado y primer pago; unidos a cohorte de primera postulación. | Fynk + HubSpot + identidad persistente. |

### Comparaciones que se deben mostrar con etiqueta de alcance

- **Chile por vía de entrada:** formulario nativo, landing u otra vía identificada; mostrar postulaciones, seleccionados, clientes y costo cuando el gasto sea asignable.
- **Chile y otros cuatro mercados:** inversión, postulaciones, promedio mensual, seleccionados, costo por seleccionado y clientes por país.
- **Referencia para Brasil:** comparar la vía prevista para Sinaxys con la equivalente de Chile y con el resultado regional ponderado; no inferir equivalencia automática.
- **Datos públicos sensibles:** separar déficit proyectado, vacantes actuales, salarios de convenio e ingresos de consulta; los textos de fuente pendientes se presentan como `por validar`, no como promesas.

### Frecuencias por canal que Claude debe representar

| Canal | Lanzamiento | Ritmo posterior | Señal que importa |
|---|---|---|---|
| Instagram | 6 reels, 6 carruseles y 6 entregas de stories en tres semanas | 3 piezas de feed por semana | retención, consultas pertinentes, visitas landing |
| Facebook | 12 publicaciones replicadas en tres semanas | distribución espejo | visitas y preguntas derivadas |
| YouTube | 2 videos principales (semana 1 y 3) + 6 shorts | 1 video principal quincenal + 2 shorts semanales | retención y paso al perfil médico |
| TikTok | hasta 6 reels reutilizados | según programación | visualizaciones con retención y visitas perfil |
| Meta Ads | mínimo 5 creativos por semana; al menos 15 en lanzamiento | iteración por resultados | costo por MQL y reuniones asistidas |
| Web / landing | disponible desde el primer anuncio | actualización al validar oferta/fricción | inicio y envío válido de formulario, preservando origen |
| Email | por evento y permiso | se detiene al responder/completar/darse de baja | perfiles retomados, respuestas y reuniones |

## 10. Organigrama y ownership vigentes

```text
NOMII — estrategia y sistema                         SINAXYS — operación humana
├─ Comunicación: Natalia · 20 h/sem                  ├─ Validación PT-BR y voceros
├─ Growth/medios: Edward · 16 h/sem                  ├─ Setter: selección humana y agenda
├─ Datos/integración: Elías · 16 h/sem               ├─ Closer: propuesta, objeciones y cierre
├─ Diseño gráfico · 20 h/sem                         ├─ Contrato, cobro y primer pago
└─ Estrategia, copy, CRM/Cal, automatización,        └─ Onboarding operativo y continuidad
   capacitación y medición
```

- **Capacidad base NOMII:** 72 h/semana para comunicación, growth, datos e integración y diseño.
- **Referencia histórica Notion:** el cuadro inicial agregaba 20 h/semana de Setter y totalizaba 92 h/semana. Esta cifra debe mostrarse en una nota de transición, porque la ejecución Setter/Closer corresponde ahora a Sinaxys por decisión explícita de Sirius.
- **Punto de control:** la inversión y el volumen de MQL sólo pueden escalar si Sinaxys confirma capacidad de Setter, Closer, tiempos de primera gestión y cupos de agenda.

## 11. Checklist de transferencia a Claude

- [ ] Diseñar el deck en español; distinguir visualmente cada muestra/guion PT-BR.
- [ ] Incorporar el copy literal de la sección 8 en la slide correspondiente.
- [ ] Usar los 43 assets versionados como guía visual, con referencia al manifest.
- [ ] Mantener las cifras marcadas como referencia, escenario o dato pendiente de validar.
- [ ] Representar los cuatro workflows de email con cantidad, cadencia, CTA, exclusión y salida.
- [ ] Mantener la división NOMII / Sinaxys del organigrama vigente.
- [ ] Dejar métricas, inversión, moneda, owners y fuentes editables.
