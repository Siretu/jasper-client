# -*- coding: utf-8-*-
import random
import re
import telnetlib
import socket

WORDS = ["SET", "THE", "MOOD"]


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
    tn.write("play 3\n")
    mic.say("Welcome back Jessie")
    #mic.say("Setting the mood")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost",5432))
    status = sock.recv(1024)

    sock.send("mood")



def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return "mood" in text.lower()
