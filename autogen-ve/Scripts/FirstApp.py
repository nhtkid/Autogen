import autogen

# Load the model
config_list = autogen.config_list_from_json(
    env_or_file="OAI_CONFIG_LIST",
    filter_dict={
        "model": {
            "gpt-3.5-turbo-16k",
            "gpt-4",
            }
    }
)

# Configure LLM
llm_config={
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0,
}

# create an AssistantAgent instance named "assistant"
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config,
#    system_message="""You are the world's best engineer. You will assess the requirement and think step by step. You continue to improve the code until it meets the requirement"""
)
# create a UserProxyAgent instance named "user_proxy"
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

# Assign Autogen task
user_proxy.initiate_chat(
    assistant,
    message="""
Give me a TLDR in time sequence on what happened at OpenAI and Sam Altman over the weekend. List the events in bullet points. Please do fact checking from reputable news sources and verified account from x.com
Do not tell me as an AI, I don't have real-time access to the internet. Figure out a way of achieving the goal.
""",
)