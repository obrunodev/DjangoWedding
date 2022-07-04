from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from invite.forms import GuestForm
from invite.models import Guest


def confirm(request, guest_id):
    guest = get_object_or_404(Guest, guest_id=guest_id)
    form = GuestForm(request.POST or None, instance=guest)
    if request.method == 'GET':
        return render(request, 'invite/pages/confirm.html', {
            'form': form,
            'guest': guest,
        })
    
    if request.method == 'POST':
        input_adult = request.POST['adult_guest']
        input_child = request.POST['child_guest']
        if int(input_adult) > guest.adult_guest:
            messages.error(request, 'O número de adultos ultrapassa o permitido!')
            return redirect('invite:confirm', guest_id=guest.guest_id)
        if int(input_child) > guest.child_guest:
            messages.error(request, 'O número de crianças ultrapassa o permitido!')
            return redirect('invite:confirm', guest_id=guest.guest_id)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.adult_guest = int(input_adult)
            obj.child_guest = int(input_child)
            obj.invite_status = 1
            obj.save()
            print(form.errors)
            return redirect('invite:index')


def index(request):
    guests = Guest.objects.order_by('first_name')
    confirmados = 0
    pendentes = 0
    for guest in guests:
        if guest.invite_status == 0:
            pendentes += guest.adult_guest + guest.child_guest
        if guest.invite_status == 1:
            confirmados += guest.adult_guest + guest.child_guest
    
    context = {
        'guests': guests,
        'confirmados': confirmados,
        'pendentes': pendentes,
    }
    return render(request, 'invite/pages/index.html', context)
