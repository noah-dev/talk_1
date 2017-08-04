import random
answers = [ "It is certain", 
            "Outlook good", 
            "You may rely on it", 
            "Ask again later", 
            "Concentrate and ask again", 
            "Reply hazy, try again", 
            "My reply is no", 
            "My sources say no"]

prompt = "Enter your question: "

while True:
    question = input(prompt)

    #Equivalent to question == ""
    if not question:
        print("Quitting...")
        break

    # In python, lists are zeo indexed. 
    # For a list of 8 responses, the first item 
    # is index 0 and the last is index 7
    response = random.randint(1,8) - 1

    print(answers[response])
