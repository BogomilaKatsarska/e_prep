from django.core import validators
from django.db import models


class Profile(models.Model):
    MAX_USERNAME_LEN = 15
    MIN_USERNAME_LEN = 2

    username = models.CharField(
        max_length=MAX_USERNAME_LEN,
        validators=(
            validators.MinLengthValidator(MIN_USERNAME_LEN),
        ),
        null=False,
        blank=False,
    )
    email = models.EmailField()
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    MAX_ALBUM_NAME_LEN = 30
    MAX_ARTIST_LEN = 30
    MAX_GENRE_LEN = 30
    MIN_PRICE = 0.0

    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    RNB_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC = 'Country Music'
    DANCE_MUSIC = 'Dance Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    OTHER_MUSIC = 'Other'

    MUSICS = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_MUSIC, RNB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
        (OTHER_MUSIC, OTHER_MUSIC),
    )

    album_name = models.CharField(
        max_length=MAX_ALBUM_NAME_LEN,
        unique=True,
    )
    artist = models.CharField(
        max_length=MAX_ARTIST_LEN,
    )
    genre = models.CharField(
        max_length=MAX_GENRE_LEN,
        choices=MUSICS,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image = models.URLField()
    price = models.FloatField(
        validators=(
            validators.MinLengthValidator(MIN_PRICE),
        ),
    )


