from django.utils.timezone import localtime
from datetime import datetime, timedelta
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []

    in_repository = Visit.objects.filter(leaved_at=None)
    for person in in_repository:
        duration = format_duration(get_duration(person))

        visit = {
            'who_entered': person.passcard.owner_name,
            'entered_at': person.entered_at,
            'duration': duration
        }

        non_closed_visits.append(visit)

    context = {

        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)


def get_duration(vizit):
    time_in_repository = str(localtime() - vizit.entered_at)
    return time_in_repository


def format_duration(duration):
    return datetime.strptime(duration, '%H:%M:%S.%f').strftime('%H:%M')
