import os
import subprocess


# We implement subprocess to keep the information for the script, and we also print it in the terminal.
def parse(input):
    output = subprocess.check_output('ffmpeg -i {} '.format(input), shell=True)
    print(output)
    cmd = 'ffmpeg -i {} '.format(input)
    os.system(cmd)
