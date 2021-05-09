from __future__ import annotations
from django.db import models
import datetime
from django.utils import timezone
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from dmlcomments.models import Comment

# for typing
from django.db.models import QuerySet
import typing as tp
from typing import Optional, Union, TypeVar, Any, Generic

if tp.TYPE_CHECKING:
    from django.db.models.expressions import Combinable
    from django.contrib.auth.models import User


_Q = TypeVar('_Q', bound='Question')


class QuestionQuerySet(QuerySet, Generic[_Q]):
    Model: _Q

    def _filter(self, *args: Any, **kwargs: Any) -> QuestionQuerySet[Question]:
        return self.filter(args, kwargs)


class Question(models.Model):
    id: models.AutoField[Union[Combinable, str, int], int]
    id = models.AutoField(primary_key=True)

    author: models.ForeignKey[Union[User, Combinable, None], Optional[User]]
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

    question_text: models.CharField[Union[str, int, Combinable], str]
    question_text = models.CharField(max_length=200)

    pub_date = models.DateTimeField('date published', auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    poll_comments = GenericRelation(Comment, related_query_name='poll_comments')
    choice_set = GenericRelation('Choice', related_query_name='choice_set')

    myobjects: models.Manager[Question] = models.Manager.from_queryset(QuestionQuerySet)

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self) -> Optional[bool]:
        """True is recent, false if not, None is error"""
        now = timezone.now()
        if self.pub_date is not None:
            return now - datetime.timedelta(days=7) <= self.pub_date <= now
        else:
            return None
        # raise AttributeError("Pub_date attribute missing for this question")

        # was_published_recently.admin_order_field = 'pub_date'
        # was_published_recently.boolean = True
        # was_published_recently.short_description = 'Published recently?'
        # poll_author.admin_order_field = 'author'

    def get_absolute_url(self) -> str:
        return reverse('dmlpolls:poll_detail', kwargs={"pk": self.pk})

    @property
    def comments(self) -> QuerySet[Comment]:
        instance = self
        qs: QuerySet[Comment] = Comment.myobjects.filter_by_instance(instance=instance)  # type: ignore
        return qs

    @property
    def get_content_type(self) -> ContentType:
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text


class Opinion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_vote = models.ForeignKey(Choice, on_delete=models.CASCADE)
