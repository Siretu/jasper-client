# -*- coding: utf-8-*-
import random
import re
import os

WORDS = ["VOLUME", "TURN", "UP", "THE", "SET", "MAX", "DOWN", "TO", "FULL", "MUTE"]


def handle(text, mic, profile, data=None):
    """
        Responds to user-input, typically speech text.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    print "In volume"
    volume = 10
    relative = ""
    if "number" in data["outcomes"][0]["entities"]:
        print "Changing absolute volume"
        volume = data["outcomes"][0]["entities"]["number"][0]["value"]
    elif "volume_relative" in data["outcomes"][0]["entities"]:
        print "Changing relative volume"
        value = data["outcomes"][0]["entities"]["volume_relative"][0]["value"]
        if value == "up":
            relative = "+"
        elif value == "down":
            relative = "-"
        elif value == "max":
            volume = 100
        elif value == "mute":
            volume = 0
    mic.say("Changing volume")
    cmd = "amixer set Master {0}%{1}".format(volume,relative)
    os.system(cmd)


def isValid(text):
    """
        Returns True if the input is related to the volume

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return "volume" in text.lower()
