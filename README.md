# 🧠TutorIA

Aplicação desenvolvida com  Streamlit, LangChain e OpenRouter para gerar planos de estudos personalizados

![Descrição da imagem](https://raw.githubusercontent.com/acrisandradee/TutorIA_Agente/main/imagem/picture.png)



## 🚀 Funcionalidades

- Interface interativa via Streamlit
- Geração de resumo
- Criação de plano de estudos
- Geração de mapa mental

## 🛠️ Tecnologias Utilizadas
  <p align="center">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" />

  <img src="https://img.shields.io/badge/LangChain-1C3C3C.svg?style=for-the-badge&logo=LangChain&logoColor=white" />
  
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
  <img src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" />
 <img src="https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white" />

  
</p>

</p>

## 📦 Como executar

1. Clone este repositório
   ```bash
  [ git clone https://github.com/seu-usuario/mentor-virtual.git](https://github.com/acrisandradee/TutorIA_Agente.git)

2. Crie e ative um ambiente virtual
   ```bash
   python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/macOS
    source venv/bin/activate

 3. Instale as dependências
   ```bash
pip install -r requirements.txt
```

4. Configure sua chave da API
   ```bash
    OPENROUTER_API_KEY=sk-xxxxxxx
5. Instale o Streamlit dentro do ambiente virtual
   ```bash
   pip install streamlit
 
6. Instale o langChain dentro do ambiente virtual
   ```bash
   pip install langchain[all]


▶️ Como executar
   ```bash
streamlit run app.py
````
 ```bash
#📁 Estrutura do Projeto
simplificaCodeMentor/
├── .venv                Ambiente virtual Python 
├── app.py               Configuração da Interface Streamlit
├── agent_tutorial.py    Classe Agent com LangChain e integração LLM
├── busca.py             Ferramenta gerar resumo
├── mapa_mental.py       Ferramenta gerar mapa mental
├── plano_estudos.py.py  Ferramenta gerar plano de estudos
├── .env                 Chave da API do OpenRouter 
├── requirements.txt     Lista de dependências Python do projeto
└── README.md            Documentação do projeto

````
 
---

<div align="center">

✨ Desenvolvido por **Cristina Andrade** – 2025  

Engenheira da Computação - CREA 2024107872

Aplicação de LLMs com Streamlit para mentoria inteligente personalizada
Construído com LangChain, OpenRouter, Streamlit e boas práticas de IA aplicada.



</div>
