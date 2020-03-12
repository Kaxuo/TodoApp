from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(max_length=40, 
    widget=forms.TextInput(
        # you should check this out , it has the same class as the index html 
        attrs={'class': 'form-control', 'placeholder': 'Enter todo e.g. Delete junk files', 'aria-label': 'Todo', 'aria-describedby': 'add-btn'}
    ))