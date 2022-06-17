from django import forms
from blog.models import Post, post2


class blogForm(forms.ModelForm):

    class Meta:
        model= Post
        fields ='__all__'

    
        
    
