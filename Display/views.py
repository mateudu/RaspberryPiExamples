from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import gpio_helper as pi
from .forms import DisplayPostForm
# Create your views here.


def display_text(request):
    if request.method == 'POST':
        lcd = pi.HD44780()
        form = DisplayPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            lcd.message(cd['first_line'][:16]+'\n'+cd['second_line'][:16])
    return render(request, 'Display/display_text.html')
