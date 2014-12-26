/*****************************************************
 *****************************************************
 ****            Arduino Plant Monitor            ****
 ****          Author: William R. Sinkey          ****
 ****       Date Completed: 1 November 2014       ****
 *****************************************************
 *****************************************************/

//Variables used for pin locations
const short ledPin[] = {
  2, 3, 4, 5, 6, 7, 8, 9, 10, 11};
const short moistPin = A5;


//Variable used for simulating moisture level
int randMoist = 9;

//Ardunio setup fucntion; used for initilization
void setup(){
  for(int i = 0; i < 10; i++) {  //Setup all LED pins to OUTPUT
    pinMode(ledPin[i], OUTPUT);
  }

  Serial.begin(9600);  //Set Serial port buad rate
  Serial.flush();

  Serial.println("Arduino Plant Monitor Initiated...");  
}

void loop(){
  //Check the mositure level and print it to the Serial port
  checkMoisture(analogRead(A5));
  Serial.println(analogRead(A5));

  //Used for troubleshooting; input values ex. "o9" = 9
  /*  if (Serial.available() > 0) {
   if (Serial.peek() == 'o') {
   randMoist = Serial.parseInt();
   while (Serial.available() > 0) {
   Serial.read();
   }
   }
   }
   Serial.println(randMoist);
   checkMoisture(randMoist);
   */
}

//alert function used to control the LEDs
void alert(int intensity) {
  delay(50);  //Delay to allow updates on moisture levels
  //Set LED displayed based on intesity level
  for(int i = 0; i < 10; i++) {
    digitalWrite(ledPin[i], HIGH);
    delay(intensity);       
  }
  for(int i = 10; i >= 0; i--) {
    digitalWrite(ledPin[i], LOW);
    delay(intensity);
  }
}

//checkMoisture function used to set the intensity of the LEDs
//and display a message to the user over the Serial port
int checkMoisture(int moisture) {
  if (moisture <= 100) {
    Serial.println("I need water NOW!!");  
    alert(15);
  }
  else if (moisture <= 200) {
    Serial.println("Starting to freak out...I need water ahora!");  
    alert(25);
  }  
  else   if (moisture <= 300) {
    Serial.println("Haha, maybe you didn't hear me");  
    alert(35);
  }
  else if (moisture <= 400) {
    Serial.println("I could really use that water right now...");  
    alert(45);
  }  
  else if (moisture <= 500) {
    Serial.println("Hey, I'm a little thirsty...");
    alert(60);
  }  
  //Serial.println(moisture);  //Used for troubleshooting
}



