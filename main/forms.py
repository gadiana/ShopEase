from django import forms
from django.forms import ModelForm
from .models import Cart

class CartEditForm(ModelForm):
    class Meta:
        model = Cart
        fields = ['cartname', 'store_wheretobuy', 'date_for_notification']
        widgets = {
            'date_for_notification': forms.DateInput(attrs={'type': 'date'}),
        }

        # Add other fields as needed

    # You can customize form fields, add validation, etc., if necessary
