# Riot API'den örnek veri çekme (Valorant özelinde basit versiyon)

import requests

API_KEY = "RGAPI-6ac6d14b-03d0-463f-86b8-802e8984f19f"  # https://developer.riotgames.com adresinden alınmalı
HEADERS = {"X-Riot-Token": API_KEY}

def fetch_riot_data(username):
    try:
        # Kullanıcı adı üzerinden puuid alma
        region = "euw1"
        summoner_url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{username}"
        res = requests.get(summoner_url, headers=HEADERS)
        if res.status_code != 200:
            return None
        summoner_data = res.json()
        puuid = summoner_data['puuid']

        # Son 10 maçı alma
        match_ids_url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=10"
        matches = requests.get(match_ids_url, headers=HEADERS).json()

        match_data = []
        for match_id in matches:
            match_url = f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}"
            data = requests.get(match_url, headers=HEADERS).json()
            # Kullanıcının verisini bul
            for p in data['info']['participants']:
                if p['puuid'] == puuid:
                    match_data.append({
                        'match_id': match_id,
                        'kills': p['kills'],
                        'deaths': p['deaths'],
                        'assists': p['assists'],
                        'headshot_percent': p.get('headshots', 0),
                        'first_bloods': 1 if p.get('firstBloodKill', False) else 0
                    })
                    break
        return match_data
    except Exception as e:
        print(f"Hata: {e}")
        return None
