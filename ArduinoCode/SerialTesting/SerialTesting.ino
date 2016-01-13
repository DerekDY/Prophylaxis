/*
  Serial Event example
 
 When new serial data arrives, this sketch adds it to a String.
 When a newline is received, the loop prints the string and 
 clears it.
 
 A good test for this is to try it with a GPS receiver 
 that sends out NMEA 0183 sentences. 
 
 Created 9 May 2011
 by Tom Igoe
 
 This example code is in the public domain.
 
 http://www.arduino.cc/en/Tutorial/SerialEvent
 
 */

String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
}

void moveF(int steps){
  String outputString;
  for (int i=0; i < steps; i++){
    outputString += "1";
  }
  Serial.println(outputString);
}

void loop() {
  // print the string when a newline arrives:
  if (stringComplete) {
    if (inputString == "who\n"){
      Serial.println("#1");
    }
    else if (inputString.substring(0,1) == "f"){
      String number = inputString.substring(1);
      //Serial.println(number);
      int steps = number.toInt();
      //Serial.println(steps);
      moveF(steps);
    }
    else { 
      Serial.println(inputString); 
      // clear the string:
      
      
    }
    inputString = "";
    stringComplete = false;
    Serial.flush();
  }
}

/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read(); 
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    } 
  }
}


