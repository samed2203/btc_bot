
Yatırım tavsiyesi değildir.
# btc_bot tanıtıM.
#btc_bot KURULUM.
BU BOTu ben yatay giden piyasada kullanıyorum. Siz de nasıl bilirseniz öyle yaparsınız.
#Bot Algoritması: 12 Saatlik Momentum & Zamanlı Çıkış

1. Veri Hazırlığı (Referans Belirleme)

Kontrol Saati:Her sabah **08:00 (TSİ)**.
Referans Fiyat:Tam 12 saat öncesi olan **Dün Akşam 20:00 (TSİ)** fiyatı.
Eşik (Threshold):%0.40(Gürültü filtresi).

2. Karar Mekanizması (Saat 08:00'de Çalışır)
Sorgu:** Saat 08:00'deki fiyat, dün akşam 20:00'deki fiyattan **en az %0.40 daha düşük mü?**
EVET İSE:** Piyasa emriyle (Market Order) anında **AL**.
HAYIR İSE:** "Pusu Modu"na geç.

3. Pusu Modu (Yedek Plan)
Eğer 08:00'de fiyat yüksekse veya yeterince düşmemişse:
Aksiyon:** Son 12 saatin (20:00 - 08:00 arası) **En Düşük Seviyesine (Low)** bir `Limit Alım Emri` koy.
Süre:** Bu emir saat 22:00'ye kadar aktif kalır. Eğer bu fiyata değerse bot alımı yapar.

#4. Kesin Çıkış Kuralı (Exit Strategy)
*Zaman:Saat **22:00 (TSİ)**.
Aksiyon:*ozisyonun kârda veya zararda olmasına bakılmaksızın tüm  bakiyesini piyasa fiyatından **SAT** ve bekleyen tüm limit emirleri iptal et.
Kritik Emniyet Kuralları (Zarar Önleyici)
Ayı Filtresi:** Eğer fiyat gün boyu sert bir düşüşteyse ve son 12 saatin en düşük seviyesinin (Low) altına sarkar ve orada kalırsa, stop-loss devreye girmelidir.
Gürültü Filtresi:** %0.40'tan daha küçük hareketlerde asla alım yapma; çünkü bu hareketler genelde yön belirlemez, sadece borsa komisyonuna para yedirir.
---
| Parametre | Değer |
| --- | --- |
| **Referans Aralığı** | 12 Saat (20:00 -> 08:00) |
| **Giriş Şartı** | Fiyat Değişimi < -%0.40 |
| **Giriş Tipi** | Market Buy (Şart sağlandığında) / Limit Buy (Pusu modu) |
| **Çıkış Zamanı** | 22:00 (TSİ) |
| **Çıkış Tipi** | Market Sell |


öNCELİKLE BORSANIZDAN APİ KURMANIZ GEREKMEKTEDİR 
ÖNCELİKLE SERVERINIZIN OLMASI GEREKMEKTEDİR 
SERVERINIZ YOKSA KODU KULLANARAK SERVERSIZ BİLGİSAYARINIZ AÇIK KALMAK KOŞULUYLA UYGULAYABİLİRSİNİZ.


cmd yi dozya dizininde açın
sunucunuzuz çalıştırmak için
ssh -i "btc-bot-key.pem" ubuntu@.eu-north-1.compute.amazonaws.com size ait adresi server sağlayıcınızdan bularak çalıştırın
# Sistem paketlerini güncelle
sudo apt update && sudo apt upgrade -y

# Python ve Kripto kütüphanesini kur
sudo apt install python3-pip -y
pip3 install ccxt --break-system-packages
nano bot.py ile dosyanızı çalıştırın
bot.py klasörünüzü verdiğmiz kod ile kaydettikten sonra /ctrl o, ctrl x
crontab -e önce bu komutu çalıştırın
1 olarak yazın sonra en alt satıra şunları ekleyin
00 08 * * * /usr/bin/python3 /home/ubuntu/bot.py --buy
00 22 * * * /usr/bin/python3 /home/ubuntu/bot.py --sell
terminalde şu kodu yazarak 
sudo timedatectl set-timezone Europe/Istanbul saat ayarını yaparız 
artık çalışır vaziyettedir.

cat /home/ubuntu/bot_ozeti.txt sunucuya bağlandıktan sonra bu komut ile şog görebilirsiniz.
