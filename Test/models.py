from django.db import models

# Create your models here.


class Manager(models.Model):
    class Meta:
        verbose_name = "Менеджер"
        verbose_name_plural = "Менеджеры"

    manager = models.TextField(verbose_name="Менеджер")
    mail = models.TextField(verbose_name="Email")

    def __str__(self):
        return f"{self.manager}"


class Client(models.Model):
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    client = models.TextField(verbose_name="Client")
    address = models.TextField(verbose_name="Address")
    manager = models.ForeignKey(
        Manager, on_delete=models.RESTRICT, verbose_name="Manager"
    )

    def __str__(self):
        return f"{self.client}"
