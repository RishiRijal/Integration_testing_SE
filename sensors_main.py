import sys

def main():
    limits = parse_limits()
    sensor_data = []

    if len(limits) > 0 and check_limits(limits):
        sensor_data = read_sensors()
        for row in sensor_data:
            print(row)
    else:
        print("Error: Incorrect command line arguments.")

def parse_limits():
    limits = []

    try:
        limits = [int(sys.argv[1]), int(sys.argv[2])]
    except Exception:
        pass
    
    return limits

def check_limits(limits):
    if limits[0] < limits[1]:
        return True
    else:
        return False

def read_sensors():
    return  [
            [21.2, 18.2, 18.2, 22.2],
            [-5.0, -4.2, -3.9, -4.5],
            [1.2, 0.0, 0.5, -0.8, -1.0],
            [25.0, -4.2, -13.9, 4.5]
            ]

if __name__ == "__main__":
    main()
