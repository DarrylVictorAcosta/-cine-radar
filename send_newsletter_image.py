#!/usr/bin/env python3
"""
Envía la edición de CineRadar como IMAGEN embebida en el correo, conservando el
diseño y la estructura EXACTOS del newsletter (render pixel por pixel).

Es la opción de máxima fidelidad visual para email: el cuerpo del correo es la
captura del newsletter (clic = abre la versión web interactiva).

USO:
    GMAIL_USER="tucorreo@gmail.com" \
    GMAIL_APP_PASSWORD="xxxx xxxx xxxx xxxx" \
    python3 send_newsletter_image.py [editions/cineradar_XXX.jpg]

Genera la imagen con (ver README/WORKFLOW):
    1. python3 -c "...emailize..."  -> /tmp/cr_shot.html
    2. Chrome --headless=new --screenshot
    3. recorte + JPEG  -> editions/cineradar_XXX.jpg
"""
import os, sys, re, ssl, glob, smtplib
from email.message import EmailMessage

REPO_USER, REPO_NAME, BRANCH = "DarrylVictorAcosta", "-cine-radar", "main"
HERE = os.path.dirname(os.path.abspath(__file__))


def latest_jpg():
    files = sorted(glob.glob(os.path.join(HERE, "editions", "cineradar_*.jpg")))
    if not files:
        sys.exit("No hay imagen de edición (.jpg) en editions/. Genérala primero.")
    return files[-1]


def load_recipients():
    path = os.path.join(HERE, "recipients.txt")
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                out.append(line)
    if not out:
        sys.exit("recipients.txt sin destinatarios activos.")
    return out


def main():
    user = os.environ.get("GMAIL_USER")
    pw = os.environ.get("GMAIL_APP_PASSWORD")
    if not user or not pw:
        sys.exit("Faltan GMAIL_USER / GMAIL_APP_PASSWORD en el entorno.")

    jpg = sys.argv[1] if len(sys.argv) > 1 else latest_jpg()
    num = (re.search(r"cineradar_(\d+)", os.path.basename(jpg)) or [None, "???"])[1]
    browser_url = (f"https://htmlpreview.github.io/?https://github.com/"
                   f"{REPO_USER}/{REPO_NAME}/blob/{BRANCH}/editions/cineradar_{num}.html")
    recipients = load_recipients()

    with open(jpg, "rb") as f:
        img_bytes = f.read()
    cid = "cineradar"

    html = f"""\
<div style="background-color:#1A252C;padding:0;margin:0;text-align:center;font-family:Arial,sans-serif;">
  <a href="{browser_url}" style="text-decoration:none;">
    <img src="cid:{cid}" width="620" alt="CineRadar — Edición #{num}"
         style="display:block;width:100%;max-width:620px;margin:0 auto;border:0;">
  </a>
  <div style="padding:14px;">
    <a href="{browser_url}" style="color:#C4A84F;font-size:12px;letter-spacing:1px;text-decoration:none;">
      🎬 Abrir versión interactiva en el navegador
    </a>
  </div>
</div>"""

    msg = EmailMessage()
    msg["Subject"] = f"🎬 CineRadar — Edición #{num} · Las 5 historias que importan"
    msg["From"] = f"CineRadar <{user}>"
    msg["To"] = ", ".join(recipients)
    msg.set_content(f"Tu edición de CineRadar #{num} está lista.\n"
                    f"Ver en el navegador: {browser_url}\n\nUntil the next screening. — CineRadar")
    msg.add_alternative(html, subtype="html")
    # adjunta la imagen embebida (cid) al alternativo HTML
    msg.get_payload()[1].add_related(img_bytes, maintype="image", subtype="jpeg", cid=f"<{cid}>")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as s:
        s.login(user, pw)
        s.send_message(msg)

    print(f"✓ Edición #{num} (imagen) enviada a {len(recipients)} destinatario(s).")
    for r in recipients:
        print("   ·", r)
    print("   Versión interactiva:", browser_url)


if __name__ == "__main__":
    main()
