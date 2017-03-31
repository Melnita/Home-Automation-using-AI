void setup() {
  // put your setup code here, to run once:
pinMode(7,OUTPUT);
pinMode(13,OUTPUT);
//Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
 // if(Serial.available()){
//  char re=Serial.read();
   // digitalWrite(13, LOW);
 // if(re=='a'){ 
    digitalWrite(7, HIGH);
 // } 
    delay(2000);
  //if(re=='c'){ 
    digitalWrite(7, LOW);
    delay(2000);
  //}
}
