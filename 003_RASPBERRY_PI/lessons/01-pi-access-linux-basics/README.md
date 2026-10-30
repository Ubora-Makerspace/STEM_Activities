# Session 1: Entry check, Pi access and Linux basics


## Part 0: Entry check (about 20 minutes, individual)

This is not a test you can fail. It is a snapshot of where you are today, so that on Session 9 you can see how far you have come. Work **alone**, with no help from your partner.

| Task | What to do |
| --- | --- |
| **A. Edit Python** | Make this program print the average of the readings, rounded to 1 decimal place. The answer should be `42.5`. |
| **B. Inspect Git** | In any existing Git project of yours, run `git status` and `git log --oneline -5`. Explain in one sentence what each one shows. |
| **C. Explain the robot** | In 4 to 5 sentences: what does the ultrasonic sensor measure and how, what does the servo do, and what is the Arduino's job? |

```python
readings = [42.6, 43.1, 41.9]
# print the average here
```

Score yourself and keep this sheet. You will fill in the same sheet in Session 9.

| Skill | 0 = not yet | 1 = with help | 2 = on my own |
| --- | --- | --- | --- |
| Edit Python and run it | | | |
| Read Git status and history | | | |
| Explain the robot's parts | | | |


## Part 1: How you reach the Pi

The Pi is a computer with no screen. **SSH** (Secure Shell) lets you type on your laptop while the commands run on the Pi, like a very long remote keyboard.


Both devices must be on the **same network**. The Pi announces its own name, like `pair1-pi.local`, so you do not need to know its IP address.

1. Plug in the Pi's power supply. The green **ACT** LED flickers while it boots. The first boot can take two to three minutes.
2. From your laptop, check that it answers:

   ```
   ping pair1-pi.local
   ```

   Press `Ctrl+C` to stop the pings.
3. Log in:

   ```
   ssh pi@pair1-pi.local
   ```

   Type `yes` if asked about the fingerprint, then type your password. **Nothing appears while you type a password.** That is normal.
4. Your prompt changes to something like `pi@pair1-pi:~ $`. That prompt means every command now runs **on the Pi**.

Use your own username and hostname where the guide says `pi` and `pair1-pi`.


## Part 2: Linux basics

A terminal waits for a **command**. Here are the ones you need today.

| Command | What it does |
| --- | --- |
| `pwd` | Prints where you are (the "working directory") |
| `ls` | Lists the files here. `ls -l` adds sizes and dates |
| `cd folder` | Moves into a folder. `cd ..` moves up. `cd` alone goes home |
| `mkdir name` | Makes a folder |
| `nano file` | Opens a simple text editor. `Ctrl+O`, `Enter` saves, `Ctrl+X` quits |
| `cat file` | Prints a file on the screen |
| `python3 file.py` | Runs a Python program |
| `clear` | Tidies the screen |
| `history` | Lists commands you have typed. Press the up arrow to reuse one |

Two tricks save a lot of typing: press `Tab` to **auto-complete** names, and press the **up arrow** to repeat the last command.

Practise:

1. Run `pwd`, then `ls`.
2. Make a folder and go into it:

   ```
   mkdir practice
   cd practice
   ```
3. Create a file with `nano hello.py`, type `print("Hello, Pi!")`, then save and quit.
4. Run it with `python3 hello.py`.
5. Go back home with `cd`.

**Swap roles.**


## Part 3: Switching the Pi off safely

The Pi keeps its whole system on the microSD card. If you pull the power while the Pi is writing, the card can be **corrupted**, and a corrupted card means a re-flash and lost work. Always shut down first.

```
sudo shutdown -h now
```

- `sudo` means "do this as the administrator".
- `-h` means halt, and `now` means do it immediately.

Your SSH session ends. **Wait until the green ACT LED stops flickering** (about 10 to 15 seconds), *then* unplug the power. Plug it in again, wait for it to boot, and log back in with `ssh`.

> **Shutdown checklist (copy this into your README in Part 5):**
> 1. Close any program that is running (`Ctrl+C`).
> 2. Type `sudo shutdown -h now`.
> 3. Wait for the green LED to stop flickering.
> 4. Unplug the power.

Practise one full cycle: shut down, unplug, plug in, log in again.


## Part 4: Get the project onto the Pi

1. Tell Git who you are (once per Pi):

   ```
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```
2. Clone the repository. Use the starter code url:

   ```
   git clone <repository-url> project
   cd project
   ls
   ```

   You should see `README.md`, `arduino`, `pi`, `tests` and `docs`.
3. Run the starter program:

   ```
   python3 pi/starter.py
   ```

   ```python
   """Starter program: proves Python runs on this Pi."""
   import datetime
   import platform

   print("Hello from the Raspberry Pi!")
   print("Hostname:", platform.node())
   print("Python:  ", platform.python_version())
   print("Time:    ", datetime.datetime.now().isoformat(timespec="seconds"))
   ```

   You should see the hostname of *your* Pi.


## Part 5: Write the instructions as you go

Instructions you write *now* are the ones you will rely on for the rest of the course. Open the README with `nano README.md` and fill in this section:

```markdown
## Using the Pi

- **Log in:** `ssh pi@pair1-pi.local`
- **Project folder:** `~/project`
- **Run the starter:** `python3 pi/starter.py`

### Shutting down
1. Close any running program with `Ctrl+C`.
2. `sudo shutdown -h now`
3. Wait for the green LED to stop flickering.
4. Unplug the power.
```

Save the file, then record your work in Git:

```
git add README.md
git commit -m "Add Pi access and shutdown instructions"
```

**Test your instructions.** Ask your partner to follow the README *without your help* from a cold start: log in, find the project, run the starter, shut down. Fix anything that confused them.


## Session output

Tick each box before you move on.

- [ ] Each teacher has logged in over SSH and run `pwd` and `ls`
- [ ] Each teacher can find the project folder and run `python3 pi/starter.py`
- [ ] Each teacher has shut down the Pi using the written instructions
- [ ] The README has the access method, project folder, run command and shutdown steps
- [ ] Baseline sheets are completed and saved


## Troubleshooting

- **`ping` or `ssh` says it can't find `pair1-pi.local`:** the laptop and Pi are not on the same network, or the Pi is still booting. Wait a minute, check the LED, and ask your facilitator for the Pi's IP address. Then use `ssh pi@<ip-address>`.
- **`WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED`:** the card was re-flashed. Run `ssh-keygen -R pair1-pi.local` on your laptop and try again.
- **`Permission denied, please try again`:** wrong username or password. Remember that nothing shows while you type a password.
- **The LED never flickers:** check the power supply and that you used the port marked **PWR IN**.
- **`git clone` says `Authentication failed` or `Permission denied (publickey)`:** the Pi does not have access to the repository yet. Ask your facilitator for the token or key.
- **`command not found`:** check your spelling and capital letters. Linux is case-sensitive.
- **You pulled the power by mistake:** boot again. If it won't start, tell your facilitator before you do anything else.

> **Challenge:** Find out five facts about your Pi and add them to the README under "Pi health":
>
> ```
> hostname -I              # IP address
> df -h /                  # disk space left
> free -h                  # memory
> vcgencmd measure_temp    # temperature
> uptime                   # how long it has been on
> ```


## Checkpoint (individual)

On your own, with only the README: log in, find the project folder, run the starter program, and shut the Pi down safely. Your facilitator will note it as observed or not yet.

## Where to go next

The starter program is one long script. In **Session 2** you will split the project into modules and give it its own **virtual environment**, so that installing a library for this project can never break anything else.

## Further reading

- [Raspberry Pi: remote access](https://www.raspberrypi.com/documentation/computers/remote-access.html)
- [Raspberry Pi getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [Pro Git book (free)](https://git-scm.com/book/en/v2)
