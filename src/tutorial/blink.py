#!/usr/bin env python3

"""
Blinks an LED light of an Arduino UNO
"""

import time
import pyfirmata


def main():
    """Entry Point"""

    board = pyfirmata.Arduino('/dev/cu.usbmodem14101')

    while True:
        board.digital[13].write(1)
        time.sleep(1)
        board.digital[13].write(0)
        time.sleep(1)


if __name__ == "__main__":
    main()
