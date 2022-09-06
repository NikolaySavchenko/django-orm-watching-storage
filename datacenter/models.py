from django.db import models
from datetime import datetime, timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


def format_duration(duration):
    hour = duration.seconds // 3600
    minutes = (duration.seconds - hour * 3600) // 60
    seconds = (duration.seconds - hour * 3600 - minutes * 60)
    return f'{hour} час {minutes} мин {seconds} сек'


def get_duration(visit):
    if visit.leaved_at:
        return visit.leaved_at - visit.entered_at
    else:
        return datetime.now(timezone.utc) - visit.entered_at


def is_visit_long(visit, minutes=60):
    if get_duration(visit).seconds > (minutes * 60):
        return True
    else:
        return False
