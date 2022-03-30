from django import forms



class CartAddForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=9)

    def __init__(self, *args, **kwargs):
        super(CartAddForm, self).__init__(*args, **kwargs)
        self.fields['quantity'].label = 'تعداد'

