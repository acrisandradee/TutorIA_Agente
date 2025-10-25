def resumir_conteudo(texto: str) -> str:
    """Cria um resumo do texto fornecido."""
    if not texto or len(texto.strip()) < 50:
        return "Por favor, cole um texto mais longo para que eu possa gerar um resumo."
    
    partes = texto.split(".")
    resumo = ". ".join(partes[:5])  # pega só as 5 primeiras frases
    return f"🧠 **Resumo do conteúdo:**\n\n{resumo.strip()}."
