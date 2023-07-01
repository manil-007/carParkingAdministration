class Reservation:
    def __init__(self, spot, hours):
        self.spot = spot
        self.hours = hours

    def calculate_price(self):
        # We are assuming the cost of per hour is 20rs
        return self.hours * 20