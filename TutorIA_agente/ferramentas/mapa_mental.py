from graphviz import Digraph
import re

def gerar_mapa_mental(conteudo: str) -> Digraph:
    """
    Gera um mapa mental textual simples a partir do conteúdo.
    Essa função será chamada pelo agente_tutoria ou diretamente do app.
    """
    dot = Digraph()
    dot.attr('node', shape='ellipse', style='filled', fillcolor='lightblue', color='black')

    linhas = [l.strip() for l in conteudo.split('\n') if l.strip()]
    tema_principal = linhas[0][:60] if linhas else "Tema principal"
    dot.node(tema_principal, tema_principal, fillcolor="lightyellow")

    for linha in linhas[1:]:
        if len(linha) > 5:
            dot.node(linha, linha)
            dot.edge(tema_principal, linha)

    return dot
