# models.py
from django.db import models

class SocialMediaLink(models.Model):
    href = models.URLField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.href

class whatsappchat(models.Model):
    whatsapp_chat_link = models.CharField(max_length=20, blank=True)
    image = models.ImageField(null=True, blank=True)
    text = models.CharField(max_length=100, default='رقم الوتساب ')

    def __str__(self):
        return self.text

class mobile(models.Model):
    mobile = models.CharField(max_length=20, blank=True)
    image = models.ImageField(null=True, blank=True)
    text = models.CharField(max_length=100, default='رقم الهاتف ')

    def __str__(self):
        return self.text

class lociation(models.Model):
    text = models.CharField(max_length=100, default=' اسم الفرع باللغة العربية')
    text_en = models.CharField(max_length=100, default=' اسم الفرع بالغه الانجليزية')
    mobile = models.CharField(max_length=20, blank=True)
    map_link = models.URLField(blank=True)

    def __str__(self):
        return self.text

class app(models.Model):
    image = models.ImageField(null=True, blank=True)
    href = models.URLField()

    def __str__(self):
        return self.href

class description(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=100, default='العنوان باللغة العربية')
    title_en = models.CharField(max_length=100, default='العنوان باللغه الانجليزية')
    description = models.TextField(default='النص باللغه العربية')
    description_en = models.TextField(default='النص باللغه الانجليزية')


    def __str__(self):
        return self.title



class description2(models.Model):
    image = models.ImageField(null=True, blank=True)
    image_en = models.ImageField(null=True, blank=True, default='الصورة بالانجليزية')


    def __str__(self):
        return self.image.name if self.image else "image"

class addlocarb(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=100, default='العنوان باللغة العربية')
    title_en = models.CharField(max_length=100, default='العنوان باللغه الانجليزية')
    href = models.URLField()

    def __str__(self):
        return self.title