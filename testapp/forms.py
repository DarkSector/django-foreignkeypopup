from django import forms
from models import ParentModel, ChildClass


class CustomSelectWidget(forms.Select):

    class Media:
        css = {
            'all': ('css/pretty.css',)
        }
        js = ('https://code.jquery.com/jquery-1.11.3.min.js', 'js/default.js')

    def __init__(self, *args, **kwargs):
        super(CustomSelectWidget, self).__init__(*args, **kwargs)


class CustomModelChoiceField(forms.ModelChoiceField):
    
    def __init__(self, *args, **kwargs):
        class_name = kwargs.pop('class_name', None)
        js = kwargs.pop('js', None)
        css = kwargs.pop('css', None)
        super(CustomModelChoiceField, self).__init__(*args, **kwargs)
        self.widget = CustomSelectWidget({'class_name': class_name, 'js': js, 'css': css})


class ChildForm(forms.ModelForm):

    class Meta:
        exclude = ('',)
        model = ChildClass

    parent = CustomModelChoiceField(queryset=ParentModel.objects.all(), class_name='', js='', css='')

    def __init__(self, *args, **kwargs):
        super(ChildForm, self).__init__(*args, **kwargs)