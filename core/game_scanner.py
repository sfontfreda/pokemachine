from pathlib import Path
import config

def get_roms(): 
  roms_list = []
  for system, path in config.ROM_PATHS.items():
      for child in Path(path).iterdir(): 
        if child.suffix in config.ROM_EXTENSIONS[system]:
          roms_list.append({"name" : child.stem, "system" : system, "path" : child})
  return roms_list
      
get_roms()