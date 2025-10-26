from django.db import models

class LearningJourney(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def str(self):
        return self.title
class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.TextField()
    hobbies = models.TextField(blank=True)

    def str(self):
        return self.name
