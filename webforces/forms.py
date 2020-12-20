from django import forms


class NewAlgForm(forms.Form):
    title = forms.CharField(max_length=100, label="",
                            widget=forms.TextInput(attrs={'id': 'NewAlgTitle', 'placeholder': 'Title'}))
    description = forms.CharField(label="",
                                  widget=forms.Textarea(attrs={'id': 'NewAlgDescription',
                                                               'placeholder': 'Description'}))
    cost = forms.IntegerField(min_value=0, label="",
                              widget=forms.TextInput(attrs={'id': 'NewAlgCost', 'placeholder': 'Cost'}))
    source = forms.CharField(label="",
                             widget=forms.Textarea(attrs={'id': 'NewAlgSource', 'placeholder': 'Source'}))


class UpdUserForm(forms.Form):
    first_name = forms.CharField(
        label="", widget=forms.TextInput(attrs={'id': 'FirstName', 'placeholder': 'First name'}))
    middle_name = forms.CharField(
        label="", widget=forms.TextInput(attrs={'id': 'MiddleName', 'placeholder': 'Middle name'}))
    second_name = forms.CharField(
        label="", widget=forms.TextInput(attrs={'id': 'SecondName', 'placeholder': 'Second name'}))


class BuyAlgForm(forms.Form):
    pass
