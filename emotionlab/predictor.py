def predict_emotion(text):
    text = text.lower()

    if "happy" in text:
        return "joy"
    elif "sad" in text:
        return "sadness"
    else:
        return "unknown"