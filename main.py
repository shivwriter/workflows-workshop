import writer as wf
from instructions import task_2, task_2_2, task_3, task_3_2   
import pandas as pd



wf.Config.feature_flags = ["workflows"]



""" ==== NOTE: You can ignore everything below. It's mostly to help the flow of the lessons. ==== """

def trigger_task_2_ns(state): 
    state["task_2_show_next_step"] = not state["task_2_show_next_step"]


def next_image(state):
    state["task_2_selected_image_index"] = (state["task_2_selected_image_index"] + 1) % len(state["task_2_images"])
    state["task_2_selected_image"] = state["task_2_images"][state["task_2_selected_image_index"]]


def prev_image(state):
    state["task_2_selected_image_index"] = (state["task_2_selected_image_index"] - 1) % len(state["task_2_images"])
    state["task_2_selected_image"] = state["task_2_images"][state["task_2_selected_image_index"]]


def load_df():
    df = pd.read_csv("data.csv")
    return df

def df_to_dict(df):
    return df.to_dict('records')


def update_df(state, index, value, column):
    print(value)
    df = state["task_3_df"]
    if column not in state["task_3_df"].columns:
        state["task_3_df"][column] = ""
    df.loc[index, column] = value
    state["task_3_df"] = df

def return_bar_chart(state):
    category_counts = state["task_3_df"]["Category"].value_counts().reset_index()
    category_counts.columns = ["Category", "Count"]
    
    return {
        "data": [{
            "type": "bar",
            "x": category_counts["Category"].tolist(),
            "y": category_counts["Count"].tolist()
        }],
        "layout": {
            "title": "Distribution of Feedback Categories",
            "xaxis": {
                "title": "Feedback Category",
                "tickangle": -45
            },
            "yaxis": {
                "title": "Number of Entries"
            },
            "margin": {
                "b": 100
            }
        }
    }


initial_state = wf.init_state({
    "task_2_text": task_2,
    "task_2_2_text": task_2_2,
    "task_2_show_next_step": False,
    "task_2_images": ["static/1.png", "static/2.png", "static/3.png", "static/4.png"],
    "task_2_selected_image": "static/1.png", 
    "task_2_selected_image_index": 0,
    "task_3_df": load_df(),
    "task_3_df_dict": df_to_dict(load_df()),
    "task_3_text": task_3,
    "task_3_2_text": task_3_2
})

