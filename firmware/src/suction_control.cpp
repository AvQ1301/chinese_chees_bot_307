/*
 * CCR3 Suction Control - Arduino Firmware
 * Controls vacuum pump and valve via serial commands from Raspberry Pi (ROS 2)
 *
 * Hardware connections:
 * - D2: Pump relay control (HIGH = ON, LOW = OFF)
 * - D3: Valve relay control (HIGH = Open, LOW = Close)
 * - A0: Pressure sensor analog input (optional)
 *
 * Serial Commands:
 * - PUMP_ON: Turn on vacuum pump
 * - PUMP_OFF: Turn off vacuum pump / release piece
 * - VALVE_OPEN: Open release valve
 * - VALVE_CLOSE: Close release valve
 * - CHECK_STATUS: Check if suction is successful (requires pressure sensor)
 */

#include <Arduino.h>

// Pin definitions
const int PUMP_PIN = 2;      // Pump relay control
const int VALVE_PIN = 3;     // Valve relay control
const int PRESSURE_SENSOR = A0;  // Pressure sensor (optional)

// Thresholds
const int PRESSURE_THRESHOLD = 300;  // Adjust based on your sensor

// State
bool pumpState = false;
bool valveState = false;

void setup() {
    Serial.begin(115200);

    // Set pin modes
    pinMode(PUMP_PIN, OUTPUT);
    pinMode(VALVE_PIN, OUTPUT);
    pinMode(PRESSURE_SENSOR, INPUT);

    // Initialize off
    digitalWrite(PUMP_PIN, LOW);
    digitalWrite(VALVE_PIN, LOW);

    Serial.println("CCR3 Suction Control Ready");
}

void loop() {
    if (Serial.available()) {
        String command = Serial.readStringUntil('\n');
        command.trim();
        command.toUpperCase();

        if (command == "PUMP_ON") {
            digitalWrite(PUMP_PIN, HIGH);
            pumpState = true;
            Serial.println("OK");
        }
        else if (command == "PUMP_OFF") {
            digitalWrite(PUMP_PIN, LOW);
            digitalWrite(VALVE_PIN, LOW);  // Also close valve
            pumpState = false;
            valveState = false;
            Serial.println("OK");
        }
        else if (command == "VALVE_OPEN") {
            digitalWrite(VALVE_PIN, HIGH);
            valveState = true;
            Serial.println("OK");
        }
        else if (command == "VALVE_CLOSE") {
            digitalWrite(VALVE_PIN, LOW);
            valveState = false;
            Serial.println("OK");
        }
        else if (command == "CHECK_STATUS") {
            int pressure = analogRead(PRESSURE_SENSOR);
            if (pressure > PRESSURE_THRESHOLD && pumpState) {
                Serial.println("SUCTION_OK");
            } else {
                Serial.println("SUCTION_FAIL");
            }
        }
        else if (command == "STATUS") {
            Serial.print("PUMP:");
            Serial.println(pumpState ? "ON" : "OFF");
            Serial.print("VALVE:");
            Serial.println(valveState ? "OPEN" : "CLOSED");
            Serial.print("PRESSURE:");
            Serial.println(analogRead(PRESSURE_SENSOR));
        }
        else {
            Serial.println("UNKNOWN");
        }
    }

    delay(10);
}
