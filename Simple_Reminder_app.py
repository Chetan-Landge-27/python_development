import json
import random
import time

def load_questions():
    """Load questions from JSON file"""
    try:
        with open('python\\programing\\questions.json', 'r', encoding='utf-8') as file:
            questions = json.load(file)
            return questions
    except FileNotFoundError:
        print("Error: questions.json file not found!")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in questions.json!")
        return []

def get_random_questions_by_difficulty(all_questions, num_questions=15):
    """Select random questions with increasing difficulty"""
    easy_questions = [q for q in all_questions if q['difficulty'] == 'Easy']
    medium_questions = [q for q in all_questions if q['difficulty'] == 'Medium']
    hard_questions = [q for q in all_questions if q['difficulty'] == 'Hard']
    expert_questions = [q for q in all_questions if q['difficulty'] == 'Expert']
    master_questions = [q for q in all_questions if q['difficulty'] == 'Master']
    
    selected_questions = []
    
    
    selected_questions.extend(random.sample(easy_questions, min(3, len(easy_questions))))
    selected_questions.extend(random.sample(medium_questions, min(4, len(medium_questions))))
    selected_questions.extend(random.sample(hard_questions, min(3, len(hard_questions))))
    selected_questions.extend(random.sample(expert_questions, min(3, len(expert_questions))))
    selected_questions.extend(random.sample(master_questions, min(2, len(master_questions))))
    
    
    random.shuffle(selected_questions)
    
    return selected_questions[:num_questions]

def display_question(question, q_num, total_q, current_score):
    """Display a single question"""
    print("\n" + "="*60)
    print(f" Question {q_num}/{total_q}  |   Score: {current_score}")
    print("="*60)
    
    print(f"\n {question['question']}")
    print("\n" + "-"*40)
    answer = input Your answer: ").strip().lower()
    
    return answer

def show_result(is_correct, question, points, current_score):
    """Show feedback after answer"""
    print("\n" + "-"*40)
    
    if is_correct:
        print(f" CORRECT! +{points} points")
        print(f" Total score: {current_score}")
    else:
        correct_answer = question['answers'][0].title()
        print(f" WRONG! The correct answer is: {correct_answer}")
        print(f"Total score: {current_score}")
    
    time.sleep(1)

def display_final_results(name, score, correct_answers, total_questions):
    """Display final results"""
    print("\n" + "="*60)
    print(" QUIZ COMPLETED! ")
    print("="*60)
    
    points = (correct_answers / total_questions) * 100
    
    print(f"\n👤 Player: {name}")
    print(f" Final Score: {score} points")
    print(f" Correct: {correct_answers}/{total_questions}")
    print(f" Points: {points:.1f}%")
    
    
    if points >= 90:
        print("\ PERFECT! You're a genius! ")
    elif points >= 75:
        print("\ EXCELLENT! Great knowledge! ")
    elif points >= 60:
        print("\ GOOD JOB! Keep learning! ")
    elif points >= 45:
        print("\ NICE TRY! Practice makes perfect! ")
    else:
        print("\ KEEP GOING! Every quiz makes you smarter! ")
    
    print("\n" + "="*60)
    print("Thanks for playing! ")
    print("="*60 + "\n")

def quiz_game():
    """Main quiz game function"""
    print("\n" + "="*60)
    print(" WELCOME TO THE QUIZ CHALLENGE ")
    print("="*60)
    
    
    all_questions = load_questions()
    if not all_questions:
        return
    
    
    name = input(" Enter your name: ").strip()
    if not name:
        name = "Player"
    
    print(f" Hello {name}! Let's begin the quiz!\n")
    time.sleep(1)
    
    
    game_questions = get_random_questions_by_difficulty(all_questions, 15)
    
    
    score = 0
    correct_answers = 0
    total_questions = len(game_questions)
    
    
    for q_num, question in enumerate(game_questions, 1):
        
        print(f"\ Current Score: {score} points")
        
        
        user_answer = display_question(question, q_num, total_questions, score)
        
        
        is_correct = user_answer in question['answers']
        
        
        if is_correct:
            points = question['points']
            score += points
            correct_answers += 1
        else:
            points = 0
        
        
        show_result(is_correct, question, points, score)
    
    
    display_final_results(name, score, correct_answers, total_questions)

if __name__ == "__main__":
    quiz_game()
