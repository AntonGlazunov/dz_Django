from crispy_forms.bootstrap import InlineCheckboxes
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Field
from django import forms

from catalog.models import Product, Version


class VisualFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class ProductForm(VisualFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            Fieldset('Товар', 'name', 'description'), Submit('submit', 'Сохранить', css_class='btn btn-success'),
        )


    class Meta:
        model = Product
        fields = ('name', 'description', 'image',)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')

        if cleaned_data.lower() in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман',
                                    'полиция', 'радар']:
            raise forms.ValidationError('Ошибка, используется запрещенное имя')

        return cleaned_data


class VersionForm(VisualFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
