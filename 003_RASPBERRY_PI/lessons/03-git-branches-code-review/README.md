# Session 3: Git branches and your first code review

You already use Git to save snapshots. Today you use it the way professional teams do: you never change the working version directly. You make your change on a **branch**, prove it works with a **test**, and ask a partner to **review** it before it is merged.

This is also the week's checkpoint. By the end, each of you has contributed one reviewed, merged change.

## What you need

- The Pi with your project, and its virtual environment working (Session 2)
- A shared remote repository you can push to (GitHub, GitLab, Gitea or similar)
- Your partner, and a fresh cup of patience for the first merge

> **Roles today:** Driver, Reviewer, Troubleshooter. In this session the **Reviewer** is real: they read the change and leave a comment before anything is merged.

## Part 0: The idea of a branch

Imagine you are editing an important printed document. You photocopy it, scribble your changes on the copy, and only when your colleague approves do you copy those changes into the original. A **branch** is that photocopy. `main` is the original that always works.

```
main     o----o----o-------------------o   (always works)
                    \                 /
feature              o----o----o-----o     (your change, tested, reviewed)
```

The working cycle you will practise:

```
git switch -c feature/<name>     make a branch
   ...edit, run tests...
git add / git commit             save a snapshot on the branch
git push -u origin feature/...   send the branch to the shared repository
open a pull request              ask for a review
review, merge                    the change joins main
git switch main / git pull       everyone gets the new main
```

## Part 1: Tests first

Today's change: the validator should **reject distances that make no sense** (below 2 cm or above 400 cm, which is what an HC-SR04 can measure). A good habit is to write the test *before* the fix, so you can watch it fail and then pass.

1. Start from an up-to-date `main`:

   ```
   cd ~/project
   source .venv/bin/activate
   git switch main
   git pull
   ```
2. Make a branch:

   ```
   git switch -c feature/range-check
   ```
3. Tell pytest where your code is. Create `pytest.ini` in the project folder:

   ```
   [pytest]
   pythonpath = pi
   testpaths = tests
   ```
4. Create `tests/sample_messages.txt`. Each line says whether the message should be accepted (`GOOD`) or rejected (`BAD`):

   ```text
   # GOOD lines must be accepted. BAD lines must be rejected.
   GOOD DIST,42.6
   GOOD DIST,120.0
   GOOD DIST,2.0
   BAD DIST,abc
   BAD DIST,
   BAD HELLO
   BAD DIST,42.6,7
   BAD DIST,-5
   BAD DIST,9999.0
   ```
5. Create `tests/test_samples.py`, which tests every line in that file:

   ```python
   from pathlib import Path

   import pytest

   from validator import parse_message, InvalidMessage

   SAMPLES = Path(__file__).parent / "sample_messages.txt"


   def load_samples():
       for row in SAMPLES.read_text().splitlines():
           if row.strip() and not row.startswith("#"):
               kind, line = row.split(" ", 1)
               yield kind, line


   @pytest.mark.parametrize("kind,line", list(load_samples()))
   def test_sample(kind, line):
       if kind == "GOOD":
           assert isinstance(parse_message(line), float)
       else:
           with pytest.raises(InvalidMessage):
               parse_message(line)
   ```
6. Run the tests:

   ```
   pytest
   ```

   Two tests **fail**: `DIST,-5` and `DIST,9999.0` are accepted when they should be rejected. That is exactly what we want. The test has found the gap.

   ```
   FAILED tests/test_samples.py::test_sample[BAD-DIST,-5]
   FAILED tests/test_samples.py::test_sample[BAD-DIST,9999.0]
   ```

**Swap roles.**

## Part 2: Make the change and watch the tests pass

Open `pi/validator.py` and add the range check. Here is the finished file. The new lines are the `import` and the `if not (...)` block.

```python
"""Check one line of text from the Arduino and turn it into a number."""

from config import MIN_DISTANCE_CM, MAX_DISTANCE_CM


class InvalidMessage(ValueError):
    """Raised when a line is not a believable 'DIST,<number>' message."""


def parse_message(line):
    """Return the distance in cm, or raise InvalidMessage with a clear reason."""
    text = line.strip()
    parts = text.split(",")
    if len(parts) != 2 or parts[0] != "DIST":
        raise InvalidMessage(f"Bad format: {text!r}")

    try:
        value = float(parts[1])
    except ValueError:
        raise InvalidMessage(f"Not a number: {parts[1]!r}")

    if not (MIN_DISTANCE_CM <= value <= MAX_DISTANCE_CM):   # also rejects nan
        raise InvalidMessage(f"Out of range ({MIN_DISTANCE_CM} to {MAX_DISTANCE_CM} cm): {value}")

    return value


if __name__ == "__main__":
    for sample in ["DIST,42.6", "DIST,abc", "HELLO", "DIST,9999.0"]:
        try:
            print(sample, "->", parse_message(sample))
        except InvalidMessage as error:
            print(sample, "-> rejected:", error)
```

Run the tests again:

```
pytest
```

Everything should pass. If a test still fails, read the message, fix the code, and run again. Read the failing line first: it tells you exactly which sample was wrong.

Try the module's own self-test too:

```
python pi/validator.py
```

## Part 3: Commit, push and open a pull request

1. See what you changed:

   ```
   git status
   git diff
   ```
2. Save the snapshot with a message that says *why*:

   ```
   git add pytest.ini tests pi/validator.py
   git commit -m "Reject distances outside the sensor's range"
   ```
3. Send the branch to the shared repository:

   ```
   git push -u origin feature/range-check
   ```
4. On the hosting site, open a **pull request** (some sites call it a merge request) from `feature/range-check` into `main`. Write one sentence on what it does and how you tested it.

**No hosting site?** Your equivalent review is for your partner to run `git diff main..feature/range-check` on the Pi, check the tests pass on the branch, and then merge it locally with `git switch main` followed by `git merge feature/range-check`.

## Part 4: Review a partner's change

Your partner now makes a **different** small change on their own branch. Pick one:

- Add two more `BAD` lines to `tests/sample_messages.txt` (for example `DIST,12,13` and `dist,42.6`). Decide whether lowercase should be accepted, and make the test say what you decided.
- Improve an error message in `validator.py` so it is clearer.
- Add a line to the README explaining how to run `pytest`.

When you are the **reviewer**, work through this checklist:

| Question | Yes? |
| --- | --- |
| Do I understand what the change does from the description? | |
| Do the tests pass on this branch? (`git switch <branch>` then `pytest`) | |
| Did a test cover the new behaviour? | |
| Is the commit message clear? | |
| Is the code easy to read? | |

Leave **one useful comment**. A useful comment is specific and kind: "I think `Not a number` could also show the full line, so we can find it in the log." Not helpful: "ok" or "looks wrong".

When the checks pass, merge the pull request (or merge locally as above), then update your Pi:

```
git switch main
git pull
pytest
```

**Swap roles** and repeat, so that both teachers have written one change and reviewed one.

If your branch was based on an old `main`, Git may report a **merge conflict**. It looks like this inside a file:

```
<<<<<<< HEAD
...your lines...
=======
...their lines...
>>>>>>> branch-name
```

Open the file, keep the lines you want, delete the three marker lines, then `git add` the file and `git commit`. Ask the facilitator the first time.

## Session output

- [ ] The parser test **failed** before the fix and **passes** after it
- [ ] Each teacher has pushed a branch and had one change reviewed and merged
- [ ] Each teacher has left at least one specific review comment
- [ ] `main` on both Pis matches the shared repository (`git pull` says "Already up to date")
- [ ] The sample file distinguishes valid input from malformed input

## Troubleshooting

- **`pytest: command not found`:** the venv is not active. Run `source .venv/bin/activate`.
- **`ModuleNotFoundError: No module named 'config'` inside the tests:** you forgot `pytest.ini`, or you ran pytest from the wrong folder.
- **`git push` is rejected:** someone merged first. Run `git pull`, fix any conflict, run the tests, and push again.
- **`fatal: The current branch has no upstream branch`:** use `git push -u origin <branch-name>` the first time.
- **You committed on `main` by accident:** do not panic. Ask your facilitator before you push.
- **You can't see your partner's branch:** run `git fetch`, then `git switch <branch-name>`.
- **A conflict you do not understand:** `git merge --abort` puts everything back as it was.

> **Challenge:** Add a test that checks the exact boundary values `DIST,2.0` and `DIST,400.0` are accepted, and `DIST,1.9` and `DIST,400.1` are rejected.

## Checkpoint (individual)

Individual, no help from your partner: from a cold start, connect to the Pi, find the project, activate the environment, run `pytest`, and create a new branch with a small change. Pair support is welcome during practice, but this check is yours alone.

## Where to go next

Week 1 is done: the Pi is ready and the project is safe to change. In **Week 2** you move to the robot. **Session 4** teaches the Arduino to measure and move at the same time, without `delay()` getting in the way.

## Further reading

- [Pro Git: branching basics](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
- [pytest documentation](https://docs.pytest.org/)
