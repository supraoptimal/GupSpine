#!/usr/bin/env python3
"""
GupSpine HTML Builder
Assembles the complete single-file HTML app from parts.
"""
import json, os, base64

OUTPUT = "/Users/gene/Desktop/Emergency Spine Guidelines/Emergency Spine - Claude/GupSpine.html"
PARTS_DIR = "/Users/gene/Desktop/Emergency Spine Guidelines/Emergency Spine - Claude/parts"

def read_part(name):
    with open(os.path.join(PARTS_DIR, name), 'r') as f:
        return f.read()

def build():
    # Load image data (optional — app works without images)
    images = {}
    img_path = "/tmp/image_data.json"
    if os.path.exists(img_path):
        with open(img_path, "r") as f:
            images = json.load(f)
    else:
        print("Note: /tmp/image_data.json not found — building without embedded images.")

    html = read_part("01_head.html")
    html += read_part("02_css.html")
    html += read_part("03_body_start.html")

    # Inject image data as JS constants (empty object if no images)
    html += "\n<script>\n// Embedded image data\nconst IMG = " + json.dumps(images) + ";\n</script>\n"

    html += read_part("04_clinical_data.html")
    html += read_part("05_app_logic.html")
    html += read_part("06_reference_content.html")
    html += read_part("07_closing.html")

    with open(OUTPUT, 'w') as f:
        f.write(html)

    size_mb = os.path.getsize(OUTPUT) / (1024*1024)
    print(f"Built {OUTPUT}")
    print(f"File size: {size_mb:.1f} MB")

if __name__ == "__main__":
    build()
