# Session 9: Individual proficiency check and teach-back

Three weeks ago you could blink an LED and move a servo. Today you show what you can do **on your own**, then show you can **teach** it. Skill is not the same as attendance, so today's evidence is something an observer can see you do.

This guide is written for both of you: the **teacher** being assessed, and the **observer** (a facilitator, or your partner when it is their turn to watch). It ends with a record sheet.

## What you need

- Your pair's Pi, robot, and project repository, all working
- A second Pi or the simulator for the prepared faults (`arduino/simulated_sender/`)
- Your Session 1 entry-check sheet, to compare
- The record sheet at the end of this guide, printed or copied
- A timer

> **Today there are no roles.** Each teacher does the tasks **alone** while the observer watches. The observer does not help, hint or point.

---

## Part 0: How this works

- Each teacher completes **Stations 1 to 4** individually, one after the other, about 10 minutes each.
- Then each **pair** gives a short demonstration and teaches one activity (Station 5).
- Observers record **observable evidence**: what the person actually did and said, not what they might know.
- If a skill needs another practice cycle, that is a normal and useful result. Note it and plan the practice. Attendance is not mastery.

---

## Station 1: Independent setup and run (10 minutes)

Starting with the Pi **switched off** and a laptop:

1. Power on, connect over SSH, and open the project folder.
2. Activate the virtual environment.
3. Start the logger with the robot (or simulator) connected: `python pi/main.py data/check.csv`.
4. Let it run for about 20 seconds, then stop it with `Ctrl+C`.
5. Find **one measurement** in the CSV file and read it aloud with its timestamp.
6. Shut the Pi down using the documented procedure.

**Evidence:** every step done without being told what comes next.

---

## Station 2: A small code change and a test (10 minutes)

The observer picks **one** of these (a different one per teacher):

| Change | Where |
| --- | --- |
| Raise the maximum accepted distance to 300 cm | `pi/config.py` |
| Reject readings below 5 cm instead of 2 cm | `pi/config.py` |
| Make the error message for an out-of-range value say "too far" or "too close" | `pi/validator.py` |

1. Create a branch.
2. Make the change.
3. Update or add a test so that it describes the new rule, and run `pytest`.
4. If any test fails, work out whether the test or the code needs to change.
5. Commit, and explain in your own words how it would be reviewed and merged.

**Evidence:** the change is correct, the relevant test was run (and updated where needed), and the Git steps were not prompted.

---

## Station 3: Diagnose a prepared fault (10 minutes)

The observer sets up **one** fault that you have not seen in this order, using `simulated_sender.ino` (see Session 6), or a physical fault on the robot.

| Fault | How it is prepared | Good diagnosis sounds like |
| --- | --- | --- |
| A | `FAULT_MODE = 1` | "Every tenth line is garbled text. The validator rejects them, so no bad data is saved." |
| B | `FAULT_MODE = 3` | "The format is right but the value is impossible. The range check rejects it." |
| C | `FAULT_MODE = 4` | "The Arduino goes quiet after 5 seconds. The reader warns that no data arrived." |
| D | A charge-only cable, or the cable in the PWR IN port | "The port does not appear in `ls /dev/ttyACM*`. The cable is the cause." |
| E | Wrong `SERIAL_PORT` or `BAUD_RATE` in `config.py` | "It either can't open the port or prints garbage. The setting does not match." |

Tell the observer: what you saw, what you suspected, which **test, log or observation** helped, and what you changed.

**Evidence:** a correct diagnosis, with the reasoning, reached without random changes.

---

## Station 4: Explain the system (5 minutes)

Without notes, explain **aloud** (or on a whiteboard):

1. What the Arduino does and what the Pi does, and **why** the Pi does not control the servo.
2. Trace one measurement from the sensor to a row in the CSV file: HC-SR04, Arduino, USB, `serial_reader.py`, `validator.py`, `csv_writer.py`.
3. One safety point: *the 5 V ECHO pin must never be connected to a Pi pin*, or *the servo has its own power supply*.

```
HC-SR04 --echo--> Arduino --"DIST,42.6" over USB--> serial_reader --> validator --> csv_writer --> data/*.csv
```

**Evidence:** a clear, correct explanation in your own words.

---

## Station 5: Pair demonstration and teach-back (15 minutes per pair)

1. **Demonstrate** the connected project with live readings.
2. **Teach** one short activity (about 5 minutes) to the observers as if they were your learners.

Plan it on this card first:

| Part of the activity | Your answer |
| --- | --- |
| Name of the activity | |
| Learning goal (what will learners be able to do?) | |
| What the learners do (steps) | |
| One safety note | |
| One troubleshooting step they might need | |
| A check-for-understanding question | |

A filled-in example:

| Part of the activity | Example |
| --- | --- |
| Name | "Is the sensor telling the truth?" |
| Learning goal | Learners can compare a sensor reading with a ruler and describe how much it varies. |
| What the learners do | Hold a book 30 cm from the sensor, run the logger, find the lowest and highest reading in the CSV. |
| Safety note | Keep the sensor wiring on the Arduino. Nobody connects wires while the robot is powered. |
| Troubleshooting step | If no lines appear, check the cable is in the **USB** port and run `ls /dev/ttyACM*`. |
| Check question | "Why would the reading change if the book were soft?" |

---

## Session output

- [ ] Each teacher has completed Stations 1 to 4 on their own
- [ ] Each pair has demonstrated the project and taught one activity
- [ ] Evidence is recorded for every teacher (see the sheet below)
- [ ] Anything needing another practice cycle is noted with a plan

---

## Record sheet (one per teacher)

Teacher: ____________________   Observer: ____________________   Date: __________

Mark each line **O** (observed, on their own), **H** (observed with a hint) or **N** (not yet).

| Skill | Evidence you saw | O / H / N |
| --- | --- | --- |
| Independent setup and run | Logged in, activated the environment, ran the logger, found a CSV row, shut down | |
| A correct code change | The change was right and sat on a branch | |
| Test use | Ran `pytest`, read a result, updated or added a test | |
| Fault diagnosis | Named the fault and the evidence (test, log or observation) | |
| Explaining Arduino vs Pi | Correct division of work and data path | |
| Safety point | One accurate safety point given | |
| Teaching explanation | Goal, safety note, troubleshooting step and check question | |

**Compare with Session 1.**

| Baseline skill | Session 1 (0 to 2) | Session 9 (0 to 2) |
| --- | --- | --- |
| Edit Python and run it | | |
| Read Git status and history | | |
| Explain the robot's parts | | |

**Next practice cycle (skills marked N or H):** ____________________________________

---

## Troubleshooting (for the day)

- **A station overruns:** stop at the time limit and record what was observed. Do not help to finish.
- **The hardware fails mid-check:** switch to the simulator so the teacher can still be assessed on the code and the data.
- **Network drops:** use the offline fallback. The tests and the parser do not need the network.
- **A pair's repository is out of date:** check `git status` before you start. Commit or stash first.
- **Nerves:** this is a snapshot, not a verdict. A skill marked "not yet" simply gets another practice cycle.

> **Challenge for those who finish early:** pick **one** extension and try it, on a branch. Only one at a time.
>
> - Run the logger automatically at startup and read its logs.
> - Add the optional dashboard, if you have not done so.
> - Add an I²C sensor using an existing library and its datasheet.
> - Add a Pi-to-Arduino command message with validation and a safe default.

---

## Where to go next

You now have a working pattern you can teach: **a microcontroller handles timing and sensors, a small computer handles data, tests prove it, Git keeps it safe.** Good next projects reuse exactly this pattern with a different sensor.

Avoid adding both MQTT and a web dashboard at once. Defer custom drivers and advanced concurrency until you have practised the core.

## Further reading

- [Raspberry Pi getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [Arduino language reference](https://docs.arduino.cc/language-reference/)
- [Python venv documentation](https://docs.python.org/3/library/venv.html)
- [Pro Git book](https://git-scm.com/book/en/v2)
