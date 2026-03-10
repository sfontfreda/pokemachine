import shutil
from pathlib import Path
import config

def save(rom):
    src = rom["path"].with_suffix(".sav")
    dest = Path(config.SAVES_PATH) / rom["system"] / src.name
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(src, dest)

def load(rom):
    src = Path(config.SAVES_PATH) / rom["system"] / rom["path"].with_suffix(".sav").name
    dest = rom["path"].with_suffix(".sav")
    shutil.copy(src, dest)