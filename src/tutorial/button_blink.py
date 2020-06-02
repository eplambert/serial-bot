#!/usr/bin env python3

"""
Pushing a button turns on an LED light
"""

import pyfirmata


def main():
    """Entry Point"""

    board = pyfirmata.Arduino('/dev/cu.usbmodem14101')

    while True:

        if board.digital[7] == "HIGH":
            board.digital[13].write(1)
        else:
            board.digital[13].write(0)


if __name__ == "__main__":
    main()