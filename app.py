### GameStatIQ MVP - app.py

import streamlit as st
from analysis.analyzer import analyze_kd_ratio, plot_kd_trend
from recommendation.suggestor import suggest_training
from data_fetching.riot_api import fetch_riot_data  # örnek olarak Riot API seçildi

st.set_page_config(page_title="GameStatIQ", layout="wide")
st.title("🎮 GameStatIQ - Kişisel Oyun Performans Analizi")

nickname = st.text_input("Oyun Nick'ini Gir")

if nickname:
    st.info("Veriler çekiliyor...")
    match_data = fetch_riot_data(nickname)

    if match_data:
        avg_kd, df = analyze_kd_ratio(match_data)
        plot_kd_trend(df)
        st.image("assets/kd_trend.png")

        st.metric("Ortalama KD", avg_kd)

        st.subheader("Gelişim Önerileri")
        for s in suggest_training(df):
            st.write(f"✅ {s}")
    else:
        st.error("Veriler çekilemedi. Lütfen nickname doğru mu kontrol et.")