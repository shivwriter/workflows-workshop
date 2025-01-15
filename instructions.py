task_2 = """
# Task #2: Chat with Data

###  Objective: Create a chatbot that allows us to chat with the data we just uploaded!

1. Add a Chatbot UI element here and have it reference a `@{conversation}` state element
2. Create a new workflow called `chat-with-kg`
3. You'll need three blocks for the chatbot below to work: Initialize chat, Add to Chat, and Complete Chat. 
   a. **Initialize chat**: This will only really be executed once. But it'll actually initialize the conversation state element
   b. **Add chat message**: This adds a user's sent message directly into the conversation state element
   c. **Chat Completion**: This actually has the LLM respond to the user's message. It also has tool calling abilities (other paths in the workflow, or a Knowledge Graph)

4. Connect the 3 blocks mentioned above together in order, use the `conversation` state element in each block to reference the same conversation. 
5. Now connect the chatbot UI element with the workflow you just created by editing the `wf-chatbot-message` handler. 
6. Try sending a message. It was probably a bit wonky. There's one more step. Click `Show Next Steps` below in purple to proceed.
"""

task_2_2 = """
# Task #2: Chat with Data

###  Objective: Create a chatbot that allows us to chat with the data we just uploaded!

7. The reason the chat app isn't yet working is becasue we haven't yet configured the "Add Chat Message" block to actually add a user's message to the conversation element. That's the next step. Review the images below for steps on how to leverage `Execution Environment` to figure out the missing context of what to add in the `Message` part of the `Add chat message` block. 
8. Give the chat app a run, it should be working now, similar to a standard General mode chat app. Let's now add our first tool - Knowledge Graph. 
   a. Go back to Workflows, and edit the Chat Completion block. 
   b. Click `Add tool` in purple
   c. Under `Tool type`, select Knowledge Graph
   d. Name your tool in the top right of the dialog box,
   e. Replace the graph id with your graph id
   f. Click Save
9. Congrats! We've added our first tool, you can now ask general questions and questions against your KG.

**A Note on `Execution Environment`**: The steps below show you how to access and understand `Execution Environment`. In short, these are the non-state variables that are available to each block at their point. **This will especially be valuable one day when you're trying to figure out how to pass the values from one block to the next**.
"""