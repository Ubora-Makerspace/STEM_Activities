int blink =2;// define the pin.
int blink2 =4;// define the pin.
void setup() {
  // put your setup code here, to run once:
pinMode(blink, OUTPUT);// Identify type of device connected pin and wether is INPUT/OUTPUT.
pinMode(blink2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(blink,HIGH);
delay(700); //microsecond 
digitalWrite(blink,LOW);
delay(700); //microsecond 

digitalWrite(blink2,HIGH);
delay(1000); //microsecond 
digitalWrite(blink2,LOW);
delay(700); //microsecond 

}
