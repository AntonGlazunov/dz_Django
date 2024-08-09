from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from django import forms

from catalog.models import Product, Version


class VisualFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.form_tag = False


class ProductForm(VisualFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(Fieldset('Товары', 'name', 'description', 'image', 'category', 'price', ),
                                    Submit('submit', 'Сохранить', css_class='button white'), )

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')

        if cleaned_data.lower() in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман',
                                    'полиция', 'радар']:
            raise forms.ValidationError('Ошибка, используется запрещенное имя')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')

        if cleaned_data.lower() in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман',
                                    'полиция', 'радар']:
            raise forms.ValidationError('Ошибка, используется запрещенное описание')

        return cleaned_data


class VersionForm(VisualFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

    # def clean_version_number(self):
    #     cleaned_data = self.cleaned_data.get('is_active')
    #     product = self.cleaned_data.get('product')
    #     is_active_version_product = Version.objects.filter(is_active=True,
    #                                                        product=Product.objects.get(pk=product.pk))
    #     if len(is_active_version_product) > 1:
    #         raise forms.ValidationError('Ошибка, может быть одна активная версия')
    #     return cleaned_data
