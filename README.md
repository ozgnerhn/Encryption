//////// WINDOWS ���N ////////

Kullan�lan �at�: Django
Yaz�ld��� Dil: Python 3 (Di�er s�r�mlerde sorun ��kartabilir. Bu y�zden Python 3 setup dosyas�n� da �dev i�ine ekleyece�im.)
Kullan�lan Platform: JetBrains PyCharm 2018.3.4 x64



Projeyi masa�st�ne myBlog klas�r� olarak tek par�ada ��kart�n.

C:\Users\...\Desktop\myBlog dizininde bulunan run.bat dosyas�n� �al��t�r�n.
Komutlar �al��t�ktan sonra komut isteminde yazan (farkl� da olabilir) 
http://127.0.0.1:8000/ sitesini kulland���n�z taray�c� �zerinden a��n.



run.bat dosyas� sorun ��kart�r ise bu y�ntemi deneyebilirsiniz.

Microsoft Komut �stemi'ni a��n.

1)cd Desktop\myBlog  yazarak dizine girin.
2)python manage.py runserver  (hala myBlog dizininde oldu�unuza emin olduktan sonra) komutunu yaz�p sunucuyu �al��t�r�n.
3)Komut isteminde yazan (farkl� da olabilir) http://127.0.0.1:8000/ sitesini kulland���n�z taray�c� �zerinden a��n.

///////////////////////////////////////
�DEV - 2   G�NCELLEME
//////////////////////////////////////

Kullan�lan Algoritma : Data Encryption Standart (DES)

Kulland���m 8-bit Anahtar : firstkey

�devde verilen �sim Soyisim, aaaaaaaaaa, aaaaabaaaa ve �ark� s�z� DES algoritmas�n�n
encoder fonksiyonu ile �ifrelenip veritaban�na kaydedilmi�tir. Bu �ifreli bilgiler veritaba-
n�ndan �ekilip decoder fonksiyonu ile tekrar ilk haline getirilip index.html'de ekrana 
bast�r�lm��t�r. �devi a�t�ktan sonra biraz a�a��ya inerek detayl� tabloyu g�rebilirsiniz.

5. senaryodaki 0 ve 1 keyleri ile �ifreledi�im metinler birbirinin ayn�s� ��kt�.

///////////////////////////////////////
�DEV - 3   G�NCELLEME
//////////////////////////////////////

Mona Lisa'n�n G�l��� - Random

///////////////////////////////////////
�DEV - 4   G�NCELLEME
//////////////////////////////////////

�devin bu ad�m�nda RSA �ifreleme algoritmas�n� kulland�m. �ncelikle kendime k�t�phanenin metodlar� yard�m�yla bir public bir de private
key olu�turdum. Olu�turdu�um public key ile 100 karakterlik metnimi �ifreledim. �ifreledi�im bu metni daha sonra �zel anahtar ile
de�ifreledim ve ilk haline kavu�mas�n� g�rd�m. Ard�ndan farkl� bir public key ile �ifreledi�im bu metni ilk �zel anahtar�m ile a�may� 
denedi�imde hata verdi�ini g�rd�m. �nceki �devlerde oldu�u gibi run.bat dosyas�n� �al��t�rarak �dev-4 K�sm�na inip detayl� bir �ekilde
yapt���m ad�mlar� g�rebilirsiniz.