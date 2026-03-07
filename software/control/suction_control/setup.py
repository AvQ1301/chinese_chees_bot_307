from setuptools import setup
import os
from glob import glob

package_name = 'ccr3_suction_control'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/srv', glob('srv/*.srv')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Vo Anh Quan',
    maintainer_email='quan.va300475@gmail.com',
    description='ROS 2 package for controlling vacuum suction cup on CCR3 Chinese Chess Robot',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'suction_control = ' + package_name + '.suction_control:main',
            'suction_test = ' + package_name + '.test.test_suction:main',
            'suction_standalone = ' + package_name + '.suction_control_standalone:main',
        ],
    },
)
