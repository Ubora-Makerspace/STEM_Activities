# Session 8: Project cleanup and classroom-ready instructions

The best test of a project is whether somebody else can use it. Today another pair tries to set up and run your logger using **only your README**. You watch silently and take notes. Then you fix the three biggest problems they hit.

If the core project is solid, you can finish with an **optional extension**: a tiny web page that shows the latest reading.

## What you need

- Your project repository, up to date (`git pull`)
- A second Pi and robot set (the other pair's, or a spare) or a fresh microSD card
- A stopwatch (a phone is fine)
- The **observation sheet** below (copy it into your notebook)

> **Roles today:** Driver, Reviewer, Troubleshooter. When you are the *observers*, you do **not** help. You only watch and write.

---

## Part 0: Why this is hard (and useful)

You know too much. When you wrote "install the requirements", you knew which folder, which environment, which Python. A new reader knows none of that. This session shows you the gaps you can no longer see yourself.

---

## Part 1: The usability test (about 40 minutes)

Swap pairs. One pair is the **testers**, the other the **observers**.

**Testers:** start with a Pi that has *no* project on it. Follow the README from the first line, until the logger is saving a CSV. Think aloud: say what you are doing and where you are confused.

**Observers:** do not help, hint or point. If the testers are stuck for more than 5 minutes, write it down and give them the smallest nudge you can.

Fill in as you go:

| Time | Where they got stuck | What they tried | What the README should have said |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |

Finish by recording:

- Total time from start to first CSV row: ________
- Did they succeed without help? Yes / No
- What was the most useful sentence in the README?

**Swap roles** (the other pair now tests yours).

---

## Part 2: Fix the three most important issues

Sit down with your observers' sheet. Do not try to fix everything. Choose the **three** issues that cost the most time and fix them in the right place:

| Where | Example fix |
| --- | --- |
| **README** | A missing step, such as "activate the environment first" |
| **Wiring diagram or `docs/wiring.md`** | A wire colour or pin that was unclear |
| **Code or its messages** | An error that said "Error" instead of saying what to do |

Use a branch and a pull request, as in Session 3:

```
git switch -c feature/usability-fixes
```

---

## Part 3: The fresh-run checklist

Before you call the project ready, confirm every line, on a **fresh** clone:

| Check | Command | Pass? |
| --- | --- | --- |
| Clone works | `git clone <url> fresh && cd fresh` | |
| Environment builds | `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt` | |
| Tests pass | `pytest` | |
| Logger runs with the robot | `python pi/main.py` | |
| A CSV file appears with a header and rows | `head data/readings.csv` | |
| Shutdown steps work | `sudo shutdown -h now` | |

Also check that a stranger could find: the wiring (`docs/wiring.md` and the diagram), the troubleshooting notes, and the safety note (**never connect the 5 V ECHO pin to a Pi pin; power the servo from its own pack**).

---

## Part 4 (optional): A simple local dashboard

Only do this if every row above is ticked. If not, spend the time making the core project more reliable and the documentation clearer. That is the better use of it.

The dashboard is a very small web page on the Pi, which shows the latest reading and whether the robot is still sending. It reads the CSV file that `main.py` writes, so the two programs stay independent.

```python
"""A very small local dashboard: shows the latest reading from the CSV log.

Run main.py in one terminal and this in another, from the project folder:
    python pi/dashboard.py
Then open  http://<pi-hostname>.local:8000  on a laptop on the same network.
"""

import csv
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

from config import CSV_PATH

PORT = 8000


def latest_reading(path):
    """Return the last complete row of the CSV, or None."""
    file_path = Path(path)
    if not file_path.exists():
        return None
    with file_path.open(newline="") as file:
        rows = list(csv.DictReader(file))      # fine for a few thousand rows
    for row in reversed(rows):
        if row.get("timestamp") and row.get("distance_cm"):
            return row
    return None


def render(reading):
    if reading is None:
        body = "<h1>No data yet</h1><p>Start <code>python pi/main.py</code>.</p>"
    else:
        age = (datetime.now() - datetime.fromisoformat(reading["timestamp"])).total_seconds()
        status = "Robot online" if age < 5 else f"No new data for {age:.0f} s"
        body = (
            f'<h1 style="font-size:4em;margin:0">{reading["distance_cm"]} cm</h1>'
            f"<p>{status}</p>"
            f'<p>Last reading: {reading["timestamp"]}</p>'
        )
    return (
        "<!doctype html><html><head><meta charset='utf-8'>"
        "<meta http-equiv='refresh' content='2'>"
        "<title>Ultrasonic monitor</title></head>"
        f"<body style='font-family:sans-serif;text-align:center;margin-top:3em'>{body}</body></html>"
    )


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        page = render(latest_reading(CSV_PATH)).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page)

    def log_message(self, *args):              # keep the terminal quiet
        pass


def main():
    print(f"Dashboard on port {PORT}. Press Ctrl+C to stop.")
    try:
        HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
```

Use two SSH sessions to the Pi (two terminal windows):

```
# window 1
python pi/main.py

# window 2
python pi/dashboard.py
```

Then, on your laptop (same network), open:

```
http://pair1-pi.local:8000
```

The number should update every two seconds as you move your hand. Cover the sensor or pull the cable, and after five seconds the page says *No new data*.

Things to remember:

- The dashboard is for the **classroom network only**. It has no password.
- It reads the whole CSV on each refresh. That is fine for a few thousand rows. Start a new file for a long run.
- Press `Ctrl+C` in each window to stop.

---

## Session output

- [ ] Another pair set up and ran the logger from your README, and you watched without helping
- [ ] You recorded where they struggled
- [ ] The three most important issues are fixed (code, wiring diagram or instructions)
- [ ] A fresh run produces a CSV and `pytest` still passes
- [ ] Either a tested core build, or the optional dashboard working

---

## Troubleshooting

- **The testers can't clone:** they do not have access. Give them read access, or a token, before the test.
- **The tests pass on your Pi but fail on theirs:** check for a file your project needs that is not in Git (look at `.gitignore`). What did you forget to commit?
- **The dashboard says `Connection refused`:** `dashboard.py` is not running, or you used the wrong hostname.
- **The dashboard says `No data yet`:** it is looking at `data/readings.csv`. Run `python pi/main.py` with **no** file name, or change the path.
- **`Address already in use`:** an old dashboard is still running. Close the old window, or wait a minute.
- **The page does not refresh:** check your browser is not blocking meta refresh. Press `F5`.
- **Your fixes created new problems:** run `pytest` before every commit, and rerun the fresh-run checklist at the end.

> **Challenge:** Add the robot's **status** to the dashboard page: show "Online" in green and "Offline" in red, using the age of the latest reading.

---

## Checkpoint

Run the fresh-run checklist with a partner reading it aloud. If every line passes without anybody improvising, the project is ready for Session 9.

## Where to go next

In **Session 9** you show what you can do on your own, and then teach it.

## Further reading

- [Python http.server](https://docs.python.org/3/library/http.server.html)
- [Raspberry Pi remote access](https://www.raspberrypi.com/documentation/computers/remote-access.html)
