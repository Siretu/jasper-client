# -*- coding: utf-8-*-
import socket

WORDS = ["TURN", "ON", "THE", "LIGHTS", "LIGHT", "OFF", "DEFAULT", "SET", "TO"]


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
    text = text.lower()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost",5432))
    status = sock.recv(1024)
    print "Got status: " + status
    if "default" in text:
        sock.send("default")
    else:
        if "on" in text and status == b"False":
            sock.send("on")
        elif "off" in text and status == b"True":
            sock.send("off")


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return "light" in text.lower()
