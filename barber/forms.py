from django import forms  
from barber.models import Order  
  
class OrderForm(forms.ModelForm):  
    class Meta:  
        model = Order  
        fields = '__all__'
        labels = {
            'client_name': ('ФИО'),
            'client_order': ('Услуга'),
            'client_comments': ('Комментарии'),
            'client_tel': ('Телефон'),
            'client_email': ('e-mail'),
            'private_data': ('Согласие на обработку персональных данных'),
        }
        widgets = {
          'client_comments': forms.Textarea(attrs={'rows':3, 'cols':19}),
        }