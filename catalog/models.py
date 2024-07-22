from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование', unique=True)
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey('Category', verbose_name='категория', on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='цена за покупку')
    create_at = models.DateField(auto_now_add=True, verbose_name='Дата создания БД')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата обновления БД')

    def __str__(self):
        return f'{self.name} {self.description} {self.price} {self.create_at} {self.updated_at}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание категории')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Contact(models.Model):
    country = models.CharField(max_length=100, verbose_name='Страна')
    inn = models.BigIntegerField(verbose_name='ИНН')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    phone_number = models.BigIntegerField(verbose_name='Номер телефона')

    def __str__(self):
        return f'{self.country} {self.inn} {self.address} {self.phone_number}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class UserFeedback(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='e-mail')
    massage = models.TextField(verbose_name='текст обращения')
    is_active = models.BooleanField(default=True, verbose_name='активное обращение')

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'


class Version(models.Model):
    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE)
    version_number = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Название версии', unique=True)
    is_active = models.BooleanField(default=True, verbose_name='признак текущей версии')

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'