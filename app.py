from flask import Flask, request, jsonify, render_template_string
import joblib
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

model, vectorizer = None, None
try:
    model = joblib.load('fake_news_model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    logging.info("Model and vectorizer loaded successfully.")
except FileNotFoundError as e:
    logging.error("File not found: %s", e)
except Exception as e:
    logging.error("Error loading model or vectorizer: %s", e)

@app.route('/')
def home():
    return '''
    <h1>Fake News Detection</h1>
    <form action="/predict" method="post">
        <textarea name="news_text" rows="5" cols="50" placeholder="Enter news text here..."></textarea><br>
        <input type="submit" value="Check News">
    </form>
    '''

@app.route('/predict', methods=['POST'])
def predict():
    if not model or not vectorizer:
        logging.error("Model or vectorizer is not loaded.")
        return '<h1 style="color: red;">Model is unavailable. Please check server logs.</h1>'

    news_text = request.form.get('news_text', '').strip()
    if not news_text:
        return '<h1 style="color: red;">Please enter some text!</h1>'  # Handle empty input

    try:
        transformed_text = vectorizer.transform([news_text])
        prediction = model.predict(transformed_text)[0]
        
        result = 'Real' if prediction == 1 else 'Fake'
        return render_template_string('''
            <h1>Result: {{ result }} News</h1>
            <a href="/">Go back</a>
        ''', result=result)
    except Exception as e:
        logging.error("Error during prediction: %s", e)
        return '<h1 style="color: red;">An error occurred during prediction.</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
