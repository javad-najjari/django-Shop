from django import forms
from .models import Comment



class ProductSearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['search'].label = ''

    search = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'جستجو بین محصولات'}))


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'نظر خود را اینجا وارد کنید'})
        }


class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

