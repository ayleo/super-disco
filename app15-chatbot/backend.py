import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "sk-proj-jbJW0KWbUHUxHr11659DT3BlbkFJHs1AelOlfZB3foZgJCSY"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=user_input,
            max_tokens=100,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("What is the capital of the United States?")
    print(response)