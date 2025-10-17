def quiz():
    questions = [
        {"q": "Should you click unknown links?", "a": "No"},
        {"q": "Is HTTPS always safe?", "a": "Not always"},
    ]
    for q in questions:
        print(q["q"])
        input("Your answer: ")
