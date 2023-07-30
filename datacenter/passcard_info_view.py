from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datetime import timedelta
from datacenter.storage_information_view import get_duration
from django.http import Http404
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    person_visit = []
    try:
        person = Passcard.objects.get(passcode=passcode)
    except Passcard.DoesNotExist:
        raise Http404

    visits = Visit.objects.filter(passcard=person)

    for visit in visits:
        entered = visit.entered_at or get_duration(visit)
        leaved = visit.leaved_at or localtime()
        visit_person = {
            'entered_at': entered,
            'duration': leaved - entered,
            'is_strange': (leaved - entered) > timedelta(hours=1)
        }
        person_visit.append(visit_person)

    this_passcard_visits = {'passcard': person, 'this_passcard_visits': person_visit}
    return render(request, 'passcard_info.html', this_passcard_visits)

