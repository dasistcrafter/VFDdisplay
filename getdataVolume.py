import subprocess
import re


def getCurrentVolume(volume):
    result = subprocess.run(
        ["pactl", "get-sink-volume", "@DEFAULT_SINK@"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True
    )
    #get only the precetage 
    match = re.search(r'(\d+)%', result.stdout)
    if match:
        volume = int(match.group(1))
    return int(volume)
    
        

