from django import forms
from models import ParentModel, ChildClass


class CustomSelectWidget(forms.Select):

    def __init__(self, *args, **kwargs):
        super(CustomSelectWidget, self).__init__(*args, **kwargs)
        if self.attrs:
            if not 'class_name' in self.attrs:
                self.attrs['class'] = 'fk-popup'
            else:
                self.attrs['class'] = self.attrs['class_name']
                self.attrs.pop('class_name', None)

    def _set_default_media(self):
        """
        Method to set the default media of the widget, as you would
        in the Media class

        class Media:
            css = {
                'all': ('css/pretty.css',)
            }
            js = ('https://code.jquery.com/jquery-1.11.3.min.js', 'js/default.js')

        .. seealso::https://docs.djangoproject.com/en/1.8/topics/forms/media/
        """
        css = {
            'all': ('css/pretty.css',)
        }
        js = ('https://code.jquery.com/jquery-1.11.3.min.js', 'js/default.js')
        return css, js

    def _media(self):
        """
        .. seealso::https://docs.djangoproject.com/en/1.8/topics/forms/media/#media-as-a-dynamic-property
        """
        css, js = self._set_default_media()
        if 'js' in self.attrs:
            js = self.attrs['js']
        if 'css' in self.attrs:
            css = self.attrs['css']
        return forms.Media(css=css, js=js)

    media = property(_media)


class CustomModelChoiceField(forms.ModelChoiceField):
    """

    """
    def __init__(self, *args, **kwargs):
        class_name = kwargs.pop('class_name', None)
        js = kwargs.pop('js', None)
        css = kwargs.pop('css', None)
        type_error_message = "js needs to be of type %s. See https://docs.djangoproject.com/en/1.8/topics/forms/media/"
        if not isinstance(js, tuple):
            raise TypeError(type_error_message % 'tuple')
        if not isinstance(css, dict):
            raise TypeError(type_error_message % 'dict')
        if not isinstance(class_name, str):
            raise TypeError("class_name needs to be of type str")
        super(CustomModelChoiceField, self).__init__(*args, **kwargs)
        self.widget = CustomSelectWidget({'class_name': class_name, 'js': js, 'css': css})


class ChildForm(forms.ModelForm):

    class Meta:
        exclude = ('',)
        model = ChildClass

    parent = CustomModelChoiceField(queryset=ParentModel.objects.all())

    def __init__(self, *args, **kwargs):
        super(ChildForm, self).__init__(*args, **kwargs)