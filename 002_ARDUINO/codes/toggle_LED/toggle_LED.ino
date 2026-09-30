// This code uses a pull down button configuration

int ledState = 0;
int ledPin = 7;
int buttonPin = 6;
int buttonNew;
int buttonOld = 1;
int dt = 50;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}

void loop() {
buttonNew = digitalRead(buttonPin);

// Check for the 0 to 1 transition
if (buttonNew == 1 && buttonOld ==0) {
  if (ledState == 0) {
    digitalWrite(ledPin, HIGH);
    ledState = 1;
  }else {
    digitalWrite(ledPin, LOW);
    ledState = 0;
  }
}

buttonOld = buttonNew;
Serial.print("ButtonOld:");
Serial.println(buttonOld);
delay(dt); // Debounce delay
}