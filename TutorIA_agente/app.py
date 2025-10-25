import streamlit as st
import pandas as pd
import re

from agentes.agente_tutoria import criar_agente_tutoria


st.set_page_config(page_title="TutorIA ", page_icon="🎓", layout="centered")

st.title("🎓 TutorIA")
st.write("""
Explore as ferramentas de IA para estudar melhor!
""")

try:
    agente = criar_agente_tutoria()
    llm = agente["llm"]
except Exception as e:
    st.error(f"Erro ao inicializar o agente de IA: {e}")
    st.stop()


    """Usei engenharia de prompt para definir exatamente como gostaria do meu retorno"""

def gerar_resumo(conteudo: str):
    prompt = f"""
Você é um assistente especialista em criar resumos de estudos claros, didáticos e organizados em tópicos.

TAREFA:
Resuma o conteúdo abaixo de forma estruturada, destacando os conceitos principais, definições, exemplos importantes e relações entre ideias.

INSTRUÇÕES:
- Organize o resumo em tópicos com marcadores ou numeração.
- Use frases curtas e linguagem simples.
- Foque nos pontos mais relevantes para revisão.
- Evite copiar trechos literais.
- Se possível, inclua uma seção final com "Resumo Geral" (2 a 3 linhas).
Texto:
{conteudo}
"""
    try:
            resposta = llm.invoke(prompt)
            return resposta.content.strip() if hasattr(resposta, "content") else str(resposta).strip()
    except Exception as e:
        return f"⚠️ Erro ao gerar resumo: {e}"






def gerar_cronograma(conteudo: str, dias: int):
    prompt = f"""
Você é um especialista em planejamento de estudos e aprendizado progressivo.

TAREFA:
Crie um cronograma de estudos baseado no conteúdo abaixo, distribuindo os temas de forma lógica e equilibrada ao longo de {dias} dias.

REQUISITOS:
- O aprendizado deve evoluir do básico ao avançado.
- Cada dia deve conter tópicos específicos e diferentes.
- Indique o tempo sugerido de dedicação por dia.
- Apresente o resultado em formato de **tabela de texto puro**, SEM usar tags HTML.

FORMATO DA TABELA:
Dia | Tópicos | Duração sugerida

INSTRUÇÕES ADICIONAIS:
- Sempre inicie com “Dia 1”.
- Mantenha os nomes das colunas exatamente como no formato acima.
- Use uma linha por dia.
- Caso o conteúdo seja extenso, priorize os temas mais importantes.

CONTEÚDO PARA O CRONOGRAMA:
{conteudo}

RESPOSTA:
"""
    try:

        resposta = llm.invoke(prompt)


        if hasattr(resposta, "content"):
            resposta = resposta.content
        else:
            resposta = str(resposta)


        resposta = resposta.replace("<br>", "\n").replace("<br/>", "\n").replace("</br>", "\n").strip()

 
        linhas = [linha.split("|") for linha in resposta.split("\n") if "|" in linha]

        if len(linhas) > 1:
            colunas = [c.strip() for c in linhas[0] if c.strip()]
            dados = [[c.strip() for c in linha if c.strip()] for linha in linhas[1:] if any(c.strip() for c in linha)]
            dados = [linha for linha in dados if not any(c.lower() in ["dia", "-----", "0"] for c in linha)]

            df = pd.DataFrame(dados, columns=pd.unique(colunas))
            if "Dia" in df.columns:
                df["Dia"] = range(1, len(df) + 1)
            return df

        else:
            return pd.DataFrame([
                {"Dia": "1", "Tópicos": "Leitura introdutória e revisão geral do conteúdo", "Duração sugerida": "1h"}
            ])

    except Exception as e:
        st.error(f"⚠️ Erro ao gerar cronograma: {e}")
        return pd.DataFrame([{"Dia": "-", "Tópicos": "Erro ao gerar cronograma", "Duração sugerida": "-"}])








def gerar_mapa_mental(conteudo: str):
    import re

    prompt = f"""
Você é um especialista em organização do conhecimento.

Crie um **mapa mental textual** sobre o tema abaixo.
Use o formato hierárquico simples:

Tema principal
- Subtema 1
  -- Conceito ou detalhe 1
  -- Conceito ou detalhe 2
- Subtema 2
  -- Conceito ou detalhe 1

Evite usar Markdown ou HTML.
Use apenas texto puro com hifens.

TEMA:
{conteudo}
"""

    try:
        resposta = llm.invoke(prompt)
        resposta = getattr(resposta, "content", str(resposta)).strip()

        if not resposta:
            return "⚠️ O mapa mental não pôde ser gerado."


        linhas = [l.strip() for l in resposta.split("\n") if l.strip()]
        tema_principal = linhas[0]
        estrutura = []
        subtema_atual = None

        for linha in linhas[1:]:
 
            if re.match(r"^[-•]\s*[A-ZÁÉÍÓÚÂÊÔÃÕ]", linha):
                subtema = linha.lstrip("-• ").strip()
                estrutura.append({"subtema": subtema, "conceitos": []})
                subtema_atual = estrutura[-1]

            elif re.match(r"^(--|—)\s*", linha) and subtema_atual:
                conceito = linha.lstrip("-—• ").strip()
                subtema_atual["conceitos"].append(conceito)

        html = f"""
        <div style='font-family: "Segoe UI", sans-serif; color: #EEE;'>
            <div style='text-align: center; margin-bottom: 1rem;'>
                <h2 style='color: #8be9fd;'>🧠 {tema_principal}</h2>
            </div>
            <div style='display: flex; flex-wrap: wrap; justify-content: center; gap: 2rem;'>
        """

        cores = ["#3DDC84", "#A970FF", "#FFA500", "#00BFFF"]
        for i, item in enumerate(estrutura):
            cor = cores[i % len(cores)]
            html += f"""
            <div style='
                background-color: rgba(255,255,255,0.05);
                border-left: 4px solid {cor};
                border-radius: 8px;
                padding: 1rem;
                width: 250px;
                box-shadow: 0 0 10px rgba(0,0,0,0.3);
            '>
                <h4 style='color: {cor}; margin-bottom: 0.5rem;'>🟢 {item["subtema"]}</h4>
                <ul style='list-style: none; padding-left: 1rem;'>
            """
            for conceito in item["conceitos"]:
                html += f"<li style='margin-bottom: 0.4rem;'>🔹 {conceito}</li>"
            html += "</ul></div>"

        html += "</div></div>"
        return html

    except Exception as e:
        st.error(f"⚠️ Erro ao gerar mapa mental: {e}")
        return None


aba1, aba2, aba3 = st.tabs(["📖 Resumir Conteúdo", "🗓️ Gerar Cronograma", "🧠 Mapa Mental"])

# Estado do texto (mantido entre abas)
if "texto" not in st.session_state:
    st.session_state["texto"] = ""


with aba1:
    st.session_state["texto"] = st.text_area(
        "✏️ Cole aqui o conteúdo ou resumo do seu material:",
        value=st.session_state["texto"],
        key="texto_resumo"
    )

    if st.button("Gerar Resumo"):
        if st.session_state["texto"].strip():
            with st.spinner("Gerando resumo..."):
                resumo = gerar_resumo(st.session_state["texto"])
            st.success("✅ Resumo criado com sucesso!")
            st.markdown("### 🧾 Resumo do conteúdo:")
            st.write(resumo)
        else:
            st.warning("⚠️ Por favor, insira um texto antes de gerar o resumo.")



with aba2:
    st.session_state["texto"] = st.text_area(
        "✏️ Cole aqui o conteúdo base para o cronograma:",
        value=st.session_state["texto"],
        key="texto_cronograma"
    )

    dias = st.slider("Quantos dias de plano?", 3, 30, 7)
    if st.button("Gerar Cronograma"):
        if st.session_state["texto"].strip():
            with st.spinner("Gerando cronograma de estudos..."):
                df = gerar_cronograma(st.session_state["texto"], dias)
            st.success("✅ Plano de estudos gerado com sucesso!")
            st.dataframe(df, use_container_width=True)
        else:
            st.warning("⚠️ Insira o conteúdo base antes de gerar o plano de estudos.")


with aba3:
    st.session_state["texto"] = st.text_area(
        "✏️ Cole aqui o conteúdo base para o mapa mental:",
        value=st.session_state["texto"],
        key="texto_mapa"
    )

    if st.button("Gerar Mapa Mental"):
        if st.session_state["texto"].strip():
            with st.spinner("Gerando mapa mental..."):
                mapa = gerar_mapa_mental(st.session_state["texto"])
            if mapa:
                st.success("✅ Mapa mental criado com sucesso!")
                st.markdown("### 🧩 Estrutura do Mapa Mental:")
                st.components.v1.html(mapa, height=600, scrolling=True)
            else:
                st.warning("⚠️ Não foi possível gerar o mapa mental.")
        else:
            st.warning("⚠️ Insira o conteúdo base antes de gerar o mapa mental.")
