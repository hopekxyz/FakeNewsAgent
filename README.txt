🤖 Agente Fake News

Este projeto implementa um agente de IA com LangChain e OpenAI, capaz de analisar notícias e consultar ferramentas externas para auxiliar na verificação de fatos.

🚀 Como executar

Clone o repositório

git clone https://github.com/seu-usuario/agente-fake-news.git
cd agente-fake-news


Crie um ambiente virtual

python -m venv venv


Ative o ambiente:

Linux/Mac

source venv/bin/activate


Windows

venv\Scripts\activate


Instale as dependências

pip install -r requirements.txt


Configure as variáveis de ambiente

Crie um arquivo .env na raiz do projeto:

OPENAI_API_KEY=sua_chave_aqui


Execute o agente

python agent.py

📂 Estrutura simplificada
.
├── agent.py              # Inicialização do agente
├── search_tool.py        # Exemplo de tool customizada
├── prompt_principal.txt  # Prompt base do agente
├── requirements.txt      # Dependências do projeto
├── .env                  # Variáveis de ambiente (não versionado)
└── README.md             # Este arquivo

⚠️ Observações

O arquivo .env não é versionado (está no .gitignore), para proteger a chave da API.

Gere seu próprio requirements.txt com:

pip freeze > requirements.txt