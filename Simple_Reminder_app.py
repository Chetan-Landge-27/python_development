
import json

def quiz_game():
    score = 0

    
    with open("python\Technohack_tasks\quiz_questions.json", "r") as f:
        quiz_questions = json.load(f)

    print("🎓 Welcome to the General Knowledge Quiz!")
    print(f"You will be asked {len(quiz_questions)} questions.\n")

    
    for idx, item in enumerate(quiz_questions, start=1):
        answer = input(f"{idx}) {item['question']} ").strip().lower()
        if answer in item["answers"]:
            print("✔️ Correct!\n")
            score += item["points"]
        else:
            print(f"❌ Wrong! Correct answer: {item['answers'][0].title()}\n")

    
    print(" --- Quiz Completed ---")
    print(f"Your final score: {score}")

    if score == sum(q["points"] for q in quiz_questions):
        print(" Excellent! You got all answers right.")
    elif score >= 150:
        print(" Great job! You scored above average.")
    elif score >= 80:
        print(" Not bad, keep practicing!")
    else:
        print(" Better luck next time, keep learning!")

if __name__ == "__main__":
    quiz_game()
