from enum import Enum


class PlaybackStatus(Enum):
    Playing = 'Playing'
    Stopped = 'Stopped'
    Paused = 'Paused'


class ShuffleMode(Enum):
    Off = 'off'
    Songs = 'songs'
