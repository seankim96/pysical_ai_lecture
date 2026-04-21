robot_name = "BumperBot"
status_msg = "Emegency STop Active"
serial_port = "/dev/ttyUSB0"

print(f"로봇 이름: {robot_name} (타입: {type(robot_name).__name__})")

readings = [22.1, 25.4, 105.0, 23.8]

filtered_data = list(filter(lambda x: x < 50.0, readings))
print(f"필더링된 센서 값: {filtered_data}")

sensors = [{"id" : 2, "val": 1.5}, {"id" : 1, "val": 0.8}]

sensors.sort(key=lambda s: s["id"])

print(sensors)

def average_readings(*args):
    return sum(args) / len(args)

def configure_sensor(**kwargs):
    print(f"센서 설정: {kwargs}")

configure_sensor(resolution=0.01, prot="/dev/ttyUSB0", mode="continous")

