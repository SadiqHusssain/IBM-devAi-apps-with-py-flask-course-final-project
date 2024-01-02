"""script that does the actual emotion detection
analysis"""
import json
import requests

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    raw_document= {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url=URL, headers=headers, json=raw_document)
    formatted_response = json.loads(response.text)
    status = response.status_code
    if status == 400:
        emotions = {'anger':None, 'sadness':None, 'fear':None, 'joy':None, 'disgust':None, 'dominant_emotion':None}
        return emotions

    emotions =  formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = [None, -100.0] # to compare scores and get name of dominant emotion.
    for emotion in emotions:
        if emotions[emotion] > dominant_emotion[-1]:
            dominant_emotion = [emotion, emotions[emotion]]
    emotions['dominant_emotion'] = dominant_emotion[0]
    return emotions






    


    