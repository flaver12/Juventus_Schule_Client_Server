class DriveBot:
    motorSpeed = 0
    direction = 0
    sensor_range = 0

    def __init__(self) -> None:
     self.motorSpeed = 5
     self.direction = 90
     self.sensor_range = 10

r2d2 = DriveBot()
print(r2d2.motorSpeed)
print(r2d2.direction)
print(r2d2.sensor_range)