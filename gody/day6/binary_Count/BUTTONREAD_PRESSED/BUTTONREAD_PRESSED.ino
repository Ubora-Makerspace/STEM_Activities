
int led=4;
int button=2;// PULL UP CONFIGURATION
int buttonread;
int buttonreadD;
int buttondown=8;//PULL DOWN 
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(led,OUTPUT);
pinMode(button,INPUT);
pinMode(buttondown,INPUT);



}

void loop() {
  // put your main code here, to run repeatedly:
buttonread=digitalRead(button);
Serial.println(buttonread);

buttonreadD=digitalRead(buttondown);
Serial.println(buttonread);

if (buttonread==1)
{
  digitalWrite(led,LOW);
}else 
{
  digitalWrite(led,HIGH);
}
/////////////////////////////////////////////////
if (buttonreadD==0)
{
  digitalWrite(led,LOW);
}else 
{
  digitalWrite(led,HIGH);
}
}
