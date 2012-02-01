from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
# class Tag(models.Model):
#     tag_name = models.TextField()

class Question(models.Model):
    question = models.TextField()
    created_on = models.DateTimeField(blank=True, auto_now_add=True)
    created_by = models.ForeignKey(User, unique=False, related_name='Created by user')
    tags = models.ManyToManyField(User, blank=True)
    selected = models.BooleanField()
    answered = models.BooleanField()
    votes = models.IntegerField(default=0)
    # hidden = models.BooleanField()

    def __str__(self):
        return self.question + '(' + str(self.votes) + ')'

    def upvote(self, user):
        """Upvote this Question. If user has already voted, return."""
        if Votes.objects.filter(qn=self).filter(user=user).count() > 0:
            return False
        new_vote = Votes(user=user, qn=self)
        new_vote.save()
        self.votes += 1
        self.save()
        return True

    def get_votes(self):
        return self.votes

    # def downvote(self, user):
    #     """Downvote this Question. If user has already voted, return."""
    #     if user in self.down_votes:
    #         return False
    #     if user in self.up_votes:
    #         self.up_votes.remove(user)

    #     self.down_votes.append(user)
    #     return True

class Votes(models.Model):
    user = models.ForeignKey(User)
    qn = models.ForeignKey(Question, related_name='Question')
                    
# admin.site.register(Tag)
admin.site.register(Question)

