#!/usr/bin/env python3
"""
Suction Control Node for CCR3 Chinese Chess Robot
ROS 2 Node to control vacuum pump and suction cup for picking/placing chess pieces
"""

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy

from std_srvs.srv import Trigger
from std_msgs.msg import Bool, Int32
from geometry_msgs.msg import Pose
from ccr3_suction_control.srv import PickChessPiece, PlaceChessPiece, CheckSuction

import serial
import time
import threading


class SuctionControl(Node):
    """
    ROS 2 Node for controlling vacuum suction cup
    Communicates with Arduino via Serial to control pump and valve
    """

    def __init__(self):
        super().__init__('suction_control')

        # Declare parameters
        self.declare_parameter('serial_port', '/dev/ttyUSB0')
        self.declare_parameter('baudrate', 115200)
        self.declare_parameter('pump_activation_time', 0.5)  # seconds
        self.declare_parameter('max_retry', 3)
        self.declare_parameter('suction_check_enabled', False)

        # Get parameters
        self.serial_port = self.get_parameter('serial_port').value
        self.baudrate = self.get_parameter('baudrate').value
        self.pump_activation_time = self.get_parameter('pump_activation_time').value
        self.max_retry = self.get_parameter('max_retry').value
        self.suction_check_enabled = self.get_parameter('suction_check_enabled').value

        # Serial connection
        self.serial_conn = None
        self.serial_lock = threading.Lock()

        # State
        self.is_picking = False
        self.last_suction_status = False

        # Initialize serial connection
        self._init_serial()

        # Create QoS profile
        qos = QoSProfile(
            reliability=ReliabilityPolicy.RELIABLE,
            history=HistoryPolicy.KEEP_LAST,
            depth=10
        )

        # Publishers
        self.status_pub = self.create_publisher(Bool, '~/status', qos)
        self.pressure_pub = self.create_publisher(Int32, '~/pressure', qos)

        # Subscribers
        self.create_subscription(Pose, '~/target_pose', self._target_pose_callback, qos)

        # Services
        self.create_service(PickChessPiece, '~/pick', self._pick_service)
        self.create_service(PlaceChessPiece, '~/place', self._place_service)
        self.create_service(CheckSuction, '~/check_suction', self._check_suction_service)
        self.create_service(Trigger, '~/pump_on', self._pump_on_service)
        self.create_service(Trigger, '~/pump_off', self._pump_off_service)

        self.get_logger().info('Suction Control Node initialized')

    def _init_serial(self):
        """Initialize serial connection with Arduino"""
        try:
            self.serial_conn = serial.Serial(
                port=self.serial_port,
                baudrate=self.baudrate,
                timeout=1.0
            )
            time.sleep(2)  # Wait for Arduino to reset
            self.get_logger().info(f'Connected to Arduino on {self.serial_port}')
        except serial.SerialException as e:
            self.get_logger().warn(f'Could not connect to Arduino: {e}')
            self.serial_conn = None

    def _send_command(self, command: str) -> bool:
        """Send command to Arduino via serial"""
        if not self.serial_conn:
            self.get_logger().error('Serial not connected')
            return False

        with self.serial_lock:
            try:
                self.serial_conn.write(f"{command}\n".encode())
                time.sleep(0.1)
                response = self.serial_conn.readline().decode().strip()
                self.get_logger().debug(f'Command: {command}, Response: {response}')
                return response == 'OK'
            except Exception as e:
                self.get_logger().error(f'Serial error: {e}')
                return False

    def _target_pose_callback(self, msg: Pose):
        """Callback for target pose - optional: auto-pick when at position"""
        # This can be used for automatic picking when arm reaches position
        pass

    def _pick_service(self, request, response):
        """Service to pick up a chess piece"""
        self.get_logger().info(f'Pick service called: position=({request.x}, {request.y}, {request.z})')

        # Check if already picking
        if self.is_picking:
            response.success = False
            response.message = 'Already picking'
            return response

        self.is_picking = True

        try:
            # Turn on pump
            if not self._send_command('PUMP_ON'):
                response.success = False
                response.message = 'Failed to turn on pump'
                return response

            # Wait for pump to create vacuum
            time.sleep(self.pump_activation_time)

            # Check suction status if enabled
            if self.suction_check_enabled:
                suction_ok = self._check_suction_status()
                if not suction_ok:
                    self._send_command('PUMP_OFF')
                    response.success = False
                    response.message = 'Suction failed - no piece detected'
                    return response

            response.success = True
            response.message = 'Piece picked successfully'
            self.last_suction_status = True

        except Exception as e:
            self.get_logger().error(f'Pick error: {e}')
            response.success = False
            response.message = str(e)
        finally:
            self.is_picking = False

        return response

    def _place_service(self, request, response):
        """Service to place a chess piece"""
        self.get_logger().info(f'Place service called: position=({request.x}, {request.y}, {request.z})')

        try:
            # Turn off pump to release piece
            if not self._send_command('PUMP_OFF'):
                response.success = False
                response.message = 'Failed to turn off pump'
                return response

            # Wait for release
            time.sleep(0.2)

            response.success = True
            response.message = 'Piece placed successfully'
            self.last_suction_status = False

        except Exception as e:
            self.get_logger().error(f'Place error: {e}')
            response.success = False
            response.message = str(e)

        return response

    def _check_suction_service(self, request, response):
        """Service to check suction status"""
        suction_ok = self._check_suction_status()
        response.success = suction_ok
        response.message = 'Suction OK' if suction_ok else 'Suction failed'
        return response

    def _check_suction_status(self) -> bool:
        """Check if suction is working (requires pressure sensor)"""
        if not self.serial_conn:
            return True  # Assume OK if no serial

        try:
            self.serial_conn.write(b"CHECK_STATUS\n")
            time.sleep(0.1)
            response = self.serial_conn.readline().decode().strip()
            return response == 'SUCTION_OK'
        except:
            return True  # Assume OK on error

    def _pump_on_service(self, request, response):
        """Service to turn on pump manually"""
        success = self._send_command('PUMP_ON')
        response.success = success
        response.message = 'Pump on' if success else 'Failed'
        return response

    def _pump_off_service(self, request, response):
        """Service to turn off pump manually"""
        success = self._send_command('PUMP_OFF')
        response.success = success
        response.message = 'Pump off' if success else 'Failed'
        return response

    def destroy_node(self):
        """Cleanup on shutdown"""
        if self.serial_conn and self.serial_conn.is_open:
            self._send_command('PUMP_OFF')
            self.serial_conn.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = SuctionControl()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
