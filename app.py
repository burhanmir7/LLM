from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from decouple import config
from langchain_core.messages import HumanMessage, SystemMessage
SECRET_KEY = config('OPENAI_API_KEY')
 

#  LLM Model
llm = OpenAI(openai_api_key=SECRET_KEY)
response = llm.invoke("who is prime minister of Pakistan?")
print(response)

# Chat Model
chat = ChatOpenAI(openai_api_key=SECRET_KEY)
response = chat.invoke("hey there how it going?")
print(response.content)

# LCEM
chat = ChatOpenAI(openai_api_key=SECRET_KEY)
messages = [
    SystemMessage(content="You're a standup comedian"),
    HumanMessage(content="Who is the most powerful person in india?")
]
response = chat.invoke(messages)
print(response.content)

# PROMPT TEMPLATE with 1 input variable
from langchain.prompts import PromptTemplate
llm = OpenAI(openai_api_key=SECRET_KEY)

oneInputPrompt = PromptTemplate(
    input_variable=["about"], template = "Tell me a joke about {about}."
)
formattedOneInputPrompt = oneInputPrompt.format(about = "india")

response = llm.invoke(formattedOneInputPrompt)
print(response)

# PROMPT TEMPLATE wit  Multiple input variable
from langchain.prompts import PromptTemplate
llm = OpenAI(openai_api_key=SECRET_KEY)

multipleInputPrompt = PromptTemplate(
    input_variable=["about", "type"], template = "Tell me a {type} joke about {about}."
)
formattedMultipleInputPrompt = multipleInputPrompt.format(about = "United kingdom", type="political")

response = llm.invoke(formattedMultipleInputPrompt)
print(response)