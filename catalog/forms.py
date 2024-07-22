from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image',)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')

        if cleaned_data.lower() in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман',
                                    'полиция', 'радар']:
            raise forms.ValidationError('Ошибка, используется запрещенное имя')

        return cleaned_data


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

    # def clean_name(self):
    #     cleaned_data = self.cleaned_data.get('is_active')
    #
    #     if cleaned_data in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман',
    #                                 'полиция', 'радар']:
    #         raise forms.ValidationError('Ошибка, используется запрещенное имя')
    #
    #     return cleaned_data
