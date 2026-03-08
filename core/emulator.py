import subprocess

def launch(rom):
  print(f"LAUNCHING {rom['name']} ({rom['system']})")
  """
  if rom["system"] in ["gb", "gba", "gbc"]:
    subprocess.run(["mgba", rom["path"]])
  else:
    subprocess.run(["dolphin", rom["path"]])
  """