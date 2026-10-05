int sensorPin = A0;
int led =6;


void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop() {
  int light = analogRead(sensorPin);   // 0 to 1023
  Serial.println(light);
  int bright=map(light,0,1023,0,255);

  analogWrite(led,bright);
  delay(200);
}