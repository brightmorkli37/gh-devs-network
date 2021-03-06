from django.db import models
import uuid
from users.models import Profile

class Project(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4, unique=True,
        primary_key=True, editable=False
    )
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(null=True, blank=True, default='default.jpg')
    description = models.TextField(blank=True, null=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, blank=True, null=True)
    vote_ratio = models.IntegerField(default=0, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset

    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='UP').count()
        totalVotes = reviews.count()

        ratio = ( upVotes / totalVotes ) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio
        self.save()


class Review(models.Model):
    UP = 'UP VOTE'
    DOWN = 'DOWN VOTE'

    VOTE_CHOICES = [
        (UP, 'up vote'),
        (DOWN, 'down vote')
    ]

    id = models.UUIDField(
        default=uuid.uuid4, unique=True,
        primary_key=True, editable=False
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    value = models.CharField(max_length=200, blank=True, null=True, choices=VOTE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['owner', 'project']]

    def __str__(self) -> str:
        return self.value


class Tag(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True,
        primary_key=True, editable=False
    )
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
