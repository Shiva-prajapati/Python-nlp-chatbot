import nltk
from nltk.chat.util import Chat, reflections

# Patterns and Responses
pairs = [
    [r"hi|hello|hey|hlo", 
     ["Hello there! 👋", "Hey! How can I help you today?", "Hi! Nice to see you."]],
    
    [r"my name is (.*)", 
     ["Hi %1! How can I assist you today?"]],
    
    [r"(what is your name|who are you)", 
     ["I'm your friendly Python chatbot 😊", "I am a chatbot made with Python and NLTK."]],
    
    [r"(how are you|how are you doing)", 
     ["I'm doing great! Thanks for asking.", "I’m good. Hope you're doing well too!"]],
    
    [r"(.*)(help|assist)(.*)", 
     ["Of course! I'm here to help. Just tell me what you need.", "Sure! What do you need help with?"]],
    
    [r"(.*)(your creator|who created you|tumhe kisne banaya h)",
     ["I was created by Shiva Prajapati as a part of a Python internship project 💻"]],

    
    [r"(.*)(joke|funny|mujhe ek joke sunao)(.*)", 
     ["Why don’t scientists trust atoms? Because they make up everything! 😂"]],
    
    [r"(.*)(weather|climate)(.*)", 
     ["I’m not connected to real-time weather, but I hope it’s sunny wherever you are! ☀️"]],
    
    [r"(.*) (happy|sad|upset|angry)", 
     ["Emotions make us human. Want to talk more about it?", "I'm here if you want to share more."]],
    
    [r"sorry(.*)", 
     ["No worries at all!", "It's okay, we all make mistakes. 😊"]],
    
    [r"(bye|goodbye|exit|quit)", 
     ["Goodbye! Take care 👋", "See you next time!", "It was nice chatting with you."]],
    
    [r"(.*)", 
     ["That's interesting... Tell me more.", "Hmm... Can you explain that a bit more?", "I'm here to listen! 😊"]]
]

# Chatbot Function
def chatbot():
    print("🤖 ChatBot: Hello! I'm your Python assistant. Type 'quit' to exit.\n")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run chatbot
if __name__ == "__main__":
    chatbot()
