import sys
from autogen import AssistantAgent
from autogen import UserProxyAgent

config_list = [
    {
        "model": "llama3.2",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama"
    }
]

assistant = AssistantAgent(
    name="assistant",
    llm_config={
        "config_list": config_list,
        "seed": 42,
        "temperature": 0,
    },
    system_message="PROPOSE ALL SOLUTIONS WITH PYTHON CODE"
)

userProxy = UserProxyAgent(
    name="proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "code", "use_docker": False},
)

reply = userProxy.initiate_chat(
    assistant,
    message="""{}""".format(sys.argv[1]),
    summary_method="reflection_with_llm"
)