"""Generate a circular favicon from the avatar photo.

Crops a square focused on the head/upper body of the original portrait image
and applies a circular alpha mask so the corners are transparent. Keeps the
body upright (no rotation).
"""

from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "src" / "lib" / "assets" / "avatar.png"
OUT_STATIC = ROOT / "static" / "avatar.png"
OUT_LIB = ROOT / "src" / "lib" / "assets" / "avatar-circle.png"

OUTPUT_SIZE = 512


def main() -> None:
    src = Image.open(SOURCE).convert("RGBA")
    w, h = src.size

    # Focus on head + upper torso: take a square whose width equals the image
    # width, anchored near the top of the photo.
    side = w
    top = max(0, int(h * 0.05))
    if top + side > h:
        top = h - side
    box = (0, top, w, top + side)
    square = src.crop(box)

    square = square.resize((OUTPUT_SIZE, OUTPUT_SIZE), Image.LANCZOS)

    mask = Image.new("L", (OUTPUT_SIZE, OUTPUT_SIZE), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, OUTPUT_SIZE, OUTPUT_SIZE), fill=255)

    result = Image.new("RGBA", (OUTPUT_SIZE, OUTPUT_SIZE), (0, 0, 0, 0))
    result.paste(square, (0, 0), mask=mask)

    OUT_STATIC.parent.mkdir(parents=True, exist_ok=True)
    result.save(OUT_STATIC, format="PNG")
    result.save(OUT_LIB, format="PNG")
    print(f"Wrote {OUT_STATIC} and {OUT_LIB} ({OUTPUT_SIZE}x{OUTPUT_SIZE}).")


if __name__ == "__main__":
    main()
