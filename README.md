# carParkingAdministration

Steps to run :
1. python -m venv vnev
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python3 app.py


Steps to test :
1. Get all parking spots:
curl http://localhost:5000/parking_spots

2. Search for nearby parking spots:
curl "http://localhost:5000/search?lat=18.559&long=73.779&radius=1000"

3. Reserve a parking spot:
curl -X POST -H "Content-Type: application/json" -d '{"spot_name": "PS1", "hours":3}' http://localhost:5000/reserve

4. Get all reservations:
curl http://localhost:5000/reservations
