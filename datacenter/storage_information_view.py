from django.utils.timezone import localtime
from datetime import datetime, timedelta
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.format_duration import format_duration, get_duration


def storage_information_view(request):
    non_closed_visits = []

    in_repository = Visit.objects.filter(leaved_at=None)
    for person in in_repository:
        duration = format_duration(str(get_duration(person)))

        visit = {
            'who_entered': person.passcard.owner_name,
            'entered_at': person.entered_at,
            'duration': duration
        }

        non_closed_visits.append(visit)

    context = {

        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
