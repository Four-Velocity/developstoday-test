from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    title = models.CharField(_("title"), max_length=100)
    link = models.URLField(_("URI of original post"), max_length=200)
    created = models.DateTimeField(_("creation date and time"), auto_now_add=True)
    upvotes = models.IntegerField(_("amount of upvotes"), default=0)

    author = models.CharField(_("author"), max_length=70)

    def __str__(self):
        if len(self.title) > 50:
            return self.title[:50] + f"... by {self.author}"
        return f"{self.title} by {self.author}"

    def upvote(self):
        self.upvotes += 1
        self.save(force_update=True)


class Comment(models.Model):
    author = models.CharField(_("author"), max_length=70)
    content = models.TextField(_("content"))
    created = models.DateTimeField(_("creation date and time"), auto_now_add=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name=_("posts"), related_name="comments"
    )

    def __str__(self):
        return f"{self.author} under {self.post.title}"
