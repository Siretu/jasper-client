# -*- coding: utf-8-*-
import random
import re
import telnetlib

WORDS = ["TURN", "OFF", "MUSIC","STOP","THE"]


def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    tn = telnetlib.Telnet("localhost",6602)
    tn.write("stop\n")



def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return "music" in text.lower()
