//#include<DiaaMind>
//Green ->3 , Red ->5 , Blue ->6 , servo ->10
#include<Servo.h>
int G=3,R=5,B=6;
int crr=90;
Servo Se;
void setup() {
Serial.begin(9600);
pinMode(R,OUTPUT);
pinMode(B,OUTPUT);
pinMode(G,OUTPUT);

Se.attach(10);
}

void loop() {
if(Serial.available()>0){
  char DiaaMake=Serial.read();
  delay(2);
  int value=Serial.read();
  if(DiaaMake=='G'){
    analogWrite(G,value);
  }
   if(DiaaMake=='R'){
    analogWrite(R,value);
  } if(DiaaMake=='B'){
    analogWrite(B,value);
  } if(DiaaMake=='S'){
    int q=map(value,0,255,0,180);
    q=q%30;
    crr+=q;
    if(crr>180)crr=0;
    else if(crr<0)crr=180;
    Se.write(crr);
    delay(150);
  }
} 
}
