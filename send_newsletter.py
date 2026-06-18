#!/usr/bin/env python3
"""
Envía la última edición de CineRadar (o una indicada) a la lista de recipients.txt
usando Gmail por SMTP.

USO:
    GMAIL_USER="tucorreo@gmail.com" \
    GMAIL_APP_PASSWORD="xxxx xxxx xxxx xxxx" \
    python3 send_newsletter.py [ruta/a/edicion.html]

- Si no se indica una edición, toma la más reciente en editions/.
- Los destinatarios se leen de recipients.txt (uno por línea; # = comentario).
- GMAIL_APP_PASSWORD es una "contraseña de aplicación" de Google, NO tu
  contraseña normal. Se crea en: https://myaccount.google.com/apppasswords
  (requiere verificación en dos pasos activada).

El correo incluye un banner "Ver edición completa" que enlaza a la versión
renderizada en el navegador (htmlpreview), de modo que la calidad visual se
mantiene aunque el cliente de email recorte parte del CSS.
"""

import os
import sys
import re
import ssl
import glob
import smtplib
from email.message import EmailMessage

REPO_USER = "DarrylVictorAcosta"
REPO_NAME = "-cine-radar"
BRANCH = "main"

HERE = os.path.dirname(os.path.abspath(__file__))


def latest_edition():
    files = sorted(glob.glob(os.path.join(HERE, "editions", "cineradar_*.html")))
    if not files:
        sys.exit("No hay ediciones en editions/. Genera una primero.")
    return files[-1]


def load_recipients():
    path = os.path.join(HERE, "recipients.txt")
    if not os.path.exists(path):
        sys.exit("Falta recipients.txt.")
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                out.append(line)
    if not out:
        sys.exit("recipients.txt no tiene destinatarios activos (todos comentados).")
    return out


def view_in_browser_url(edition_path):
    name = os.path.basename(edition_path)
    raw = f"https://github.com/{REPO_USER}/{REPO_NAME}/blob/{BRANCH}/editions/{name}"
    return f"https://htmlpreview.github.io/?{raw}"


def edition_number(edition_path):
    m = re.search(r"cineradar_(\d+)\.html", os.path.basename(edition_path))
    return m.group(1) if m else "???"


def build_html(edition_html, browser_url, num):
    banner = f"""
    <div style="background:#1A252C;padding:16px;text-align:center;font-family:Inter,Arial,sans-serif;">
      <a href="{browser_url}"
         style="display:inline-block;background:#8B3A2F;color:#E8E0D0;
                text-decoration:none;font-weight:600;font-size:13px;letter-spacing:1px;
                padding:11px 22px;border-radius:6px;border:1px solid #C4A84F;">
        🎬 Ver edición completa en el navegador
      </a>
      <p style="color:#A8A098;font-size:11px;margin:10px 0 0;">
        Si el correo no se ve bien, abre la versión web de calidad completa.
      </p>
    </div>
    """
    if "<body>" in edition_html:
        return edition_html.replace("<body>", "<body>" + banner, 1)
    return banner + edition_html


def main():
    user = os.environ.get("GMAIL_USER")
    pw = os.environ.get("GMAIL_APP_PASSWORD")
    if not user or not pw:
        sys.exit("Faltan GMAIL_USER y/o GMAIL_APP_PASSWORD en el entorno.")

    edition = sys.argv[1] if len(sys.argv) > 1 else latest_edition()
    with open(edition, encoding="utf-8") as f:
        edition_html = f.read()

    num = edition_number(edition)
    browser_url = view_in_browser_url(edition)
    html = build_html(edition_html, browser_url, num)
    recipients = load_recipients()

    msg = EmailMessage()
    msg["Subject"] = f"🎬 CineRadar — Edición #{num} · Las 5 historias que importan"
    msg["From"] = f"CineRadar <{user}>"
    msg["To"] = ", ".join(recipients)
    msg.set_content(
        f"Tu edición de CineRadar está lista.\n\n"
        f"Ver en el navegador (calidad completa): {browser_url}\n\n"
        f"Until the next screening. — CineRadar"
    )
    msg.add_alternative(html, subtype="html")

    ctx = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ctx) as s:
        s.login(user, pw)
        s.send_message(msg)

    print(f"✓ Edición #{num} enviada a {len(recipients)} destinatario(s):")
    for r in recipients:
        print(f"   · {r}")
    print(f"   Link de calidad completa: {browser_url}")


if __name__ == "__main__":
    main()
