from django.db import models
from django.utils import timezone
from string import Template


class DurationTemplate(Template):
    delimiter = "%"   


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
    
    def get_duration(self):
        now = timezone.now()
        if self.leaved_at:
            return self.leaved_at - self.entered_at
        return now - self.entered_at

    def is_visit_long(self, minutes=60):
        visit_duration = self.get_duration()
        return visit_duration > timezone.timedelta(minutes=minutes)

    duration = property(get_duration)

    def format_duration(self, duration, frmt):
        difference = 0
        splitted_timedelta = {}
        if "%D" in frmt:
            splitted_timedelta["D"] = duration.days
        else:
            difference = duration.days*24*3600 
            difference += duration.seconds
        if "%H" in frmt:     
            splitted_timedelta["H"], difference = divmod(difference, 3600)
            if  splitted_timedelta["H"] in range(10):
              splitted_timedelta["H"]= "0" + str(splitted_timedelta["H"])
        if "%M" in frmt:
            splitted_timedelta["M"], difference = divmod(difference, 60)
            if  splitted_timedelta["M"] in range(10):
                splitted_timedelta["M"]= "0" + str(splitted_timedelta["M"])
        splitted_timedelta["S"] = difference
        if  splitted_timedelta["S"] in range(10):
            splitted_timedelta["S"]= "0" + str(splitted_timedelta["S"])
        template = DurationTemplate(frmt)
        return template.substitute(**splitted_timedelta)
