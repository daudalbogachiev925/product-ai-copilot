import os
import requests
import streamlit as st

API = os.getenv("API_URL", "http://api:8000")
st.set_page_config(page_title="PM Copilot", layout="wide")
st.title("Product AI Copilot")

@st.cache_data(ttl=15)
def fetch(path): return requests.get(f"{API}{path}").json()

stats = fetch("/api/admin/stats")
c1, c2, c3 = st.columns(3)
c1.metric("Документов", stats["documents"])
c2.metric("Диалогов", stats["chats"])
c3.metric("Avg confidence", stats["avg_confidence"])

st.subheader("Задать вопрос")
question = st.text_input("Вопрос по продуктовой базе")
if st.button("Спросить") and question:
    r = requests.post(f"{API}/api/chat", json={"question": question}).json()
    st.write(f"**Ответ:** {r['answer']}")
    st.write(f"**Confidence:** {r['confidence']}")
    if r["sources"]:
        st.subheader("Источники")
        for s in r["sources"]:
            st.write(f"- {s['title']} (score {s['score']})")

st.subheader("Добавить документ")
with st.form("add_doc"):
    title = st.text_input("Заголовок")
    category = st.text_input("Категория", "general")
    text = st.text_area("Текст", height=120)
    if st.form_submit_button("Добавить"):
        r = requests.post(f"{API}/api/documents", json={
            "title": title, "category": category, "text": text})
        if r.ok:
            st.success("Добавлено")
            st.cache_data.clear()

st.subheader("История диалогов")
logs = fetch("/api/admin/logs?limit=30")
for l in logs:
    st.write(f"**Q:** {l['question']}")
    st.write(f"**A:** {l['answer']}")
    st.write(f"_confidence: {l['confidence']}_")
    st.divider()
