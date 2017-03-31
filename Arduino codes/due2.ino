#define RELAYBULB 7

void setup() {
  // put your setup code here, to run once:
pinMode(RELAYBULB,OUTPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
  char re=Serial.read();
  if(re=='a'){ 
    digitalWrite(RELAYBULB, HIGH);
  } 
  if(re=='c'){ 
    digitalWrite(RELAYBULB, LOW);
  }
}
