from langchain_azure_ai.chat_models import AzureAIOpenAIApiChatModel
from dotenv import load_dotenv
load_dotenv()
import os

llm = AzureAIOpenAIApiChatModel(
    endpoint="https://models.inference.ai.azure.com",
    credential=os.getenv("OPENAI_API_KEY"),
    model="gpt-4o"   # or deployed model
)

print(llm.invoke("What is the capital of France?").content)