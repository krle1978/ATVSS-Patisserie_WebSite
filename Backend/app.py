from flask import Flask, send_from_directory, jsonify

app = Flask(__name__)

# Ruta za početnu stranicu
@app.route('/')
def home():
    return send_from_directory('../', 'index.html')  # Služi index.html iz glavnog direktorijuma

# Ruta za statičke fajlove (CSS i JS)
@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('../', filename)  # Služi fajlove kao što su styles.css i script.js

# Test ruta za API
@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({"message": "API radi ispravno!"})

if __name__ == '__main__':
    app.run(debug=True)
