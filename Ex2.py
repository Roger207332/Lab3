import os


def cutout(input, n, str):
    if str == 'start':
        cmd = 'ffmpeg -i {} -ss 00:00:00 -t {} -async 1 1min.mp4'.format(input, n)
        os.system(cmd)
    elif str == 'end':
        cmd = 'ffmpeg -i {} -ss {} -t 00:10:34 -async 1 1min.mp4'.format(input, n)
        os.system(cmd)
    else:
        print("incorrect word")


def ex2(input):
    cmd = 'ffmpeg -i {} -c:a copy output_acc.aac'.format(input)
    os.system(cmd)
    cmd = 'ffmpeg -i {} -async 1 1min2.mp3'.format(input)
    os.system(cmd)
    cmd = 'ffmpeg -i 1min.mp4 -i 1min.mp3 -i output2.aac -map 0:v -map 1:a -map 2:a -codec copy final.mp4'
    os.system(cmd)
