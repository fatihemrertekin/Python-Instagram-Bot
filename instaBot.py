import time
from termcolor import colored
from selenium import webdriver
from pygame import mixer
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InstaBot:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
    
    def hakkindaBilgisi(self):
        print("")
        self.mesajOlustur("  _____           _                                    ____        _   ", 2)
        self.mesajOlustur(" |_   _|         | |                                  |  _ \      | |  ", 2)
        self.mesajOlustur("   | |  _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___   | |_) | ___ | |_ ", 2)
        self.mesajOlustur("   | | | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \  |  _ < / _ \| __|", 2)
        self.mesajOlustur("  _| |_| | | \__ \ || (_| | (_| | | | (_| c | | | | | | |_) | (_) | |_ ", 2)
        self.mesajOlustur(" |_____|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_| |____/ \___/ \__|", 2)
        self.mesajOlustur("                            __/ |                                      ", 2)
        self.mesajOlustur("                           |___/                                       ", 2)
        self.mesajOlustur("# ==============================================================================", 2)
        self.mesajOlustur("# author         :Fatih Emre Ertekin", 2)
        self.mesajOlustur("# instagram      :https://www.instagram.com/yazilimtechno/", 2)
        self.mesajOlustur("# youtube        :https://www.youtube.com/channel/UCaBa10zNtyjx7m9oENfT3UA", 2)
        self.mesajOlustur("# email          :fatihemrertekin.74@gmail.com", 2)
        self.mesajOlustur("# date           :17.12.2022", 2)
        self.mesajOlustur("# version        :1.0", 2)
        self.mesajOlustur("# python_version :3.9.5", 2)
        self.mesajOlustur("# ==============================================================================", 2)
        print("")

    def mesajOlustur(self, mesaj, durum):
        if durum == 1:
            uyari= colored(mesaj, "red")
        elif durum == 2:
            uyari =  colored(mesaj, "green")
        elif durum == 3:
            uyari =  colored(mesaj, "cyan")
        elif durum == 4:
            uyari = colored(mesaj, "yellow")
        print(uyari)

    def birSaniyeUyut(self):
        time.sleep(1)

    def ikiSaniyeUyut(self):
        time.sleep(2)

    def ucSaniyeUyut(self):
        time.sleep(3)

    def dortSaniyeUyut(self):
        time.sleep(4)

    def besSaniyeUyut(self):
        time.sleep(5)

    def onSaniyeUyut(self):
        time.sleep(10)
    
    def otuzSaniyeUyut(self):
        time.sleep(30)

    def besDakikaUyut(self):
        time.sleep(300)

    def onDakikaUyut(self):
        time.sleep(600)

    def birSaatUyut(self):
        time.sleep(3600)

    def scrollDown(self,takipSayisi):
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
            self.ikiSaniyeUyut()
            self.browser.implicitly_wait(35)
            sayfaSonu = self.browser.execute_script(jsKomut)
            self.mesajOlustur(f"{i+1}. Scroll", 2)
            if son == sayfaSonu:
                break

        self.mesajOlustur("Scroll i??lemi tamamland??.", 2)

    def sayfaScrollDown(self,pixelSayac):
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
            self.ikiSaniyeUyut()
            self.browser.implicitly_wait(35)
            sayfaSonu = self.browser.execute_script(jsKomut)
            self.mesajOlustur(f"{i+1}. Scroll", 2)
            if son == sayfaSonu:
                break

        self.mesajOlustur("Scroll i??lemi tamamland??.", 2)


    def girisYap(self):
        self.mesajOlustur("???? Taray??c?? ekran?? a????l??yor...", 4)
        self.birSaniyeUyut()

        self.browser.get("https://www.instagram.com/")
        self.ucSaniyeUyut()
        self.browser.implicitly_wait(35)

        """ implicitly_wait(30) Hakk??nda Yorum Sat??r??.
        Selenium???da Implicit Wait, web s??r??c??s??ne ???No Such Element Exception??? olu??turmadan ??nce belirli bir s??re beklemesini s??ylemek i??in kullan??l??r. Varsay??lan ayar 0???d??r. S??reyi belirledikten sonra, web s??r??c??s?? bir exception atmadan ??nce bu s??reyi bekleyecektir.
        """

        usernameInput = self.browser.find_element_by_css_selector("input[name='username']") # insta giri?? ekran??ndaki kullan??c?? ad?? input'unun xpath'i.
        passwordInput = self.browser.find_element_by_css_selector("input[name='password']") # insta giri?? ekran??ndaki ??ifre input'unun xpath'i.
        signInButton = self.browser.find_element_by_css_selector("body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > main:nth-child(2) > article:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(3)") # insta giri?? ekran??ndaki button'un xpath'i.

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        self.birSaniyeUyut()
        signInButton.click()
        
        self.mesajOlustur("??? Instagrama giri?? yap??ld??.", 2)
        self.dortSaniyeUyut()


    def takipcileriTakipEt(self):
        self.mesajOlustur("???? Takip etme i??lemi ba??lat??l??yor...", 4)
        self.birSaniyeUyut()

        self.mesajOlustur("Hangi sayfa i??in arama yapmak istiyorsunuz ?", 3)
        kullaniciAdi = input()

        self.mesajOlustur("Ka?? ki??iyi takip etmek istiyorsunuz ? (Tavsiye edilen g??nl??k max de??er: 50)", 3)
        takipSayisi = int(input())

        self.mesajOlustur(f"???? {kullaniciAdi} adl?? kullan??c?? sayfas?? a????l??yor...", 4)
        self.browser.get(f"https://www.instagram.com/{kullaniciAdi}/")
        self.ucSaniyeUyut()
        
        self.browser.implicitly_wait(35)
        self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a").click() # takip edilecek ki??inin takip??ilerinin say??s??n??n yazd?????? link
        self.dortSaniyeUyut()

        InstaBot.scrollDown(self,takipSayisi) # A????lan penceredeki b??t??n elemanlar?? y??klemek i??in scroll bar?? a??a???? kayd??ran kod.

        dialog = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]") # takip??ilerin konteyn??r??

        takipEtButtonlari = dialog.find_elements_by_css_selector("button") # scrool yap??lmadan ??nce takip??ilerin say??s??

        counter = 1
        sum = 0
        for takipEt in takipEtButtonlari:
            if takipEt.text == "Takip Et":
                takipEt.click()
                self.mesajOlustur(f"{counter}. Kullan??c?? takip edildi. ???", 2)
                self.besSaniyeUyut()
                counter = counter + 1
                sum = counter

            elif takipEt.text == "??stek G??nderildi":
                self.mesajOlustur("Zaten istek g??ndermi??tin. Yan??t bekleniyor... ????", 4)

            else:
                self.mesajOlustur("Zaten takiptesin. ???", 1)
                
            if counter == 21 or counter == 41 or counter == 61 or counter == 81 or counter == 101:
                self.mesajOlustur("Ban yememek i??in program 30 saniye beklemede. ????", 4)
                self.otuzSaniyeUyut() # instagramdan ban yememek i??in her 20 ki??ide bir 30 saniye bekletme kodu.

            if counter == 11 or counter == 31 or counter == 51 or counter == 71 or counter == 91:
                self.mesajOlustur("Ban yememek i??in program 10 saniye beklemede. ????", 4)
                self.onSaniyeUyut() # instagramdan ban yememek i??in n'inci ki??ilere gelindi??inde 10 saniye bekletme kodu.

            if counter == takipSayisi + 1:
                self.mesajOlustur(f"Toplam {sum - 1} ki??i takip edildi.", 3)
                break
        
    def takiptenCik(self):
        self.mesajOlustur("???? Takipten ????kma i??lemi ba??lat??l??yor...", 4)
        self.birSaniyeUyut()

        self.mesajOlustur("Ka?? ki??iyi takipten ????karmak istiyorsunuz ? (Tavsiye edilen g??nl??k max de??er: 50)", 3)
        takipSayisi = int(input())

        self.browser.get(f"https://www.instagram.com/{self.username}/")
        self.ucSaniyeUyut()
        self.browser.implicitly_wait(35)

        self.browser.find_element_by_xpath(f"//a[@href='/{self.username}/following/']//div[@class='_aacl _aacp _aacu _aacx _aad6 _aade']").click() # takip edilenler say??s??n?? g??steren profil linki
        self.dortSaniyeUyut()
        
        InstaBot.scrollDown(self,takipSayisi) # A????lan penceredeki b??t??n elemanlar?? y??klemek i??in scroll bar?? a??a???? kayd??ran kod.

        dialog = self.browser.find_element_by_css_selector("._aano") # takip??ilerin konteyn??r??

        takiptenCikButtonlari = dialog.find_elements_by_css_selector("button") # scrool yap??lmadan ??nce takip??ilerin say??s??
        
        counter = 1
        sum = 0
        for takiptenCik in takiptenCikButtonlari:
            if takiptenCik.text == "Takiptesin":
                takiptenCik.click()
                self.birSaniyeUyut()
                self.browser.implicitly_wait(35)
                self.browser.find_element_by_xpath("//button[text()='Takibi B??rak']").click()
                self.mesajOlustur(f"{counter}. Kullan??c?? takipten ????k??ld??. ???", 2)
                self.besSaniyeUyut()
                counter = counter + 1
                sum = counter
                
            if counter == 21 or counter == 41 or counter == 61 or counter == 81 or counter == 101:
                self.mesajOlustur("Ban yememek i??in program 30 saniye beklemede. ????", 4)
                self.otuzSaniyeUyut() # instagramdan ban yememek i??in her 20 ki??ide bir 30 saniye bekletme kodu.

            if counter == 11 or counter == 31 or counter == 51 or counter == 71 or counter == 91:
                self.mesajOlustur("Ban yememek i??in program 10 saniye beklemede. ????", 4)
                self.onSaniyeUyut() # instagramdan ban yememek i??in n'inci ki??ilere gelindi??inde 10 saniye bekletme kodu.

            if counter == takipSayisi + 1:
                self.mesajOlustur(f"Toplam {sum - 1} ki??i takipten ????k??ld??.", 3)
                break
    
    def etiketeGoreBegen(self):
        self.mesajOlustur("???? Etikete g??re post be??enme i??lemi ba??lat??l??yor...", 4)
        self.birSaniyeUyut()

        self.mesajOlustur("Hangi etiket i??in arama yapmak istiyorsunuz ?", 3)
        etiketAdi = input()

        self.mesajOlustur("Ka?? tane g??nderi be??enmek istiyorsunuz ? (Tavsiye edilen g??nl??k max de??er: 50)", 3)
        gonderiSayisi = int(input())

        self.mesajOlustur(f"???? {etiketAdi} adl?? etiketiyle ilgili g??nderiler a????l??yor...", 4)
        self.browser.get(f"https://www.instagram.com/explore/tags/{etiketAdi}/")
        self.ucSaniyeUyut()

        pixelSayac = 1150
        InstaBot.sayfaScrollDown(self,pixelSayac)
        pixelSayac = pixelSayac + 870

        self.browser.implicitly_wait(35)
        dialog = self.browser.find_element_by_css_selector("body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > section:nth-child(1) > main:nth-child(2) > article:nth-child(2) > div:nth-child(3)")
        gonderiler = dialog.find_elements_by_tag_name("a")

        counter = 1
        sum = 0
        for gonderi in gonderiler:
            if counter <= gonderiSayisi:
                gonderi.click()
                self.ikiSaniyeUyut()
                self.browser.implicitly_wait(35)
                self.browser.find_element_by_css_selector("span[class='_aamw'] button[type='button']").click()
                self.birSaniyeUyut()
                self.browser.back()
                self.mesajOlustur(f"{counter}. G??nderi be??enildi. ???", 2)
                self.ucSaniyeUyut()
                sum = counter
                counter += 1

            else:
                self.mesajOlustur(f"Toplam {sum} tane g??nderi be??enildi.", 3)
                break

            if counter == 10 or counter == 19 or counter == 28 or counter == 37 or counter == 46 or counter == 55:
                InstaBot.sayfaScrollDown(self,pixelSayac)
                pixelSayac = pixelSayac + 870

            if counter == 21 or counter == 41 or counter == 61 or counter == 81 or counter == 101:
                self.mesajOlustur("Ban yememek i??in program 30 saniye beklemede. ????", 4)
                self.otuzSaniyeUyut() # instagramdan ban yememek i??in her 20 ki??ide bir 30 saniye bekletme kodu.

            if counter == 11 or counter == 31 or counter == 51 or counter == 71 or counter == 91:
                self.mesajOlustur("Ban yememek i??in program 10 saniye beklemede. ????", 4)
                self.onSaniyeUyut() # instagramdan ban yememek i??in n'inci ki??ilere gelindi??inde 10 saniye bekletme kodu.

    def menu(self):
        print("")
        self.besSaniyeUyut()
        instaCMD.hakkindaBilgisi()
        instaCMD.girisYap()
        print("")

        while True:
            self.mesajOlustur("--------------------------- SE????M EKRANI ---------------------------", 4)
            self.mesajOlustur("1- Kullan??c?? ad??na g??re arama ile sayfan??n takip??ilerini takip etme.", 3) # ????lem listesi.
            self.mesajOlustur("2- Takip edilen ki??ileri takipten ????karma.", 3)
            self.mesajOlustur("3- Girilen etikete g??re g??nderi be??enme.", 3)
            
            self.mesajOlustur("Se??iminiz (??rnek: 1): ", 4)

            secim = int(input())
            if secim == 1:
                instaCMD.takipcileriTakipEt()
            elif secim == 2:
                instaCMD.takiptenCik()
            elif secim == 3:
                instaCMD.etiketeGoreBegen()

            self.mesajOlustur("Ba??ka bir i??lem yapmak istiyor musunuz ? (EVET i??in e, HAYIR i??in h)", 1)
            islemDevamMi = input()

            if islemDevamMi == "e":
                print("")
                continue
            else:
                self.mesajOlustur("Programdan ????k???? yap??l??yor... ????", 4)
                self.browser.quit()
                break

mixer.init() # mikser ??rne??ini ba??lat
mixer.music.load('acilisSes.mp3') # m??zik y??kler, mp3 dosyas?? da olabilir.
mixer.music.play() # m??zi??i ??alar #Todo: Yaz??lar?? Seslendirme ????lemi Yap??lacak !

print(colored("Kullan??c?? ad??n??z?? girin:", "red"))
username = input()

print(colored("??ifrenizi girin:", "red"))
password = input()

instaCMD = InstaBot(username,password)
instaCMD.menu()




