# Arduino Buttons and Digital Inputs

## Learning progression

Start with the input itself, observe its value in the Serial Monitor, and then use that value to control an output.

### Step 1: Read the button

For this first example, connect a roughly 10 kΩ resistor between pin 2 and the board's logic voltage (typically 5 V or 3.3 V). Connect the button between pin 2 and `GND`. The external resistor keeps the input stable while the button is released.

```cpp
const int buttonPin = 2;

void setup() {
	pinMode(buttonPin, INPUT);
	Serial.begin(9600);
}

void loop() {
	int buttonState = digitalRead(buttonPin);
	Serial.println(buttonState);
	delay(100);
}
```

Students should observe these readings in the Serial Monitor:

| Button   | Reading      |
| -------- | ------------ |
| Released | `1` (`HIGH`) |
| Pressed  | `0` (`LOW`)  |

### Step 2: Print a useful button state

Replace the numeric reading with a message students can interpret:

```cpp
const int buttonPin = 2;

void setup() {
	pinMode(buttonPin, INPUT);
	Serial.begin(9600);
}

void loop() {
	int buttonState = digitalRead(buttonPin);
	if (buttonState == LOW) {
		Serial.println("Button Pressed");
	} else {
		Serial.println("Button Released");
	}

	delay(100);
}
```

### Step 3: Understand `HIGH`, `LOW`, and active LOW

With this external pull-up circuit and `INPUT`, the input is `HIGH` when the button is released and `LOW` when it is pressed. This is called **active LOW**: the pressed state is represented by `LOW`.

### Step 4: Use the button to control an LED

Connect an LED and a suitable current-limiting resistor to pin 8, or use an onboard LED if available.

```cpp
const int buttonPin = 2;
const int ledPin = 8;

void setup() {
	pinMode(buttonPin, INPUT);
	pinMode(ledPin, OUTPUT);
}

void loop() {
	int buttonState = digitalRead(buttonPin);

	if (buttonState == LOW) {
		digitalWrite(ledPin, HIGH);
	} else {
		digitalWrite(ledPin, LOW);
	}
}
```

The signal path is:

```text
BUTTON -> digitalRead() -> HIGH / LOW -> if statement -> digitalWrite() -> LED
```

### Step 5: Compare pull-up and pull-down inputs

A pull-up holds the input at `HIGH` while the button is released. In this lesson, use an external roughly 10 kΩ resistor from the input pin to the board's logic voltage, and wire the button between the input pin and `GND`. Set the pin mode to `INPUT`.

| Configuration | Button released | Button pressed |
| ------------- | --------------- | -------------- |
| Pull-up       | `HIGH`          | `LOW`          |
| Pull-down     | `LOW`           | `HIGH`         |

A pull-down holds the input at `LOW` while the button is released. For comparison, use a roughly 10 kΩ resistor from the input pin to `GND`, and wire the button between the input and the board's supported logic voltage (typically 5 V or 3.3 V). Do not exceed the board's input voltage rating. Most classic Uno-style boards do not provide an internal pull-down option.

Button contacts can bounce and create multiple quick readings. The delays in the Serial examples limit output speed but are not full debouncing; add debounce logic when each press must register exactly once.

### Step 6: Challenge

Modify the LED program so the LED blinks while the button is held down and stays off when the button is released. Test it, then explain why the pressed check uses `LOW`.

### References

1. https://www.circuitbasics.com/pull-up-and-pull-down-resistors/
2. https://docs.arduino.cc/tutorials/generic/digital-input-pullup/
