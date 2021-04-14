from django.db import models

class Words(models.Model):
    word = models.TextField(max_length=150, unique=True);
    translated_word = models.TextField(max_length=150);

    def __str__(self):
        return f'{self.translated_word}'

class FilesAdmin(models.Model):
	adminupload=models.FileField(upload_to='media')
	title=models.CharField(max_length=50)

	def __str__(self):
		return self.title