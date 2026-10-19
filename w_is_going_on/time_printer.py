#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import time

class TimePrinter(Node):
    def __init__(self):
        super().__init__('time_printer_node')
        self.timer = self.create_timer(5.0, self.timer_callback)
        self.get_logger().info("Узел time_printer запущен. Ждем 5 секунд...")

    def timer_callback(self):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.get_logger().info(f"Текущее время: {current_time}")

def main(args=None):
    rclpy.init(args=args)
    node = TimePrinter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
