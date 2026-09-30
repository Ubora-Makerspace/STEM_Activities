int gid4=5;
int gid3=4;
int gid2=3;
int gid1=2;

void setup() {
  // put your setup code here, to run once:
pinMode(gid1,OUTPUT);
pinMode(gid2,OUTPUT);
pinMode(gid3,OUTPUT);
pinMode(gid4,OUTPUT);
}

void loop() {
  // Binary 0001
digitalWrite(gid1,LOW);
digitalWrite(gid2,LOW);
digitalWrite(gid3,LOW);
digitalWrite(gid4,HIGH);
delay(1000);
  // Binary 0010
digitalWrite(gid1,LOW);
digitalWrite(gid2,LOW);
digitalWrite(gid3,HIGH);
digitalWrite(gid4,LOW);
delay(1000);
  // Binary 0011
digitalWrite(gid1,LOW);
digitalWrite(gid2,LOW);
digitalWrite(gid3,HIGH);
digitalWrite(gid4,HIGH);
delay(1000);

 // Binary 0100
digitalWrite(gid1,LOW);
digitalWrite(gid2,HIGH);
digitalWrite(gid3,LOW);
digitalWrite(gid4,LOW);
delay(1000);

 // Binary 0101
digitalWrite(gid1,LOW);
digitalWrite(gid2,HIGH);
digitalWrite(gid3,LOW);
digitalWrite(gid4,HIGH);
delay(1000);

 // Binary 0110
digitalWrite(gid1,LOW);
digitalWrite(gid2,HIGH);
digitalWrite(gid3,HIGH);
digitalWrite(gid4,LOW);
delay(1000);

// Binary 0111
digitalWrite(gid1,LOW);
digitalWrite(gid2,HIGH);
digitalWrite(gid3,HIGH);
digitalWrite(gid4,HIGH);
delay(1000);

// Binary 0100
digitalWrite(gid1,LOW);
digitalWrite(gid2,HIGH);
digitalWrite(gid3,LOW);
digitalWrite(gid4,LOW);
delay(1000);
}