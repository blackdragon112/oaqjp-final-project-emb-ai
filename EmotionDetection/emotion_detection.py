# Import the requests library to handle HTTP requests
import requests
# Import the json library to convert text into a JSON file
import json

def emotion_detector(text_to_analyse):
    # URL:
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Input JSON:
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Headers:
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json = myobj, headers=header)
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting required set of emotions and scores from the response
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Code logic to find the dominant emotion (emotion with the highest score)
    sorted_emotions = sorted(emotions.items(), key=lambda item: item[1], reverse=True)

    # Get the dominant emotion name (the first key in sorted_emotions)
    dominant_emotion = sorted_emotions[0][0]

    # Add dominant emotion to emotions dictionary
    emotions['dominant_emotion'] = dominant_emotion
    
    # Returning a dictionary containing sentiment analysis results
    return emotions
    