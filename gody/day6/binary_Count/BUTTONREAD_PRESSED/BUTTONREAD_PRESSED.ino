
int led=2;
int led1=4;
int button=7;// PULL UP CONFIGURATION
int buttonread;
int buttonreadD;
int buttondown=8;//PULL DOWN 
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(led,OUTPUT);
pinMode(led1,OUTPUT);
pinMode(button,INPUT);
pinMode(buttondown,INPUT);

}

void loop() {
  //put your main code here, to run repeatedly:
buttonread=digitalRead(button);
Serial.println(buttonread);


if (buttonread==1)
{
  digitalWrite(led,LOW);
}else 
{
  digitalWrite(led,HIGH);

}

///////////////////////////
buttonreadD=digitalRead(buttondown);
Serial.println(buttonreadD);

if (buttonreadD==1)
{
  digitalWrite(led1,HIGH);
}else 
{
  digitalWrite(led1,LOW);

}
}
