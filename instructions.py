task_2 = """
# Task #2: Chat with Data

###  Objective: Create a chatbot that allows us to chat with the data we just uploaded!

1. Add a Chatbot UI element here (to the column on the right) and have it reference a `@{conversation}` state element
2. Create a new workflow called `chat-with-kg`
3. You'll need three blocks for the chatbot to work: Initialize chat, Add to Chat, and Complete Chat. 
   a. **Initialize chat**: This will only really be executed once. But it'll actually initialize the conversation state element
   b. **Add chat message**: This adds a user's sent message directly into the conversation state element
   c. **Chat Completion**: This actually has the LLM respond to the user's message. It also has tool calling abilities (other paths in the workflow, or a Knowledge Graph)

4. Connect the 3 blocks mentioned above together in order, use the `conversation` state element in each block to reference the same conversation. (So edit all three blocks for this step)
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


task_3 = """
# Task #3: Classify Feedback

###  Objective: Classify Text into Categories
The classification block is a really powerful tool that allows you to classify some text into predefined categories. This effectively allows you to add some level of reasoning and smart logic/pathing to your workflow. It sounds like an if/then statement but it's actually much more powerful because it's less rigid in the conditioning. It's more natural language conditioning.

1. Inspect the data on the right hand side. You'll see there is a good bit of customer feedback provided to our website. We would like to start understanding the types of inputs we get and also start crafting responses back to each of these customers.
2. Let's first investigate the Workflow `run-analysis`. This is already connected and called with the `Run Analysis` button on the right hand side.
   a. Specifically note the `Workflow key` is currently set to `task_3_logging`. This means for each item in whatever is passed in `Items`, it will trigger the `task_3_logging` workflow.
   b. AFTER we've gone through each item and run the `task_3_logging` workflow, the next two blocks will be executed. You can ignore them :) (but feel free to inspect, and ask questions if you're curious)
   c. Below is an example of what you'll see for the for each block.
"""
task_3_2 = """
3. Go ahead and click the `Run Analysis` button. You'll see some errors, ignore them :) The main thing is that now we can review the execution environment to see `item` and `itemId`. These are the values that are being passed in to the `task_3_logging` workflow for each item.
4. TASK: Try to edit the `Message` in the `task_3_logging` workflow to include the `itemId` and `item` values. Give it a run and see if it works.
5. Now let's go back to the `run-analysis` workflow and let's edit it to use the `task-3-classifying` workflow, and let's start editing that workflow.
6. TASK: Let's go ahead and add a classification block.
   a. Under `Text`, add `@{item.ORIGINAL_TEXT}` 
   b. Under `Categories`, add `product_feedback`, `customer_frustration`, `customer_satisfaction`, `other`. You can use this as both the key/value pair.
   c. Connect each of these categories to the next block (the `Call event handler block`)
7. Now let's go ahead and click the `Run Analysis` button again. You'll see that the `task_3_classifying` workflow is now being called for each item. You should also see that afterwards, a nice bar chart is created showing the distribution of feedback categories.
8. TASK: Now let's take customer first mentality to the next level. Let's go back into the `task_3_classifying` workflow and let's add a new No Code block where we craft responses just to those giving `customer_frustration` feedback.
   a. Download the json on the left hand side within the Codespace. Import that No Code App, Deploy it, and save the app id.
   b. Add a new No Code block in your workflow. Connect the `customer_frustration` path to the new No Code block.
   c. Edit the No code block with the relevant inputs: 
      i. App ID: App ID you saved from 8a.
      i. customer_name: `@{item.NAME}`
      ii. customer_feedback: `@{item.ORIGINAL_TEXT}`
   d. Now Connect the No Code block back to the `Add Response` Custom Event Handler block.
9. We should be good to go! Click the `Run Analysis` button again. You should see in the data frame that we are now also adding our response to each customer frustration feedback category. In the future, we may want to also auto-email the customer. 



CONGRATS! You've just completed your (maybe) first set of workflows. 
"""