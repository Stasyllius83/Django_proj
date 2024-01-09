from django import forms
from catalog.models import Product, Version




class StylyFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ProductForm(StylyFormMixin, forms.ModelForm):

    Prohibited_Products = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        exclude = ('owner',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name'].lower()
        for word in self.Prohibited_Products:
            if word in cleaned_data:
                raise forms.ValidationError('Запрещенное имя продукта')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description'].lower()
        for word in self.Prohibited_Products:
            if word in cleaned_data:
                raise forms.ValidationError('Запрещенные слова в описании продукта')
        return cleaned_data


class VersionForm(StylyFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
