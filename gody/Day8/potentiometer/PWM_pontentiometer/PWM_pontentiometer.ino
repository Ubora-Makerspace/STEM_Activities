int led=3;
int port=A0;
int value;
float voltage;
int bright;
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
// delay (1000);

bright=map(value,0,1023,0,255);
Serial.print("bright: ");
Serial.println(bright);
analogWrite(led,bright);
}
