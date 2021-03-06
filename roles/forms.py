from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import forms as auth_forms


from roles.models import ClinicUser, Paciente, Medico


class ClinicUserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = ClinicUser
        fields = '__all__'

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class ClinicUserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = ClinicUser
        fields = ('nome', 'email', 'password', 'is_patient', 'is_doctor', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class ClinicUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = ClinicUserChangeForm
    add_form = ClinicUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin  
    # that reference specific fields on auth.User.
    list_display = ('nome', 'email', )
    list_filter = ('is_admin', 'is_doctor', 'is_patient')
    fieldsets = (
        (None, {'fields': ('nome', 'email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_doctor', 'is_patient')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nome', 'email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()



class PatientCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Paciente
        fields = ['nome', 'email', 'rg', 'cpf']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        patient = super().save(commit=False)
        patient.set_password(self.cleaned_data["password1"])
        patient.is_patient = True
        if commit:
            patient.save()
        return patient

class PatientChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Paciente
        fields = ['nome', 'email', 'rg', 'cpf']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class PatientAdmin(admin.ModelAdmin):
    
    change_form = PatientChangeForm
    add_form = PatientCreationForm
 
    list_display = ('nome', 'email', 'rg', 'cpf')
    #fieldsets = (
    #     ('Informações', {'fields': ('nome', 'email', 'password', 'rg', 'cpf')}),
    # )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nome', 'email', 'rg', 'cpf', 'password1', 'password2')}
        ),
    )

    search_fields = ('nome', 'email', 'rg', 'cpf')
    ordering = ('email',)
    filter_horizontal = ()

    readonly_fields = ('last_login', )


    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = self.add_form
        else:
            self.form = self.change_form

        return super(PatientAdmin, self).get_form(request, obj, **kwargs)
    


    
    # change_form = PatientCreationForm
    # add_form = PatientCreationForm

    # list_display = ('nome', 'email', 'rg', 'cpf')
    # fieldsets = (
    #     ('Informções', {'fields': ('nome', 'email', 'password', 'rg', 'cpf')}),
    # )

    # search_fields = ('nome', 'email', 'rg', 'cpf')
    # ordering = ('email',)
    # filter_horizontal = ()

# /////////////////////////////////////////////////////////////////////////////


class MedicoUserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Medico
        fields = ['nome', 'email', 'crm']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        medico = super().save(commit=False)
        medico.set_password(self.cleaned_data["password1"])
        medico.is_doctor = True
        if commit:
            medico.save()
        return medico

class MedicoUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Medico
        fields = ['nome', 'email', 'crm']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class MedicoAdmin(admin.ModelAdmin):

    change_form = MedicoUserChangeForm
    add_form = MedicoUserCreationForm
 
    list_display = ('nome', 'email', 'crm')
    # fieldsets = (
    #     (None, {'fields': ('nome', 'email', 'password')}),
    #     ('Permissions', {'fields': ('is_admin', 'is_doctor', 'is_patient')}),
    # )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nome', 'email', 'crm', 'password1', 'password2')}
        ),
    )

    search_fields = ('nome', 'email', 'crm')
    ordering = ('email',)
    filter_horizontal = ()

    readonly_fields = ('last_login', )


    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = self.add_form
        else:
            self.form = self.change_form

        return super(MedicoAdmin, self).get_form(request, obj, **kwargs)