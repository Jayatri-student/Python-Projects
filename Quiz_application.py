print("******Welcome to Quiz Application******")
name=input("Enter your Name:")
print("Lets start the quiz",name)
question=[{"q":"What is the capital of India?",
           "options":["a) New Delhi","b) Mumbai","c) Kolkata","d) Chennai"],
           "answer":"a"},
        {"q":"What is the SI unit of Energy?",
           "options":["a) Joule","b) Newton","c) Watt","d) Pascal"],
           "answer":"a"},
        {"q":"What is the chemical formula of water?",
           "options":["a) CO2","b) H2O","c) O2","d) H2SO4"],
           "answer":"b"},
        {"q":"What is the largest planet in our solar system?",
           "options":["a) Earth","b) Jupiter","c) Saturn","d) Mars"],
           "answer":"b"}]
if name:

    score=0
    for q in question:
        print("\n" + q["q"])
        for option in q["options"]:
            print(option)
        answer=input("Enter your answer:")
        if answer==q["answer"]:
            score+=1
        else:
            print("Wrong answer")
    print("Your score is:" + str(score) + "/" + str(len(question)))
         
print("Thank You!")