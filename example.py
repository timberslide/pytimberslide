"""
This is an example of how to use the Timberslide Python API
"""
import sys
import time

from pytimberslide import Timberslide


TOKEN = b"TqPeDFG30Fz147NeCB59SUgT"
TOPIC = "kris/pytesting"


def main():
    # Create a client and connect to Timberslide
    ts = Timberslide(TOKEN)
    ts.connect()

    # Send a few messages into our topic
    ts.send(TOPIC, "Hello from the example")
    ts.send(TOPIC, "This is line 2")
    ts.send(TOPIC, "And a final line for good measure")

    # Get those message from Timberside and print them
    for message in ts.get_topic(TOPIC):
        print("Received from Timberslide: {}".format(message))


if __name__ == "__main__":
    if sys.version_info[0] < 3:
        sys.stderr.write("WARNING: running under python 2.x, ctrl-c does not work, use ctrl-\\\n")
    main()
