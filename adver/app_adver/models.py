from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Advertisements(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name="пользователь", on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='')


    class Meta:
        db_table = "advertisements"
