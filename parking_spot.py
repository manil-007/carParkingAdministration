from math import sin, cos, sqrt, atan2, radians


class ParkingSpot:
    def __init__(self, name, latitude, longitude, available_hours):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.available_hours = available_hours

    def calculate_distance(self, lat, long):
        R = 6371
        lat1 = radians(self.latitude)
        long1 = radians(self.longitude)
        lat2 = radians(lat)
        long2 = radians(long)

        dlat = lat2 - lat1
        dlong = long2 - long1

        a = sin(dlat/2) ** 2 + cos(lat1) * cos(lat2) * sin(dlong/2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = R * c * 1000
        return distance

    def get_available_hours(self):
        return self.available_hours

    def update_available_hours(self, hours):
        self.available_hours = hours
