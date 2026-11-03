from emotionlab.predictor import predict_emotion


def main():
    user_text = input("请输入一句英文：")

    result = predict_emotion(user_text)

    print(f"情感识别结果：{result}")


if __name__ == "__main__":
    main()