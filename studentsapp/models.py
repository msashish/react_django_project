from django.db import models


class Student(models.Model):
    # By extending from djangp's Model, we can use makemigrations tool to propogate Model changes to DB schema directly
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    document = models.CharField("Document", max_length=20)
    phone = models.CharField(max_length=20)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)

    def __str__(self):
        return self.name
