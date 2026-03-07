#!/usr/bin/env python3
"""
Test script for Suction Control Node
Tests pick, place, and check_suction functions
"""

import rclpy
from rclpy.node import Node

from ccr3_suction_control.srv import PickChessPiece, PlaceChessPiece, CheckSuction
from std_srvs.srv import Trigger


class SuctionTest(Node):
    def __init__(self):
        super().__init__('suction_test')

    def test_pick(self):
        """Test picking a piece"""
        self.get_logger().info('Testing PICK...')
        client = self.create_client(PickChessPiece, '/suction_control/pick')

        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn('Service not available, waiting...')

        request = PickChessPiece.Request()
        request.x = 0.0
        request.y = 0.0
        request.z = 0.0

        future = client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            result = future.result()
            self.get_logger().info(f'Pick result: {result.success}, {result.message}')
            return result.success
        else:
            self.get_logger().error('Service call failed')
            return False

    def test_place(self):
        """Test placing a piece"""
        self.get_logger().info('Testing PLACE...')
        client = self.create_client(PlaceChessPiece, '/suction_control/place')

        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn('Service not available, waiting...')

        request = PlaceChessPiece.Request()
        request.x = 1.0
        request.y = 1.0
        request.z = 0.0

        future = client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            result = future.result()
            self.get_logger().info(f'Place result: {result.success}, {result.message}')
            return result.success
        else:
            self.get_logger().error('Service call failed')
            return False

    def test_check_suction(self):
        """Test checking suction status"""
        self.get_logger().info('Testing CHECK SUCTION...')
        client = self.create_client(CheckSuction, '/suction_control/check_suction')

        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn('Service not available, waiting...')

        request = CheckSuction.Request()

        future = client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            result = future.result()
            self.get_logger().info(f'Check suction result: {result.success}, {result.message}')
            return result.success
        else:
            self.get_logger().error('Service call failed')
            return False


def main(args=None):
    rclpy.init(args=args)
    tester = SuctionTest()

    try:
        # Run tests
        print("\n" + "="*50)
        print("CCR3 Suction Control Test")
        print("="*50)

        # Test 1: Check suction before picking
        tester.test_check_suction()

        # Test 2: Pick a piece
        tester.test_pick()

        # Test 3: Check suction after picking
        tester.test_check_suction()

        # Test 4: Place the piece
        tester.test_place()

        print("="*50)
        print("Test completed!")
        print("="*50 + "\n")

    except KeyboardInterrupt:
        pass
    finally:
        tester.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
