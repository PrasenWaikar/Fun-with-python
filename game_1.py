def quiz():
    questions = [
        "What is the capital of France? ",
        "Which planet is known as the Red Planet? ",
        "Who wrote the play 'Romeo and Juliet'? ",
        "What is the largest mammal in the world? ",
        "What is the chemical symbol for gold? ",
        "How many continents are there in the world? ",
        "Who painted the Mona Lisa? ",
        "What is the tallest mountain in the world? ",
        "What is the largest ocean on Earth? ",
        "What is the powerhouse of the cell called? "
    ]

    answers = [
        "Paris",
        "Mars",
        "William Shakespeare",
        "Blue whale",
        "Au",
        "7",
        "Leonardo da Vinci",
        "Mount Everest",
        "Pacific Ocean",
        "Mitochondria"
    ]

    score = 0

    for i in range(10):
        user_answer = input(questions[i])
        if user_answer.lower() == answers[i].lower():
            score += 1

    if score == 10:
        print("Congratulations! You are a winner!")
    else:
        print("Better luck next time!")
    
    print(f"Your score is: {score}/10")

quiz()
