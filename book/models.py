from django.db import models
from django.utils import timezone
from user.models import CustomUser


class Book(models.Model):

    DOCUMENT_TYPE = (
        (1, '書籍'),
        (2, '論文'),
        (3, 'ニュース記事'),
        (4, 'その他'),
    )

    STARS = (
        (1, '☆'),
        (2, '☆☆'),
        (3, '☆☆☆'),
        (4, '☆☆☆☆'),
        (5, '☆☆☆☆☆')
    )

    user = models.ForeignKey(CustomUser,verbose_name='ユーザー名', editable=False, 
                             on_delete=models.CASCADE)

    book_title = models.CharField('タイトル', max_length=100)  

    image = models.ImageField('表紙画像', blank=True, null=True, help_text='')

    document_type = models.IntegerField('カテゴリ', choices=DOCUMENT_TYPE)

    text = models.TextField('書評', blank=True, null=True)

    stars = models.IntegerField('評価', choices=STARS)

    posted_date = models.DateField('投稿日',editable=False ,default=timezone.now)

    
    def __str__(self):
        return f'{self.user} - {self.book_title} - {self.get_stars_display()} - {self.posted_date}'

  

# Create your models here.
