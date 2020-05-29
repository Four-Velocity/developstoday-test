from django_cron import CronJobBase, Schedule

from api.models import Post


class NullifyUpvotes(CronJobBase):
    """
    Set all posts upvotes to zero avery 24 hours
    """

    RUN_EVERY_MINS = 60 * 24

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = "news.nullify_upvotes"

    def do(self):
        Post.objects.filter(upvotes__gt=0).update(upvotes=0)
