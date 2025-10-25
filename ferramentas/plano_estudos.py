import pandas as pd
from datetime import datetime, timedelta

def gerar_plano_estudos(conteudo: str, dias: int = 7) -> pd.DataFrame:
    """Cria um plano de estudos com base no conteúdo fornecido."""
    topicos = [t.strip() for t in conteudo.split("\n") if len(t.strip()) > 10]
    topicos = topicos[:dias] if len(topicos) >= dias else (topicos * (dias // len(topicos) + 1))[:dias]

    hoje = datetime.today()
    plano = [{"Data": (hoje + timedelta(days=i)).strftime("%d/%m/%Y"), "Tópico": topicos[i]} for i in range(dias)]
    return pd.DataFrame(plano)
