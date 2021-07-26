from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    votes = models.ManyToManyField(
        User, default=None, blank=True, related_name='votes')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    @property
    def num_votes(self):
        return self.votes.all().count()


VOTE_CHOISES = {
    ('Vote', 'Vote'),
    ('Downvote', 'Downvote')
}


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(choices=VOTE_CHOISES,
                             default='Vote', max_length=10)

    def __str__(self):
        return str(self.user)
