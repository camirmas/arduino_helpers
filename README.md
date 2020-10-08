#  :robot: Arduino Helpers
> Helper scripts for working with Arduino

### Setup

1. Install [Python](https://www.python.org/)
2. Download or clone this repository
3. From inside the `arduino_helpers` directory, run the setup script:
```bash
. setup.sh
```

### Serial to CSV

This feature reads serial data (numbers, or, more specifically, anything that can be resolved to Python's `float` type and outputs it to a CSV file with two columns, one with  timestamps, and the other with the processed serial data. The CSV filename format is `data_[timestamp].csv`.

Make sure that you have your Arduino connected to your computer and running a script that outputs serial data. Here's a very simple example:

```c
int i = 0;

setup()
{
  Serial.begin(9600);
}

loop()
{
  Serial.println(i);
  i++;
}
```

To run the script (after completing **Setup** steps 1-3):
```bash
python arduino_helpers/serial_to_csv.py
```

By default, the port that the script uses is `/dev/ttyACM0`. If your Arduino communicates from a different port, you can specify it:
```
python arduino_helpers/serial_to_csv.py --port "path/to/port"
```
_Note: If you're not sure what your port is, from the Arduino IDE see Tools -> Port._

If everything is working properly, you should see the following message, followed by your printed serial data:
```
Running. Press CTRL-C to exit.
1.0
2.0
3.0
4.0
5.0
```
