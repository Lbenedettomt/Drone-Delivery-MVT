from django.forms import ModelForm
from app.models import Register

# Create the form class.
class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ['drone', 'product']