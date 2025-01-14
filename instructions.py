task_2 = """
# Task #2: Chat with Data

###  Objective: Create a chatbot that allows us to chat with the data we just uploaded!

1. Add a Chatbot UI element here and have it reference a `\@{conversation}` state element
2. Create a new workflow called `chat-with-kg`
3. You'll need three blocks for the chatbot below to work: Initialize chat, Add to Chat, and Complete Chat. 
   a. **Initialize chat**: This will only really be executed once. But it'll actually initialize the conversation state element
   b. **Add chat message**: This adds a user's sent message directly into the conversation state element
   c. **Chat Completion**: This actually has the LLM respond to the user's message. It also has tool calling abilities (other paths in the workflow, or a Knowledge Graph)

4. Connect the 3 blocks mentioned above together in order, use the `conversation` state element in each block to reference the same conversation. 
5. Now connect the chatbot UI element with the workflow you just created by editing the `wf-chatbot-message` handler. 
6. Try sending a message. It was probably a bit wonky. There's one more step. 
"""

task_2_2 = """
# Task #2: Chat with Data

###  Objective: Create a chatbot that allows us to chat with the data we just uploaded!

7. The reason the chat app isn't yet working is becasue we haven't yet configured the "Add Chat Message" block to actually add a user's message to the conversation element. That's the next step. Review the images below for steps on how to 
"""