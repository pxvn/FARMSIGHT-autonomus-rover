#include <MD_Parola.h>
#include <MD_MAX72xx.h>
#include <SPI.h>

// Uncomment according to your hardware type
#define HARDWARE_TYPE MD_MAX72XX::FC16_HW
//#define HARDWARE_TYPE MD_MAX72XX::GENERIC_HW

// Defining size and output pins
#define MAX_DEVICES 4
#define CS_PIN 5

// Create an instance of the MD_Parola class
MD_Parola myDisplay = MD_Parola(HARDWARE_TYPE, CS_PIN, MAX_DEVICES);

void setup() {
  // Initialize the display
  myDisplay.begin();

  // Set the brightness of the display (0 to 15)
  myDisplay.setIntensity(5); // Moderate intensity for visibility

  // Clear the display at the start
  myDisplay.displayClear();

  // Set the animation and scrolling parameters (for main message)
  myDisplay.displayText("DigiKey", PA_CENTER, 50, 2000, PA_PRINT, PA_NO_EFFECT);
}

void loop() {
  // Check if the animation has completed
  if (myDisplay.displayAnimate()) {
    static bool showDigiKey = true;  // Toggle between DigiKey and the main message

    // Clear the display before showing new text
    myDisplay.displayClear();

    if (showDigiKey) {
      // Display "DigiKey" for 2 seconds
      myDisplay.displayText("DigiKey", PA_CENTER, 50, 4000, PA_PRINT, PA_NO_EFFECT);
    } else {
      // Display main marketing message with scrolling
      myDisplay.displayText("FarmSight Field Survey Rover - Powered by Maixduino - K210", 
                            PA_CENTER, 
                            50,          // Scroll speed (lower = faster)
                            1000,        // Pause after scrolling completes
                            PA_SCROLL_LEFT, 
                            PA_SCROLL_LEFT);
    }

    // Toggle to show the next message in the next loop
    showDigiKey = !showDigiKey;

    // Reset the display for the next animation cycle
    myDisplay.displayReset();
  }
}

