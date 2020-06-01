from Question import Question

question_prompts = [
    "A group of Squirrels are Called?\n(a)Drury\n(b)Spike\n(c)Scarlet\n(d)Scurry\n\n",
    "A group of Monkeys are Called?\n(a)Scurry\n(b)Troop\n(c)Scree\n(d)Bunch\n\n",
    "A group of Giraffes are Called?\n(a)Tower\n(b)Prickle\n(c)Scurry\n(d)Toasters\n\n",
    "A group of Porcupines are Called?\n(a)Shoal\n(b)Troop\n(c)Prickle\n(d)Dazzle\n\n"
    "A group of Lions are Called?\n(a)Den\n(b)Lions\n(c)Pride\n(d)Prides\n\n"
]

questions = [
    Question(question_prompts[0], "d"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "c"),

]

def run_test(questions):
    score = 0
    for qtn in questions:
        answer = input(qtn.prompt)
        if answer == qtn.answer:
            score += 1
    print("You Scored: " + str(score) + "/" + str(len(questions)))

run_test(questions)

