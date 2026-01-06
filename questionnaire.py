def anxiety_questionnaire():
    questions = [
        "Saya merasa gugup atau cemas",
        "Saya sulit mengendalikan kekhawatiran",
        "Saya merasa gelisah",
        "Saya mudah lelah",
        "Saya sulit berkonsentrasi"
    ]

    score = 0
    print("Jawab dengan angka 0-3")
    print("0=Tidak Pernah | 1=Kadang | 2=Sering | 3=Hampir Selalu\n")

    for q in questions:
        ans = int(input(f"{q}: "))
        score += ans

    return score
