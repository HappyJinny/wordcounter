from django import forms

class TextAreaForm(forms.Form):
    fulltext = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': '심플 텍스트'}), 
        label='텍스트 입력'
        )