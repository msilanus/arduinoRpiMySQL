const int sensorPin = A0;    // select the input pin for the potentiometer
const int led = 13;
int sensorValue = 0;  // variable to store the value coming from the sensor
char recu;

void setup() {
  Serial.begin(9600);
  pinMode(led,OUTPUT);
  digitalWrite(led,LOW);
}

void loop() {
  // read the value from the sensor:
  sensorValue = analogRead(sensorPin);
  if(Serial.available()>0)
  {
    recu = Serial.read();
    if(recu=='M')
    {
      digitalWrite(led,HIGH);
      Serial.println(sensorValue);
      delay(250);
    }
    digitalWrite(led,LOW);
  }
}
