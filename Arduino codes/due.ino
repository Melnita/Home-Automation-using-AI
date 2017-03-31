void setup() {
  // put your setup code here, to run once:
pinMode(13, OUTPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available()){
  char re=Serial.read();
  
  if(re=='a'){ 
    digitalWrite(13, HIGH);
  } 
   if(re=='b'){ 
    digitalWrite(13, LOW);
  } 
  }
}
