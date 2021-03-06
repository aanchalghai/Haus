from django import forms
from django.contrib.auth import get_user_model
from .models import PersonalInfo,RentListings,PgListings,SellListings

class NameForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name',)

class PersonalInfoForm(forms.ModelForm):
    GENDER = (
        ('C','Choose'),
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control',}),choices=GENDER)
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control',}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','id':'date',}))
    class Meta:
        model = PersonalInfo
        fields = ('gender','phone','address','date_of_birth',)


class RentListingsForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg',}))
    bedrooms = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg',}))
    bathrooms = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg',}))
    area = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg',}))
    locality = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg',}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg',}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg',}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg',}))
    pin_code = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg',}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control form-control-lg',}))
    pictures = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control-file'}))

    class Meta:
        model = RentListings
        fields = ('title', 'price', 'bedrooms', 'bathrooms', 'area', 'locality', 'city', 'state', 'country', 'pin_code', 'description','pictures')

class PgListingsForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg',}))
    bedrooms = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg',}))
    bathrooms = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg',}))
    area = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg',}))
    locality = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg',}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg',}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg',}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg',}))
    pin_code = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg',}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control form-control-lg',}))
    pictures = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control-file'}))

    class Meta:
        model = PgListings
        fields = ('title', 'price', 'bedrooms', 'bathrooms', 'area', 'locality', 'city', 'state', 'country', 'pin_code', 'description','pictures')

class SellListingsForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg',}))
    bedrooms = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg',}))
    bathrooms = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg',}))
    area = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg',}))
    locality = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg',}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg',}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg',}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg',}))
    pin_code = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg',}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control form-control-lg',}))
    pictures = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control-file'}))

    class Meta:
        model = SellListings
        fields = ('title', 'price', 'bedrooms', 'bathrooms', 'area', 'locality', 'city', 'state', 'country', 'pin_code', 'description','pictures')
