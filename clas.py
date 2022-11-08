import os
from resize import *


class Video:
    def __init__(self, path, resolution):
        self.path = path
        self.resolution = resolution

    def resize(self, resolution):
        resize(self.path, resolution, resolution)
        self.resolution = resolution

    def __str__(self):
        return f"You've created a Video instance with name {self.path} and resolution {self.resolution}"
