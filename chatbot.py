import random
import datetime

print("hello im ur ai robot")
print("Type 'bye' to exit.\n")

name = ""

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Bot: Goodbye! See you soon 😄")
        break

    elif "my name is" in user_input:
        name = user_input.replace("my name is", "").strip()
        print(f"Bot: Nice to meet you, {name.title()}! 😊")

    elif "your name" in user_input:
        print("Bot: I'm your Advanced Python Chatbot 😎")

    elif "how are you" in user_input:
        responses = [
            "I'm functioning perfectly! 🤖",
            "All systems running smoothly 😄",
            "Better now that you're here!"
        ]
        print("Bot:", random.choice(responses))

    elif "time" in user_input:
        now = datetime.datetime.now()
        print("Bot: Current time is", now.strftime("%H:%M:%S"))

    elif "calculate" in user_input:
        try:
            expression = user_input.replace("calculate", "").strip()
            result = eval(expression)
            print("Bot: The answer is", result)
        except:
            print("Bot: I couldn't calculate that 😅")

    elif "joke" in user_input:
        jokes = [
            "Why do programmers hate nature? Too many bugs! 🐛",
            "Why was the computer cold? It left its Windows open! 🪟",
            "Why do Java developers wear glasses? Because they don't C# 😆"
        ]
        print("Bot:", random.choice(jokes))

    elif name and "who am i" in user_input:
        print(f"Bot: You are {name.title()} 😎")

    else:
        default_responses = [
            "Interesting... tell me more 🤔",
            "Hmm, I see...",
            "Can you explain that differently?",
            "That's cool 😎"
        ]  
        print("Bot:", random.choice(default_responses))
