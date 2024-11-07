#include <SoftwareSerial.h>
#include <CytronMotorDriver.h>

int invar;

//100 to stop
//200 to forward
//300 to backward
//400 to left
//500 to right

//left motors
CytronMD motorlf(PWM_DIR, 6, 36);
CytronMD motorlm(PWM_DIR, 4, 40);
CytronMD motorlb(PWM_DIR, 2, 44);
//right motors
CytronMD motorrf(PWM_DIR, 7, 38);
CytronMD motorrm(PWM_DIR, 5, 42);
CytronMD motorrb(PWM_DIR, 3, 46);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  delay(5000);

  forward();
  delay(6000);

  brake();
  delay(1000);

  rightturn();
  delay(5000);

  brake();
  delay(1000);

  forward();
  delay(4000);

  brake();
  delay(1000);

  leftturn();
  delay(5000);

  brake();
  delay(1000);

  backward();
  delay(4000);

  brake();
}

void forward() {
  motorlf.setSpeed(-100);
  motorlm.setSpeed(-100);
  motorlb.setSpeed(-100);
  motorrf.setSpeed(100);
  motorrm.setSpeed(100);
  motorrb.setSpeed(100);
}

void rightturn() {
  motorlf.setSpeed(-100);
  motorlm.setSpeed(-100);
  motorlb.setSpeed(-100);
  motorrf.setSpeed(-100);
  motorrm.setSpeed(-100);
  motorrb.setSpeed(-100);
}

void backward() {
  motorlf.setSpeed(100);
  motorlm.setSpeed(100);
  motorlb.setSpeed(100);
  motorrf.setSpeed(-100);
  motorrm.setSpeed(-100);
  motorrb.setSpeed(-100);
}

void leftturn() {
  motorlf.setSpeed(100);
  motorlm.setSpeed(100);
  motorlb.setSpeed(100);
  motorrf.setSpeed(100);
  motorrm.setSpeed(100);
  motorrb.setSpeed(100);
}

void brake() {
  motorlf.setSpeed(0);
  motorlm.setSpeed(0);
  motorlb.setSpeed(0);
  motorrf.setSpeed(0);
  motorrm.setSpeed(0);
  motorrb.setSpeed(0);
}

void loop() {
  
}
