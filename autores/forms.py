from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def add_attr(field, attr, value):
    attr_existente = field.widget.attrs.get(attr, '')
    field.widget.attrs[attr] = f'{attr_existente} {value}'.strip()

def add_placeholder(field, value):
    add_attr(field, 'placeholder', value)

class CadastroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['first_name'], 'Ex: João')
        add_placeholder(self.fields['last_name'], 'Ex: Silva')
        add_placeholder(self.fields['username'], 'Digite seu usuário')
        add_placeholder(self.fields['email'], 'Ex: email@email.com')
        
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha'
        }),
        error_messages={
            'required':'A senha deve possuir pelo menos 8 caracteres'
        },
        help_text=(
            'A senha deverá possuir 1 caractere maiúsculo, 1 caractere '
            'minúsculo, 1 símbolo especial (Ex: @, !, &) e ao menos 8 caracteres'
        )
    )
    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirme sua senha'
        }),
        # error_messages='A confirmação de senha é obrigatória e deverá'
        # 'ter o mesmo valor do campo "senha"',
        # help_text='Repita sua senha inserida previamente'
    )
    class Meta:
        model= User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        ]
        
        help_texts = {
            'email': 'O campo de e-mail precisa ser válido'
        }
        
        error_messages = {
            'username': {
                'required': 'O preenchimento do campo é obrigatório'
            }
        }
        
        widgets = {
            # 'first_name':forms.TextInput(attrs={
            #     'placeholder': 'Digite o primeiro nome'
            # }),
            'password':forms.PasswordInput(attrs={
                'placeholder': 'Digite sua senha'
            })
        }
        
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if 'vinicius' in first_name:
            raise ValidationError(
                'O nome não pode ser %(value)s',
                code='invalid',
                params={'value': 'vinicius'}
            )
        return first_name
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise ValidationError({
                'password':'As senhas não conferem'
            })