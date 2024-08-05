# Final Project - emotion detection

# Import modules
import requests, json

# Functions
def emotion_detector(text_to_analyze):
    """ function to analyze emotive feel of text
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_text = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = input_text, headers = headers)

    json_reponse = json.loads(response.text)
    anger_value = json_reponse['emotionPredictions'][0]['emotion']['anger']
    disgust_value = json_reponse['emotionPredictions'][0]['emotion']['disgust']
    fear_value = json_reponse['emotionPredictions'][0]['emotion']['fear']
    joy_value = json_reponse['emotionPredictions'][0]['emotion']['joy']
    sadness_value = json_reponse['emotionPredictions'][0]['emotion']['sadness']

    dominant_emotion = "anger"
    dominant_value = anger_value

    if disgust_value > dominant_value:
        dominant_emotion = "disgust"
        dominant_value = disgust_value
    if fear_value > dominant_value:
        dominant_emotion = "fear"
        dominant_value = fear_value
    if joy_value > dominant_value:
        dominant_emotion = "joy"
        dominant_value = joy_value
    if sadness_value > dominant_value:
        dominant_emotion = "sadness"
        dominant_value = sadness_value

    return {
    'anger': anger_value,
    'disgust': disgust_value,
    'fear': fear_value,
    'joy': joy_value,
    'sadness': sadness_value,
    'dominant_emotion': dominant_emotion
    }
