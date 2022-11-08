from parse import *
from Ex2 import *
from parse import *
from resize import *
from audios import *
from clas import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Exercise 1: We compute the information from the audio input
    input = 'BBB.mp4'
    parse(input)

    # Exercise 2: We use the function that we created in lab2 to cut the video.
    input = 'BigBuckBunny.mp4'
    n = '00:01:00'
    str = 'start'
    cutout(input, n, str)
    # Then, we change the input to the new 1min video, and we call the ex2 function, where we extract the acc and mp3
    # audio formats, and we pack them with the video in the final outcome final.mp4.
    input = '1min.mp4'
    ex2(input)

    # Exercise 3: We use the 1min video, and we resize it to multiple different resolutions.
    input = '1min.mp4'
    size = '1280x720'
    resize(input, size, size)
    size = '640x480'
    resize(input, size, size)
    size = '360x240'
    resize(input, size, size)
    size = '160x120'
    resize(input, size, size)
    size = '2560x1440'
    resize(input, size, size)

    # Exercise 4: We get the audios information of the video that we introduce
    input = 'final2.mp4'
    tracks(input)

    # Exercise 5: We have created the class with the path and size atributes. Then we have created a method to resize
    # the video and another one to print the information reference to the clas instance.
    input = '1min.mp4'
    size = '1280x720'
    v1 = Video(input, size)
    size = '160x120'
    v1.resize(size)
    print(v1)
