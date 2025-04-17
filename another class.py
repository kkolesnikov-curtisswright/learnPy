class TemperatureData:
    # Constructor to create object
    def __init__(self, name, readings):
        self.name = name
        self.readings = readings

    # Calculate average temperatures
    def calculate_average_temp(self):
        return sum(self.readings) / len(self.readings)

    # Find highest temperature
    def find_high_temp(self):
        return max(self.readings)

    # Find lowest temperature
    def find_low_temp(self):
        return min(self.readings)
    
    # Find temperature range (max-min)
    def calc_range(self):
        highest = self.find_high_temp()
        lowest = self.find_low_temp()

        if (highest > lowest):
            return highest - lowest
        else:
            return lowest - highest

# Create a name for a sensor
sensor_name = "East Forest Road Sensor"

sensor = TemperatureData(sensor_name, [75, 71, 90, 64, 88])

average_temp = sensor.calculate_average_temp()
print(f"Average temperature for sensor {sensor_name}: {average_temp} degrees Fahrenheit")

highest = sensor.find_high_temp()
lowest = sensor.find_low_temp()
print(f"Temperature extremes for sensor {sensor_name}: Highest {highest}, Lowest {lowest}") 
# Code above this point is unchanged, except for removing the function

# New call to method in TemperatureData
range = sensor.calc_range()
print(f"Temperature range for sensor {sensor_name}: {range} degrees Fahrenheit")
