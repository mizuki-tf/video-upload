from django import forms
from .models import Video

class VideoCreateForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ('title','description','thumbnail','upload')

        """
        全てに'form-control'をつけたい --> __init__メソッド内で指定
        それ以外，個別になんかつけたい --> widgets = ｛｝ で指定
        """
        widgets = {
            'title': forms.TextInput(attrs={ #<input type="text" class="form-control">
                'class':'form-control',

            }),
            'description': forms.Textarea(attrs={ #<textarea class="form-control">
                'class':'form-control',

            }),
            'thumbnail': forms.ClearableFileInput(attrs={ #<input type="file" class="form-control-file">
                'class':'form-control-file', #ファイル投稿のBootstrapは-file

            }),
            'upload': forms.ClearableFileInput(attrs={
                'class':'form-control-file',

            }),
        }
