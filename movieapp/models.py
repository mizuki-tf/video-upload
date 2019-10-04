from django.db import models

class Video(models.Model):
    title = models.CharField('タイトル',max_length=255)
    description = models.TextField('説明',blank=True) #空欄可

    """「 upload_to 」フィールドのアップロード場所
    アップロード場所は /media/upload_to に保存される
    """
    thumbnail = models.ImageField('サムネイル',upload_to='thumbnails/',null=True,blank=True) #空欄可
    upload = models.FileField('ファイル',upload_to='uploads/%Y/%m/%d/')
    #modelformで「input type="file"」なhtmlになる．DBにはファイルの置き場所(パス)を保存,
    #/media/uploads/2019/10/20/ファイル名

    created_at = models.DateTimeField('作成部',auto_now_add=True) #dedefault=timezone.nowと違い，編集できなくなる
    updated_at = models.DateTimeField('更新日',auto_now=True) #更新の度に更新した日時が入る．編集不可

    def __str__(self):
        return self.title
