from django.utils.timezone import localtime
from datetime import datetime


def get_duration(vizit):
    leaved = vizit.leaved_at or localtime()
    time_in_repository = leaved - vizit.entered_at
    return time_in_repository


def format_duration(duration):
    return datetime.strptime(duration, '%H:%M:%S.%f').strftime('%H:%M')