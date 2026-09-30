int blue =2;// define the pin.
int green =4;// define the pin.
int red =7;// define the pin.
void setup() {
  // put your setup code here, to run once:
pinMode(blue, OUTPUT);// Identify type of device connected pin and wether is INPUT/OUTPUT.
pinMode(green, OUTPUT);
pinMode(red, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(red,HIGH); 
digitalWrite(green,HIGH); 
digitalWrite(blue,HIGH);
// delay(50); //microsecond 
// digitalWrite(red,LOW);
// digitalWrite(green,LOW);
// delay(50); //microsecond 
}

// digitalWrite(green,HIGH);
// delay(50); //microsecond 
// digitalWrite(green,LOW);
// delay(50); //microsecond 
// }

// digitalWrite(blue,HIGH);
// delay(50); //microsecond 
// digitalWrite(blue,LOW);
// delay(50); //microsecond 
// }
