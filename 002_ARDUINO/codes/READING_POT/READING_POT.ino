int pot = A0;
void setup() {
  Serial.begin(9600);
}

void loop() {
  int value = analogRead(pot);            // 0 to 1023
  float volts = value * (5.0 / 1023.0);

  Serial.print(value);
  Serial.print("  ->  ");
  Serial.print(volts);
  Serial.println(" V");

  delay(200);
}