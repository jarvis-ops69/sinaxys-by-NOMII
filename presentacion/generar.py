"""Construye el HTML de la presentación a partir del orden del roadmap."""

from html import escape
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parent
ROADMAP_LINK = re.compile(r"^\| \[(D\d+) · [^\]]+\]\(diapositivas/(D\d+)\.md\)", re.M)


def render_deck():
    order = ROADMAP_LINK.findall((ROOT / "ROADMAP.md").read_text(encoding="utf-8"))
    ids = [key for key, path_key in order if key == path_key]
    sheets = {p.stem for p in (ROOT / "diapositivas").glob("D*.md")}
    if not ids or len(set(ids)) != len(order) or set(ids) != sheets:
        raise ValueError("Revisa los códigos, rutas y orden de las fichas en ROADMAP.md.")

    contents = []
    navigation = []
    for key in ids:
        source = (ROOT / "diapositivas" / f"{key}.md").read_text(encoding="utf-8")
        heading, _, body = source.partition("\n")
        prefix = f"# {key} · "
        if not heading.startswith(prefix) or not heading[len(prefix):].strip():
            raise ValueError(f"{key}.md necesita un título que identifique la lámina.")
        title = escape(heading[len(prefix):].strip())
        body = re.sub(r"<!--.*?-->", "", body, flags=re.S).strip()
        if body:
            rendered = subprocess.run(
                ["pandoc", "--from=gfm-raw_html", "--to=html5", "--wrap=none"],
                input=body, text=True, check=True, capture_output=True, cwd=ROOT,
            ).stdout
        else:
            rendered = '<p class="pending">Pendiente de contenido</p>'
        navigation.append(f'<li><a href="#{key}">{key} · {title}</a></li>')
        contents.append(f'<section id="{key}"><p class="code">{key}</p><h2>{title}</h2>{rendered}</section>')

    template = (ROOT / "plantilla.html").read_text(encoding="utf-8")
    result = template.replace("<!-- INDICE -->", "\n".join(navigation)).replace(
        "<!-- LAMINAS -->", "\n".join(contents)
    )
    (ROOT / "index.html").write_text(result, encoding="utf-8")


if __name__ == "__main__":
    render_deck()
