/* 
 *  MotorY 
 *  Serial Communication and Bluetooth
 */

//Serial
#define clkPin 2
#define dirPin 3
#define initSpeed 800 // lower is faster
#define maxSpeed 100    // lower is faster
#define limitPin 7
#define fiveVolt = 27

String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

//Bluetooth
#include <SPI.h>
#include "Adafruit_BLE_UART.h"

// Connect CLK/MISO/MOSI to hardware SPI
// e.g. On UNO & compatible: CLK = 13, MISO = 12, MOSI = 11
#define ADAFRUITBLE_REQ 10
#define ADAFRUITBLE_RDY 2     // This should be an interrupt pin, on Uno thats #2 or #3
#define ADAFRUITBLE_RST 9

Adafruit_BLE_UART BTLEserial = Adafruit_BLE_UART(ADAFRUITBLE_REQ, ADAFRUITBLE_RDY, ADAFRUITBLE_RST);

//Serial
void setup() {
  //Serial
  // initialize serial:
  Serial.begin(9600);
  //pinMode(fiveVolt, OUTPUT);
  //digitalWrite(fiveVolt, HIGH);
  pinMode(clkPin, OUTPUT); //5v pin
  pinMode(dirPin, OUTPUT); //5v pinf299
  pinMode(limitPin, INPUT); //limit switch 
  digitalWrite(dirPin, LOW);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);

  //Bluetooth
  //Serial.begin(9600);
  while(!Serial); // Leonardo/Micro should wait for serial init
  //Serial.println(F("Adafruit Bluefruit Low Energy nRF8001 Print echo demo"));

  BTLEserial.setDeviceName("ProphBT"); /* 7 characters max! */

  BTLEserial.begin();
}

void moveF(int steps){
  long speedup = 0;
  boolean errorFound = false;
  digitalWrite(dirPin, HIGH);
  for(long i = 0; i < steps; i++){
    if (digitalRead(limitPin) == HIGH){
      errorFound = true;
      Serial.println("Zero Error");
      break;
    }
    digitalWrite(clkPin, HIGH);  
    delayMicroseconds(initSpeed - speedup);        //10000 hz       
    digitalWrite(clkPin, LOW);   
    delayMicroseconds(initSpeed - speedup);
    if ((i < ((initSpeed - maxSpeed))) && steps > (initSpeed - maxSpeed) * 2){
      speedup += 1;
    }
    else if ((i >= (initSpeed - maxSpeed)) && (i > (steps-(initSpeed - maxSpeed))) && (steps > (initSpeed - maxSpeed)*2)){
      speedup -= 1; 
    }
  }
  if(!errorFound){
    Serial.println("Done");
  }
}

void moveB(int steps){
  long speedup = 0;
  boolean errorFound = false;
  digitalWrite(dirPin, LOW);
  for(long i = 0; i < steps; i++){
    if (digitalRead(limitPin) == HIGH){
      errorFound = true;
      Serial.println("Zero Error");
      break;
    }
    digitalWrite(clkPin, HIGH);  
    delayMicroseconds(initSpeed - speedup);        //10000 hz       
    digitalWrite(clkPin, LOW);   
    delayMicroseconds(initSpeed - speedup);
    if ((i < ((initSpeed - maxSpeed))) && steps > (initSpeed - maxSpeed) * 2){
      speedup += 1;
    }
    else if ((i >= (initSpeed - maxSpeed)) && (i > (steps-(initSpeed - maxSpeed))) && (steps > (initSpeed - maxSpeed)*2)){
      speedup -= 1; 
    }
  }
  if(!errorFound){
    Serial.println("Done");
  }
}


void zero(){
  digitalWrite(dirPin, LOW);
  while (true) {
    if (digitalRead(limitPin) == HIGH){
      break;
    }
    digitalWrite(clkPin, HIGH);  
    delayMicroseconds(initSpeed);        //10000 hz       
    digitalWrite(clkPin, LOW);   
    delayMicroseconds(initSpeed);
  }
  Serial.println("Done");
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




void bluetooth(String sendStr){
      Serial.println("BT\n");
      //convert string to bytes for bluetooth
      uint8_t sendbuffer[20];
      sendStr.getBytes(sendbuffer, 20);
      char sendbuffersize = min(20, sendStr.length());
      //write to bluetooth
      BTLEserial.write(sendbuffer, sendbuffersize);
}


aci_evt_opcode_t laststatus = ACI_EVT_DISCONNECTED;

void loop()
{
  //Bluetooth Loop
  
  // Tell the nRF8001 to do whatever it should be working on.
  BTLEserial.pollACI();

  // Ask what is our current status
  aci_evt_opcode_t status = BTLEserial.getState();
  // If the status changed....
  if (status != laststatus) {
    // print it out!
    if (status == ACI_EVT_DEVICE_STARTED) {
        Serial.println(F("* Advertising started"));
    }
    if (status == ACI_EVT_CONNECTED) {
        Serial.println(F("* Connected!"));
    }
    if (status == ACI_EVT_DISCONNECTED) {
        Serial.println(F("* Disconnected"));
    }
    // OK set the last status change to this one
    laststatus = status;
  }

  if (status == ACI_EVT_CONNECTED) {
    // Lets see if there's any data for us!
    if (BTLEserial.available()) {
      Serial.print("* "); Serial.print(BTLEserial.available()); Serial.println(F(" bytes available from BTLE"));
    }
    // OK while we still have something to read, get a character and print it out
    while (BTLEserial.available()) {
      char c = BTLEserial.read();
      Serial.print(c);
    }

    // Next up, see if we have any data to get from the Serial console
/*
    if (Serial.available()) {
      // Read a line from Serial
      Serial.setTimeout(100); // 100 millisecond timeout
      String s = Serial.readString();

      // We need to convert the line to bytes, no more than 20 at this time
      uint8_t sendbuffer[20];
      s.getBytes(sendbuffer, 20);
      char sendbuffersize = min(20, s.length());

      Serial.print(F("\n* Sending -> \"")); Serial.print((char *)sendbuffer); Serial.println("\"");

      // write the data
      BTLEserial.write(sendbuffer, sendbuffersize);
    }
*/
  }

  //Serial Loop

  // print the string when a newline arrives:
  if (stringComplete) {
    if (inputString == "who\n"){
      Serial.println("Y");
    }
    else if (inputString.substring(0,1) == "f"){
      String number = inputString.substring(1);
      //Serial.println(number);
      long steps = number.toInt();
      //Serial.println(steps);
      moveF(steps);
    }
    else if (inputString.substring(0,1) == "b"){
      String number = inputString.substring(1);
      //Serial.println(number);
      long steps = number.toInt();
      //Serial.println(steps);
      moveB(steps);
    }
    else if (inputString.substring(0,1) == "t"){
      Serial.println("inT\n");
      String sendStr = inputString.substring(1,7);
      Serial.println("Str:\n");
      Serial.println(sendStr);
      /*
      if (Serial.available()) {
      // Read a line from Serial
      Serial.setTimeout(100); // 100 millisecond timeout
      String s = Serial.readString();
      */
      bluetooth(sendStr);    
    }
    else if (inputString == "zero\n"){
      zero();
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















