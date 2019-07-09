myBlog dizininde bulunan run.bat dosyasını çalıştırın.
Komutlar çalıştıktan sonra komut isteminde yazan (farklı da olabilir) 
http://127.0.0.1:8000/ sitesini kullandığınız tarayıcı üzerinden açın.


run.bat dosyası sorun çıkartır ise şu yöntemi deneyebilirsiniz:

Microsoft Komut İstemi'ni açın.

1)cd [Dizin]\myBlog  yazarak dizine girin.
2)python manage.py runserver  (hala myBlog dizininde olduğunuza emin olduktan sonra) komutunu yazıp sunucuyu çalıştırın.
3)Komut isteminde yazan (farklı da olabilir) http://127.0.0.1:8000/ sitesini kullandığınız tarayıcı üzerinden açın.

///////////////////////////////////////
DES Kullanım
//////////////////////////////////////

Kullanılan Algoritma : Data Encryption Standart (DES)

Kullandığım 8-bit Anahtar : firstkey

Verilen İsim Soyisim, aaaaaaaaaa, aaaaabaaaa ve şarkı sözü DES algoritmasının
encoder fonksiyonu ile şifrelenip veritabanına kaydedilmiştir. Bu şifreli bilgiler veritaba-
nından çekilip decoder fonksiyonu ile tekrar ilk haline getirilip index.html'de ekrana 
bastırılmıştır. Projeyi açtıktan sonra biraz aşağıya inerek detaylı tabloyu görebilirsiniz.

///////////////////////////////////////
RSA Kullanım
//////////////////////////////////////

Bu adımda RSA şifreleme algoritmasını kullanıldı. Öncelikle kendimize kütüphanenin metodları yardımıyla bir public bir de private
key oluşturuyoruz. Oluşturduğumuz public key ile 100 karakterlik metnimizi şifreliyoruz. Şifrelediğimiz bu metni daha sonra özel anahtar ile deşifreleme işlemine tabi tutuyoruz ve ilk haline tekrar geldiğini görüyoruz. Ardından farklı bir public key ile şifrelediğimiz bu metni ilk private keyimiz ile açmayı denediğimizde hata verdiğini görüyoruz. Bu adımlar sayesinde de RSA nın işleyişini anlayabiliyoruz.
