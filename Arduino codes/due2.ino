
#define RELAYBULB 7
#define RELAYBULB1 A0
void setup() {
  // put your setup code here, to run once:
pinMode(7,OUTPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
  char re=Serial.read();
  if(re=='c' || re=='d'){ 
    digitalWrite(RELAYBULB, HIGH);
    if(re=='c'){
      analogWrite(RELAYBULB1, 0);
    }
    else{
      analogWrite(RELAYBULB1, 255);
    }
  } 
  if(re=='b'){ 
    digitalWrite(RELAYBULB, LOW);
    analogWrite(RELAYBULB1, 0);

  }
}
}
