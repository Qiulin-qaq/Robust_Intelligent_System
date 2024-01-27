# python learning
# coding time: 2023/8/22 23:07
from django import forms


class BootStrap:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {
                    'class': 'form-control',
                    'placeholder': field.label
                }


class BootStrapForm(BootStrap, forms.Form):
    pass


class BootStrapModelForm(BootStrap, forms.ModelForm):
    pass
