import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Транзакции", layout="centered")
st.title(" Транзакции")

url = st.text_input("Ссылка на API", "http://localhost:8000/transactions")

try:
    r = requests.get(url)
    r.raise_for_status()
    j = r.json()
    d = pd.DataFrame(j)

    if d.empty:
        st.warning("Нет данных.")
    else:
        st.subheader("Таблица")
        st.dataframe(d)

        if "amount" in d.columns:
            st.subheader("График сумм")
            st.bar_chart(d["amount"])

        if "category" in d.columns and "amount" in d.columns:
            st.subheader("По категориям")
            g = d.groupby("category")["amount"].sum().reset_index()
            st.bar_chart(g.set_index("category"))

        if "date" in d.columns:
            d["date"] = pd.to_datetime(d["date"])
            d["month"] = d["date"].dt.to_period("M")
            m = d.groupby("month")["amount"].sum()
            st.subheader("По месяцам")
            st.line_chart(m)

        st.subheader("Статистика")
        st.write(d.describe())

except Exception as e:
    st.error(f"Ошибка: {e}")