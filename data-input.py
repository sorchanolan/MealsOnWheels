import pandas as pd


def get_day(day_string):
    if "Sat" in day_string:
        return day_string.replace(" only", "urday")
    else:
        return day_string.replace(" only", "day")


class Driver:
    def __init__(self, row):
        if row.get('name') != 'Driver: ':
            self.name = row.get('name')
        else:
            self.name = ""
        self.route = row.get('route')
        self.day = get_day(row.get('day'))

    def __str__(self):
        return f"{self.name}, {self.route}, {self.day}"

    def __repr__(self):
        return f"{self.name}, {self.route}, {self.day}"


def main():
    driver_data = pd.read_csv('drivers.csv')
    drivers = []
    for index, driver in driver_data.iterrows():
        drivers.append(Driver(driver))


if __name__ == "__main__":
    main()
