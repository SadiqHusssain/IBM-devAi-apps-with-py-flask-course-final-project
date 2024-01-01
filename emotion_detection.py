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
    emotions =  formatted_response['emotionPredictions'][0]['emotion']
    return emotions
    # anger = emotions['anger']
    # disgust = emotions['disgust']
    # fear = emotions['fear']
    # joy = emotions['joy']
    # sadness = emotions['sadness']





    


    