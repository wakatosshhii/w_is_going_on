from setuptools import find_packages, setup

package_name = 'w_is_going_on'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wakat',
    maintainer_email='wakat@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
     entry_points={
        'console_scripts': [
            'first_node = w_is_going_on.first_node:main',
            'time_printer = w_is_going_on.time_printer:main', 
        ],
    },
)
