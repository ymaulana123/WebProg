from django import forms

class StudentRegisterForm(forms.Form):
    fullname = forms.CharField(
        label='Nama Lengkap', 
        label_suffix=" : ", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John Smith'}),
        help_text="Nama lengkap mahasiswa", 
        error_messages={'required': "Harus Diisi"}
    )
    nim = forms.CharField(
        label='Nim', 
        label_suffix=" : ", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '102988444'}),
        help_text="nomor induk mahasiswa", 
        error_messages={'required': "Harus Diisi"}
    )
    email = forms.EmailField(
        label='Email', 
        label_suffix=" : ", 
        required=True, 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'john@smith.co'}),
        help_text="email aktif", 
        error_messages={'required': "Harus Diisi"}
    )

    def clean(self):
        cleaned_data = super().clean()
        
        fullname = cleaned_data.get("fullname")
        nim = cleaned_data.get("nim")
        email = cleaned_data.get("email")
        
        if not fullname:
            self.add_error('fullname', 'Harus di isi!')
        
        if not nim:
            self.add_error('nim', 'Harus di isi!')
        
        if not email:
            self.add_error('email', 'Harus di isi!')
        
        return cleaned_data
