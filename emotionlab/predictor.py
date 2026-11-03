from emotionlab.preprocessing import clean_text

def predict_emotion(text):
    text = clean_text(text)

    if "happy" in text:
        return "joy"
    elif "sad" in text:
        return "sadness"
    else:
        return "unknown"