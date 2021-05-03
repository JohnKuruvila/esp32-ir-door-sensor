#include "WiFi.h"
#include "WebServer.h"

const char* ssid = "";
const char* password =  "";
const byte sensorPin = ;

bool door_open = false;

WebServer server(80);

void handle_door_status() {
  String response_string;
  
  if(door_open){
    response_string = "{\"door_open\" : 1}";
  }
  else {
    response_string = "{\"door_open\" : 0}";
  }
  
  server.send(200, "text/json", response_string);
}

void setup() {
  Serial.begin(9600);
  WiFi.begin(ssid, password);

  server.on("/door_status", handle_door_status);
  server.begin();
}

void loop() {
  int reading = !digitalRead(sensorPin);
  if(reading) {
    door_open = false;
  }
  else {
    door_open = true;
  }
  server.handleClient();
  delay(200);
}
