# -*- coding: utf-8-*-
import socket

WORDS = ["TURN", "ON", "THE", "LIGHTS", "LIGHT", "OFF", "DEFAULT", "SET", "TO"]


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
    print "Handling lights"
    text = text.lower()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost",5432))
    print "Socket connected"
    #status = sock.recv(1024)
    #print "Got status: " + status
    if "default" in text:
        sock.send("default")
    else:
        print "Sending message"
        if "on" in text:
            mic.say("On")
            sock.send("on")
        elif "off" in text:
            mic.say("Off")
            sock.send("off")
        print "Sent message"


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return "light" in text.lower()
