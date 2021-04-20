from django.db import models


class Pokemon(models.Model):
    title = models.CharField(verbose_name='имя на русском', max_length=200)
    image = models.ImageField(verbose_name='изображение покемона',
                              upload_to='pokemon_pic',
                              null=True)
    title_en = models.CharField(verbose_name='имя на английском',
                                max_length=200,
                                blank=True)
    title_jp = models.CharField(verbose_name='имя на японском',
                                max_length=200,
                                blank=True)
    description = models.TextField(verbose_name='описание', blank=True)
    previous_evolution = models.ForeignKey('self',
                                           verbose_name='эолюционировал из',
                                           null=True,
                                           blank=True,
                                           on_delete=models.SET_NULL,
                                           related_name='next_evolution')

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        verbose_name='покемон',
        on_delete=models.CASCADE
    )
    latitude = models.FloatField(verbose_name='широта',
                                 blank=True,
                                 null=True)
    longitude = models.FloatField(verbose_name='долгота',
                                  blank=True,
                                  null=True)
    appeared_at = models.DateTimeField(verbose_name='Появился на карте в ',
                                       blank=True,
                                       null=True)
    disappeared_at = models.DateTimeField(verbose_name='Исчез с карты в ',
                                          blank=True,
                                          null=True)
    level = models.IntegerField(verbose_name='уровень',
                                blank=True,
                                null=True)
    health = models.IntegerField(verbose_name='здоровье',
                                 blank=True,
                                 null=True)
    strength = models.IntegerField(verbose_name='атака',
                                   blank=True,
                                   null=True)
    defence = models.IntegerField(verbose_name='защита',
                                  blank=True,
                                  null=True)
    stamina = models.IntegerField(verbose_name='выносливость',
                                  blank=True,
                                  null=True)

    def __str__(self):
        return f'{self.pokemon}'
