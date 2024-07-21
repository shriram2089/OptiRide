from flask import Flask, request, jsonify
from geopy.distance import geodesic
import heapq

app = Flask(__name__)

# In-memory data structures for simplicity
drivers = []
riders = []

@app.route('/register_driver', methods=['POST'])
def register_driver():
    data = request.get_json()
    driver_id = data['driver_id']
    location = data['location']
    drivers.append({'driver_id': driver_id, 'location': location, 'available': True})
    return jsonify({"status": "Driver registered successfully"}), 201

@app.route('/request_ride', methods=['POST'])
def request_ride():
    data = request.get_json()
    rider_id = data['rider_id']
    location = data['location']
    destination = data['destination']
    
    # Find the nearest available driver
    nearest_driver = find_nearest_driver(location)
    if nearest_driver:
        nearest_driver['available'] = False
        riders.append({'rider_id': rider_id, 'location': location, 'destination': destination, 'driver_id': nearest_driver['driver_id']})
        return jsonify({"status": "Ride confirmed", "driver_id": nearest_driver['driver_id']}), 200
    else:
        return jsonify({"status": "No available drivers"}), 200

def find_nearest_driver(rider_location):
    min_distance = float('inf')
    nearest_driver = None
    for driver in drivers:
        if driver['available']:
            distance = geodesic(rider_location, driver['location']).km
            if distance < min_distance:
                min_distance = distance
                nearest_driver = driver
    return nearest_driver

@app.route('/complete_ride', methods=['POST'])
def complete_ride():
    data = request.get_json()
    driver_id = data['driver_id']
    for driver in drivers:
        if driver['driver_id'] == driver_id:
            driver['available'] = True
            break
    return jsonify({"status": "Ride completed successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
    