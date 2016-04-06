from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from datetime import *

import os
import uuid

# Create your models here.

def upload_image_directory(instance, filename):
    # file will be upload to MEDIA_ROOT/user_<id>/filename
    _, postfix = os.path.splitext(filename) 
    return '%s/%s' % (datetime.now().strftime('%Y/%m'), str(uuid.uuid1()) + postfix)

@python_2_unicode_compatible  # only if you need to support Python 2
class Test(models.Model):
    test_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.test_text


@python_2_unicode_compatible  # only if you need to support Python 2
class Post(models.Model):
    EDITING = 1
    NORMAL = 0
    PENDING = 2
    FORBIDDEN = 3

    STATUS_CHOICES = (
        (EDITING, 'editing'),
        (NORMAL, 'normal'),
        (PENDING, 'pending'),
        (FORBIDDEN, 'forbidden'),
    )

    title = models.CharField(max_length = 150)
    content = models.TextField(blank = True)
    tags = models.CharField(max_length = 200, blank = True)
    status = models.SmallIntegerField(choices = STATUS_CHOICES,
                                        default=NORMAL)
    create_time = models.DateTimeField('date published', auto_now_add = True)
    update_time = models.DateTimeField('last edited', auto_now = True)
    author = models.ForeignKey('User', on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.title

@python_2_unicode_compatible  # only if you need to support Python 2
class User(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 200)
    salt = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    avatar_width = models.PositiveIntegerField()
    avatar_height = models.PositiveIntegerField()
    avatar = models.ImageField(upload_to = upload_image_directory, height_field='avatar_height', width_field='avatar_width')
    profile = models.CharField(max_length = 200)

    def __str__(self):
        return self.username

@python_2_unicode_compatible  # only if you need to support Python 2
class Image(models.Model):
    desc = models.CharField(max_length = 100)
    image_width = models.PositiveIntegerField()
    image_height = models.PositiveIntegerField()
    image = models.ImageField(upload_to = upload_image_directory, height_field='image_height', width_field='image_width')

    def __str__(self):
        return self.desc
