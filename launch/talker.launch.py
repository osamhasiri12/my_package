from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
          packeage='demo_node_ccp',
          executable='talker'
        )
    ])