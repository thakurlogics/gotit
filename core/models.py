from django.db import models

class SiteSettings(models.Model):
    company_name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=300)
    
    from ckeditor.fields import RichTextField

    about_content = RichTextField()

    def __str__(self):
        return self.company_name


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name