from django.db import models

# Create your models here.
class Message(models.Mode):
    user = mdels.Charfield("姓名",max_length=50)
    subject = models.Charfield ("主題", max_length=200)
    content = models.Texyfield("內容")
    