int led=2;
int state=0;
int oldbutton=0;
int buttonpin=7;
int newpressed;

void setup() {
  // put your setup code here, to run once:
pinMode(buttonpin, INPUT);
pinMode(led, OUTPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
newpressed=digitalRead(buttonpin);
// Serial.println(newpressed);
//check the state
if (oldbutton==1 && newpressed==0){
       // if (state==0){
        digitalWrite(led,HIGH);
        state=1;
       // }

        else {
          digitalWrite(led, LOW);
          state=0;
        }

//}
oldbutton=newpressed;
Serial.print("oldbutton: ");
Serial.println(oldbutton);
delay(200);
}
