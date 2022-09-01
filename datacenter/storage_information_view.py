from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.models import format_duration
from datacenter.models import get_duration
from django.shortcuts import get_list_or_404


def storage_information_view(request):
    in_storage_passcards = get_list_or_404(Visit.objects, leaved_at=None)
    non_closed_visits = []
    for i in range(len(in_storage_passcards)):
        temp = {
            'who_entered': in_storage_passcards[i].passcard,
            'entered_at': localtime(in_storage_passcards[i].entered_at),
            'duration': format_duration(get_duration(in_storage_passcards[i]))
        }
        non_closed_visits.append(temp)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
