
int ledPins[] = {7, 6, 5, 4};

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 4; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  
  for (int number = 0; number <= 15; number++) {

    
    for (int bit = 0; bit < 4; bit++) {
      digitalWrite(ledPins[bit], bitRead(number, bit));
    }

    Serial.println(number);   
    delay(1000);              
  }
}