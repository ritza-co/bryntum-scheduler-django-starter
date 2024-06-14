from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255, null=False)
    readOnly = models.BooleanField(default=False, null=True)
    timeZone = models.CharField(max_length=255, null=True, default=None)
    draggable = models.BooleanField(default=True, null=True)
    resizable = models.BooleanField(default=True, null=True)
    children = models.CharField(max_length=255, null=True, default=None)
    allDay = models.BooleanField(default=False, null=True)
    duration = models.FloatField(null=True, default=None)
    durationUnit = models.CharField(max_length=255, default="day", null=True)
    startDate = models.DateTimeField(null=True, default=None)
    endDate = models.DateTimeField(null=True, default=None)
    exceptionDates = models.JSONField(null=True, default=None)
    recurrenceRule = models.CharField(max_length=255, null=True, default=None)
    cls = models.CharField(max_length=255, null=True, default=None)
    eventColor = models.CharField(max_length=255, null=True, default=None)
    eventStyle = models.CharField(max_length=255, null=True, default=None)
    iconCls = models.CharField(max_length=255, null=True, default=None)
    style = models.CharField(max_length=255, null=True, default=None)

    class Meta:
        db_table = 'events'


class Dependency(models.Model):
    fromEvent = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='from_dependencies',
                                  db_column='from')
    toEvent = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='to_dependencies', db_column='to')
    fromSide = models.CharField(max_length=255, default="right", null=True)
    toSide = models.CharField(max_length=255, default="left", null=True)
    cls = models.CharField(max_length=255, null=True, default=None)
    lag = models.FloatField(default=0, null=True)
    lagUnit = models.CharField(max_length=255, default="day", null=True)
    type = models.IntegerField(default=2, null=True, blank=True)

    class Meta:
        db_table = 'dependencies'


class Resource(models.Model):
    name = models.CharField(max_length=255, null=False)
    eventColor = models.CharField(max_length=255, null=True, default=None)
    readOnly = models.BooleanField(default=False, null=True)

    class Meta:
        db_table = 'resources'


class Assignment(models.Model):
    eventId = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='assignments', db_column='eventId')
    resourceId = models.ForeignKey('Resource', on_delete=models.CASCADE, related_name='assignments',
                                 db_column='resourceId')

    class Meta:
        db_table = 'assignments'
