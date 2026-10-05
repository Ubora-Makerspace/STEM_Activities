int blink =2;// define the pin.
int blink2 =4;// define the pin.
int blink3 =7;// define the pin.
void setup() {
  // put your setup code here, to run once:
pinMode(blink, OUTPUT);// Identify type of device connected pin and wether is INPUT/OUTPUT.
pinMode(blink2, OUTPUT);
pinMode(blink3, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
for(int i=0; i<=2; i++) {
digitalWrite(blink,HIGH);
delay(50); //microsecond 
digitalWrite(blink,LOW);
delay(50); //microsecond 
}
for(int i=0; i<=2; i++) {
digitalWrite(blink2,HIGH);
delay(50); //microsecond 
digitalWrite(blink2,LOW);
delay(50); //microsecond 
}
for(int i=0; i<=2; i++) {
digitalWrite(blink3,HIGH);
delay(50); //microsecond 
digitalWrite(blink3,LOW);
delay(50); //microsecond 
}
}
