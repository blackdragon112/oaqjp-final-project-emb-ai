''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the EmotionDetection package
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotion and its confidence
        score as well as the most dominant emotion of all emotions
        for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector() function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the emotions and their scores from the response
    emotions = response.copy()
    if 'dominant_emotion' in emotions:
        del emotions['dominant_emotion']
    formated_emotions = ', '.join([f"'{key}': {value}" for key, value in emotions.items()])
    dominant_emotion = response['dominant_emotion']

    # Check if the dominant_emotion is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    else:
        # Return a formatted string with the emotions and scores
        return f"For the given statement, the system response is {formated_emotions}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000 '''
    app.run(host="0.0.0.0", port=5000)
