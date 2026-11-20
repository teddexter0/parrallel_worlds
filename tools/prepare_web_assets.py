from pathlib import Path
import math
import random
import shutil
import struct
import wave
from zipfile import ZipFile

from PIL import Image

import generate_placeholder_assets

ROOT = Path(__file__).resolve().parents[1]
game = ROOT / "Parallel Worlds" / "game"
BASE_ARCHIVE = ROOT / "ParallelWorlds-1.0.0-dists/ParallelWorlds-1.0.0-web/game.zip"


def preserve_script_ids():
    with ZipFile(BASE_ARCHIVE) as previous:
        for source in game.glob("*.rpy"):
            filename = "game/" + source.with_suffix(".rpyc").name
            if filename in previous.namelist():
                source.with_suffix(".rpyc").write_bytes(previous.read(filename))


def render(file_name, seconds, seed, signal):
    sample_rate = 22050
    samples = bytearray()
    rng = random.Random(seed)
    slower, faster = 0.0, 0.0
    for index in range(int(seconds * sample_rate)):
        time = index / sample_rate
        white = rng.uniform(-1, 1)
        slower += 0.025 * (white - slower)
        faster += 0.15 * (white - faster)
        sample = signal(time, slower, faster)
        edge = min(1.0, time / 0.1, (seconds - time) / 0.1)
        samples.extend(struct.pack("<h", int(max(-1, min(1, sample * edge)) * 32767)))

    with wave.open(str(game / "audio" / file_name), "wb") as audio:
        audio.setparams((1, 2, sample_rate, 0, "NONE", "not compressed"))
        audio.writeframes(samples)


def tone(frequency, time):
    return math.sin(math.tau * frequency * time)


def city(time, low, high):
    passing_traffic = sum(math.exp(-((time - moment) / 1.7) ** 2) for moment in (4.3, 12.9, 20.7, 29.4))
    air = 0.10 * high + 0.20 * low
    distant_road = passing_traffic * (0.20 * low + 0.023 * tone(54, time))
    return air + distant_road


def tension(time, low, high):
    pulse = (time % 1.6) / 1.6
    heartbeat = 0.095 * tone(56, time) * (math.exp(-13 * pulse) + 0.4 * math.exp(-((pulse - 0.20) / 0.05) ** 2))
    bass = 0.045 * tone(73.42, time) * (0.7 + 0.3 * tone(0.17, time))
    cue_time = time % 3.2
    key = (146.83, 164.81, 130.81, 138.59)[int(time / 3.2) % 4]
    piano = 0.055 * (tone(key, cue_time) + 0.3 * tone(key * 2, cue_time)) * math.exp(-1.8 * cue_time) * min(1, cue_time * 90)
    return heartbeat + bass + piano + 0.045 * low


def cafe(time, low, high):
    murmur = sum(
        (0.5 + 0.5 * tone(rate, time + offset)) ** 2 * tone(pitch + 7 * tone(rate, time), time)
        for rate, offset, pitch in ((0.58, 0.1, 106), (0.79, 1.5, 123), (1.08, 2.1, 157), (0.91, 4.2, 184))
    )
    cup = sum(0.07 * math.exp(-35 * (time - hit)) * tone(1550, time - hit) for hit in (2.2, 6.1, 6.27, 10.84, 16.4, 21.3) if time >= hit and time - hit < 0.5)
    return 0.023 * murmur + 0.32 * low + 0.07 * high + cup



def main():
    generate_placeholder_assets.main()
    cover = game / "gui/cover.jpg"
    with Image.open(cover) as image:
        image.save(game / "gui/main_menu.png", optimize=True)
    shutil.copyfile(cover, game.parent / "web-presplash.jpg")
    render("music/ambient_city.wav", 32, 21, city)
    render("music/tension_rising.wav", 25.6, 29, tension)
    render("sfx/cafe_ambience.wav", 24, 31, cafe)
    preserve_script_ids()


if __name__ == "__main__":
    main()
