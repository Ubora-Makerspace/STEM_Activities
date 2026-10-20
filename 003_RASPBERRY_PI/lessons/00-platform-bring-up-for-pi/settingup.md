# Set up the Raspberry Pi and connect over SSH

This guide shows how to prepare a Raspberry Pi OS card and connect to the Pi
from a laptop without a monitor or keyboard. The laptop and Pi must be on the
same network.

## What you need

- Raspberry Pi Zero 2 W and a microSD card
- A laptop connected to Wi-Fi
- Raspberry Pi Imager installed on the laptop
- The Wi-Fi network name and password

## 1. Write the image

1. Insert the microSD card into the laptop and open **Raspberry Pi Imager**.
2. Choose the correct Raspberry Pi model, **Raspberry Pi OS Lite (64-bit)**,
   and the microSD card. Check the card selection carefully; writing erases it.
3. Open the Imager's OS customization settings (gear icon or **Edit Settings**).
   Configure:
   - **Hostname:** for example, `pair1-pi`
   - **Username and password:** choose a username and a strong password. Record
     them somewhere private; current Raspberry Pi OS images do not necessarily
     create a default `pi` account.
   - **Wireless LAN:** enter the Wi-Fi name, password, and the correct country.
   - **Services / SSH:** enable SSH and choose password authentication.
4. Save the settings, write the image, and wait until Imager confirms it is
   finished. Eject the card using the laptop's safe-eject option.

## 2. Start the Pi

Insert the card into the Pi and connect its power. Give it a few minutes on the
first boot to start up and join Wi-Fi. Keep the laptop connected to the same
Wi-Fi network configured in Imager. A guest or school network may prevent
devices from seeing one another; ask the network administrator if the Pi cannot
be reached.

## 3. Connect from the laptop

Open **PowerShell** or **Terminal** on Windows, or Terminal on macOS/Linux, and
run the following. Replace `your-username` with the username set in Imager and
`pair1-pi` with the Pi's hostname:

```sh
ssh your-username@pair1-pi.local
```

On the first connection, SSH asks whether to trust the Pi's host key. Check that
you are connecting to your Pi, then type `yes` and press Enter. When prompted,
type the password set in Imager and press Enter. The password will not appear
on screen as you type; this is normal.

You are connected when the prompt changes to something like:

```text
your-username@pair1-pi:~ $
```

Commands you type now run on the Pi. To end the SSH session, type `exit` and
press Enter.

## If the hostname does not work

First, wait another minute and check that both devices are on the same Wi-Fi.
Then try these alternatives:

1. Find the Pi's IP address in the router's connected-device list, or ask the
   facilitator for it.
2. Connect using the address instead of the hostname:

   ```sh
   ssh your-username@192.168.1.25
   ```

   Replace `192.168.1.25` with the Pi's actual IP address.
3. If you cannot connect at all, power off the Pi, put the card back in the
   laptop, and use Raspberry Pi Imager to confirm Wi-Fi settings and that SSH
   is enabled. Save the settings, safely eject the card, and boot the Pi again.

Common messages:

- **Could not resolve hostname:** the hostname is mistyped, the Pi has not
  joined Wi-Fi, or the network does not support `.local` name discovery. Try
  the Pi's IP address.
- **Connection refused:** SSH may not be enabled or the Pi may still be
  starting. Check Imager's SSH setting and try again after waiting.
- **Permission denied:** check the username and password configured in Imager.
  Password characters are not displayed while typing.
- **REMOTE HOST IDENTIFICATION HAS CHANGED:** this can happen after re-imaging
  a Pi. Verify its identity with the facilitator before removing the old host
  key entry.

> **Keep credentials private.** Do not put the Wi-Fi password or Pi login
> password in a shared README, code repository, or classroom handout.

## Shut down safely

Before unplugging the Pi, end running programs with `Ctrl+C`, then run:

```sh
sudo shutdown -h now
```

Wait until the activity light stops flickering before disconnecting power.