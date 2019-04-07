from django import forms
from multiselectfield import MultiSelectFormField
class ContactForm(forms.Form):
    name = forms.CharField(
        label='Enter your name',
        widget=forms.TextInput(
            attrs={
               'class': 'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    email = forms.EmailField(
        label='Enter your email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email'
            }
        )
    )
    mobile = forms.IntegerField(
        label='Enter Your Mobile',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Mobile Number'
            }
        )
    )
    COURSES_CHOICES = (
        ('python', 'Python'),
        ('django', 'Django'),
        ('restapi', 'RestApi'),
        ('ui', 'UI'),
        ('flask', 'Flask')
    )
    courses = MultiSelectFormField(choices=COURSES_CHOICES)
    LOCATION_CHOICES = (
        ('hyd', 'Hyderabad'),
        ('bang', 'Bangalore'),
        ('che', 'Chennai'),
        ('pune', 'Pune'),
        ('del', 'Delhi')
    )
    location = MultiSelectFormField(choices=LOCATION_CHOICES)
    SHIFT_CHOICES = (
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
        ('night', 'Night')
    )
    shift = MultiSelectFormField(choices=SHIFT_CHOICES)

class FeedbackForm(forms.Form):
    name = forms.CharField(
        label='Enter your name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    rating = forms.IntegerField(
        label='Enter your rating',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your rating here'
            }
        )
    )
    feedback= forms.CharField(
        label='Enter your feedback',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your feedback here'
            }
        )
    )
