from django.db import models


class Home(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    title2 = models.CharField(max_length=20, default="")
    encode_name = models.CharField(max_length=100)
    encode_a = models.CharField(max_length=100)
    encode_b = models.CharField(max_length=100)
    encode_t = models.CharField(max_length=100)
    key = models.CharField(max_length=50)
    random_text = models.CharField(max_length=120)
    pub_key_byte = models.CharField(max_length=2000)
    pri_key_byte = models.CharField(max_length=2000)
    encrypt_text = models.CharField(max_length=300)
    decrypt_text = models.CharField(max_length=300)
    dif_key = models.CharField(max_length=2000)

    def __str__(self):
        return self.title