import subprocess

subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", "50%"], check=True)