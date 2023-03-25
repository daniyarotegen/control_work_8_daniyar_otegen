from django import forms
from reviewer.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'image')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('feedback', 'rating')

