from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datetime import timedelta
from datacenter.format_duration import get_duration
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):

    person_visit = []
    person = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=person)

    for visit in visits:

        visit_person = {
            'entered_at': visit.entered_at,
            'duration': get_duration(visit),
            'is_strange': get_duration(visit) > timedelta(hours=1)
        }
        person_visit.append(visit_person)

    this_passcard_visits = {'passcard': person, 'this_passcard_visits': person_visit}
    return render(request, 'passcard_info.html', this_passcard_visits)

