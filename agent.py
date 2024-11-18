import tempfile
from autogen import ConversableAgent
from autogen.coding import LocalCommandLineCodeExecutor

temp_dir = tempfile.TemporaryDirectory()

executor = LocalCommandLineCodeExecutor(
    timeout=10,
    work_dir=temp_dir.name,
)

code_executor_agent = ConversableAgent(
    "name",
    llm_config=False,
    code_execution_config={"executor": executor},
    human_input_mode="ALWAYS",
)

reply = code_executor_agent.generate_reply(messages=[{"role": "user", "content": "PUT MSG HERE"}])
print(reply)
temp_dir.cleanup()