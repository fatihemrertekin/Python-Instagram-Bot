import time
import sys
import getpass
from pygame import mixer
from termcolor import colored
from selenium import webdriver
from abc import ABC, abstractmethod
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def get_password(self):
        return self.__password
    
    def set_password(self, new_password):
        self.__password = new_password

class InstagramActions(ABC):
    def __init__(self):
        self.browser = webdriver.Chrome()

    @abstractmethod
    def print_message(self, message, state):
        pass

    @abstractmethod
    def sleepers(self):
        pass

    def scroll_down(self, takipSayisi):
        jsKomut = """
        sayfa = document.querySelector("._aano");
        sayfa.scrollTo(0,sayfa.scrollHeight);
        var sayfaSonu = sayfa.scrollHeight;
        return sayfaSonu;
        """
        takipSayisinaGoreScroll = int(takipSayisi / 12) + 15
        self.browser.implicitly_wait(35)
        sayfaSonu = self.browser.execute_script(jsKomut)

        for i in range(takipSayisinaGoreScroll):
            son = sayfaSonu
            self.sleepers(2)
            self.browser.implicitly_wait(35)
            sayfaSonu = self.browser.execute_script(jsKomut)
            self.print_message(f"{i+1}. Scroll", 2)
            if son == sayfaSonu:
                break

        self.print_message("Scroll işlemi tamamlandı.", 2)

    def page_scroll_down(self, pixelSayac):
        jsKomut = f"""
        sayfa = document.querySelector("html");
        sayfa.scrollTo(0,{pixelSayac});
        var sayfaSonu = sayfa.scrollHeight;
        return sayfaSonu;
        """

        self.browser.implicitly_wait(35)
        sayfaSonu = self.browser.execute_script(jsKomut)

        for i in range(1):
            son = sayfaSonu
            self.sleepers(2)
            self.browser.implicitly_wait(35)
            sayfaSonu = self.browser.execute_script(jsKomut)
            self.print_message(f"{i+1}. Scroll", 2)
            if son == sayfaSonu:
                break

        self.print_message("Scroll işlemi tamamlandı.", 2)
    
class InstagramUser(User, InstagramActions):
    def __init__(self, username, password):
        User.__init__(self, username, password)
        InstagramActions.__init__(self)
        self.text = ""

    def sleepers(self, second):
        if second == 1:
            time.sleep(1)
        elif second == 2:
            time.sleep(2)
        elif second == 3:
            time.sleep(3)
        elif second == 4:
            time.sleep(4)
        elif second == 5:
            time.sleep(5)
        elif second == 10:
            time.sleep(10)
        elif second == 30:
            time.sleep(30)

    def print_message(self, message, state):
        if state == 1:
            self.text = colored(message, "red")
        elif state == 2:
            self.text =  colored(message, "green")
        elif state == 3:
            self.text =  colored(message, "cyan")
        elif state == 4:
            self.text = colored(message, "yellow")
        print(self.text)

    def about_starter(self):
        print("")
        self.print_message("  _____           _                                    ____        _   ", 2)
        self.print_message(" |_   _|         | |                                  |  _ \\      | |  ", 2)
        self.print_message("   | |  _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___   | |_) | ___ | |_ ", 2)
        self.print_message("   | | | '_ \\/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \\  |  _ < / _ \\| __|", 2)
        self.print_message("  _| |_| | | \\__ \\ || (_| | (_| | | | (_| c | | | | | | |_) | (_) | |_ ", 2)
        self.print_message(" |_____|_| |_|__/ \\_ \\__,| \\__, |_|  \\__,_|_| |_| |_| |____/ \\___/ \\__|", 2)
        self.print_message("                            __/ |                                      ", 2)
        self.print_message("                           |___/                                       ", 2)
        self.print_message("# ==============================================================================", 2)
        self.print_message("# Author                 :Fatih Emre Ertekin", 2)
        self.print_message("# Department             :Computer Engineering", 2)
        self.print_message("# App Version            :1.0", 2)
        self.print_message("# Python Version         :3.12.0", 2)
        self.print_message("# Date                   :25.12.2023", 2)
        self.print_message("# Chrome Browser Version :120.0.6099.130 (Resmi Derleme) (64 bit) Sürümü", 2)
        self.print_message("# ==============================================================================", 2)
        print("")

    def login(self):
        self.print_message("🔄 Tarayıcı ekranı açılıyor...", 4)
        self.sleepers(1)

        self.browser.get("https://www.instagram.com/")
        self.sleepers(3)
        self.browser.implicitly_wait(35)

        """ implicitly_wait(30) Hakkında Yorum Satırı.
        Selenium’da Implicit Wait, web sürücüsüne “No Such Element Exception” oluşturmadan önce belirli bir süre beklemesini söylemek için kullanılır. Varsayılan ayar 0’dır. Süreyi belirledikten sonra, web sürücüsü bir exception atmadan önce bu süreyi bekleyecektir.
        """

        usernameInput = self.browser.find_element(By.CSS_SELECTOR, "input[name='username']") # insta giriş ekranındaki kullanıcı adı input'unun xpath'i.
        passwordInput = self.browser.find_element(By.CSS_SELECTOR, "input[name='password']") # insta giriş ekranındaki şifre input'unun xpath'i.
        signInButton = self.browser.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button > div") # insta giriş ekranındaki button'un xpath'i.


        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.get_password())
        self.sleepers(1)
        signInButton.click()
        self.print_message("✅ Instagrama giriş yapılıyor.", 2)
        self.sleepers(2)

        
        try:
            error_element = self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/span/div')
            self.print_message("Kullanıcı Adı veya Şifreniz yanlış! Lütfen programı tekrar çalıştırın.", 1)
            sys.exit()

        except NoSuchElementException:
            self.print_message("✅ Instagrama giriş yapıldı.", 2)
            self.sleepers(4)

    def follow_followers(self):
        self.print_message("🔄 Takip etme işlemi başlatılıyor...", 4)
        self.sleepers(1)

        self.print_message("Hangi sayfa için arama yapmak istiyorsunuz ?", 3)
        kullaniciAdi = input()

        self.print_message("Kaç kişiyi takip etmek istiyorsunuz ? (Tavsiye edilen günlük max değer: 50)", 3)
        takipSayisi = int(input())

        self.print_message(f"🔄 {kullaniciAdi} adlı kullanıcı sayfası açılıyor...", 4)
        self.browser.get(f"https://www.instagram.com/{kullaniciAdi}/")
        self.sleepers(3)
        
        self.browser.implicitly_wait(35)
        self.browser.find_element(By.CSS_SELECTOR, ".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._alvs._a6hd").click() # takip edilecek kişinin takipçilerinin sayısının yazdığı link
        self.sleepers(4)

        InstagramActions.scroll_down(self,takipSayisi) # Açılan penceredeki bütün elemanları yüklemek için scroll barı aşağı kaydıran kod.

        dialog = self.browser.find_element(By.CSS_SELECTOR, "body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div:nth-child(2) > div") # takipçilerin konteynırı
        takipEtButtonlari = dialog.find_elements(By.CSS_SELECTOR, "button") # scrool yapılmadan önce takipçilerin sayısı

        counter = 1
        sum = 0

        for takipEt in takipEtButtonlari:
            if takipEt.text == "Takip Et":
                takipEt.click()
                self.print_message(f"{counter}. Kullanıcı takip edildi. ✅", 2)
                self.sleepers(5)
                counter = counter + 1
                sum = counter

            elif takipEt.text == "İstek Gönderildi":
                self.print_message("Zaten istek göndermiştin. Yanıt bekleniyor... 🔄", 4)

            else:
                self.print_message("Zaten takiptesin. ⭕", 1)
                
            if counter == 21 or counter == 41 or counter == 61 or counter == 81 or counter == 101:
                self.print_message("Ban yememek için program 30 saniye beklemede. 🔄", 4)
                self.sleepers(30) # instagramdan ban yememek için her 20 kişide bir 30 saniye bekletme kodu.

            if counter == 11 or counter == 31 or counter == 51 or counter == 71 or counter == 91:
                self.print_message("Ban yememek için program 10 saniye beklemede. 🔄", 4)
                self.sleepers(10) # instagramdan ban yememek için n'inci kişilere gelindiğinde 10 saniye bekletme kodu.

            if counter == takipSayisi + 1:
                self.print_message(f"Toplam {sum - 1} kişi takip edildi.", 3)
                break

    def unfollow(self):
        self.print_message("🔄 Takipten çıkma işlemi başlatılıyor...", 4)
        self.sleepers(1)

        self.print_message("Kaç kişiyi takipten çıkarmak istiyorsunuz ? (Tavsiye edilen günlük max değer: 50)", 3)
        takipSayisi = int(input())

        self.browser.get(f"https://www.instagram.com/{self.username}/")
        self.sleepers(3)
        self.browser.implicitly_wait(35)

        self.browser.find_element(By.CSS_SELECTOR, f"a[href='/{self.username}/following/']").click() # takip edilenler sayısını gösteren profil linki
        self.sleepers(4)
        
        InstagramActions.scroll_down(self,takipSayisi) # Açılan penceredeki bütün elemanları yüklemek için scroll barı aşağı kaydıran kod.

        dialog = self.browser.find_element(By.CSS_SELECTOR, "body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div:nth-child(1) > div") # takipçilerin konteynırı

        takiptenCikButtonlari = dialog.find_elements(By.CSS_SELECTOR, "button") # scrool yapılmadan önce takipçilerin sayısı
        
        counter = 1
        sum = 0
        for takiptenCik in takiptenCikButtonlari:
            if takiptenCik.text == "Takiptesin":
                takiptenCik.click()
                self.sleepers(1)
                self.browser.implicitly_wait(35)
                self.browser.find_element(By.XPATH, "//button[text()='Takibi Bırak']").click()
                self.print_message(f"{counter}. Kullanıcı takipten çıkıldı. ✅", 2)
                self.sleepers(5)
                counter = counter + 1
                sum = counter
                
            if counter == 21 or counter == 41 or counter == 61 or counter == 81 or counter == 101:
                self.print_message("Ban yememek için program 30 saniye beklemede. 🔄", 4)
                self.sleepers(30) # instagramdan ban yememek için her 20 kişide bir 30 saniye bekletme kodu.

            if counter == 11 or counter == 31 or counter == 51 or counter == 71 or counter == 91:
                self.print_message("Ban yememek için program 10 saniye beklemede. 🔄", 4)
                self.sleepers(10) # instagramdan ban yememek için n'inci kişilere gelindiğinde 10 saniye bekletme kodu.

            if counter == takipSayisi + 1:
                self.print_message(f"Toplam {sum - 1} kişi takipten çıkıldı.", 3)
                break

    def like_by_hashtag(self):
        self.print_message("🔄 Etikete göre post beğenme işlemi başlatılıyor...", 4)
        self.sleepers(1)

        self.print_message("Hangi etiket için arama yapmak istiyorsunuz ?", 3)
        etiketAdi = input()

        self.print_message("Kaç tane gönderi beğenmek istiyorsunuz ? (Tavsiye edilen günlük max değer: 50)", 3)
        gonderiSayisi = int(input())

        self.print_message(f"🔄 {etiketAdi} adlı etiketiyle ilgili gönderiler açılıyor...", 4)
        self.browser.get(f"https://www.instagram.com/explore/tags/{etiketAdi}/")
        self.sleepers(3)

        pixelSayac = 0
        InstagramActions.page_scroll_down(self,pixelSayac)
        pixelSayac = pixelSayac + 870

        self.browser.implicitly_wait(35)
        dialog = self.browser.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > section:nth-child(1) > main:nth-child(1) > article:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)")
        gonderiler = dialog.find_elements(By.TAG_NAME, "a")

        counter = 1
        sum = 0
        for gonderi in gonderiler:
            if counter <= gonderiSayisi:
                gonderi.click()
                self.sleepers(2)
                self.browser.implicitly_wait(35)
                self.browser.find_element(By.CSS_SELECTOR, "span[class='_aamw'] div[class='x6s0dn4 x78zum5 xdt5ytf xl56j7k']").click()
                self.sleepers(1)
                self.browser.back()
                self.print_message(f"{counter}. Gönderi beğenildi. ✅", 2)
                self.sleepers(3)
                sum = counter
                counter += 1

            else:
                self.print_message(f"Toplam {sum} tane gönderi beğenildi.", 3)
                break

            if counter == 10 or counter == 19 or counter == 28 or counter == 37 or counter == 46 or counter == 55:
                InstagramActions.page_scroll_down(self,pixelSayac)
                pixelSayac = pixelSayac + 870

            if counter == 21 or counter == 41 or counter == 61 or counter == 81 or counter == 101:
                self.print_message("Ban yememek için program 30 saniye beklemede. 🔄", 4)
                self.sleepers(30) # instagramdan ban yememek için her 20 kişide bir 30 saniye bekletme kodu.

            if counter == 11 or counter == 31 or counter == 51 or counter == 71 or counter == 91:
                self.print_message("Ban yememek için program 10 saniye beklemede. 🔄", 4)
                self.sleepers(10) # instagramdan ban yememek için n'inci kişilere gelindiğinde 10 saniye bekletme kodu.

if __name__ == "__main__":
    mixer.init()
    mixer.music.load('starter_voice.mp3')
    mixer.music.play()
    
    username = input(colored("Kullanıcı adınızı girin:", "red"))
    password = getpass.getpass(colored("Şifrenizi girin:", "red"))

    instaBot = InstagramUser(username, password)

    instaBot.about_starter()
    instaBot.login()

    while True:
        print(colored("--------------------------- SEÇİM EKRANI ---------------------------", "yellow"))
        print(colored("1- Kullanıcı adına göre arama ile sayfanın takipçilerini takip etme.", "cyan")) # İşlem listesi.
        print(colored("2- Takip edilen kişileri takipten çıkarma.", "cyan"))
        print(colored("3- Girilen etikete göre gönderi beğenme.", "cyan"))
        print(colored("Seçiminiz (örnek: 1): ", "yellow"))

        secim = int(input())

        if secim == 1:
            # Takipçileri takip etme işlemleri için
            instaBot.follow_followers()

        elif secim == 2:
            # Takipten çıkmak için
            instaBot.unfollow()

        elif secim == 3:
            # Beğeni işlemleri için
            instaBot.like_by_hashtag()

        islemDevamMi = input(colored("Başka bir işlem yapmak istiyor musunuz ? (EVET için e, HAYIR için h)", "red"))

        if islemDevamMi == "e":
            print("")
            continue
        else:
            print(colored("Programdan çıkış yapılıyor... 🔄", "yellow"))
            break
            

    

