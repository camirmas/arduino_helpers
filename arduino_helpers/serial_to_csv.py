"""
This script will read serial data from an Arduino, convert
to a float, and write to a CSV.
"""
import serial
import csv
import time
import argparse
from signal import signal, SIGINT


def handler(sig_recv, _):
    print("\nExiting...")
    exit(0)


def run():
    parser = argparse.ArgumentParser(
        description="Write Arduino serial data to CSV.")
    parser.add_argument(
        '-p', '--port', default="/dev/ttyACM0", required=False)

    args = parser.parse_args()

    timestr = time.strftime("%Y%m%d-%H%M%S")
    output_file = "data_%s.csv" % timestr

    wire = serial.Serial(args.port, 9600)
    wire.flushInput()
    wire.timeout = 30

    with open(output_file, 'w') as csvfile:
        writer = csv.writer(csvfile)

        while True:
            strn = wire.readline()

            try:
                value = float(strn)

                print(value)

                writer.writerow([value])
            except Exception as e:
                print(e)


if __name__ == "__main__":
    signal(SIGINT, handler)

    print("Running. Press CTRL-C to exit.")

    run()
