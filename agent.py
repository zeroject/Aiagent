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
        "temperature": 0,
    },
    system_message="YOU ARE A CODING ASSITENT HELPING WITH PROBLEMS. COME WITH PYTHON SOLUTIONS TO THE PROBLEMS. IF YOU WANT THE USER TO SAVE THE CODE IN A FILE BEFORE EXECUTING IT, PUT # filename: <filename> inside the code block as the first line. DONT INCLUDE MUTIPLE CODE BLOCKS IN ONE RESPONSE. WHEN EVERYTHING IS DONE AND THE RESULT IS CORRECT REPLY WITH 'TERMINATE'"
)

userProxy = UserProxyAgent(
    name="proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "code", "use_docker": False},
)

reply = userProxy.initiate_chat(
    assistant,
    message="""{}""".format(sys.argv[1]),
    summary_method="reflection_with_llm"
)