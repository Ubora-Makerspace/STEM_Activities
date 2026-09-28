int green = 8;
int yellow = 5;
int red = 2;

int stopGoTime = 10000;   // red and green both use this (10 seconds)

void setup() {
  pinMode(green, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(red, OUTPUT);
}

// Blinks the yellow LED twice
void blinkYellow() {
  for (int i = 0; i < 2; i++) {
    digitalWrite(yellow, HIGH);
    delay(500);
    digitalWrite(yellow, LOW);
    delay(500);
  }
}

void loop() {
  // RED - stop
  digitalWrite(red, HIGH);
  delay(stopGoTime);
  digitalWrite(red, LOW);

  // YELLOW - get ready to go
  blinkYellow();

  // GREEN - go
  digitalWrite(green, HIGH);
  delay(stopGoTime);
  digitalWrite(green, LOW);

  // YELLOW - get ready to stop
  blinkYellow();

  // loop() now repeats from RED
}