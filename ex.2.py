from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

eggs_data = []

@app.route('/api/eggs', methods=['POST'])
def log_eggs():
    data = request.get_json()

    
    if not data or 'shed' not in data or 'date' not in data or 'count' not in data:
        return jsonify({"error": "Missing required fields: shed, date, count"}), 400

    try:
        count = int(data['count'])
        if count < 0:
            return jsonify({"error": "Count cannot be negative"}), 400
    except (ValueError, TypeError):
        return jsonify({"error": "Count must be a number"}), 400

    record = {
        "shed": data['shed'],
        "date": data['date'],
        "count": count
    }

    eggs_data.append(record)
    return jsonify({"message": "Record logged successfully", "record": record}), 201


@app.route('/api/eggs', methods=['GET'])
def get_eggs():
    #
    total = sum(record['count'] for record in eggs_data)

    response = {
        "records": eggs_data,
        "running_total": total
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, port=5000)