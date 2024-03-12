# rps_app/views.py

from django.shortcuts import render, redirect
import random
from .forms import ChoiceForm

def play_game(request):
    form = ChoiceForm(request.POST or None)
    result = None

    if form.is_valid():
        user_choice = form.cleaned_data['user_choice']
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            result = "You win!"
        else:
            result = "Computer wins!"

        return redirect('result', result=result)  # Redirect to the result page with the game result
    return render(request, 'choice_form.html', {'form': form})

def game_result(request, result):
    return render(request, 'result.html', {'result': result})
