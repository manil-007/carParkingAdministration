from flask import Flask, jsonify, request
from parking_spot import ParkingSpot
from reservation import Reservation


app = Flask(__name__)

parking_spots = [
    ParkingSpot("PS1", 18.559658, 73.779938, 10),
    ParkingSpot("PS2", 18.559657, 73.779937, 12),
    ParkingSpot("PS3", 18.559656, 73.779936, 24),
    ParkingSpot("PS4", 18.559655, 73.779935, 2),
    ParkingSpot("PS5", 20.0958295, 73.9272835, 25),
]

reservations = []


@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    if 'email' in data:
        return jsonify({'message': 'Signup successfully'})
    elif 'phone' in data:
        return jsonify({'message': 'Signup successfully'})
    else:
        return jsonify({'error': 'Invalid data'}) ,400


@app.route('/parking_spots', methods=['GET'])
def get_parking_spots():
    spots = []
    for spot in parking_spots:
        spots.append({
            'name': spot.name,
            'latitude': spot.latitude,
            'longitude': spot.longitude,
            'available_hours': spot.get_available_hours()
        })
    return jsonify(spots)


@app.route('/search', methods=['GET'])
def search_parking_spots():
    lat = float(request.args.get('lat'))
    long = float(request.args.get('long'))
    radius = float(request.args.get('radius'))
    nearby_spots = []
    for spot in parking_spots:
        distance = spot.calculate_distance(lat, long)
        if distance <= radius:
            nearby_spots.append({
                'name': spot.name,
                'latitude': spot.latitude,
                'longitude': spot.longitude,
                'distance': distance,
                'available_hours': spot.get_available_hours()
            })
    return jsonify(nearby_spots)


@app.route('/reserve', methods=['POST'])
def reserve_parking_spot():
    data = request.json
    spot_name = data.get('spot_name')
    hours = data.get('hours')

    for spot in parking_spots:
        if spot.name == spot_name:
            if hours <= spot.get_available_hours():
                spot.update_available_hours(spot.get_available_hours() - hours)
                reservation = Reservation(spot, hours)
                reservations.append(reservation)
                return jsonify({
                    'message': 'Reserved parking spot successfully',
                    'spot_name': reservation.spot.name,
                    'hours': reservation.hours,
                    'price': reservation.calculate_price()
                })
            else:
                return jsonify({'error': 'Requested hours exceeded'}), 400
    return jsonify({'error': 'Parking Spot not found'}), 404


@app.route('/reservations', methods=['GET'])
def get_reservations():
    user_reservations = []
    for reservation in reservations:
        user_reservations.append({
            'spot_name': reservation.spot.name,
            'hours': reservation.hours,
            'price': reservation.calculate_price()
        })
    return jsonify(user_reservations)


if __name__ == '__main__':
    app.run(debug=True)
