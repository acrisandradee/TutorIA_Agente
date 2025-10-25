import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from ferramentas.busca import resumir_conteudo
from ferramentas.plano_estudos import gerar_plano_estudos
from ferramentas.mapa_mental import gerar_mapa_mental

load_dotenv()

def criar_agente_tutoria():
    """Cria o agente TutorIA com ferramentas de resumo, cronograma e mapa mental."""
    llm = ChatOpenAI(
        model="anthropic/claude-3.5-sonnet",
        temperature=0.5,
            api_key=os.getenv("OPENROUTER_API_KEY"),  # 👈 Corrigido aqui
        base_url=os.getenv("OPENAI_API_BASE"),
    )

    ferramentas = {
        "resumir_conteudo": resumir_conteudo,
        "gerar_plano_estudos": gerar_plano_estudos,
        "gerar_mapa_mental": gerar_mapa_mental
    }

    return {"llm": llm, "ferramentas": ferramentas}
