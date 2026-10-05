int led = 6;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop() {
  int value = analogRead(A0);            
  float volts = value * (5.0 / 1023.0);

  // if (volts >=3.5){
  //   digitalWrite(led, HIGH);
  // }
  // else {
  //   digitalWrite(led, LOW);zq  w
  // }

  int bright = map(value,0,1023,0,255);

  analogWrite(led,bright);
  Serial.println(value);
  Serial.print("  ->  ");
  Serial.print(volts);
  Serial.println(" V");

  
}