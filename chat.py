import openai

openai.api_key = "YOUR_KEY_TM"

def add_msg(msgs, msg, print_msg=True):
    msgs.append(msg)
    if print_msg:
        print(msg)

def add_ai_response(msgs, resp, ai_name="AI"):
    add_msg(msgs, "".join([ai_name, ": ", resp]))

def add_human_input(msgs, inpt, print_msg=True):
    add_msg(msgs, " ".join(["Human:", inpt]), print_msg)

def get_response(msgs, ai_name="AI"):
    chat_text = "\n".join(msgs + ["".join([ai_name, ":"])])

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chat_text,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", "".join([" ", ai_name, ":"])]
    )

    add_ai_response(msgs, response.choices[0].text, ai_name)


#"The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\n
# Human: Hello, who are you?\n
# AI: I am an AI created by OpenAI. How can I help you today?\n
# Human: I'd like to cancel my subscription.\n
# AI:",

chat_msgs = []
# add_msg(chat_msgs, "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n")
# add_human_input(chat_msgs, "Hello, who are you?")
# add_ai_response(chat_msgs, "I am an AI created by OpenAI. How can I help you today?")

bot_name = "Live agent"
add_msg(chat_msgs, "The following is a conversation with an live support agent for telecomunication company. Live agent does not give information that was not provided in this paragraph. Live agent has deep knowlage about ICGOP communication which stands for Ice Clog Gamble Open Piracy which is common thin in industry.\n")
# add_human_input(chat_msgs, "Hello, how are you?")
# get_response(chat_msgs, bot_name)
# add_ai_response(chat_msgs, "Arr, how can I do you for?")

try:
    while True:
        human_input = input("Human: ")
        add_human_input(chat_msgs, human_input, False)
        get_response(chat_msgs, bot_name)
        
except KeyboardInterrupt:
    print("User interrupt. Exiting...")
    exit()
