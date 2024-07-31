from datetime import datetime

# region Task 1
dogum_yili = datetime.strptime(input("Doğum Yılınızı Giriniz:(GG.AA.YYYY) : "), "%d.%m.%Y")
yas = datetime.now() - dogum_yili

print(f'Şu zamana kadar {yas.total_seconds()} saniye yaşadınız. Sağlıklı günler dileriz.')
# endregion




# region Task 2
dogum_yili = datetime.strptime(input("Doğum Tarihinizi Giriniz (GG.AA.YYYY) : "), "%d.%m.%Y")

simdi = datetime.now()
fark = simdi - dogum_yili

# Farkı yıl, ay, hafta, gün, saat ve dakika cinsinden hesaplama
gunler = fark.days
yillar = gunler // 365
aylar = gunler // 30
haftalar = gunler // 7
saatler = fark.total_seconds() // 3600
dakikalar = fark.total_seconds() // 60

print(f"Şu zamana kadar {yillar} yıl, {aylar} ay, {haftalar} hafta, {gunler} gün, {saatler:.2f} saat, ve {dakikalar:.2f} dakika yaşadınız. Sağlıklı günler dileriz.")
# endregion