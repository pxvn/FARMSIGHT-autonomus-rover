#include <IBusBM.h>
#include <MD_MAX72xx.h>
#include <SPI.h>
#include <MD_Parola.h>
#include <CytronMotorDriver.h>
#include <Servo.h>

// Dot Matrix Display Configuration
#define HARDWARE_TYPE MD_MAX72XX::FC16_HW
#define MAX_DEVICES 4
#define CS_PIN 8

// Create an instance of the MD_Parola class for the dot matrix display
MD_Parola myDisplay = MD_Parola(HARDWARE_TYPE, CS_PIN, MAX_DEVICES);

// Motor Control Configuration
CytronMD motorlf(PWM_DIR, 6, 36);
CytronMD motorlm(PWM_DIR, 4, 40);
CytronMD motorlb(PWM_DIR, 2, 44);
CytronMD motorrf(PWM_DIR, 7, 38);
CytronMD motorrm(PWM_DIR, 5, 42);
CytronMD motorrb(PWM_DIR, 3, 46);

// Servo Configuration
Servo servoVertical, servoHorizontal1, servoHorizontal2;
int verticalServoPin = 11, horizontalServo1Pin = 10, horizontalServo2Pin = 9;

// iBus configuration
IBusBM ibus;

// Rover control variables
int throttle = 0;
int steering = 0;
int brake = 0;
int speedMultiplier = 100;  // Control speed scaling
int maxSpeed = 100;

// Define pins for the breathing LEDs
const int leftLED = 12;  // Left-side LED
const int rightLED = 13; // Right-side LED

// Variables for breathing and blinking effect
int ledBrightness = 0;       // Initial brightness
int fadeAmount = 15;         // Increased amount for faster breathing
bool fadingIn = true;        // Direction of the fade
unsigned long lastBlinkTime = 0; // Timestamp for blinking intervals
int blinkInterval = 100;     // Interval between blinks in milliseconds

void setup() {
  Serial.begin(115200);
  Serial2.begin(115200);
  Serial1.begin(115200);
  ibus.begin(Serial1);

  // Initialize Dot Matrix Display
  myDisplay.begin();
  myDisplay.setIntensity(5);
  myDisplay.displayClear();
  myDisplay.displayText("DigiKey", PA_CENTER, 50, 3000, PA_PRINT, PA_NO_EFFECT);

  // Show initial display
  delay(3000);

  // Initialize Servos
  servoVertical.attach(verticalServoPin);
  servoHorizontal1.attach(horizontalServo1Pin);
  servoHorizontal2.attach(horizontalServo2Pin);

  // Set up LED pins as output
  pinMode(leftLED, OUTPUT);
  pinMode(rightLED, OUTPUT);
}

void loop() {
  // Read values from the iBus channels
  int throttleRaw = ibus.readChannel(0);
  int steeringRaw = ibus.readChannel(1);
  int brakeRaw = ibus.readChannel(3);
  int verticalAngle = ibus.readChannel(2);  // Knob for vertical control
  int horizontalAngle = ibus.readChannel(5);  // Knob for horizontal control

  // Debug print to Serial Monitor
  Serial.print("Throttle: "); Serial.print(throttleRaw);
  Serial.print(" | Steering: "); Serial.print(steeringRaw);
  Serial.print(" | Brake: "); Serial.print(brakeRaw);
  Serial.print(" | Vertical: "); Serial.print(verticalAngle);
  Serial.print(" | Horizontal: "); Serial.println(horizontalAngle);

  // Check if the values are within valid iBus range (assuming 1000-2000)
  if (throttleRaw >= 1000 && throttleRaw <= 2000 && 
      steeringRaw >= 1000 && steeringRaw <= 2000 && 
      brakeRaw >= 1000 && brakeRaw <= 2000) {

    // Map and scale the values
    throttle = map(throttleRaw, 1000, 2000, -maxSpeed, maxSpeed);  // Throttle channel
    steering = map(steeringRaw, 1000, 2000, -maxSpeed, maxSpeed);  // Steering channel
    brake = map(brakeRaw, 1000, 2000, 0, 1);                       // Brake channel (toggle)

    // Control the motors based on iBus inputs
    driveMotors(throttle, steering, brake);
  }

  // Map servo angles for smooth control
  int mappedVertical = map(verticalAngle, 1000, 2000, 0, 180);
  int mappedHorizontal = map(horizontalAngle, 1000, 2000, 0, 180);

  // Control the servo smoothly with interpolation
  controlArmServoSmooth(servoVertical, mappedVertical);
  controlArmServoSmooth(servoHorizontal1, mappedHorizontal);
  controlArmServoSmooth(servoHorizontal2, mappedHorizontal);

  // Dot Matrix Animation
  if (myDisplay.displayAnimate()) {
    static int displayStage = 0;

    myDisplay.displayClear();
    if (displayStage == 0) {
      myDisplay.displayText("DigiKey", PA_CENTER, 50, 3000, PA_PRINT, PA_NO_EFFECT);
    } else {
      myDisplay.displayText("FarmSight - Field Survey Rover powered by Sipeed Maixduino and Arduino Mega",
                            PA_CENTER, 50, 1000, PA_SCROLL_LEFT, PA_SCROLL_LEFT);
    }

    displayStage = (displayStage + 1) % 2;  // Toggle between 0 and 1
    myDisplay.displayReset();
  }

  // Control LEDs for breathing and blinking effect
  breathingAndBlinkingEffect();
}

// Motor Control Function
void driveMotors(int throttle, int steering, int brake) {
  int leftSpeed = throttle + steering;
  int rightSpeed = throttle - steering;

  // Apply braking if brake channel is active
  if (brake == 1) {
    leftSpeed = 0;
    rightSpeed = 0;
  }

  // Constrain motor speeds within bounds
  leftSpeed = constrain(leftSpeed, -maxSpeed, maxSpeed);
  rightSpeed = constrain(rightSpeed, -maxSpeed, maxSpeed);

  // Set motor speeds for the left side
  motorlf.setSpeed(leftSpeed);
  motorlm.setSpeed(leftSpeed);
  motorlb.setSpeed(leftSpeed);

  // Set motor speeds for the right side
  motorrf.setSpeed(rightSpeed);
  motorrm.setSpeed(rightSpeed);
  motorrb.setSpeed(rightSpeed);
}

// Smooth Servo Control Function
void controlArmServoSmooth(Servo &servo, int targetAngle) {
  int currentAngle = servo.read();
  if (currentAngle < targetAngle) {
    for (int angle = currentAngle; angle <= targetAngle; angle++) {
      servo.write(angle);
      delay(5);  // Adjust for smoothness
    }
  } else if (currentAngle > targetAngle) {
    for (int angle = currentAngle; angle >= targetAngle; angle--) {
      servo.write(angle);
      delay(5);  // Adjust for smoothness
    }
  }
}

// Function for the breathing and blinking effect
void breathingAndBlinkingEffect() {
  unsigned long currentTime = millis();

  // Adjust brightness up or down based on fade direction
  if (fadingIn) {
    ledBrightness += fadeAmount;
    if (ledBrightness >= 255) {
      ledBrightness = 255;
      fadingIn = false;  // Switch to fading out
    }
  } else {
    ledBrightness -= fadeAmount;
    if (ledBrightness <= 0) {
      ledBrightness = 0;
      fadingIn = true;  // Switch to fading in
    }
  }

  // Set LED brightness
  analogWrite(leftLED, ledBrightness);
  analogWrite(rightLED, ledBrightness);

  // Blink briefly at min and max brightness
  if ((ledBrightness == 255 || ledBrightness == 0) && (currentTime - lastBlinkTime > blinkInterval)) {
    analogWrite(leftLED, 0);   // Turn off LEDs momentarily
    analogWrite(rightLED, 0);
    delay(50);                 // Short blink delay
    lastBlinkTime = currentTime;
  }

  // Small delay for smooth breathing effect
  delay(20);
}

