from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):


    class Meta:
        model = Product
        fields = "__all__"


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['product', 'version_number', 'version_name', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'