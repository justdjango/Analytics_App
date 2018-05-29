from django.db import models, transaction

class Vote(models.Model):
    book_name = models.CharField(max_length=200)
    count = models.IntegerField(default=0)

    def __str__(self):
        return '%s: %d votes' % (self.book_name, self.count)

    @classmethod
    def bulk_vote(cls, book_names):
        with transaction.atomic():
            for book_name in book_names:
                if len(book_name) == 0:
                    continue

                if Vote.objects.filter(book_name=book_name).exists():
                    Vote.objects.filter(book_name=book_name).update(count=models.F('count') + 1)
                else:
                    Vote.objects.create(book_name=book_name, count=1)
