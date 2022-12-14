from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.models import format_duration
from datacenter.models import get_duration
from django.shortcuts import get_list_or_404


def storage_information_view(request):
    in_storage_passcards = get_list_or_404(Visit.objects, leaved_at__isnull=True)
    non_closed_visits = []
    for in_storage_passcard in in_storage_passcards:
        non_closed_visit = {
            'who_entered': in_storage_passcard.passcard,
            'entered_at': localtime(in_storage_passcard.entered_at),
            'duration': format_duration(get_duration(in_storage_passcard))
        }
        non_closed_visits.append(non_closed_visit)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
