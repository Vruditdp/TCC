from flask import Flask, request, jsonify
import pickle
# from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, GPT2Tokenizer, VisionEncoderDecoderConfig


app = Flask(__name__)


with open('toxic_comment_pipeline.pkl', 'rb') as file:
    loaded_pipeline = pickle.load(file)


@app.route('/filter', methods=['POST'])
def filter():
    try:
        data = request.json
        text = data['text']

        preds = loaded_pipeline.predict([text])
        if preds == 1:
            ans = "The given text is in toxic context."
        elif preds == 0:
            ans = "There is not any toxic content in the given text!"
        else:
            ans = "I am not able to recognize the context of the text. SORRY ...!"

        return jsonify({'prediction': ans})

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/')
def hello():
    return "<p> Yes, It is functional ! </p>"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"),debug=True)


# curl -X POST -H "Content-Type: application/json" -d '{"text": "I love you!"}' http://localhost:5000/predict_toxicity
