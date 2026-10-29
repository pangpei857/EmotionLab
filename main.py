def predict_emotion(text):
    text = text.lower()

    if "happy" in text:
        return "joy"
    elif "sad" in text:
        return "sadness"
    else:
        return "unknown"


if __name__ == "__main__":
    user_text = input("请输入一句英文：")
    result = predict_emotion(user_text)

    print(f"情感识别结果：{result}")