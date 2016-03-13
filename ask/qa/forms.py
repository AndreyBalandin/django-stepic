from django import forms
from django.forms import ModelForm
from models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class ModelChoiceField_title(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.title


class AnswerForm(ModelForm):
    question = ModelChoiceField_title(queryset=Question.objects.all())

    class Meta:
        model = Answer
        fields = ['question','text']

