class DriveBot:
    motorSpeed = 0
    direction = 0
    sensor_range = 0

    def __init__(self) -> None:
     self.motorSpeed = 5
     self.direction = 90
     self.sensor_range = 10

    def ajdust_sensor(self, value):
       self.sensor_range = value

    def control_bot(self, new_speed, new_direction):
       self.motorSpeed = new_speed
       self.direction = new_direction

r2d2 = DriveBot()
print(r2d2.motorSpeed)
print(r2d2.direction)
print(r2d2.sensor_range)

r2d2.ajdust_sensor(10)
r2d2.control_bot(20, 180)

print('===============')

print(r2d2.motorSpeed)
print(r2d2.direction)
print(r2d2.sensor_range)