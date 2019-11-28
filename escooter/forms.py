from django.forms import ModelForm
from .models import EScooter


class EScooterForm(ModelForm):
    class Meta:
        model = EScooter
        fields = ['name',
                  'manufacturer',
                  'image',
                  'price',
                  'serie',
                  'description',
                  'year',
                  'identityNum',
                  'weight',
                  'scooter_amount',
                  'available',
                  'rate']