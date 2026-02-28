import pyttsx3
import datetime
import re

# Voice engine
engine = pyttsx3.init()

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

def is_math_expression(text):
    return re.match(r'^[0-9+\-*/().\s]+$', text)

print("Talking AI Chatbot 🤖")
print("Type 'bye' to exit\n")

while True:
    user_input = input("You: ").strip().lower()

    if user_input == "bye":
        speak("Goodbye! See you later.")
        break

    # 🧮 Calculator
    if is_math_expression(user_input):
        try:
            result = eval(user_input)
            speak(f"The answer is {result}")
        except:
            speak("Invalid calculation.")
        continue

    # 🤖 Normal Replies
    if "hello" in user_input or "hi" in user_input:
        speak("Hello there!")
    elif "how are you" in user_input:
        speak("I am functioning perfectly.")
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    else:
        speak("I don't understand that yet.")
