class CoffeeBot:

    def __init__(self):

        # keywords for each intent
        self.responses = {
            "greeting": ["hello", "hi", "hey", "good morning"],
            "menu": ["menu", "order", "drink", "coffee", "tea"],
            "hours": ["hours", "open", "time", "closing"],
            "location": ["where", "address", "location", "place"],
            "thanks": ["thanks", "thank you", "bye", "goodbye"]
        }

        # bot replies
        self.answers = {
            "greeting": "Hello! Welcome to Brew & Byte. How can I help you today?",
            "menu": "We offer Espresso, Latte, Cappuccino, and Green Tea.",
            "hours": "We are open from 7:00 AM to 8:00 PM every day.",
            "location": "You can find us at 123 Java Lane, Silicon Valley.",
            "thanks": "You're welcome! Have a great day!",
            "fallback": "Sorry, I didn't understand. Try asking menu or hours."
        }

    def get_intent(self, user_input):

        user_input = user_input.lower()

        for intent, keywords in self.responses.items():
            for word in keywords:
                if word in user_input:
                    return intent

        return "fallback"

    def chat(self):

        print("Brew & Byte Support Bot")
        print("Type 'quit' to exit.\n")

        while True:

            user_text = input("You: ")

            if user_text.lower() in ["quit", "exit"]:
                print("Bot: Goodbye!")
                break

            intent = self.get_intent(user_text)

            print("Bot:", self.answers[intent])


# Run chatbot
if __name__ == "__main__":
    bot = CoffeeBot()
    bot.chat()