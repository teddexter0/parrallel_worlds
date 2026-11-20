from __future__ import annotations

import math
import random
import wave
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT / "Parallel Worlds" / "game"
WEB = ROOT / "ParallelWorlds-1.0.0-dists" / "ParallelWorlds-1.0.0-web"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    names = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/georgiab.ttf" if bold else "C:/Windows/Fonts/georgia.ttf",
        "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf",
    ]
    for name in names:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def gradient(size: tuple[int, int], top: tuple[int, int, int], bottom: tuple[int, int, int]) -> Image.Image:
    w, h = size
    img = Image.new("RGB", size, top)
    px = img.load()
    for y in range(h):
        t = y / max(h - 1, 1)
        row = tuple(int(top[i] * (1 - t) + bottom[i] * t) for i in range(3))
        for x in range(w):
            px[x, y] = row
    return img


def add_noise(img: Image.Image, amount: int = 10) -> Image.Image:
    random.seed(7)
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    px = overlay.load()
    w, h = img.size
    for y in range(0, h, 3):
        for x in range(0, w, 3):
            v = random.randint(-amount, amount)
            if v >= 0:
                px[x, y] = (255, 255, 255, v)
            else:
                px[x, y] = (0, 0, 0, -v)
    return Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")


def draw_window(draw: ImageDraw.ImageDraw, box, lit=(245, 202, 110), frame=(42, 64, 75)):
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=8, fill=frame)
    pad = 8
    draw.rectangle((x1 + pad, y1 + pad, x2 - pad, y2 - pad), fill=lit)
    draw.line((x1 + (x2 - x1) // 2, y1 + pad, x1 + (x2 - x1) // 2, y2 - pad), fill=frame, width=4)
    draw.line((x1 + pad, y1 + (y2 - y1) // 2, x2 - pad, y1 + (y2 - y1) // 2), fill=frame, width=4)


def draw_multiverse_background(img: Image.Image, title: bool = False) -> Image.Image:
    d = ImageDraw.Draw(img, "RGBA")
    w, h = img.size
    random.seed(22)

    for _ in range(180):
        x, y = random.randrange(0, w), random.randrange(0, int(h * 0.78))
        a = random.randrange(45, 160)
        d.ellipse((x, y, x + 2, y + 2), fill=(200, 235, 255, a))

    center = (int(w * 0.62), int(h * 0.48))
    for i, color in enumerate([(80, 200, 255), (117, 238, 190), (240, 190, 92), (190, 140, 255)]):
        rx = int(w * (0.22 + i * 0.045))
        ry = int(h * (0.10 + i * 0.023))
        bbox = (center[0] - rx, center[1] - ry, center[0] + rx, center[1] + ry)
        d.ellipse(bbox, outline=color + (160,), width=5)

    for offset, radius, color in [
        ((0, 0), 135, (74, 196, 255)),
        ((-235, -95), 74, (119, 236, 190)),
        ((220, 118), 88, (240, 190, 92)),
        ((120, -170), 58, (190, 140, 255)),
    ]:
        x = center[0] + offset[0]
        y = center[1] + offset[1]
        d.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color + (48,), outline=color + (220,), width=4)
        d.ellipse((x - radius // 2, y - radius // 2, x + radius // 2, y + radius // 2), outline=(235, 250, 255, 125), width=2)

    for angle in range(-35, 50, 17):
        y = center[1] + angle * 7
        d.line((int(w * 0.28), y, int(w * 0.94), y - angle * 5), fill=(98, 210, 255, 46), width=2)

    d.rectangle((0, int(h * 0.74), w, h), fill=(8, 13, 22, 205))
    for x in range(0, w, 155):
        top = int(h * 0.74) - (x * 19 % int(h * 0.20)) - 40
        d.rectangle((x, top, x + 92, h), fill=(12, 23, 36, 220))
        for wy in range(top + 38, int(h * 0.74), 54):
            if (x + wy) % 3:
                d.rectangle((x + 24, wy, x + 43, wy + 24), fill=(91, 219, 255, 72))

    if title:
        d.text((int(w * 0.08), int(h * 0.36)), "Parallel\nWorlds", fill=(245, 250, 255), font=font(96, True), spacing=8)
        d.text((int(w * 0.085), int(h * 0.56)), "multiverse theory in motion", fill=(124, 230, 255), font=font(34))

    return add_noise(img, 7)


def generate_main_menu() -> None:
    img = gradient((1920, 1080), (8, 18, 33), (10, 11, 18))
    img = draw_multiverse_background(img)
    d = ImageDraw.Draw(img, "RGBA")
    d.rectangle((0, 0, 760, 1080), fill=(5, 8, 15, 112))
    out = GAME / "gui" / "main_menu.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)


def background(path: str, kind: str) -> None:
    img = gradient((1920, 1080), (34, 47, 55), (14, 19, 26))
    d = ImageDraw.Draw(img, "RGBA")

    if kind == "campus_day":
        img = gradient((1920, 1080), (121, 176, 203), (218, 196, 146))
        d = ImageDraw.Draw(img, "RGBA")
        d.ellipse((-180, -180, 360, 360), fill=(255, 220, 128, 185))
        d.rectangle((0, 710, 1920, 1080), fill=(72, 118, 83, 255))
        d.polygon([(0, 1080), (830, 700), (1090, 700), (1920, 1080)], fill=(212, 198, 170, 255))
        for x in (210, 520, 1390, 1660):
            d.rectangle((x, 380, x + 140, 745), fill=(126, 85, 67, 255))
            d.polygon([(x - 50, 380), (x + 70, 230), (x + 190, 380)], fill=(64, 105, 75, 255))
        d.rectangle((690, 385, 1230, 720), fill=(166, 125, 92, 255))
        d.polygon([(650, 385), (960, 235), (1270, 385)], fill=(94, 73, 78, 255))
        for x in range(735, 1130, 110):
            draw_window(d, (x, 445, x + 65, 540), lit=(233, 241, 224))
        d.rectangle((880, 570, 1040, 720), fill=(71, 60, 62, 255))

    elif kind == "library_steps_evening":
        img = gradient((1920, 1080), (78, 95, 128), (45, 35, 63))
        d = ImageDraw.Draw(img, "RGBA")
        d.ellipse((1400, 95, 1640, 335), fill=(255, 190, 109, 170))
        d.rectangle((360, 290, 1560, 720), fill=(119, 97, 94, 255))
        d.polygon([(300, 290), (960, 120), (1620, 290)], fill=(90, 70, 79, 255))
        for x in range(470, 1400, 210):
            d.rectangle((x, 345, x + 92, 720), fill=(82, 65, 69, 255))
            draw_window(d, (x + 18, 390, x + 74, 520), lit=(245, 189, 107))
        for y in range(720, 1030, 52):
            d.rectangle((240, y, 1680, y + 32), fill=(132, 118, 109, 255))
            d.line((240, y, 1680, y), fill=(72, 61, 66, 185), width=4)

    elif kind == "cafe":
        img = gradient((1920, 1080), (128, 83, 62), (45, 40, 43))
        d = ImageDraw.Draw(img, "RGBA")
        d.rectangle((0, 0, 1920, 210), fill=(83, 46, 42, 255))
        d.rectangle((0, 710, 1920, 1080), fill=(92, 62, 52, 255))
        for x in range(190, 1710, 360):
            d.ellipse((x, 110, x + 150, 260), fill=(255, 202, 119, 70))
            d.line((x + 75, 0, x + 75, 140), fill=(54, 39, 39), width=5)
        d.rectangle((260, 320, 720, 600), fill=(50, 61, 66, 255))
        d.rectangle((290, 350, 690, 570), fill=(176, 205, 204, 255))
        d.rectangle((940, 365, 1600, 615), fill=(101, 60, 48, 255))
        d.rectangle((940, 615, 1600, 700), fill=(74, 42, 38, 255))
        for x in (390, 760, 1250):
            d.ellipse((x, 700, x + 260, 760), fill=(45, 35, 35, 255))
            d.rectangle((x + 115, 740, x + 145, 920), fill=(45, 35, 35, 255))

    elif kind == "rooftop_night":
        img = gradient((1920, 1080), (14, 28, 52), (5, 8, 18))
        d = ImageDraw.Draw(img, "RGBA")
        random.seed(5)
        for _ in range(120):
            x, y = random.randrange(0, 1920), random.randrange(0, 520)
            d.ellipse((x, y, x + 2, y + 2), fill=(255, 244, 199, random.randrange(80, 180)))
        d.ellipse((1450, 115, 1600, 265), fill=(236, 224, 183, 205))
        for x, h, c in [(0, 430, (20, 31, 48)), (240, 560, (17, 27, 42)), (510, 460, (26, 36, 52)), (870, 610, (18, 25, 39)), (1240, 500, (24, 33, 49)), (1540, 580, (16, 24, 36))]:
            d.rectangle((x, 1080 - h, x + 310, 1080), fill=c + (255,))
            for wx in range(x + 35, x + 260, 70):
                for wy in range(1080 - h + 50, 1000, 95):
                    if random.random() > 0.45:
                        d.rectangle((wx, wy, wx + 26, wy + 38), fill=(244, 190, 90, 150))
        d.rectangle((0, 785, 1920, 1080), fill=(21, 20, 24, 255))
        d.rectangle((0, 735, 1920, 795), fill=(38, 39, 45, 255))

    elif kind == "dean_office":
        img = gradient((1920, 1080), (90, 66, 55), (39, 35, 39))
        d = ImageDraw.Draw(img, "RGBA")
        d.rectangle((0, 680, 1920, 1080), fill=(78, 53, 45, 255))
        d.rectangle((270, 190, 720, 650), fill=(56, 44, 42, 255))
        for y in range(235, 600, 95):
            d.rectangle((310, y, 680, y + 42), fill=(104, 78, 60, 255))
        d.rectangle((1020, 165, 1580, 610), fill=(54, 67, 74, 255))
        d.rectangle((1060, 205, 1540, 570), fill=(166, 189, 188, 255))
        d.rectangle((690, 650, 1460, 870), fill=(84, 49, 38, 255))
        d.rectangle((760, 600, 1390, 680), fill=(123, 72, 47, 255))
        d.rectangle((870, 515, 1260, 600), fill=(36, 38, 45, 255))

    elif kind == "room_night":
        img = gradient((1920, 1080), (37, 48, 72), (12, 15, 25))
        d = ImageDraw.Draw(img, "RGBA")
        d.rectangle((0, 690, 1920, 1080), fill=(43, 38, 43, 255))
        d.rectangle((1180, 150, 1660, 520), fill=(36, 45, 60, 255))
        d.rectangle((1220, 190, 1620, 480), fill=(14, 29, 52, 255))
        for x in range(1260, 1600, 85):
            for y in range(235, 440, 72):
                d.rectangle((x, y, x + 24, y + 28), fill=(244, 190, 90, 130))
        d.rectangle((300, 585, 900, 820), fill=(58, 56, 68, 255))
        d.rectangle((330, 520, 875, 620), fill=(73, 83, 103, 255))
        d.rectangle((960, 625, 1320, 800), fill=(70, 44, 37, 255))
        d.rectangle((1030, 560, 1250, 625), fill=(40, 42, 50, 255))
        d.ellipse((140, 290, 330, 480), fill=(255, 213, 124, 45))
        d.line((235, 455, 235, 680), fill=(62, 54, 51), width=12)

    elif kind == "kitchen_morning":
        img = gradient((1920, 1080), (239, 203, 151), (226, 231, 215))
        d = ImageDraw.Draw(img, "RGBA")
        d.ellipse((1420, -90, 1760, 250), fill=(255, 232, 152, 120))
        d.rectangle((0, 690, 1920, 1080), fill=(193, 154, 121, 255))
        d.rectangle((165, 240, 630, 610), fill=(116, 147, 151, 255))
        d.rectangle((205, 280, 590, 570), fill=(225, 241, 236, 255))
        d.rectangle((770, 320, 1510, 610), fill=(230, 219, 199, 255))
        for x in range(800, 1450, 160):
            d.rectangle((x, 350, x + 105, 505), fill=(186, 139, 98, 255))
        d.rectangle((705, 610, 1580, 750), fill=(116, 82, 67, 255))
        d.rectangle((760, 750, 1540, 930), fill=(94, 64, 55, 255))

    elif kind == "phone_screen":
        img = gradient((1920, 1080), (20, 25, 36), (9, 11, 17))
        d = ImageDraw.Draw(img, "RGBA")
        d.rounded_rectangle((690, 90, 1230, 1010), radius=65, fill=(16, 20, 28, 255), outline=(78, 89, 105, 255), width=8)
        d.rounded_rectangle((730, 145, 1190, 955), radius=42, fill=(226, 238, 235, 255))
        d.rectangle((730, 145, 1190, 305), fill=(50, 84, 93, 255))
        d.text((775, 190), "Messages", fill=(245, 247, 240), font=font(50, True))
        for i, (name, msg, color) in enumerate([
            ("Mom", "Are you home?", (229, 113, 89)),
            ("Casey", "We need to talk.", (69, 139, 176)),
            ("Unknown", "You saw it too.", (92, 75, 141)),
        ]):
            y = 345 + i * 165
            d.rounded_rectangle((775, y, 1145, y + 116), radius=26, fill=(255, 255, 255, 255), outline=(211, 220, 218, 255), width=3)
            d.ellipse((805, y + 27, 865, y + 87), fill=color + (255,))
            d.text((890, y + 25), name, fill=(35, 41, 48), font=font(32, True))
            d.text((890, y + 65), msg, fill=(82, 91, 96), font=font(24))

    else:
        img = gradient((1920, 1080), (39, 31, 50), (10, 11, 18))
        d = ImageDraw.Draw(img, "RGBA")
        d.polygon([(0, 1080), (1920, 1080), (1450, 520), (470, 520)], fill=(30, 30, 39, 255))
        d.rectangle((620, 265, 1300, 640), fill=(48, 42, 59, 255))
        d.rectangle((680, 325, 1240, 580), fill=(26, 29, 42, 255))
        d.text((760, 420), "Unknown Location", fill=(219, 204, 184), font=font(58, True))

    img = add_noise(img, 8)
    out = GAME / "images" / "bg" / path
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)


def character(path: str, name: str, gender: str, emotion: str, palette: tuple[tuple[int, int, int], tuple[int, int, int]]) -> None:
    img = Image.new("RGBA", (720, 1080), (0, 0, 0, 0))
    d = ImageDraw.Draw(img, "RGBA")
    hair, clothes = palette
    skin = (174, 119, 87) if gender == "male" else (192, 134, 101)
    if name == "jordan":
        skin = (139, 96, 75)
    if name == "riley":
        skin = (210, 151, 105)

    d.ellipse((250, 115, 470, 355), fill=hair + (255,))
    d.rounded_rectangle((285, 250, 435, 430), radius=72, fill=skin + (255,))
    d.pieslice((240, 80, 480, 320), 180, 360, fill=hair + (255,))
    d.rectangle((310, 405, 410, 510), fill=skin + (255,))
    d.rounded_rectangle((150, 485, 570, 1010), radius=92, fill=clothes + (255,))
    d.polygon([(150, 620), (20, 985), (185, 1010)], fill=clothes + (230,))
    d.polygon([(570, 620), (700, 985), (535, 1010)], fill=clothes + (230,))
    d.polygon([(255, 505), (360, 690), (465, 505)], fill=(232, 224, 209, 255))

    eye_y = 285
    brow_y = 252
    mouth_y = 365
    d.ellipse((300, eye_y, 322, eye_y + 18), fill=(32, 37, 42, 255))
    d.ellipse((398, eye_y, 420, eye_y + 18), fill=(32, 37, 42, 255))
    if emotion in {"angry", "frustrated", "serious", "suspicious"}:
        d.line((290, brow_y + 8, 330, brow_y), fill=(35, 32, 30, 255), width=6)
        d.line((390, brow_y, 430, brow_y + 8), fill=(35, 32, 30, 255), width=6)
    else:
        d.arc((288, brow_y - 6, 332, brow_y + 22), 200, 340, fill=(35, 32, 30, 255), width=5)
        d.arc((388, brow_y - 6, 432, brow_y + 22), 200, 340, fill=(35, 32, 30, 255), width=5)

    if emotion in {"happy", "relieved"}:
        d.arc((315, mouth_y - 16, 405, mouth_y + 42), 15, 165, fill=(87, 39, 45, 255), width=7)
    elif emotion in {"sad", "worried"}:
        d.arc((318, mouth_y, 402, mouth_y + 58), 200, 340, fill=(87, 39, 45, 255), width=7)
    elif emotion == "angry":
        d.line((320, mouth_y + 22, 400, mouth_y + 10), fill=(87, 39, 45, 255), width=7)
    elif emotion == "listening":
        d.ellipse((346, mouth_y + 5, 374, mouth_y + 28), outline=(87, 39, 45, 255), width=5)
    else:
        d.line((326, mouth_y + 18, 394, mouth_y + 18), fill=(87, 39, 45, 255), width=6)

    img = img.filter(ImageFilter.SMOOTH_MORE)
    out = GAME / "images" / "characters" / path
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)


def write_wav(path: Path, seconds: float, builder, rate: int = 44100) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    n = int(seconds * rate)
    with wave.open(str(path), "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(rate)
        frames = bytearray()
        for i in range(n):
            t = i / rate
            amp = max(-1.0, min(1.0, builder(t, i / n)))
            frames += int(amp * 32767).to_bytes(2, "little", signed=True)
        f.writeframes(frames)


def generate_audio() -> None:
    random.seed(4)
    write_wav(
        GAME / "audio" / "music" / "ambient_city.wav",
        24,
        lambda t, p: 0.16 * math.sin(2 * math.pi * 146.83 * t)
        + 0.08 * math.sin(2 * math.pi * 220.00 * t)
        + 0.035 * math.sin(2 * math.pi * 329.63 * t)
        + 0.018 * math.sin(2 * math.pi * 0.21 * t),
    )
    write_wav(
        GAME / "audio" / "music" / "tension_rising.wav",
        18,
        lambda t, p: (0.08 + p * 0.12) * math.sin(2 * math.pi * (92 + p * 72) * t)
        + 0.05 * math.sin(2 * math.pi * 185 * t)
        + 0.025 * math.sin(2 * math.pi * 370 * t),
    )
    write_wav(
        GAME / "audio" / "sfx" / "cafe_ambience.wav",
        18,
        lambda t, p: 0.035 * math.sin(2 * math.pi * 90 * t)
        + 0.025 * math.sin(2 * math.pi * 235 * t)
        + 0.02 * math.sin(2 * math.pi * 0.73 * t),
    )
    write_wav(
        GAME / "audio" / "sfx" / "phone_buzz.wav",
        0.7,
        lambda t, p: (0.45 if int(t * 35) % 2 == 0 else 0.12) * math.sin(2 * math.pi * 155 * t) * (1 - p),
    )
    write_wav(
        GAME / "audio" / "sfx" / "phone_unlock.wav",
        0.55,
        lambda t, p: 0.38 * math.sin(2 * math.pi * (660 + 420 * p) * t) * (1 - p),
    )
    write_wav(
        GAME / "audio" / "sfx" / "chair_scrape.wav",
        0.9,
        lambda t, p: 0.22 * math.sin(2 * math.pi * (90 + 40 * math.sin(30 * t)) * t) * (1 - p * 0.4),
    )


def generate_presplash() -> None:
    if not WEB.exists():
        return
    img = gradient((1920, 1080), (8, 18, 33), (10, 11, 18))
    img = draw_multiverse_background(img, title=True)
    img.save(WEB / "web-presplash.jpg", quality=92)


def main() -> None:
    for kind in [
        "campus_day",
        "library_steps_evening",
        "cafe",
        "rooftop_night",
        "dean_office",
        "room_night",
        "kitchen_morning",
        "phone_screen",
        "unknown_location",
    ]:
        background(f"{kind}.png", kind)

    palettes = {
        "jordan": ((38, 32, 30), (55, 88, 111)),
        "casey_female": ((63, 39, 51), (129, 69, 92)),
        "casey_male": ((54, 39, 31), (88, 93, 128)),
        "morgan": ((74, 51, 40), (75, 104, 137)),
        "anchor": ((34, 39, 52), (62, 129, 131)),
        "parent": ((55, 43, 34), (116, 82, 67)),
        "riley_female": ((43, 38, 52), (78, 118, 88)),
        "riley_male": ((38, 35, 31), (129, 93, 58)),
    }
    emotions = ["angry", "frustrated", "happy", "listening", "neutral", "sad", "serious", "suspicious", "worried"]
    for folder, palette in palettes.items():
        name, gender = folder.split("_", 1) if "_" in folder else (folder, "male")
        for emotion in emotions:
            character(f"{folder}/{emotion}.png", name, gender, emotion, palette)

    generate_audio()
    generate_main_menu()
    generate_presplash()


if __name__ == "__main__":
    main()
