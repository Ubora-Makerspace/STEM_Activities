# Session 6: Fault handling and repeatable tests

Last session you saw the system work. Today you learn to work out why it *doesn't*. Real systems fail in boring ways: a cable is loose, a line is garbled, a sketch stops. A good engineer does not guess. They have **tests** that run without any hardware, and **logs** that say what happened.

You will write a full set of parser tests, then break the connected system on purpose, one fault at a time, and write down how you found each one.

## What you need

- The Pi with your project, venv and robot connected (Session 5)
- Your Arduino sketches, and your laptop for uploading
- `arduino/simulated_sender/simulated_sender.ino` for creating faults safely
- Your pair's `docs/troubleshooting.md` (a table template is in the starter files)

> **Roles today:** Driver, Reviewer, Troubleshooter. The **Troubleshooter** leads every diagnosis and the Driver must not touch anything until they have a theory.

---

## Part 0: The diagnosis habit

When something breaks, resist the urge to change things at random. Instead:

1. **Observe:** what exactly happened? Write the symptom.
2. **Guess:** what could cause that? List two or three possibilities.
3. **Test:** use a test, a log line or a cable swap to rule each one in or out.
4. **Fix and confirm:** change *one* thing, and check the symptom is gone.
5. **Record:** write the symptom, diagnosis and fix, so the next person (maybe you) has it in a minute.

Tests are your fastest way to rule things in or out, because they don't need the robot at all.

---

## Part 1: Write the parser tests

Create `tests/test_parser.py`. It covers a normal reading, a malformed line, a missing value and an out-of-range value, plus the edges.

```python
import pytest

from validator import parse_message, InvalidMessage


def test_normal_reading():
    assert parse_message("DIST,42.6") == 42.6


def test_line_ending_is_ignored():
    assert parse_message("DIST,42.6\r\n") == 42.6


def test_malformed_line_is_rejected():
    with pytest.raises(InvalidMessage):
        parse_message("DI@T;4x2")


def test_missing_value_is_rejected():
    with pytest.raises(InvalidMessage):
        parse_message("DIST,")


@pytest.mark.parametrize("line", ["DIST,9999.0", "DIST,-5", "DIST,1.9", "DIST,400.1", "DIST,nan"])
def test_out_of_range_is_rejected(line):
    with pytest.raises(InvalidMessage):
        parse_message(line)


@pytest.mark.parametrize("line,expected", [("DIST,2.0", 2.0), ("DIST,400.0", 400.0)])
def test_range_limits_are_allowed(line, expected):
    assert parse_message(line) == expected
```

A few things to notice:

- `pytest.raises(InvalidMessage)` says "this should raise an error". If the error does **not** happen, the test fails.
- `@pytest.mark.parametrize` runs the same test with several inputs, so you write it once.
- `DIST,2.0` and `DIST,400.0` are the **boundaries**. Bugs love boundaries.
- `DIST,nan` ("not a number") is a sneaky one: `float("nan")` works, but comparisons with it are always false.

---

## Part 2: Run the tests with no hardware

Unplug the robot if you like. Nothing in these tests needs it.

```
source .venv/bin/activate
pytest -v
```

Every test should pass. If one fails:

1. Read the failure message. It shows the input that failed and what happened.
2. Decide whether the **test** or the **code** is wrong. Which behaviour do you actually want?
3. Fix one, run again, and repeat until all pass.

Deliberately break something to see how a failure looks: change `MAX_DISTANCE_CM` in `config.py` to `300.0`, run `pytest`, read the failure on the `DIST,400.0` test, then change it back.

Commit your tests on a branch, as in Session 3:

```
git switch -c feature/parser-tests
git add tests/test_parser.py
git commit -m "Add parser tests for normal, malformed, missing and out-of-range input"
git push -u origin feature/parser-tests
```

**Swap roles.**

---

## Part 3: Break it on purpose

Use the simulator so you control the faults. Open `arduino/simulated_sender/simulated_sender.ino` on your laptop:

```cpp
// Simulated robot: needs NO sensor and NO servo, just an Arduino and a USB cable.
// Use it as an offline fallback, and to create faults on purpose.
//
// Change FAULT_MODE, upload again, and watch what the Pi does.
//   0 = no fault
//   1 = every 10th line is garbled text
//   2 = every 10th line has a missing value ("DIST,")
//   3 = every 10th line is out of range ("DIST,9999.0")
//   4 = the sketch goes silent after about 5 seconds

const int FAULT_MODE = 0;

unsigned long lastMs = 0;
unsigned long count = 0;
float fake = 40.0;
int direction = 1;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (millis() - lastMs < 100) {
    return;
  }
  lastMs = millis();
  count++;

  fake += direction * 1.3;
  if (fake > 150.0 || fake < 10.0) {
    direction = -direction;
  }

  if (FAULT_MODE == 4 && count > 50) {
    return;                                    // silent
  }

  bool badLine = (count % 10 == 0);
  if (badLine && FAULT_MODE == 1) {
    Serial.println("DI@T;4x2");
  } else if (badLine && FAULT_MODE == 2) {
    Serial.println("DIST,");
  } else if (badLine && FAULT_MODE == 3) {
    Serial.println("DIST,9999.0");
  } else {
    Serial.print("DIST,");
    Serial.println(fake, 1);
  }
}
```

For each fault below, follow the same steps:

1. Set `FAULT_MODE` (or do the physical action), and upload.
2. Run `python pi/print_readings.py` on the Pi.
3. **Before** you look at the code, write down the symptom you see.
4. Use the logs and the tests to find the cause.
5. Return `FAULT_MODE` to 0 and confirm the symptom is gone.

| Fault | How to create it | What to look for |
| --- | --- | --- |
| Garbled line | `FAULT_MODE = 1` | `BAD  Bad format: ...` every tenth line |
| Missing value | `FAULT_MODE = 2` | `BAD  Not a number: ''` or a format error |
| Out-of-range reading | `FAULT_MODE = 3` | `BAD  Out of range ...` with 9999.0 |
| Silent Arduino | `FAULT_MODE = 4` | `No data for 2 s. Is the sketch running?` after about 5 seconds |
| Unplugged cable | Pull the USB cable out | `Serial problem ... Trying again` and later `Connected.` |

Pick **at least two** faults. Do at least one with the real robot (the cable pull is the easiest).

For each fault ask yourself: which one of *these* told me the cause: the **test**, the **log message**, or my own **observation**?

**Swap roles.**

---

## Part 4: Keep a troubleshooting log

Add a row to `docs/troubleshooting.md` for each fault you diagnosed. Write it so a stranger can use it:

| Symptom (what you saw) | Diagnosis (how you found the cause) | Fix |
| --- | --- | --- |
| Program prints "Serial problem ... No such file or directory" | `ls /dev/ttyACM*` showed nothing. The cable was charge-only. | Swapped to a known-good USB data cable. |
| `BAD  Out of range ... 9999.0` every 10th line | The simulator was in `FAULT_MODE = 3`. The test `test_out_of_range_is_rejected` already covers this. | Set `FAULT_MODE = 0` and re-uploaded. |

Commit it:

```
git add docs/troubleshooting.md
git commit -m "Add troubleshooting notes"
```

---

## Session output

- [ ] The parser tests pass without hardware
- [ ] They cover a normal reading, a malformed line, a missing value and an out-of-range value
- [ ] At least two faults were created, diagnosed and fixed
- [ ] `docs/troubleshooting.md` explains how to find at least one fault
- [ ] Tests and notes are committed and pushed

---

## Troubleshooting

- **All tests fail with `ModuleNotFoundError`:** check `pytest.ini` exists in the project folder and contains `pythonpath = pi`.
- **A test passes when it should fail:** check that you really changed `FAULT_MODE` and re-uploaded. The Arduino keeps running the *old* sketch until you upload.
- **`pytest` finds no tests:** test files must start with `test_` and the functions with `test_`.
- **The cable pull crashes the program:** read the last lines of the traceback and look at `serial_reader.py`. Is the `try/except SerialException` there?
- **You cannot tell whether it is the Arduino or the Pi:** use `python -m serial.tools.miniterm /dev/ttyACM0 9600`. If you see good lines there, the Arduino is fine and the problem is in your Python.
- **The simulator will not upload:** close the Serial Monitor and any program that has the port open.

> **Challenge:** Add a test that a line with extra spaces around the number, like `DIST, 42.6`, is accepted. Does your code already do this? If not, change the parser and make the test pass.

---

## Checkpoint (end of Week 2)

Each pair demonstrates live serial readings and recovers from one fault you introduce on the spot. Each teacher explains why the Arduino handles the sensor and servos, while the Pi handles logging and presentation.

## Where to go next

The system is reliable. In **Week 3** you will start keeping the data it produces. **Session 7** adds timestamps and a CSV log, and asks the question that makes data worth keeping: what does it tell us?

## Further reading

- [pytest: parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html)
- [Python exceptions tutorial](https://docs.python.org/3/tutorial/errors.html)
