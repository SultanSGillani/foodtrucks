import csv
from io import StringIO
import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Define the endpoint URL
DATA_URL = "https://data.sfgov.org/api/views/rqzj-sfat/rows.csv"


@app.route('/', methods=['GET'])
def get_foodtrucks():
    try:
        # Fetch the data from the URL with a timeout of 10 seconds
        response = requests.get(DATA_URL, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Read the CSV data
        csv_data = StringIO(response.text)
        reader = csv.DictReader(csv_data)

        # Convert the CSV data to a list of dictionaries
        foodtrucks = list(reader)

        return render_template('foodtrucks.html', foodtrucks=foodtrucks)

    except requests.RequestException as e:
        return jsonify({'error': 'Failed to fetch data from the URL.', 'details': str(e)}), 500
    except csv.Error as e:
        return jsonify({'error': 'Failed to parse CSV data.', 'details': str(e)}), 500
    except ValueError as e:
        return jsonify({'error': 'Data processing error.', 'details': str(e)}), 500
    except KeyError as e:
        return jsonify({'error': 'Missing data field.', 'details': str(e)}), 500
    except IOError as e:
        return jsonify({'error': 'I/O error occurred.', 'details': str(e)}), 500


if __name__ == '__main__':
    # Use Gunicorn for production
    app.run(debug=False, host='0.0.0.0', port=5000)
