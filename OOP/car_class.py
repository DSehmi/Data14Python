class Car:
    def __init__(self, colour, speed: int):
        self.colour = colour
        self._speed = speed
        self.max_speed = 200

    def accelerate(self, increase: int):
        self._speed = self._speed + increase
        if self._speed > 200:
            self._speed = 200
        return self._speed

    def decelerate(self, decrease: int):
        self._speed = self._speed - decrease
        if self._speed < 0:
            self._speed = 0
        return self._speed

    def get_speed(self):
        return f"Your car is going at {self._speed}mph"


tesla = Car("Red", 180)
tesla.accelerate(30)
tesla.decelerate(0)
print(tesla.get_speed())

