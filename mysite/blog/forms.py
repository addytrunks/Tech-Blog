from django import forms
from .models import Post,Category
from django.contrib.auth.models import User

choices = Category.objects.all().values_list('name','name')
choice_list = []

for item in choices:
    choice_list.append(item)

class AddPostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('title','author','category','text')

        widgets = {
        'title':forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Do not enter more than 30 characters'}),
        'author':forms.TextInput(attrs={'class':'form-control form-control-sm','id':'user','value':'','type':'hidden'}),
        'category':forms.Select(choices=choice_list,attrs={'class':'form-control form-control-sm'}),
        'text':forms.Textarea(attrs={'class':'form-control form-control-sm','id':'text','placeholder':'Enter your text here','rows':'7','cols':5})
        }

class UpdatePostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('title','category','text')

        widgets = {
        'title':forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Do not enter more than 30 characters'}),
        'category':forms.Select(choices=choice_list,attrs={'class':'form-control form-control-sm'}),
        'text':forms.Textarea(attrs={'class':'form-control form-control-sm','placeholder':'Enter your text here','rows':'7','cols':5})
        }
