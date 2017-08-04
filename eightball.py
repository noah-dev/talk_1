import random

prompt = "Enter your question: "

while True:
    question = input(prompt)

    #Equivalent to question == ""
    if not question:
        print("Quitting...")
        break

    response = random.randint(1,4)
    if response == 1:
        print("It is certain")
    elif response == 2:
        print("Outlook good")
    elif response == 3:
        print("You may rely on it")
    elif response == 4:
        print("Ask again later")
