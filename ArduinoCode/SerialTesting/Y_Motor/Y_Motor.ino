/*
Serial Comunication witht the motors 
 */

#define clkPin 2
#define dirPin 3
#define initSpeed 800 // lower is faster
#define maxSpeed 100    // lower is faster
#define limitPin 7
#define fiveVolt = 27

String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

void setup() {
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



void loop() {
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


