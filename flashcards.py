import random

flashcards = [
    {"question": "What is the STAR method in interviews?", 
     "answer": "STAR stands for Situation, Task, Action, Result."},
    
    {"question": "What does 'screening' mean in recruitment?", 
     "answer": "Initial process of reviewing resumes to filter suitable candidates."},
    
    {"question": "Difference between HR generalist and HR specialist?", 
     "answer": "Generalist handles all HR tasks, Specialist focuses on a specific area like recruitment or training."},
    
    {"question": "What are behavioral interview questions?", 
     "answer": "Questions based on past behavior, e.g., 'Tell me about a time you...'"},

    {"question": "What is the notice period?", 
     "answer": "The time an employee must serve after resigning before leaving the company."}
]

def show_flashcards():
    random.shuffle(flashcards)
    for card in flashcards:
        print("\nQuestion: " + card["question"])
        input("Press Enter to see the answer...")
        print("Answer: " + card["answer"])
        input("Press Enter for the next card...")

if __name__ == "__main__":
    print(" HR Interview Prep Flashcards")
    show_flashcards()
    print("\n All flashcards done!")
