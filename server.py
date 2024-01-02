from flask import Flask, request, render_template, url_for, redirect
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection webApp")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotionDetector():
    text_to_analyse = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyse)
    # Extracting emotions and their values
    emotions = ', '.join(f"'{emotion}': {value}" for emotion, value in result.items() if emotion != 'dominant_emotion')
    dominant_emotion = result['dominant_emotion']
    # Creating the statement
    response = f"For the given statement, the system response is {emotions}. The dominant emotion is {dominant_emotion}."
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
