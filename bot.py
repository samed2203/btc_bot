import ccxt
import sys
from datetime import datetime

# --- AYARLAR ---
exchange = ccxt.kucoin({
    'apiKey': 'apikeyiniz',
    'secret': 'secretkeyiniz',
    'password': 'passwordunuz',
})

symbol = 'BTC/USDT'
buy_amount_usd = 30

def log_yaz(mesaj):
    zaman = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("/home/ubuntu/bot_ozeti.txt", "a") as f:
        f.write(f"[{zaman}] {mesaj}\n")

def run_logic():
    try:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe='4h', limit=50)
        current_price = ohlcv[-1][4]
        ma50 = sum(c[4] for c in ohlcv) / 50

        if current_price < ma50:
            log_yaz(f"İşlem İptal: Fiyat ({current_price}) MA50 ({ma50:.2f}) altında. (Minik Ayı)")
            return

        btc_amount = buy_amount_usd / current_price
        exchange.create_market_buy_order(symbol, btc_amount)
        log_yaz(f"ALIM YAPILDI: {current_price} fiyattan {buy_amount_usd} USD'lik BTC alındı.")
    except Exception as e:
        log_yaz(f"ALIM HATASI: {str(e)}")

def sell_logic():
    try:
        balance = exchange.fetch_balance()
        btc_free = balance['total']['BTC']
        if btc_free > 0.00005:
            exchange.create_market_sell_order(symbol, btc_free)
            log_yaz(f"SATIŞ YAPILDI: {btc_free} BTC piyasa fiyatından satıldı. Nakite geçildi.")
        else:
            log_yaz("SATIŞ İPTAL: Cüzdanda yeterli BTC bulunamadı.")
    except Exception as e:
        log_yaz(f"SATIŞ HATASI: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--buy": 
            run_logic()
        elif sys.argv[1] == "--sell": 
            sell_logic()
