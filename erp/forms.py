from django import forms
from .models import Sale

class SaleForm(forms.Models):
    class Meta:
        model = Sale
        fields = __all__

# add others
# or just use admin for now
