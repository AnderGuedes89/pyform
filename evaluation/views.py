from django.shortcuts import redirect, render
from evaluation.forms import EvaluationForm


def evaluation(request):
    data = {}
    form = EvaluationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_thanks')
    data['form'] = form
    return render(request, 'evaluation.html', data)


def thanks(request):
    data = {}
    return render(request, 'thanks.html', data)
