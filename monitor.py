import os
import requests
from bs4 import BeautifulSoup

URL = "https://www.nintendo.com/it-it/Console-e-accessori/Nintendo-Switch-2/Bundle-Nintendo-Switch-2/Nintendo-Switch-2-Bundle-2785628.html"

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

html = requests.get(URL, timeout=20, headers={
    "User-Agent": "Mozilla/5.0"
}).text

soup = BeautifulSoup(html, "html.parser")
text = soup.get_text(" ", strip=True).lower()

keywords = [
    "preordina ora",
    "pre-ordina ora",
    "preorder",
]

available = any(word in text for word in keywords)

if available:
    message = "🚨 PREORDINE NINTENDO DISPONIBILE! 🚨\n\n" + URL

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message
        },
        timeout=20
    )

print("Controllo completato. Disponibile:", available)
