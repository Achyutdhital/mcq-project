from django import forms
from app.models import *
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'

class QuestionSetsForm(forms.ModelForm):
    class Meta:
        model = QuestionSets
        fields = '__all__'
        
class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = '__all__'
        
class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Question'})
        }

        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'
        widgets = {
            'answer': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Answer'})
        }




# class AnswerForm(forms.ModelForm):
#     class Meta:
#         model = Answer
#         fields = ['answer']

# AnswerFormSet = forms.inlineformset_factory(Questions, Answer, form=AnswerForm, extra=1, can_delete=True)

# class QuestionsForm(forms.ModelForm):
#     class Meta:
#         model = Questions
#         fields = ['set_name', 'question', 'image']
#         widgets = {
#             'set_name': forms.Select(attrs={'class': 'form-control'}),
#         }