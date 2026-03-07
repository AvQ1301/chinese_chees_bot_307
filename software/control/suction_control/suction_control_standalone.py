#!/usr/bin/env python3
"""
Standalone Suction Control - No ROS Required
For testing and development without ROS 2 running

Usage:
    python3 suction_control_standalone.py
    then type commands: PICK, PLACE, CHECK, PUMP_ON, PUMP_OFF
"""

import serial
import time
import sys


class SuctionControlStandalone:
    """Standalone suction control for direct Arduino communication"""

    def __init__(self, port='/dev/ttyUSB0', baudrate=115200):
        self.serial_port = port
        self.baudrate = baudrate
        self.serial_conn = None
        self.is_connected = False

    def connect(self):
        """Connect to Arduino"""
        try:
            self.serial_conn = serial.Serial(
                port=self.serial_port,
                baudrate=self.baudrate,
                timeout=1.0
            )
            time.sleep(2)
            self.is_connected = True
            print(f"Connected to {self.serial_port}")
        except serial.SerialException as e:
            print(f"Connection failed: {e}")
            self.is_connected = False

    def send_command(self, command: str) -> str:
        """Send command and return response"""
        if not self.is_connected:
            print("Not connected!")
            return ""

        try:
            self.serial_conn.write(f"{command}\n".encode())
            time.sleep(0.2)
            response = self.serial_conn.readline().decode().strip()
            return response
        except Exception as e:
            print(f"Error: {e}")
            return ""

    def pick(self) -> bool:
        """Pick up a chess piece"""
        print("Picking...")
        # Turn on pump
        self.send_command("PUMP_ON")
        # Wait for vacuum
        time.sleep(0.5)
        # Check status
        response = self.send_command("CHECK_STATUS")
        if "OK" in response:
            print("Pick successful!")
            return True
        else:
            print("Pick failed!")
            self.send_command("PUMP_OFF")
            return False

    def place(self) -> bool:
        """Place the chess piece"""
        print("Placing...")
        self.send_command("PUMP_OFF")
        time.sleep(0.2)
        print("Place successful!")
        return True

    def check_suction(self) -> bool:
        """Check suction status"""
        response = self.send_command("CHECK_STATUS")
        return "OK" in response

    def interactive(self):
        """Interactive mode"""
        print("\n" + "="*50)
        print("CCR3 Suction Control - Interactive Mode")
        print("="*50)
        print("Commands: PICK, PLACE, CHECK, PUMP_ON, PUMP_OFF, STATUS, QUIT")
        print("="*50 + "\n")

        while True:
            try:
                cmd = input("> ").strip().upper()

                if cmd == "QUIT":
                    break
                elif cmd == "PICK":
                    self.pick()
                elif cmd == "PLACE":
                    self.place()
                elif cmd == "CHECK":
                    if self.check_suction():
                        print("Suction OK")
                    else:
                        print("Suction FAIL")
                elif cmd == "PUMP_ON":
                    self.send_command("PUMP_ON")
                    print("Pump ON")
                elif cmd == "PUMP_OFF":
                    self.send_command("PUMP_OFF")
                    print("Pump OFF")
                elif cmd == "STATUS":
                    self.send_command("STATUS")
                else:
                    self.send_command(cmd)
                    print(f"Response: {self.send_command(cmd)}")

            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Error: {e}")

        print("\nDisconnecting...")
        if self.is_connected:
            self.send_command("PUMP_OFF")
            self.serial_conn.close()


def main():
    port = '/dev/ttyUSB0'
    if len(sys.argv) > 1:
        port = sys.argv[1]

    control = SuctionControlStandalone(port)
    control.connect()

    if control.is_connected:
        control.interactive()
    else:
        # Demo mode without hardware
        print("\nRunning in DEMO mode (no hardware)...")
        print("This simulates the suction control workflow.\n")

        print("=== DEMO: Pick and Place Sequence ===\n")

        print("1. Arm moves to piece position...")
        time.sleep(0.5)

        print("2. Turning on pump...")
        time.sleep(0.5)

        print("3. Checking suction...")
        time.sleep(0.2)
        print("   -> Suction OK! Piece picked.\n")

        print("4. Arm moves to destination...")
        time.sleep(1.0)

        print("5. Placing piece...")
        time.sleep(0.2)
        print("   -> Piece placed successfully!\n")

        print("=== Demo Complete ===")
        print("\nTo use with real hardware:")
        print("  1. Upload suction_control.cpp to Arduino")
        print("  2. Connect Arduino to Raspberry Pi via USB")
        print("  3. Run: python3 suction_control_standalone.py /dev/ttyUSB0")


if __name__ == '__main__':
    main()
