int led=3;
int port=A0;
int value;
float voltage;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(led,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
value= analogRead(port);
Serial.print("Value: ");
Serial.println(value);
voltage=((value*5)/1023);
Serial.print("voltage: ");
Serial.println(voltage);
delay (1000);

if (voltage >= 3){
digitalWrite(led,HIGH);
}
else {
  digitalWrite(led,LOW);
}
}
