# Cómo trabajar en sinaxys-by-NOMII

Estas instrucciones aplican a todos los agentes que trabajen con este repositorio. `main` contiene la versión acordada por el equipo. **Solo Edward Marinao decide qué se incorpora y ejecuta personalmente el merge a `main` en GitHub.** Los agentes entregan su trabajo mediante una pull request (PR).

## Primera respuesta obligatoria al iniciar o retomar una tarea

Antes de editar, localiza el identificador D01–D18 en el [roadmap](presentacion/ROADMAP.md). Lee la ficha de Notion, el issue, el guion, la bitácora y la PR existente. Si la persona dice «quiero avanzar» sin especificar la tarea, usa el contexto de su frente para proponer la más probable y pregúntale cuál quiere tomar.

**Explica el proceso en voz alta a la persona, en tu primera respuesta.** En tres o cuatro frases indica qué tarea y entrega le corresponden, qué ya se sabe y el próximo paso. Dile que ella define cómo resolverla, que registrarás sus decisiones en su ficha de Notion y que, cuando te pida llevarlas a la presentación, le mostrarás una vista previa en una PR que Edward integrará. En una reanudación incluye el último acuerdo y el pendiente. Al cerrar ese mensaje, haz la primera pregunta útil y espera la respuesta.

**Guía la conversación con hasta tres preguntas en total, una por turno.** Usa cada respuesta para elegir la siguiente. Omite lo que esté resuelto y evita exigir un formulario. Por ejemplo, en D17 pregunta por el plan proyectado o dónde encontrar la referencia. Si Edward elige México, averigua qué quiere reutilizar (distribución, costos o etapas). Si ya eligió también las etapas, pregunta si el cálculo parte de un presupuesto o una meta. México y TOFU/MOFU/BOFU son ejemplos hasta que el responsable los confirme para esta tarea.

**La memoria de trabajo está en Notion.** En cada avance registra fecha, autor, decisión o respuesta, fuente o enlace, pendiente y siguiente paso. Conserva las aportaciones anteriores. Si falta acceso, indica qué necesitas registrar y conserva el texto para guardarlo cuando haya acceso. Actualiza el estado de la tarea en GitHub Projects al cambiar de etapa. El responsable decide cuándo el contenido está listo para redactar la lámina.

**Entrega editorial.** Solo al recibir esa indicación, edita el Markdown libre de la diapositiva en la rama de la tarea. Añade al issue el enlace a la PR y a la ficha la rama y la PR. En la bitácora deja una entrada por PR con Dxx e issue, fecha, autor, rama, cambio concreto, fuente o supuesto, verificación, pendientes y decisión de Edward. Incluye el enlace a la vista previa. Actualiza la misma entrada al corregir. El [roadmap](presentacion/ROADMAP.md) explica cómo generar la vista. Usa el guion de referencia y conserva en Notion los materiales de trabajo.

## Cómo entregar los cambios en GitHub

1. **Antes de editar**, lee el `README.md`, las últimas entradas de `BITACORA.md` y las PR abiertas que toquen tu tema. La minuta de Notion define cómo se presenta la estrategia. El PDF es la propuesta de partida y el guion en `main` es la versión integrada.
2. **Una tarea nueva, una rama nueva.** Parte del último `main` remoto. Nombra la rama `frente/descripcion-breve`. Usa `medios` para inversión (Edward), `comunicaciones` para contenido y marca (Natalia), `datos` para medición e integraciones (Elías) y `equipo` para tareas compartidas. Si retomas una tarea que ya tiene PR, continúa en su rama.
3. **Trabaja dentro del alcance acordado.** Si el cambio toca otro frente, indica en la PR a quién afecta y qué necesita revisar. Acompaña cifras y afirmaciones con su fuente. Identifica los supuestos y las decisiones pendientes.
4. **Registra el trabajo en la bitácora.** Añade una entrada por PR con fecha, frente, autor o agente, rama, enlace a la PR, cambio, verificación y decisión que necesita Edward. Si recibes observaciones, actualiza la misma entrada. Conserva las entradas de los demás.
5. **Sube los commits a tu rama y abre una PR hacia `main`.** En la descripción indica qué cambió, dónde revisarlo, qué comprobaste y qué falta decidir. Comprueba que el último commit esté en GitHub y entrega el enlace a la PR. Puedes dejarla en borrador si queda trabajo pendiente.
6. **La revisión y la integración son pasos distintos.** Atiende las observaciones en la misma rama. Si `main` avanzó y hay conflictos, incorpora los cambios preservando el trabajo de ambos frentes y vuelve a verificar. La aprobación en una reunión, en Notion o en el chat permite registrar el acuerdo. El último paso del agente es dejar la PR lista para Edward. El push directo, el merge y el auto-merge hacia `main` quedan fuera de las acciones de los agentes.
