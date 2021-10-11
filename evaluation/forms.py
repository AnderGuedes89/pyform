from django import forms
from django.forms import ModelForm
from evaluation.models import Evaluation, Instructor, Training

EVALUATION_CHOICES = [
    ('excelente', 'Excelente'),
    ('bom', 'Bom'),
    ('regular', 'Regular'),
]

YES_NO_CHOICES = [
    ('sim', 'Sim'),
    ('nao', 'Não'),
]

class EvaluationForm(ModelForm):
    name = forms.CharField(
        label='Nome', widget=forms.TextInput(attrs={"placeholder": "Nome", "class": "form-control input"})
    )

    city = forms.CharField(
        label='Cidade', widget=forms.TextInput(attrs={"placeholder": "Cidade", "class": "form-control input"})
    )

    company = forms.CharField(
        label='Empresa', widget=forms.TextInput(attrs={"placeholder": "Empresa", "class": "form-control input"})
    )

    training = forms.ModelChoiceField(
        label='Treinamento',
        queryset=Training.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control input'})
    )

    instructor = forms.ModelChoiceField(
        label='Instrutor',
        queryset=Instructor.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control input'})
    )

    expectation = forms.CharField(
        label='O treinamento correspondeu as suas expectativas?', 
        widget=forms.RadioSelect(choices=YES_NO_CHOICES)
    )

    courseware = forms.CharField(
        label='A qualidade do material didático foi', 
        widget=forms.RadioSelect(choices=EVALUATION_CHOICES)
    )

    instructor_assessment = forms.CharField(
        label='A atuação do instrutor foi', 
        widget=forms.RadioSelect(choices=EVALUATION_CHOICES)
    )

    general_evaluation = forms.CharField(
        label='Avaliação Geral', 
        widget=forms.RadioSelect(choices=EVALUATION_CHOICES)
    )

    others = forms.CharField(
        label='Comentários, Criticas e Sugestões', 
        widget=forms.Textarea(attrs={"placeholder": "Comentários, Criticas e Sugestões", "class": "form-control textarea", "rows": 3})
    )

    class Meta:
        model = Evaluation
        fields = ['name', 'city', 'company', 'training', 'instructor', 'expectation', 'courseware', 'instructor_assessment', 'general_evaluation', 'others']
