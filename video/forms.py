from django import forms
from django.contrib.auth.models import User
from main.models import Video

class videoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(videoUploadForm, self).__init__(*args, **kwargs)
        self.fields['videoFile'].required = False
        self.fields['videoURL'].required = False
        self.fields['content'].required = False
        self.fields['user'].required = False
        self.fields['publishedDate'].required = False

        for key, value in self.fields.items():
            if key in ['title', 'content', 'videoURL', 'user', 'publishedDate']:
                self.fields[key].widget.attrs.update({'class': 'inputForm'})
            else:
                self.fields[key].widget.attrs.update({'class': 'selector'})
