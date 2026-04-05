
def quiz_game():
    score = 0
    
    # Store questions and answers in a list of dictionaries
    quiz_questions = [
        {"q": "What is the capital of France?", "a": ["paris"]},
        {"q": "Who wrote 'Hamlet'?", "a": ["shakespeare", "william shakespeare"]},
        {"q": "What is the largest planet in our solar system?", "a": ["jupiter"]},
        {"q": "Who painted the Mona Lisa?", "a": ["leonardo da vinci", "da vinci"]},
        {"q": "What is the chemical symbol for Gold?", "a": ["au"]},
        {"q": "Which continent is the Sahara Desert located in?", "a": ["africa"]},
        {"q": "What is 12 × 8?", "a": ["96"]},
        {"q": "Who was the first President of the United States?", "a": ["george washington", "washington"]},
        {"q": "What gas do plants absorb during photosynthesis?", "a": ["carbon dioxide", "co2"]},
        {"q": "Which is the smallest prime number?", "a": ["2"]},
    ]
    
    print("🎓 Welcome to the General Knowledge Quiz!")
    print(f"You will be asked {len(quiz_questions)} questions. Each correct answer gives you +1 point.\n")
    
    # Loop through questions
    for idx, item in enumerate(quiz_questions, start=1):
        answer = input(f"{idx}) {item['q']} ").strip().lower()
        if answer in item["a"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {item['a'][0].title()}.\n")
    
    # Final feedback
    print("📊 --- Quiz Completed ---")
    print(f"Your final score: {score}/{len(quiz_questions)}")
    
    if score == len(quiz_questions):
        print("🌟 Excellent! You got all answers right.")
    elif score >= 7:
        print("👍 Great job! You scored above average.")
    elif score >= 4:
        print("🙂 Not bad, keep practicing!")
    else:
        print("📘 Better luck next time, keep learning!")

if __name__ == "__main__":
    quiz_game()