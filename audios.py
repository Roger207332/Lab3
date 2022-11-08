import os
import subprocess


def tracks(input):
    output = subprocess.check_output("ffprobe -i {} 2>&1 | grep 'Stream.*Audio'".format(input), shell=True)
    list = output.split()
    count = 0
    for i in list:
        if i == b'Audio:':
            count = count + 1
    print('The are {} audio channels in the video {}. In the following lines you can check its info:'.format(count,
                                                                                                             input))
    cmd = "ffprobe -i {} 2>&1 | grep 'Stream.*Audio'".format(input)
    os.system(cmd)
