# settings.py
API_URL = "https://api.ouedkniss.com/graphql"
HEADER = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://www.ouedkniss.com",
    "Referer": "https://www.ouedkniss.com/"
}
COUNT = 60
TRIES = 5  # Increase retries
WAIT_TIME_RETRY = 5
WAIT_TIME = 1.0  # ⬅️ Increase from 0.2 to 1.0 seconds
TYPE = "MINI"
