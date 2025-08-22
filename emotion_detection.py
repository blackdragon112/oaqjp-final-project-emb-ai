# Import the requests library to handle HTTP requests
import requests

def emotion_detector(text_to_analyse):
    # URL:
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Input JSON:
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Headers:
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json = myobj, headers=header)
    
    # Return the response text from the API
    return response.text
    