import openai
#---------------------------------------------
API_KEY = "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"
openai.api_key = API_KEY
chat_log = []
print("Welcome to PlutonChat, this is a innovational AI system that will provide a answer to all your questions")
while True:
    user_message = input("You:")
    if user_message.lower() == "quit":
        break
    else:
        chat_log.append({"role": "user", "content": user_message})
        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=chat_log
            )
        assistant_response = response['choices'][0]['message']['content']
        print("Pluton:", assistant_response.strip("\n").strip())
        chat_log.append({"role": "assistant", "content": assistant_response.strip("\n").strip()})
#-----------------------------------------------------------------------------------------------------------
