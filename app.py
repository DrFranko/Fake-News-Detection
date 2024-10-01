from flask import Flask, request, jsonify
import torch
from model import FakeNewsClassifier  # Import your model class
import pickle

# Load vectorizer
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

app = Flask(__name__)

# Load the model
model = FakeNewsClassifier(input_size=5000)
model.load_state_dict(torch.load('fakenews_model.pth'))
model.eval()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['text']
    vectorized_data = vectorizer.transform([data]).toarray()
    tensor_data = torch.tensor(vectorized_data, dtype=torch.float32)
    with torch.no_grad():
        output = model(tensor_data)
        _, predicted = torch.max(output, 1)
        return jsonify({'prediction': int(predicted.item())})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)