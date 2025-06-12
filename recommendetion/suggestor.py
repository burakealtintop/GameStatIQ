def suggest_training(df):
    tips = []
    if df['headshot_percent'].mean() < 25:
        tips.append("Nişan alma eğitimi yap: Aim Lab veya Kovaak önerilir.")
    if df['first_bloods'].mean() < 1:
        tips.append("Maç başlarında daha agresif oynayabilirsin.")
    if df['kd'].mean() < 1:
        tips.append("Savunma oyununu geliştir, pozisyon hataları yapıyor olabilirsin.")
    return tips
