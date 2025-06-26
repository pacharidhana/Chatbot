def chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there!"
    elif "learn python" in user_input:
        return "Great choice! You can start with the basics like variables, loops, and functions. Would you like a free beginner’s roadmap?"
    elif "where" in user_input and ("get" in user_input or "resources" in user_input):
        return "There are many resources available like YouTube, Google, and online courses!"
    else:
        return "Sorry, I do not understand that yet."

# Chat loop
while True:
    user = input("You: ")
    if user.lower() == "exit":
        print("Chatbot: Bye!")
        break
    print("Chatbot:", chatbot(user))
