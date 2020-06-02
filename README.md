# serial-bot

This project is meant to be a repo of beginner code that uses a serial
connection to power an Arduino Uno development board.

## Setup
First need to download the Arduino IDE which contains example code. To
install the Arduino IDE on a Mac use brew.
use brew.
```bash
brew cask install arduino 
```
Be sure to download python. You can use conda if you'd like. The code
uses pyfirmata to to execute serial commands. 
```bash
pip install pyfirmata
```
Once software is installed you need to upload `StandardFormata` from
the Arduino IDE Examples.

## How to run code
Once your environment is setup you run the code on your Arduino exactly
how you'd run python from the command line.
```bash
python blink.py
```
