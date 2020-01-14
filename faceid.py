#!/usr/bin/env python3
import sys
import signal

from src.controller.Controller import main


def signal_handler(signal, frame):
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
