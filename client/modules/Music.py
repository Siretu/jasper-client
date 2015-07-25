# -*- coding: utf-8-*-
import random
import re
import telnetlib

WORDS = ["TURN", "OFF", "MUSIC","STOP","THE","GIVE","ME","SOME"]


def handle(text, mic, profile, data=None):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    print "In music"
    tn = telnetlib.Telnet("localhost",6602)
    if "OFF" in text or "STOP" in text or "OF" in text:
        tn.write("stop\n")
    else:
        print "Starting playlist"
        tn.write("play 2\n")
    


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return "music" in text.lower()
