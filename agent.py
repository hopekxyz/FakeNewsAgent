from langchain.agents import create_openai_functions_agent, AgentExecutor, tool
from search_tool import search
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from env_variables import OPENAI_API_KEY

# Especificações do modelo de llm que vai ser usado.
llm = ChatOpenAI(
    temperature=0,
    model="gpt-4o-mini",
    api_key = OPENAI_API_KEY
)

def load_prompt(file_path="prompt_principal.txt"):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().replace("{", "{{").replace("}", "}}")
    except FileNotFoundError:
            return (f"Arquivo de prompt '{file_path}' não encontrado. Verifique se ele está no repositório.")

template = ChatPromptTemplate.from_messages([
    ('system', load_prompt()),
    ('human', '{question}'),
    ('placeholder', '{agent_scratchpad}')
])

tools = [search]
agent = create_openai_functions_agent(
    llm = llm,
    prompt = template,
    tools = tools
)

agent_executor = AgentExecutor(agent = agent, tools = tools, verbose = True)

question = input("Qual é a sua pergunta? ")
resultado = agent_executor.invoke({"question": question})

