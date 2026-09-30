
int potPin = A0;
int ledPin = 9;   // must be a PWM pin (~)
int buzz = 5;


void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buzz, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int potValue = analogRead(potPin);                 // 0 to 1023
  int brightness = map(potValue, 0, 1023, 0, 255);   // scale to 0 to 255
  int sound = map(potValue, 0, 1023, 0, 255);   // scale to 0 to 255


  analogWrite(ledPin, brightness);
  analogWrite(buzz,sound);

  Serial.print("Pot: ");
  Serial.print(potValue);
  Serial.print("  Brightness: ");
  Serial.println(brightness);
  Serial.print("  Sound Level: ");
  Serial.println(sound);

  delay(400);
}