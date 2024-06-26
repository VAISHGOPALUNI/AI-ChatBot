# -*- coding: utf-8 -*-
"""llama3-on-groq-api.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/VAISHGOPALUNI/ac89c685cd9b470ce64544310d8721cf/llama3-on-groq-api.ipynb
"""

!pip install -q groq

from google.colab import userdata

"""### Basic Example of Getting Started"""

import os

from groq import Groq

client = Groq(
    api_key=userdata.get('GROQ_API_KEY'),
)



"""### Streaming"""

from groq import Groq

# client = Groq()
def get_answer(question):

    chat_completion  = client.chat.completions.create(
    #
    # Required parameters
    #
    messages=[
        # Set an optional system message. This sets the behavior of the
        # assistant and can be used to provide specific instructions for
        # how it should behave throughout the conversation.
        {
            "role": "system",
            "content": "You are an AI tutor named sophia who is specialized in explaining machine learning concepts. Be detailed and include best GenAI models to learn."
                        f"Here is a question from a student: {question} "
                       "Please keep the answers short and crisp & also provide them in chinese language for the client who resides in china"
        },
        # Set a user message for the assistant to respond to.

    ],

    # The language model which will generate the completion.
    model="llama3-70b-8192",

    #
    # Optional parameters
    #

    # Controls randomness: lowering results in less random completions.
    # As the temperature approaches zero, the model will become deterministic
    # and repetitive.
    temperature=1,

    # The maximum number of tokens to generate. Requests can use up to
    # 2048 tokens shared between prompt and completion.
    max_tokens=1024,

    # Controls diversity via nucleus sampling: 0.5 means half of all
    # likelihood-weighted options are considered.
    top_p=1,

    # A stop sequence is a predefined or user-specified text string that
    # signals an AI to stop generating content, ensuring its responses
    # remain focused and concise. Examples include punctuation marks and
    # markers like "[end]".
    stop=None,

    # If set, partial message deltas will be sent.
    stream=False,
)


# Print the incremental deltas returned by the LLM.
    return chat_completion .choices[0].message.content + '\n'
def main():
    while True:
        print("Hi there! Welcome to your Vaishu AI | Type 'exit' to end the session. \n")
        question = input("Enter your Query: \n")
        if question.lower() == 'exit':
            print("Have a good one Vaishu! \n")
            break
        answer = get_answer(question)
        print(f"Vaishu Bot: \n {answer}")

if __name__ == '__main__':
    main()



