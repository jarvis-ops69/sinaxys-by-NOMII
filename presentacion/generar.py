"""Genera la presentación y un documento HTML autónomo por diapositiva."""
from base64 import b64encode
from html import escape
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parent
SHEET = re.compile(r"^\| \[(S(?:M?\d+[A-Z]?|TR)) · [^\]]+\]\(diapositivas/([^/)]+)\.md\)", re.M)
COMMENTS = re.compile(r"<!--.*?-->", re.S)


def embed_png(match):
    # El HTML general y el individual deben poder abrirse también sin conexión.
    data = (ROOT / "recursos" / match[1]).read_bytes()
    encoded = b64encode(data).decode("ascii")
    return f'<img src="data:image/png;base64,{encoded}"'


def slide_body(markdown, key):
    """Agrupa los apartados de la lámina y deja el pie fuera de las columnas."""
    html = subprocess.run(
        ["pandoc", "--from=gfm-raw_html", "--to=html5", "--wrap=none", "--id-prefix", key + "-"],
        input=markdown, text=True, check=True, capture_output=True, cwd=ROOT,
    ).stdout.strip()
    html = re.sub(r'<img src="\.\./recursos/([A-Za-z0-9_-]+\.png)"', embed_png, html)
    html = html.replace("<table>", '<div class="table-scroll" tabindex="0" role="region" aria-label="Tabla de la diapositiva"><table>').replace("</table>", "</table></div>")
    groups = re.split(r"(?=<h3\b)", html)
    if len(groups) == 1:
        return html
    last, separator, footer = groups[-1].partition("<blockquote>")
    groups[-1] = last
    cards = "".join(f'<div class="panel">{part}</div>' for part in groups[1:])
    return f'{groups[0]}<div class="panels">{cards}</div>{separator}{footer}'


def render_deck():
    roadmap = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
    entries = SHEET.findall(roadmap)
    order = [key for key, stem in entries if key == stem]
    sheets = {p.stem for p in (ROOT / "diapositivas").glob("S*.md")}
    if not order or len(set(order)) != len(entries) or set(order) != sheets:
        raise ValueError("Comprueba que cada ficha S figure una sola vez en el roadmap y use su misma ruta.")

    template = (ROOT / "plantilla.html").read_text(encoding="utf-8")
    out = ROOT / "html"
    out.mkdir(exist_ok=True)
    contents, links = [], []
    for position, key in enumerate(order):
        source = (ROOT / "diapositivas" / f"{key}.md").read_text(encoding="utf-8")
        heading, _, markdown = source.partition("\n")
        prefix = f"# {key} · "
        if not heading.startswith(prefix) or not heading[len(prefix):].strip():
            raise ValueError(f"Revisa el título de {key}.md.")
        title = escape(heading[len(prefix):].strip())
        kicker = re.search(r"<!-- Antetítulo: (.+?) -->", markdown)
        eyebrow = f'<p class="eyebrow">{escape(kicker[1])}</p>' if kicker else ""
        rendered = slide_body(COMMENTS.sub("", markdown).strip(), key)
        if key == "STR":
            label = "Transición"
        elif key.startswith("SM"):
            label = "Propuesta de medios " + key[2:].lstrip("0")
        else:
            label = "Slide " + key[1:].lstrip("0")
        theme = "dark" if key in {"S01", "S02", "STR"} else "light"
        body = (f'<article id="{key}" class="slide {theme}" aria-labelledby="title-{key}">'
                f'<div class="slide-id">{label}</div><div class="editorial">{eyebrow}'
                f'<h2 id="title-{key}">{title}</h2>{rendered}</div></article>')
        single = template.replace("<!-- TITLE -->", title + " · Sinaxys Brasil").replace(
            "<!-- HEADER -->", "").replace("<!-- CONTENT -->", body)
        (out / f"{key}.html").write_text(single, encoding="utf-8")
        links.append(f'<li><a href="#{key}"><span>{label}</span> {title}</a></li>')
        actions = []
        if position:
            actions.append(f'<a href="#{order[position-1]}">← Anterior</a>')
        actions.append('<a href="#indice">Índice</a>')
        if position + 1 < len(order):
            actions.append(f'<a href="#{order[position+1]}">Siguiente →</a>')
        contents.append(body + '<nav class="paging" aria-label="Navegar desde ' + label + '">' + " ".join(actions) + "</nav>")

    header = ('<header id="indice"><p class="wordmark">Sinaxys × NOMII</p>'
              '<h1>Presentación de la alianza en Brasil</h1><details><summary>Índice de diapositivas</summary>'
              '<nav aria-label="Índice"><ol>' + "".join(links) + '</ol></nav></details></header>')
    deck = template.replace("<!-- TITLE -->", "Presentación Sinaxys Brasil").replace(
        "<!-- HEADER -->", header).replace("<!-- CONTENT -->", "\n".join(contents))
    (ROOT / "index.html").write_text(deck, encoding="utf-8")
    # Solo se retiran salidas generadas de diapositivas eliminadas de la secuencia.
    for file in out.glob("S*.html"):
        if file.stem not in sheets:
            file.unlink()


if __name__ == "__main__":
    render_deck()
