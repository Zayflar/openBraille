int motorPins[6][2] = {
  {2, 3},
  {4, 5},
  {6, 7},
  {8, 9},
  {10, 11},
  {12, 13}
};


int motorStates[6] = {1, 0, 1, 0, 1, 1};

void setup() {
  for (int i = 0; i < 6; i++) {
    pinMode(motorPins[i][0], OUTPUT);
    pinMode(motorPins[i][1], OUTPUT);
    digitalWrite(motorPins[i][0], LOW);
    digitalWrite(motorPins[i][1], LOW);
  }
}

void loop() {
  runMotorsAccordingToState();
  delay(2000);
  stopAllMotors();
  delay(1000);
}

void runMotorsAccordingToState() {
  for (int i = 0; i < 6; i++) {
    if (motorStates[i] == 1) {
      digitalWrite(motorPins[i][0], HIGH);
      digitalWrite(motorPins[i][1], LOW);
    } else {
      digitalWrite(motorPins[i][0], LOW);
      digitalWrite(motorPins[i][1], LOW);
    }
  }
}

void stopAllMotors() {
  for (int i = 0; i < 6; i++) {
    digitalWrite(motorPins[i][0], LOW);
    digitalWrite(motorPins[i][1], LOW);
  }
}
