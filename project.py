
import openai

openai.api_key = "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"
questions = ["What are your interests and hobbies?",
             "What type of tasks do you enjoy?",
             "What subjects do you enjoy studying?",
             "What are your strengths?",
             "What are your weaknesses?"]


def create_conv():
    chat = "Проаналізуй відповіді користувача та надай рекомендації щодо вибору майбутньої професії, аналізуючи дані " \
           "зазначенні нижче:"
    ans = ""
    for item in questions:
        print(item)
        ans = input("answer: ")
        chat += f"""
question:{item}
answer:{ans}\n
"""
    chat += "Відповідь надай українською мовою."
    return chat


def gpt_3_1(question):
    prompt = question
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful career guidance"},
            {"role": "assistant", "content": prompt}
        ],
    )
    return response['choices'][0]['message']['content']


def main():
    print("Welcome to the Career Orientation Test!")
    print("Please answer the following questions. Enter the number of your choice.")

    answer = gpt_3_1(create_conv())
    print(f"Assistant: {answer}")
    print("\nThank you for taking the Career Orientation Test!")


main()
