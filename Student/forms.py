from django import forms


class DobForm(forms.ModelForm):
    dob = forms.DateField(
        widget=forms.DateInput(
        attrs={
            "type":'date',
            "class":'form-control'
        }
        )
    )

    