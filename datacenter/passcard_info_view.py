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
    in_visit_person = passcard_person.id
    all_visits_person = get_list_or_404(Visit.objects, passcard=in_visit_person)
    this_passcard_visits = []
    for i in range(len(all_visits_person)):
        temp = {
            'entered_at': localtime(all_visits_person[i].entered_at),
            'duration': format_duration(get_duration(all_visits_person[i])),
            'is_strange': is_visit_long(all_visits_person[i])
        }
        this_passcard_visits.append(temp)

        context = {
            'passcard': passcard_person,
            'this_passcard_visits': this_passcard_visits
        }
    return render(request, 'passcard_info.html', context)
