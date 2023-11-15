from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name_product', 'description_product', 'category_product', 'image_product', 'price',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name_product(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['name_product']

        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError('Вы не можете загружать запрещенные продукты на платформу')

        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ('version_number', 'name_version', 'sing_version',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('is_published', 'description_product', 'category_product',)
