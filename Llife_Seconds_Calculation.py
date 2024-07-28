from datetime import datetime

dogum_yili = datetime.strptime(input("Doğum Yılınızı Giriniz:(GG.AA.YYYY) "), "%d.%m.%Y")
yas = datetime.now() - dogum_yili

print(f'Şu zamana kadar {yas.total_seconds()} saniye yaşadınız. Sağlıklı günler dileriz.')