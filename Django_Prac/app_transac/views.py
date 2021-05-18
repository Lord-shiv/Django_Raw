from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Payment
from .models import customer
from django.db.models import F
import decimal
from django.db import transaction


def process_payment(request):

    if request.method == 'POST':

        form = Payment(request.POST)

        if form.is_valid():
            sender_name = form.cleaned_data['sender']
            receiver_name = form.cleaned_data['receiver']
            amt = decimal.Decimal(form.cleaned_data['amount'])

            sender = customer.objects.select_for_update().get(name=sender_name)
            receiver = customer.objects.select_for_update().get(name=sender_name)

        with transaction.atomic():
            sender.balance -= amt
            sender.save()

            receiver.balance += amt
            receiver.save()

            return HttpResponseRedirect('/')

    else:
        form = Payment()

    return render(request, 'index.html', {'form': form})


def process_payment_a(request):

    if request.method == 'POST':

        form = Payment(request.POST)

        if form.is_valid():
            sender_name = form.cleaned_data['sender']
            receiver_name = form.cleaned_data['receiver']
            amt = decimal.Decimal(form.cleaned_data['amount'])

        with transaction.atomic():
            sender = customer.objects.get(name=sender_name)
            sender.balance -= amt
            sender.save()

            receiver = customer.objects.get(name=receiver_name)
            receiver.balance += amt
            receiver.save()

            # sender = customer.objects.select_for_update().get(name=x)
            # receiver = customer.objects.select_for_update().get(name=y)

        # with transaction.atomic():
        #     sender.balance -= z
        #     sender.save()

        #     receiver.balance += z
        #     receiver.save()

            # customer.objects.filter(name=x).update(balance=F('balance') - z)
            # customer.objects.filter(name=y).update(balance=F('balance') + z)

            return HttpResponseRedirect('/')

    else:
        form = Payment()

    return render(request, 'index.html', {'form': form})

# simple way just put it
@transaction.atomic
def process_payment_b(request):

    if request.method == 'POST':

        form = Payment(request.POST)

        if form.is_valid():
            sender_name = form.cleaned_data['sender']
            receiver_name = form.cleaned_data['receiver']
            amt = decimal.Decimal(form.cleaned_data['amount'])

            sender = customer.objects.get(name=sender_name)
            sender.balance -= amt
            sender.save()

            receiver = customer.objects.get(name=receiver_name)
            receiver.balance += amt
            receiver.save()

            return HttpResponseRedirect('/')

    else:
        form = Payment()

    return render(request, 'index.html', {'form': form})


def process_payment_c(request):

    if request.method == 'POST':

        form = Payment(request.POST)

        if form.is_valid():
            sender_name = form.cleaned_data['sender']
            receiver_name = form.cleaned_data['receiver']
            amt = decimal.Decimal(form.cleaned_data['amount'])
            '''                   '''
            '''Without transaction'''
            '''                   '''
            if customer.objects.filter(name=receiver_name).exists():
                sender = customer.objects.get(name=sender_name)
                sender.balance -= amt
                sender.save()

                receiver = customer.objects.get(name=receiver_name)
                receiver.balance += amt
                receiver.save()

            return HttpResponseRedirect('/')

    else:
        form = Payment()

    return render(request, 'index.html', {'form': form})


# https://www.youtube.com/watch?v=BchP5Mn1IYg
