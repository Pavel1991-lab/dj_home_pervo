from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    FORBIDDEN = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def form_valid(self, form):
        form.instance.user = self.request.user  # привязываем текущего пользователя к полю user
        return super().form_valid(form)

    def clean_name(self):
        name = self.cleaned_data.get('name')

        for word in self.FORBIDDEN:
            if word.lower() in name.lower():
                raise forms.ValidationError('Запрещенное слово: {}'.format(word))
        return name


    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "purchase_price", "is_published"]



class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['product', 'version_number', 'version_name', 'is_active']



