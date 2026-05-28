import random

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Chennai", "D. Kolkata"],
        "answer": "A"
    },
    {
        "question": "Which language is used for Python programming?",
        "options": ["A. Java", "B. Python", "C. C++", "D. HTML"],
        "answer": "B"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "Who is the father of computers?",
        "options": ["A. Charles Babbage", "B. Newton", "C. Einstein", "D. Tesla"],
        "answer": "A"
    }
]

random.shuffle(questions)

score = 0

print("===== Quiz Application =====")

for i, q in enumerate(questions, start=1):

    print(f"\nQuestion {i}: {q['question']}")

    options = q["options"][:]
    random.shuffle(options)

    for option in options:
        print(option)

    try:
        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print("Correct Answer!")
            score += 1
        else:
            print("Wrong Answer!")

    except:
        print("Invalid Input")

print("\n===== Quiz Finished =====")
print("Your Final Score is:", score)
print("Total Questions:", len(questions))
