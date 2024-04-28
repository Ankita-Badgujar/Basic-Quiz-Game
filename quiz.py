def main():
    # Define the questions, choices, and correct answers
    # The questions are based on India
    questions = [
        {
            "question": "What is the capital of India?",
            "choices": ["A) Mumbai", "B) New Delhi", "C) Kolkata", "D) Chennai"],
            "answer": "B"
        },
        {
            "question": "Who is known as the 'Father of the Nation' in India?",
            "choices": ["A) Jawaharlal Nehru", "B) Subhas Chandra Bose", "C) Bhagat Singh", "D) Mahatma Gandhi"],
            "answer": "D"
        },
        {
            "question": "What is the national animal of India?",
            "choices": ["A) Elephant", "B) Lion", "C) Tiger", "D) Peacock"],
            "answer": "C"
        },
        {
            "question": "Which river is considered holy in India?",
            "choices": ["A) Godavari", "B) Yamuna", "C) Brahmaputra", "D) Ganges"],
            "answer": "D"
        },
        {
            "question": "What is the official language of India?",
            "choices": ["A) English", "B) Hindi", "C) Tamil", "D) Telugu"],
            "answer": "B"
        },
        # Add more questions as needed
    ]
    
    # Initialize the score
    score = 0

    # Ask each question in turn
    for i, question_data in enumerate(questions):
        # Display the question and choices
        print(f"\nQuestion {i + 1}: {question_data['question']}")
        for choice in question_data["choices"]:
            print(choice)
        
        # Validate the user's input
        while True:
            user_answer = input("Your answer (A, B, C, or D): ").strip().upper()
            if user_answer in ["A", "B", "C", "D"]:
                break  # Valid answer, break out of the loop
            print("Invalid input. Please enter A, B, C, or D.")

        # Check if the answer is correct and update the score
        if user_answer == question_data["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {question_data['answer']}.")

    # Display the final score
    total_questions = len(questions)
    print(f"\nYour final score is: {score}/{total_questions}")
    print(f"That's {score / total_questions * 100:.2f}% correct!")
    print("Thanks for playing the quiz game!")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
