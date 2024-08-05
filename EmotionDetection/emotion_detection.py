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

    if response.status_code == 500:
        return "Error"

    
