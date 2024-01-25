<h1 align="center">Instagram Bot</h1>

<p align="center">
  <a href="https://github.com/fatihemrertekin/Python-Instagram-Bot">
    <img src="https://github.com/fatihemrertekin/Python-Instagram-Bot/blob/main/InstaBot.png?raw=true" alt="Instagram Bot" width="300">
  </a>
</p>

## Açıklama

**Selenium framework'ü kullanılarak geliştirilmiş bir Instagram botu**

## Özellikler

:large_blue_circle: **Kullanıcı adına göre arama yaparak aranan kullanıcının takipçilerini istenilen miktarda takip etme.**
<br>
:large_blue_circle: **İstenilen miktarda takip edilen kişileri takipten çıkarma.**.
<br>
:large_blue_circle: **Girilen etiket adına göre istenilen miktarda gönderi beğenme.**
<br>

## Diğer Özellikler

:large_blue_circle: Türkçe dil desteği.

## Ayrıntılar

:large_blue_diamond: İnstagram oturumunuzu açarak yukarıdaki özellikleri kullanabilirsiniz.  
:large_blue_diamond: Varsayılan uygulama dili Türkçe'dir.

## Yapılandırma Ayarları

:gear: Proje webdriver olarak Google Chrome tarayıcısını kullanmaktadır. Bu yüzden Chrome'un kurulu olması gerekmektedir.  
 :gear: Chrome'un kullanılabilmesi için Chrome sürümünüzü destekleyen chrome webdriver'ı [webdriver](https://chromedriver.chromium.org/downloads) indirilmeli ve indirilen webdriver program'ın bulunduğu klasör ile aynı dizinde bulunmalıdır.

- ### Config Ayarları

:gear: **time:** **time.sleep()** kullanılan yerler için işlem bekleme sürelerini belirtir. time.sleep() fonksiyonları için ayrı ayrı "birSaniyeUyut(), ikiSaniyeUyut()" gibi metotlar tanımlanmıştır.

- ### Windows için paketlerin kurulumu

```
python -m pip install -r .\requirements.txt
```

## Kullanım

:small_blue_diamond: Kullanıcıdan bilgi girişi yapılması, mesaj gönderimleri vb. yönergeler ile program sizi yönlendirecektir.

```
python instaBot.py
```

### Notlar

:small_blue_diamond: işlemlerde hesabınızın engellenmemesi için işlem süre aralıkları uzun süreler olarak ayarlanmıştır.
<br>
:small_blue_diamond: Yapılan işlemler için belirlenen işlem süreleri "birSaniyeUyut(), ikiSaniyeUyut()" gibi metotlar ile tanımlanmış olup, değiştirilmek istendiğinde metot içerisindeki time.sleep(x) fonsiyonunun x parametresine saniye cinsinden bir değer vererek güncelleme yapılabilir.
<br>
:small_blue_diamond: Sadece Windows işletim sisteminde test edilmiştir.
<br>
:small_blue_diamond: Python versiyonu: 3.12
<br>

### Kullanılan Teknolojiler

- Python
- Selenium
- Javascript
