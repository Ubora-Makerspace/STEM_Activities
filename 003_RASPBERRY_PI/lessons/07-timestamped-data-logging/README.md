# Session 7: Timestamped data logging

Until now the Pi has shown you numbers and forgotten them. Today it starts keeping a record. A number on its own tells you little, but a number with a **time** attached lets you ask questions: when was something close, how fast did it move, how noisy is this sensor?

You will add a timestamp and column headings to each saved reading, collect three short data samples, turn one into a graph, and write one honest sentence about what the data shows.

## What you need

- The Pi with your robot connected and the tests passing (Sessions 5 and 6)
- A laptop with a spreadsheet program (Excel, LibreOffice Calc or Google Sheets)
- Some objects to measure: a flat book, a cushion or jumper, and your hand
- A tape measure or ruler

> **Roles today:** Driver, Reviewer, Troubleshooter. The Reviewer also keeps the **lab notebook**: what was in front of the sensor for each sample.

---

## Part 0: What makes a good record

A CSV (comma-separated values) file is just text, with one row per reading. Any spreadsheet can open it:

```
timestamp,distance_cm
2026-10-20T10:15:01.204,42.6
2026-10-20T10:15:01.305,42.5
```

Good logs follow three rules:

- **Headings.** The first row names each column.
- **Timestamps.** Every row says *when*, in a format a computer can sort (ISO 8601: year first, then month, day, time).
- **Only valid data.** Bad lines are counted and reported, but never written as if they were readings.

---

## Part 1: Add timestamps and headings

Replace `pi/csv_writer.py` with this version, which writes the header once and stamps each row:

```python
"""Save validated readings to a CSV file with a timestamp."""

import csv
from datetime import datetime
from pathlib import Path

HEADER = ["timestamp", "distance_cm"]


def append_reading(path, distance_cm):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    is_new_file = not path.exists()
    with path.open("a", newline="") as file:
        writer = csv.writer(file)
        if is_new_file:
            writer.writerow(HEADER)
        stamp = datetime.now().isoformat(timespec="milliseconds")
        writer.writerow([stamp, f"{distance_cm:.1f}"])
```

Then replace `pi/main.py`. It now reads from the real serial port, validates each line, saves the good ones, and counts the rest:

```python
"""The connected ultrasonic monitor: read, validate, save.

Run from the project folder:   python pi/main.py [optional/output.csv]
"""

import sys

from config import SERIAL_PORT, BAUD_RATE, RECONNECT_DELAY_S, CSV_PATH
from csv_writer import append_reading
from serial_reader import read_lines
from validator import parse_message, InvalidMessage


def main():
    csv_path = sys.argv[1] if len(sys.argv) > 1 else CSV_PATH
    saved = 0
    rejected = 0
    print(f"Logging to {csv_path}. Press Ctrl+C to stop.")

    try:
        for line in read_lines(SERIAL_PORT, BAUD_RATE, RECONNECT_DELAY_S):
            try:
                distance = parse_message(line)
            except InvalidMessage as error:
                rejected += 1
                print(f"Rejected: {error}")
                continue

            append_reading(csv_path, distance)
            saved += 1
            if saved % 10 == 0:
                print(f"{saved} readings saved, {rejected} rejected")
    except KeyboardInterrupt:
        print(f"\nStopped. {saved} readings saved, {rejected} rejected.")


if __name__ == "__main__":
    main()
```

The program takes an optional output file name so you can keep samples separate:

```
python pi/main.py data/sample1.csv
```

Check the file:

```
head -5 data/sample1.csv
```

---

## Part 2: Collect three short samples

Run each sample for about **30 seconds**, then press `Ctrl+C`. The Reviewer writes down what was in front of the sensor.

| Sample | File | What to do |
| --- | --- | --- |
| 1: Moving | `data/sample1.csv` | Slowly move a flat book towards the sensor and then away |
| 2: Still | `data/sample2.csv` | Hold a flat book still, 30 cm from the sensor (measure it with a ruler) |
| 3: Challenging | `data/sample3.csv` | Point the sensor at a cushion or jumper, or at an open space |

```
python pi/main.py data/sample1.csv
python pi/main.py data/sample2.csv
python pi/main.py data/sample3.csv
```

**Check that invalid lines were not saved as valid ones.** Upload the simulator with `FAULT_MODE = 1` (see Session 6), run the logger for 10 seconds into a test file, and compare:

```
python pi/main.py data/fault_test.csv      # Ctrl+C after about 10 s
wc -l data/fault_test.csv                   # lines in the file, including the header
grep -c "@" data/fault_test.csv             # should print 0
```

The program told you how many it rejected. The number of rows (minus the header) plus the number rejected should add up to the lines the Arduino sent. Delete `fault_test.csv` afterwards and put `FAULT_MODE` back to 0.

**Swap roles.**

---

## Part 3: Make one graph

The easiest route is a spreadsheet on your laptop.

1. Copy a sample from the Pi to your laptop. Run this **on your laptop**, not on the Pi:

   ```
   scp pi@pair1-pi.local:~/project/data/sample1.csv .
   ```
2. Open `sample1.csv` in a spreadsheet.
3. Select both columns, insert a **line chart** (or scatter with lines), and give it a title and axis labels: *Time* and *Distance (cm)*.
4. Save the chart as an image into your project's `docs/` folder.

**Option: draw it with Python.** This script makes a PNG. It needs `matplotlib`, which is heavy on a Pi Zero, so it is easiest to run on your laptop in a venv of its own:

```python
"""Draw distance over time from a CSV file (easiest on a laptop).

Usage:  python pi/plot_readings.py data/sample1.csv [output.png]
Needs:  pip install matplotlib
"""

import csv
import sys
from datetime import datetime

import matplotlib
matplotlib.use("Agg")                      # draw to a file, no screen needed
import matplotlib.pyplot as plt


def main():
    path = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else path.replace(".csv", ".png")

    times, values = [], []
    with open(path, newline="") as file:
        for row in csv.DictReader(file):
            times.append(datetime.fromisoformat(row["timestamp"]))
            values.append(float(row["distance_cm"]))

    figure, axis = plt.subplots(figsize=(8, 4))
    axis.plot(times, values)
    axis.set_xlabel("Time")
    axis.set_ylabel("Distance (cm)")
    axis.set_title(path)
    figure.autofmt_xdate()
    figure.tight_layout()
    figure.savefig(output, dpi=120)
    print("Saved", output)


if __name__ == "__main__":
    main()
```

```
pip install matplotlib
python pi/plot_readings.py sample1.csv
```

---

## Part 4: Say something true about the data

Compare the three samples. Then write **one sentence** about a pattern or a limitation. A good sentence is specific and measurable. Some examples:

- "With the book held still at 30 cm, the readings varied between 29.8 and 30.4 cm, about ± 0.3 cm."
- "The cushion sample had many gaps, because soft surfaces absorb the sound."
- "In sample 1 the distance changes in a repeating wave. This matches the servo sweep (the sensor looks at different things as it turns)."

Hint: if the sensor is mounted on the servo, part of what you are graphing is the *sweep*, not the world.

Put your sentence in `docs/observations.md`, with the sample file names and the graph. Commit the notes and the graph (the data files stay out of Git on purpose):

```
git switch -c feature/data-logging
git add pi/csv_writer.py pi/main.py docs/
git commit -m "Log timestamped readings and add first observations"
git push -u origin feature/data-logging
```

Open a pull request and have your partner review it, as in Session 3.

---

## Session output

- [ ] A readable CSV with a header, a timestamp and a distance on every row
- [ ] Three samples collected, with notes on what was in front of the sensor
- [ ] Rejected lines were counted and were not saved as readings
- [ ] One graph of distance over time is in `docs/`
- [ ] One specific sentence about a pattern or limitation

---

## Troubleshooting

- **`data/` does not exist:** `csv_writer.py` creates it. If you see a permission error, check you are running from the project folder.
- **The header appears twice:** you appended to an old file that already had the header from a different version of the program. Delete the file and start again.
- **The CSV has gaps in the timestamps:** the sensor returned no echo (soft or angled surface). Not a bug.
- **Spreadsheet puts everything in one column:** use *Data > Text to Columns* (or Import) and choose comma as the separator.
- **`scp` says `No such file or directory`:** check the path. In the Pi terminal, `pwd` inside the project folder tells you the full path.
- **The Pi seems slow when saving:** at 10 lines a second it should be fine. Close any other programs.
- **The graph looks like a saw:** that is the servo sweeping. Compare the period of the wave with the sweep time.

> **Challenge:** Add a third column to the CSV with the **angle** of the servo. You will need to change the Arduino sketch (and the message format, for example `DIST,42.6,90`) *and* the parser and tests. Do it on a branch and keep the tests green.

---

## Checkpoint

Show a readable CSV, one graph, and your observation to another pair. Can they understand it without your help?

## Where to go next

Your data and your code work. **Session 8** hands the project to another pair to see whether it works for someone who isn't you.

## Further reading

- [Python csv module](https://docs.python.org/3/library/csv.html)
- [Python datetime: isoformat](https://docs.python.org/3/library/datetime.html)
- [scp basics (Raspberry Pi docs)](https://www.raspberrypi.com/documentation/computers/remote-access.html)
