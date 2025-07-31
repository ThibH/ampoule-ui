from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={
            'placeholder': 'votre@email.com',
            'class': 'input'
        })
    )
    
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Votre mot de passe',
            'class': 'input'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if email == 'test@gmail.com' and password == 'test':
            return cleaned_data
        
        # If password is not test, return an error on the password field
        self.add_error('password', 'Mot de passe incorrect')
        return cleaned_data
