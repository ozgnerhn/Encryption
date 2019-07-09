from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Home
from .forms import HomeForm
import pydes as pyDes
import rsa
import random
import string

#DES baslangic


def encoder(data, key):
    k = pyDes.des(key[:8], pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    d = k.encrypt(data)
    return str(d)[2:-1]


def decoder(data, key):
    k = pyDes.des(key[:8], pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    b = bytes(data, "utf-8")
    b = b.decode('unicode-escape').encode('ISO-8859-1')
    return str(k.decrypt(b))[2:-1]

#DES bitis

#random metın baslangic


def random_string(length=100):
    character_set = string.ascii_letters
    return ''.join(random.choice(character_set) for i in range(length))

#random metın baslangic

#rsa icin key uretim baslangic


def create_keys():
    return rsa.newkeys(1024)

#rsa icin key uretim bitis

#rsa metin sifreleme baslangic


def encrypt_msg(msg,pub_key):
    msg = msg.encode('utf-8')
    return rsa.encrypt(msg, pub_key)

#rsa metin sifreleme bitis

#rsa metin desifreleme baslangic


def decrypt_msgs(enc_msg,pri_key):
    enc_msg = rsa.decrypt(enc_msg, pri_key)
    return enc_msg.decode("utf-8")

#rsa metin desifreleme baslangic


class HomeView(TemplateView):
    def home_view(request):
        home = Home.objects.all()
        form = HomeForm()
        (different_pub_key, _) = create_keys()
        #enc_msg = encrypt_msg(home[3].random_text, home[3].pub_key_byte)
        #dex_msg = decrypt.msg(enc.msg, home[3].pri_key_byte)
        context = {
            'isim': 'admin',
            'home_text': home[0].text,
            'home_title': home[0].title,
            'title2': home[0].title2,
            'random_text': home[3].random_text,
            'public_key': home[3].pub_key_byte,
            'private_key': home[3].pri_key_byte,
            'dif_pub_key': home[4].dif_key,
            'encrypt_text': home[4].encrypt_text,
            'decrypt_text': home[4].decrypt_text,

            'enc_name': home[0].encode_name,
            'enc_atext': home[0].encode_a,
            'enc_btext': home[0].encode_b,
            'enc_text': home[0].encode_t,
            'dec_name': decoder(home[0].encode_name, home[0].key),
            'dec_atext': decoder(home[0].encode_a, home[0].key),
            'dec_btext': decoder(home[0].encode_b, home[0].key),
            'dec_text': decoder(home[0].encode_t, home[0].key),
            'key_0': home[0].key,

            'enc_name1': home[1].encode_name,
            'enc_atext1': home[1].encode_a,
            'enc_btext1': home[1].encode_b,
            'enc_text1': home[1].encode_t,
            'dec_name1': decoder(home[1].encode_name, home[1].key),
            'dec_atext1': decoder(home[1].encode_a, home[1].key),
            'dec_btext1': decoder(home[1].encode_b, home[1].key),
            'dec_text1': decoder(home[1].encode_t, home[1].key),
            'key_1': home[1].key,

            'enc_name2': home[2].encode_name,
            'enc_atext2': home[2].encode_a,
            'enc_btext2': home[2].encode_b,
            'enc_text2': home[2].encode_t,
            'dec_name2': decoder(home[2].encode_name, home[2].key),
            'dec_atext2': decoder(home[2].encode_a, home[2].key),
            'dec_btext2': decoder(home[2].encode_b, home[2].key),
            'dec_text2': decoder(home[2].encode_t, home[2].key),
            'key_2': home[2].key,

            'form': form
        }
        return render(request, 'post/index.html', context)