# YAZILIM PRENSİPLERİ

# Yazılım prensipleri, yazılım geliştirme sürecinde kaliteli, sürdürülebilir, okunabilir ve ölçeklenebilir kod üretmek için takip edilmesi gereken genel kuralları ve yönergeleri ifade eder. Bu prensipler, yazılım mühendisliğinde daha iyi uygulamalar geliştirmek ve yazılım projelerinin başarısını artırmak için kullanılır.

# Unutulmaması gereken en önemli faktör bir yazılım projesinde birden fazla yazılım prensibi kullanılabilir ve genellikle kullanılmaktadırlar. Ancak her proje için hangi prensiplerin daha fazla vurgulanacağı ve hangi kombinasyonun kullanılacağı, projenin gereksinimlerine, boyutuna ve diğer faktörlere bağlı olarak değişebilir.



# region DRY (Don't Repeat Yourself)
# "Kendini Tekrar Etme" anlamına gelir ve bir yazılım geliştirme prensibidir. Bu prensip, bir yazılım projesindeki kodun tekrarlanmasını önlemeyi ve karmaşıklığı azaltmayı amaçlar. DRY prensibi, kodun tekrarlanması yerine, ortak kod parçalarının birleştirilmesi ve yeniden kullanılabilir hale getirilmesi gerektiğini vurgular. Bu sayede, kodun bakımı ve değiştirilmesi daha kolay hale gelir, hataların tekrarlanma olasılığı azalır ve kodun genel kalitesi artar. Bu prensip, yazılım geliştirme sürecinde daha verimli ve sürdürülebilir bir yaklaşım benimsemeyi teşvik eder.


def calculate_circle_area(radius):
    return 3.14 * radius ** 2

def calculate_circle_circumference(radius):
    return 2 * 3.14 * radius

# Yukarıdaki fonksiyonlar, dairenin alanını ve çevresini hesaplar.
# İki fonksiyon da dairenin yarıçapını parametre olarak alır ve hesaplama yapar.
# Yukarıdaki örnekte, dairenin alanını ve çevresini hesaplayan iki ayrı fonksiyon var. Bu fonksiyonlar, hesaplama için gereken formülü uygular ve yarıçapı parametre olarak alır. DRY prensibine uygun olarak, aynı mantığı tekrar tekrar yazmak yerine, bu mantığı tek bir yerde, yani iki ayrı fonksiyon içinde birleştirdik. Bu sayede, aynı hesaplama mantığını tekrarlamaktan kaçındık ve kodun daha bakımı kolay, daha okunabilir ve daha esnek olmasını sağladık.
# endregion





# region WET (Write Everything Twice)
# "Her Şeyi İki Kez Yaz" veya "We Enjoy Typing" (Yazmaktan Zevk Alırız) olarak da bilinen bir yazılım geliştirme antiprensibidir. DRY'nin tam tersi olarak kabul edilir. WET prensibine göre, kod tekrarının ve gereksiz tekrarların önemli olmadığı, hatta bazen tercih edilmesi gerektiği düşünülür.DRY prensibinin aksine, WET prensibi, tekrar eden kod parçalarının kodun okunabilirliğini artırabileceğini ve özellikle farklı durumlar için ayrı kod parçaları yazmanın daha anlaşılır olabileceğini savunur. Ancak, WET prensibi genellikle gereksiz kod tekrarlarına ve bakım zorluklarına yol açabilir, bu nedenle genellikle yazılım geliştirme pratiğinde tercih edilen bir yaklaşım değildir.


def check_string_length(string):
    length = 0
    for char in string:
        length += 1
    return length

def check_list_length(lst):
    length = 0
    for item in lst:
        length += 1
    return length

def check_dict_length(dictionary):
    length = 0
    for key in dictionary:
        length += 1
    return length

# Bu fonksiyonlar aynı mantığı uygulayarak farklı veri tiplerinin uzunluğunu kontrol ediyor.
# Bu örnek, aynı işlemi farklı veri tipleri için tekrar tekrar yapar ve bu da WET prensibine uygun bir kod örneği olarak kabul edilebilir. Ancak, genel olarak, bu tür tekrarlar kaçınılmalı ve DRY (Don't Repeat Yourself) prensibine uygun bir kod yapısı tercih edilmelidir.
# endregion





# region SOC (Separation of Concerns)
# "Endişelerin Ayrılması" kısaltmasıyla bilinen bir yazılım mühendisliği prensibidir. Bu prensip, bir yazılım sisteminin farklı sorumlulukların (concerns) birbirinden ayrılması yoluyla organize edilmesini önerir. Her bir modül, sınıf veya fonksiyon, belirli bir endişeyle ilgilenmeli ve bu endişenin dışındaki diğer işlevleri etkilememelidir.Bu prensip, kodun daha modüler, bakımı daha kolay ve yeniden kullanılabilir olmasını sağlar. Ayrıca, kodu daha anlaşılır hale getirir ve değişikliklerin belirli endişelerle sınırlı kalmasını sağlayarak hataların izole edilmesine yardımcı olur. Örneğin, bir MVC (Model-View-Controller) tasarım deseni, endişeleri ayrı modüllere ayırarak bu prensibi uygular. Model, veri işleme ve mantıksal işlevleri, View, kullanıcı arayüzüyle ilgili işlevleri, Controller ise giriş ve işlem yönlendirme işlevlerini yerine getirir. Bu şekilde, her bir bileşen belirli bir endişeye odaklanır ve diğerlerinden bağımsız olarak değiştirilebilir.


# Model
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save_to_database(self):
        # Veritabanına kullanıcıyı kaydet
        pass

# View
class UserView:
    def render(self, user):
        # Kullanıcı arayüzünü oluştur
        pass

# Controller
class UserController:
    def __init__(self, user_view):
        self.user_view = user_view

    def register_user(self, username, email):
        new_user = User(username, email)
        new_user.save_to_database()
        self.user_view.render(new_user)

# Kullanım
user_view = UserView()
user_controller = UserController(user_view)

user_controller.register_user("john_doe", "john@example.com")

# Bu örnekte, Model sınıfı veri ve iş mantığını içerir, View sınıfı kullanıcı arayüzünü oluşturur ve Controller sınıfı kullanıcı girişini işler ve View ile Model arasında arabuluculuk yapar. Bu şekilde, her bir bileşen kendi sorumluluklarına odaklanır ve uygulama kodu daha düzenli, bakımı kolay ve genişletilebilir hale gelir.
# endregion





# region SRP (Single Responsibility Principle)
# "Tek Sorumluluk Prensibi" kısaltmasıyla bilinen bir yazılım mühendisliği prensibidir. Bu prensip, her bir sınıfın veya modülün yalnızca bir tek sorumluluğu olması gerektiğini belirtir. Bir sınıf veya modülün tek bir görevi olmalıdır ve bu görevi en iyi şekilde yerine getirmelidir. Bu prensip, kodun bakımını kolaylaştırır, yeniden kullanılabilirliği artırır ve kodun daha anlaşılır olmasını sağlar. Ayrıca, bir sınıfın veya modülün birden fazla sorumluluğu olması durumunda, bu durum kodun karmaşıklığını artırabilir ve değişikliklerin yayılmasına neden olabilir. Örneğin, bir kullanıcı sınıfı yalnızca kullanıcı bilgilerini saklamalı ve işlememelidir. Kullanıcının oturum açma veya yetkilendirme gibi işlevleri başka bir sınıfa veya modüle atanmalıdır. Bu şekilde, her bir sınıf veya modül yalnızca belirli bir sorumluluğa odaklanır ve bu prensip doğrultusunda tasarlanmış olur.


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save_to_database(self):
        # Kullanıcı verilerini veritabanına kaydet
        pass

    def send_notification_email(self):
        # Kullanıcıya bildirim e-postası gönder
        pass

# Bu sınıf sadece kullanıcı arayüzüyle ilgilenir
class UserInterface:
    def display_user_info(self, user):
        # Kullanıcı bilgilerini ekrana yazdır
        pass

    def get_user_input(self):
        # Kullanıcıdan giriş al
        pass

# Bu örnekte, User sınıfı yalnızca kullanıcı verilerini temsil eder ve işler, veritabanına kaydetme ve bildirim e-postası gönderme gibi işlevlere sahiptir. UserInterface sınıfı ise kullanıcı arayüzü oluşturma işlevini üstlenir ve User sınıfı ile ilişkili değildir. Bu şekilde, her bir sınıfın sadece bir sorumluluğu vardır ve sınıflar birbirinden bağımsızdır, bu da kodun daha modüler ve bakımı daha kolay hale gelir.
# endregion





# region KISS (Keep It Simple Stupid)
# "Basit Tut Aptal" kısaltmasıyla bilinen bir yazılım prensibidir. Bu prensip, yazılımın tasarımında ve geliştirilmesinde basitlik ilkesinin önemini vurgular. KISS prensibine göre, bir problemi çözmek için kullanılan çözümün en basit ve en anlaşılır olması tercih edilmelidir. Bu prensip, gereksiz karmaşıklığı önler, kodun daha okunabilir ve bakımı daha kolay hale getirir. Basit bir çözüm, kodun daha az hata yapmasını sağlar ve yeni eklemeler veya değişikliklerin daha sorunsuz yapılmasını sağlar. KISS prensibinin uygulanması gereksiz karmaşıklıklardan kaçınılmasını, minimum sayıda bileşen veya yöntem kullanılmasını ve kodun gereksiz ayrıntılarla dolmamasını içerir. Bu prensip, yazılımın tasarımında ve kodun yazımında rehberlik eder ve daha temiz, daha etkili bir kod oluşturmayı amaçlar.


# İki sayının toplamını hesaplayan basit bir fonksiyon
def add_numbers(a, b):
    return a + b

# Bu fonksiyon, iki sayının toplamını hesaplamak için oldukça basit ve anlaşılır bir şekilde yazılmıştır. Gereksiz karmaşıklıklardan kaçınılmıştır ve doğrudan amaca yöneliktir. KISS prensibine göre, kodun karmaşıklığı arttıkça hata yapma olasılığı da artar. Bu nedenle, kod yazarken mümkün olduğunca basit ve anlaşılır olmaya özen göstermek önemlidir.
# endregion