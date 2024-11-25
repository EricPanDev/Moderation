import joblib
from flask import Flask, jsonify, request

loaded_model = joblib.load('model.pkl')
vectorizer = joblib.load('model_vectorizer.pkl')

app = Flask(__name__)

API_KEY = ""

@app.route('/run', methods=['POST'])
def run():
    global loaded_model, vectorizer

    api_key = request.headers.get('x-api-key')
    if not api_key or api_key != API_KEY:
        return jsonify({'error': 'Unauthorized. Invalid API key.'}), 401

    if not request.json or 'text' not in request.json:
        return jsonify({'error': 'Invalid request. JSON with "text" field is expected.'}), 400
    
    text = request.json['text']

    new_data_vectorized = vectorizer.transform([text])

    probabilities = loaded_model.predict_proba(new_data_vectorized)

    data = {}

    labels = ['sexual', 'hate', 'violence', 'harassment', 'self-harm', 'sexual/minors', 'hate/threatening', 'violence/graphic']
    for label, probs in zip(labels, probabilities):
        data[label] = float(f"{probs[0][1]:.2f}")

    return jsonify(data), 200

print("Starting Moderation Server @ http://127.0.0.1:9235. Refer to https://github.com/ericpandev/Moderation for docs.")
app.run("127.0.0.1", port=9235)
