//////// WINDOWS ÝÇÝN ////////

Kullanýlan Çatý: Django
Yazýldýðý Dil: Python 3 (Diðer sürümlerde sorun çýkartabilir. Bu yüzden Python 3 setup dosyasýný da ödev içine ekleyeceðim.)
Kullanýlan Platform: JetBrains PyCharm 2018.3.4 x64



Projeyi masaüstüne myBlog klasörü olarak tek parçada çýkartýn.

C:\Users\...\Desktop\myBlog dizininde bulunan run.bat dosyasýný çalýþtýrýn.
Komutlar çalýþtýktan sonra komut isteminde yazan (farklý da olabilir) 
http://127.0.0.1:8000/ sitesini kullandýðýnýz tarayýcý üzerinden açýn.



run.bat dosyasý sorun çýkartýr ise bu yöntemi deneyebilirsiniz.

Microsoft Komut Ýstemi'ni açýn.

1)cd Desktop\myBlog  yazarak dizine girin.
2)python manage.py runserver  (hala myBlog dizininde olduðunuza emin olduktan sonra) komutunu yazýp sunucuyu çalýþtýrýn.
3)Komut isteminde yazan (farklý da olabilir) http://127.0.0.1:8000/ sitesini kullandýðýnýz tarayýcý üzerinden açýn.

///////////////////////////////////////
ÖDEV - 2   GÜNCELLEME
//////////////////////////////////////

Kullanýlan Algoritma : Data Encryption Standart (DES)

Kullandýðým 8-bit Anahtar : firstkey

Ödevde verilen Ýsim Soyisim, aaaaaaaaaa, aaaaabaaaa ve þarký sözü DES algoritmasýnýn
encoder fonksiyonu ile þifrelenip veritabanýna kaydedilmiþtir. Bu þifreli bilgiler veritaba-
nýndan çekilip decoder fonksiyonu ile tekrar ilk haline getirilip index.html'de ekrana 
bastýrýlmýþtýr. Ödevi açtýktan sonra biraz aþaðýya inerek detaylý tabloyu görebilirsiniz.

5. senaryodaki 0 ve 1 keyleri ile þifrelediðim metinler birbirinin aynýsý çýktý.

///////////////////////////////////////
ÖDEV - 3   GÜNCELLEME
//////////////////////////////////////

Mona Lisa'nýn Gülüþü - Random

///////////////////////////////////////
ÖDEV - 4   GÜNCELLEME
//////////////////////////////////////

Ödevin bu adýmýnda RSA þifreleme algoritmasýný kullandým. Öncelikle kendime kütüphanenin metodlarý yardýmýyla bir public bir de private
key oluþturdum. Oluþturduðum public key ile 100 karakterlik metnimi þifreledim. Þifrelediðim bu metni daha sonra özel anahtar ile
deþifreledim ve ilk haline kavuþmasýný gördüm. Ardýndan farklý bir public key ile þifrelediðim bu metni ilk özel anahtarým ile açmayý 
denediðimde hata verdiðini gördüm. Önceki ödevlerde olduðu gibi run.bat dosyasýný çalýþtýrarak Ödev-4 Kýsmýna inip detaylý bir þekilde
yaptýðým adýmlarý görebilirsiniz.