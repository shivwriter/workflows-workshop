import writer as wf
from instructions import task_2, task_2_2

# This is a placeholder to get you started or refresh your memory.
# Delete it or adapt it as necessary.
# Documentation is available at https://dev.writer.com/framework

# Shows in the log when the app starts

wf.Config.feature_flags = ["workflows"]

def trigger_task_2_ns(state): 
    state["task_2_show_next_step"] = not state["task_2_show_next_step"]


def next_image(state):
    state["task_2_selected_image_index"] = (state["task_2_selected_image_index"] + 1) % len(state["task_2_images"])
    state["task_2_selected_image"] = state["task_2_images"][state["task_2_selected_image_index"]]

initial_state = wf.init_state({
    "task_2_text": task_2,
    "task_2_2_text": task_2_2,
    "task_2_show_next_step": False,
    "task_2_images": ["static/1.png", "static/2.png", "static/3.png", "static/4.png"],
    "task_2_selected_image": "static/1.png", 
    "task_2_selected_image_index": 0
})

