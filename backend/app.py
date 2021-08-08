from flask import Flask, request
from flask_cors import CORS
print('Initializing inference script...')
from inference import SentimentClassifier, Predictor
import torch

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# loading the predictor
print('Loading Model...')
model = SentimentClassifier()
model.load_state_dict(torch.load('inference.pth'))

print('Initializing Predictor...')
predictor = Predictor(model)

@app.route('/pred', methods=['POST'])
def prediction():

    # POST request
    if request.method == 'POST':
        print('Incoming..')
        payload = request.get_json()
        print(payload['body'])
        pred, prob = predictor.predict(payload['body'])
        return str(pred), 200


if __name__ == '__main__':
   app.run(port=5000)
