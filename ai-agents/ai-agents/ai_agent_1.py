# AI Agent 1: Smart Chat Assistant

print("Welcome! I am your AI Assistant.")
print("Type 'bye' to exit.\n")

def ai_response(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you today?"
    
    elif "name" in message:
        return "I am a simple AI agent created in Python!"
    
    elif "weather" in message:
        return "I can't check live weather yet, but I can chat with you."

    elif "help" in message:
        return "Sure! Tell me what you want help with."

    elif "bye" in message:
        return "Goodbye! Have a great day 😊"

    else:
        return "I am not fully trained yet, but I'm learning!"

# Main loop
while True:
    user_input = input("You: ")
    response = ai_response(user_input)
    print("AI:", response)

    if "bye" in user_input.lower():
        break
