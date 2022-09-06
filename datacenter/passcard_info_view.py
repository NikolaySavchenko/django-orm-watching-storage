from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import format_duration
from datacenter.models import get_duration
from django.utils.timezone import localtime
from datacenter.models import is_visit_long
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard_person = get_object_or_404(Passcard.objects, passcode=passcode)
    all_visits_persons = get_list_or_404(Visit.objects, passcard=passcard_person.id)
    persons_visits = []
    for all_visits_person in all_visits_persons:
        persons_visit = {
            'entered_at': localtime(all_visits_person.entered_at),
            'duration': format_duration(get_duration(all_visits_person)),
            'is_strange': is_visit_long(all_visits_person)
        }
        persons_visits.append(persons_visit)

        context = {
            'passcard': passcard_person,
            'this_passcard_visits': persons_visits
        }
    return render(request, 'passcard_info.html', context)
