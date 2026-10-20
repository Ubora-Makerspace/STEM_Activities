# Session 2: Python project structure and environment

Last session your Pi ran one small script. A real project does several jobs, and if they all live in one long file, a bug in one job is hard to find and harder to fix. Today you will do what a good kitchen does: give every job its own station. You will also give the project its own **virtual environment**, so the libraries it needs live in the project and nowhere else.

Nothing today needs the Arduino. The program reads pretend lines, so you can test everything on its own.

## What you need

- The Pi, logged in over SSH, with your project cloned (Session 1)
- An internet connection for the Pi (to install two Python libraries)
- Your README with the Session 1 instructions

> **Roles today:** Driver, Reviewer, Troubleshooter. Swap at every **Swap roles** marker.

---

## Part 0: One job per module (10 minutes)

Our project does three separate jobs:

```
read a line  -->  check the line  -->  save the number
(serial_reader)   (validator)         (csv_writer)
```

Each job becomes a **module**, which is a Python file with a clear name. A fourth file, `main.py`, simply connects them. A fifth, `config.py`, holds the settings, so no number is buried in the middle of some other file.

```
pi/
  config.py          settings (port, baud rate, limits, file name)
  serial_reader.py   gets lines of text
  validator.py       turns a line into a trustworthy number
  csv_writer.py      saves numbers to a file
  main.py            connects the three
```

Why bother? You can test the checker without any hardware, replace the reader without touching the checker, and a partner can read one small file instead of one huge one.

---

## Part 1: A virtual environment

### What is it and why?

Python programs use **libraries** written by other people. If every project installs into the same place, one project's needs can break another's. A **virtual environment** (venv) is a private folder of libraries that belongs to one project.

Modern Raspberry Pi OS also *refuses* to install Python libraries system-wide. You will see an `externally-managed-environment` error if you try. A venv is the correct answer, not a workaround.

### Create and use one

From the project folder (`cd ~/project`):

```
python3 -m venv .venv
source .venv/bin/activate
```

Your prompt now starts with `(.venv)`. That is how you know it is active. Check:

```
which python
```

It should point inside `.venv`. Inside a venv the command `python` is correct. Outside, you use `python3`.

### Install only what the project needs

Create a file called `requirements.txt`:

```
pyserial>=3.5
pytest>=7.0
```

Then install:

```
pip install -r requirements.txt
```

- **pyserial** lets Python read the USB serial port (Session 5).
- **pytest** runs our automatic tests (Session 3).

Make sure Git does not track the venv or data files. Create a `.gitignore` containing:

```
.venv/
__pycache__/
.pytest_cache/
*.pyc
data/
```

To leave the environment later, type `deactivate`. To come back, run `source .venv/bin/activate` again from the project folder.

**Swap roles.**

---

## Part 2: Split the starter program into modules

Create these files inside `pi/`. Use `nano pi/config.py` and so on.

### `config.py`: the settings

```python
"""Settings in one place, so nothing is hidden inside other files."""

SERIAL_PORT = "/dev/ttyACM0"     # check with: ls /dev/ttyACM* /dev/ttyUSB*
BAUD_RATE = 9600                 # must match Serial.begin() in the sketch
RECONNECT_DELAY_S = 2            # wait this long before trying the port again

MIN_DISTANCE_CM = 2.0            # HC-SR04 cannot measure closer than this
MAX_DISTANCE_CM = 400.0          # ...or farther than this

CSV_PATH = "data/readings.csv"
```

### `validator.py`: check one line

```python
"""Check one line of text from the Arduino and turn it into a number."""


class InvalidMessage(ValueError):
    """Raised when a line does not look like 'DIST,<number>'."""


def parse_message(line):
    """Return the distance in cm, or raise InvalidMessage with a clear reason."""
    text = line.strip()
    parts = text.split(",")
    if len(parts) != 2 or parts[0] != "DIST":
        raise InvalidMessage(f"Bad format: {text!r}")

    try:
        return float(parts[1])
    except ValueError:
        raise InvalidMessage(f"Not a number: {parts[1]!r}")


if __name__ == "__main__":
    for sample in ["DIST,42.6", "DIST,abc", "HELLO"]:
        try:
            print(sample, "->", parse_message(sample))
        except InvalidMessage as error:
            print(sample, "-> rejected:", error)
```

The block at the bottom only runs when you start this file directly. It is a quick self-test.

### `serial_reader.py`: a pretend source of lines (for now)

```python
"""Source of lines. Version 1 uses pretend data so no Arduino is needed."""


def read_lines():
    for line in ["DIST,42.6", "DIST,43.1", "DIST,abc", "DIST,44.0"]:
        yield line
```

In Session 5 you will replace the body with the real serial port, and nothing else will need to change.

### `csv_writer.py`: save a number

```python
"""Save readings to a CSV file."""

import csv
from pathlib import Path


def append_reading(path, distance_cm):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", newline="") as file:
        csv.writer(file).writerow([distance_cm])
```

### `main.py`: connect them

```python
"""Read, validate, save."""

from config import CSV_PATH
from csv_writer import append_reading
from serial_reader import read_lines
from validator import parse_message, InvalidMessage

for line in read_lines():
    try:
        distance = parse_message(line)
    except InvalidMessage as error:
        print("Rejected:", error)
        continue
    append_reading(CSV_PATH, distance)
    print("Saved:", distance)
```

### Run each piece

Always run from the **project folder**, not from inside `pi/`:

```
python pi/validator.py
python pi/main.py
cat data/readings.csv
```

You should see three numbers saved and one line rejected:

```
Saved: 42.6
Saved: 43.1
Rejected: Not a number: 'abc'
Saved: 44.0
```

Notice the error message says *what* was wrong and shows the bad text. A good message saves a lot of debugging time later.

**Swap roles.**

---

## Part 3: Write the setup so someone else can follow it

Add a section to the README:

```markdown
## Setting up the Python environment

From the project folder:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## Running the project

    python pi/main.py

Always run commands from the project folder with the environment active
(the prompt starts with `(.venv)`).
```

First save your work and send it to the shared repository:

```
git add .
git commit -m "Split project into modules and add venv instructions"
git push
```

Now **prove it works**. Your partner clones the repository into a *new* folder and follows only the README:

```
cd ~
git clone <repository-url> project-test
cd project-test
```

A fresh clone only contains what you have **committed and pushed**, so run `git push` from your project folder first. If they get stuck, the README is missing something. Fix it, then delete the test folder with `rm -r ~/project-test`.

---

## Session output

- [ ] The project runs from its documented virtual environment
- [ ] `config.py`, `validator.py`, `serial_reader.py`, `csv_writer.py` and `main.py` each do one job
- [ ] `requirements.txt` lists only `pyserial` and `pytest`
- [ ] `.venv/` and `data/` are ignored by Git
- [ ] A partner followed the README and ran the project without your help

---

## Troubleshooting

- **`error: externally-managed-environment`:** you ran `pip` without the venv. Run `source .venv/bin/activate` first.
- **`source: not found`:** you are in the wrong kind of shell. Use `bash`, or run `. .venv/bin/activate`.
- **`ModuleNotFoundError: No module named 'config'`:** run commands from the project folder using `python pi/main.py`, not from inside `pi/`.
- **`ModuleNotFoundError: No module named 'serial'`:** the venv is not active, or the install failed. Check for `(.venv)` in your prompt and re-run `pip install -r requirements.txt`.
- **`ensurepip is not available` when creating the venv:** run `sudo apt install python3-venv`, then try again.
- **`pip` hangs or times out:** the Pi may have lost its network. Check `ping 8.8.8.8` and your Wi-Fi.
- **`cat: data/readings.csv: No such file`:** `main.py` did not run, or you ran it from another folder.
- **The CSV has more rows than expected:** the file is appended to each time. Delete it with `rm data/readings.csv` and run again.

> **Challenge:** Make `main.py` count how many lines were saved and how many were rejected, and print the totals when the loop ends.

---

## Checkpoint

Not yet individual: today's checkpoint is the partner test in Part 3. The individual checkpoint comes at the end of Session 3.

## Where to go next

You have a project with clear parts. **Session 3** teaches you to change it safely, using Git **branches** and a **code review**, and to write your first automatic tests.

## Further reading

- [Python venv documentation](https://docs.python.org/3/library/venv.html)
- [Python csv module](https://docs.python.org/3/library/csv.html)
- [pyserial documentation](https://pyserial.readthedocs.io/en/latest/)
