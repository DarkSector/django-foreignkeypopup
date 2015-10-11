from django import forms
from models import ParentModel, ChildClass


class CustomSelectWidget(forms.Select):

    class Media:
        css = {
            'all': ('css/pretty.css',)
        }
        js = ('js/selectfield.js', 'https://code.jquery.com/jquery-1.11.3.min.js')

    def __init__(self, *args, **kwargs):
        super(CustomSelectWidget, self).__init__(*args, **kwargs)


class CustomModelChoiceField(forms.ModelChoiceField):
    
    def __init__(self, *args, **kwargs):
        super(CustomModelChoiceField, self).__init__(*args, **kwargs)


class ChildForm(forms.ModelForm):

    class Meta:
        exclude = ('',)
        model = ChildClass

    parent = forms.ModelChoiceField(queryset=ParentModel.objects.all(), widget=CustomSelectWidget())

    def __init__(self, *args, **kwargs):
        super(ChildForm, self).__init__(*args, **kwargs)