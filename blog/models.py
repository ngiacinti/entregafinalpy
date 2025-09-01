from django.db import models

class Blog(models.Model):
    title = models.CharField('Título', max_length=150)
    content = models.TextField('Contenido', blank=True)
    created_at = models.DateTimeField('Creado el', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'

    def __str__(self):
        return self.title
