import pandas as pd
import matplotlib.pyplot as plt

def analyze_kd_ratio(match_data):
    df = pd.DataFrame(match_data)
    df['kd'] = df['kills'] / df['deaths']
    avg_kd = df['kd'].mean()
    return round(avg_kd, 2), df

def plot_kd_trend(df):
    plt.plot(df['match_id'], df['kd'], marker='o')
    plt.title('KD Oranı Zamanla')
    plt.xlabel('Maç')
    plt.ylabel('KD')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("assets/kd_trend.png")
