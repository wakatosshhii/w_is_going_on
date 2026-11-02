import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberPublisher(Node):
    def __init__(self):
        super().__init__('even_pub')
        
        self.publisher_ = self.create_publisher(Int32, '/even_numbers', 10)
        self.overflow_publisher_ = self.create_publisher(Int32, '/overflow', 10)
        
        self.current_number = 0
        
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        msg.data = self.current_number
        
        self.publisher_.publish(msg)

        self.get_logger().info(f'Чётное число: {self.current_number}')
        
        if self.current_number >= 100:
            overflow_msg = Int32()
            overflow_msg.data = self.current_number
            self.overflow_publisher_.publish(overflow_msg)
            
            self.current_number = 0
        else:
            self.current_number += 2

def main(args=None):
    rclpy.init(args=args)
    node = EvenNumberPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()