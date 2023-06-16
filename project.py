import openai

openai.api_key = " ### "

questions = [
    {
        "question": "What are your interests and hobbies?",
        "options": ["Sports", "Art", "Reading"]
    },
    {
        "question": "What type of tasks do you enjoy?",
        "options": ["Problem-solving", "Creativity", "Communication"]
    },
    {
        "question": "What subjects do you enjoy studying?",
        "options": ["Mathematics", "Science", "Languages"]
    },
    {
        "question": "What are your strengths?",
        "options": ["Leadership", "Creativity", "Analytical thinking"]
    },
    {
        "question": "What are your weaknesses?",
        "options": ["Public speaking", "Time management", "Attention to detail"]
    },
    {
        "question": "What is your preferred work environment?",
        "options": ["Collaborative", "Quiet and focused", "Fast-paced and dynamic"]
    },
    {
        "question": "What are your long-term career goals?",
        "options": ["Entrepreneurship", "Advancement in a specific field", "Work-life balance"]
    },
    {
        "question": "How do you handle challenges?",
        "options": ["Problem-solving", "Seeking help from others", "Perseverance"]
    },
    {
        "question": "Do you prefer working independently or in a team?",
        "options": ["Independently", "In a team", "Depends on the task"]
    },
    {
        "question": "What motivates you in your work?",
        "options": ["Recognition and rewards", "Making a difference", "Continuous learning"]
    },
    {
        "question": "What kind of projects do you enjoy working on?",
        "options": ["Creative projects", "Research-oriented projects", "Hands-on projects"]
    },
    {
        "question": "How do you handle work-related stress?",
        "options": ["Taking breaks and practicing self-care", "Seeking support from colleagues", "Developing a stress management plan"]
    },
    {
        "question": "What do you value most in a work environment?",
        "options": ["Flexibility", "Supportive colleagues", "Opportunities for growth"]
    },
    {
        "question": "What skills or knowledge would you like to further develop?",
        "options": ["Technical skills", "Leadership skills", "Interpersonal skills"]
    },
    {
        "question": "What industries or fields are you interested in?",
        "options": ["Technology", "Healthcare", "Finance"]
    },
    {
        "question": "How do you stay updated on industry trends?",
        "options": ["Reading industry publications", "Attending conferences and webinars", "Networking with professionals"]
    },
    {
        "question": "What kind of tasks do you find boring or uninteresting?",
        "options": ["Repetitive tasks", "Administrative tasks", "Data entry"]
    },
    {
        "question": "Do you prefer a structured or flexible work schedule?",
        "options": ["Structured", "Flexible", "Balanced combination"]
    },
    {
        "question": "What kind of leadership style do you respond well to?",
        "options": ["Authoritative", "Supportive", "Collaborative"]
    },
    {
        "question": "How do you handle constructive criticism?",
        "options": ["Open-mindedly consider it", "Defend your perspective", "Seek feedback to improve"]
    },
    {
        "question": "What kind of company culture do you thrive in?",
        "options": ["Innovative and risk-taking", "Stable and structured", "Diverse and inclusive"]
    },
    {
        "question": "How do you prioritize your tasks and manage your time?",
        "options": ["Using a to-do list and setting deadlines", "Prioritizing based on urgency and importance", "Delegating tasks when possible"]
    },
    {
        "question": "What do you consider to be your greatest accomplishment so far?",
        "options": ["Completing a challenging project", "Overcoming a personal obstacle", "Receiving recognition or awards"]
    }
]

chat_log = []


def ask_gpt3(question, options):
    prompt = "\n".join(chat_log + [question] + options)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    answer = response.choices[0].text.strip()
    return answer


print("Welcome to the Career Orientation Test!")
print("Please answer the following questions. Enter the number of your choice.")

for i, question_info in enumerate(questions):
    question = question_info["question"]
    options = question_info["options"]

    print(f"\nQuestion {i+1}: {question}")
    for j, option in enumerate(options):
        print(f"{j+1}. {option}")

    user_input = input("Your answer: ")

    chat_log.append(f"You: {user_input}")
    answer = ask_gpt3(question, options)
    chat_log.append(f"Assistant: {answer}")

print("\nThank you for taking the Career Orientation Test!")
