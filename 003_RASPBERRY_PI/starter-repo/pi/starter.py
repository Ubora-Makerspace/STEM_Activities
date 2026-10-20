"""Starter program: proves Python runs on this Pi."""
import datetime
import platform

print("Hello from the Raspberry Pi!")
print("Hostname:", platform.node())
print("Python:  ", platform.python_version())
print("Time:    ", datetime.datetime.now().isoformat(timespec="seconds"))
