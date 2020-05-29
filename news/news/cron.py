from django_cron import CronJobBase, Schedule

from api.models import Post


class NullifyUpvotes(CronJobBase):

    TIME_STAMP = ["5:00"]

    schedule = Schedule(run_at_times=TIME_STAMP)
    code = "news.nullify_upvotes"

    def do(self):

        Post.objects.filter(upvotes__gt=0).update(upvotes=0)
