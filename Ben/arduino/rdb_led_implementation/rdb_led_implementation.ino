
int redPin   = 9;
int greenPin = 10;
int bluePin  = 11;


bool commonAnode = false;

void setup() {
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}


void setColor(int r, int g, int b) {
  if (commonAnode) {
    r = 255 - r;
    g = 255 - g;
    b = 255 - b;
  }
  analogWrite(redPin, r);
  analogWrite(greenPin, g);
  analogWrite(bluePin, b);
}


void showMainColors() {
  setColor(255, 0, 0);     delay(1000);  // Red
  setColor(0, 255, 0);     delay(1000);  // Green
  setColor(0, 0, 255);     delay(1000);  // Blue
  setColor(255, 255, 0);   delay(1000);  // Yellow
  setColor(0, 255, 255);   delay(1000);  // Cyan
  setColor(255, 0, 255);   delay(1000);  // Magenta
  setColor(255, 128, 0);   delay(1000);  // Orange
  setColor(128, 0, 255);   delay(1000);  // Purple
  setColor(255, 105, 180); delay(1000);  // Pink
  setColor(255, 255, 255); delay(1000);  // White (balanced)
  setColor(0, 0, 0);       delay(1000);  // Off
}

// Smoothly fades through every color of the rainbow
void rainbowFade() {
  // Red -> Yellow (green goes up)
  for (int i = 0; i <= 255; i++) { setColor(255, i, 0);       delay(10); }
  // Yellow -> Green (red goes down)
  for (int i = 255; i >= 0; i--) { setColor(i, 255, 0);       delay(10); }
  // Green -> Cyan (blue goes up)
  for (int i = 0; i <= 255; i++) { setColor(0, 255, i);       delay(10); }
  // Cyan -> Blue (green goes down)
  for (int i = 255; i >= 0; i--) { setColor(0, i, 255);       delay(10); }
  // Blue -> Magenta (red goes up)
  for (int i = 0; i <= 255; i++) { setColor(i, 0, 255);       delay(10); }
  // Magenta -> Red (blue goes down)
  for (int i = 255; i >= 0; i--) { setColor(255, 0, i);       delay(10); }
}

void loop() {
  showMainColors();   // step through named colors
  rainbowFade();      // then smooth rainbow
  rainbowFade();      // twice for a nice effect
}