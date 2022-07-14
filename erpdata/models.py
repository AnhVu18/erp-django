

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    avatar = models.ImageField(upload_to = 'avatar/%y/%m')
    diachi = models.TextField()
    ngaysinh = models.DateField(null=True)
    sodienthoai = models.CharField(max_length=12)
    quyenquanlyduan = models.BooleanField(default=False)
    part = models.ForeignKey('Part', on_delete=models.CASCADE, default=None, null=True)
    


class Part(models.Model):
    tenbophan = models.CharField(max_length=100, unique=True)
    tenphongban = models.CharField(max_length=100, unique=True)
    ngaytao = models.DateField(auto_now=True)
    def __str__(self):
        return self.tenbophan


class ItemBase(models.Model):
      class Meta():
        abstract: True
      ten = models.CharField(max_length=100, unique=True)
      ngaybatdau = models.DateTimeField(null=True, blank=True,default=None)
      ngayketthuc = models.DateTimeField(null=True, blank=True, default=None)
      ngaybatdauthucte = models.DateField(null=True, blank=True, default=None)
      ngayketthucthute= models.DateField(null=True, blank=True, default=None)
      ngaytao = models.DateField(auto_created=True)
      idnhanvienthamgia = models.ManyToManyField('User', blank=True, null=True)
      def __str__(self):
        return self.ten

class Project(ItemBase):
    loaiduan = models.CharField(max_length=100)
    trangthai = models.IntegerField(default=1)
    duanquantrong = models.BooleanField()
    maduan = models.CharField(max_length=100)

    idbophanthamgiaduan = models.ManyToManyField('Part', blank=True, null=True)

class Stage(models.Model):
    
    ten = models.CharField(max_length=100, unique=True)
    vitri = models.CharField(max_length=100, unique=True)
    ngaytao = models.DateTimeField(auto_created=True)
    
    
    project = models.ForeignKey('Project',  on_delete=models.CASCADE)
    def __str__(self):
        return self.ten

class Categorys(ItemBase):
    chiphi = models.IntegerField()
    trangthai = models.BooleanField(default=False)
    mota = models.TextField()

    stage = models.ForeignKey('Stage', on_delete=models.CASCADE)

    role = models.ManyToManyField('Role', null=True)

class Work(ItemBase):
    mota = models.TextField()
    trangthai = models.BooleanField(default=False)
    chiphi = models.IntegerField()

    category = models.ForeignKey('Categorys', on_delete=models.CASCADE) 
    process = models.ForeignKey('Process', on_delete=models.CASCADE, default=None, blank=True)

class ExtraWork(models.Model):
    ten = models.CharField(max_length=100, unique=True)
    mota = models.TextField()
    trangthai = models.BooleanField()
    
    Work = models.ForeignKey('Work', on_delete=models.CASCADE)
    createby = models.ForeignKey('User', on_delete=models.CASCADE)

    nguoiduyet = models.ManyToManyField('User', related_name='nguuoiduyetcvbs',blank=True)
    nguoinhanthongbao = models.ManyToManyField('User', related_name='nguoinhanthongbaocvbs', blank=True)
    def __str__(self):
        return self.ten

class Document(models.Model):
    ten = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    ngaytao = models.DateTimeField(auto_created=True)

    work = models.ForeignKey("Work", on_delete=models.CASCADE)
    def __str__(self):
        return self.ten


class Process(models.Model):
    ten = models.CharField(max_length=100, unique=True)
    mota = models.TextField()

    createby = models.ForeignKey('User', on_delete=models.CASCADE)
    def __str__(self):
        return self.ten


class SampleDoc(models.Model):
    ten = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    ngaytao = models.DateTimeField(auto_created=True)

    process = models.ForeignKey('Process', on_delete=models.CASCADE)
    def __str__(self):
        return self.ten

class SampleStep(models.Model):
    ten = models.CharField(max_length=100)
    mota = models.TextField()
    trangthai = models.BooleanField(default=False)

    createby = models.ForeignKey('User', on_delete=models.CASCADE)
    process = models.ForeignKey('Process', on_delete=models.CASCADE)

    nguoiduyet = models.ManyToManyField('User', related_name='nguuoiduyetbm',blank=True)
    nguoinhanthongbao = models.ManyToManyField('User', related_name='nguoinhanthongbaobm', blank=True)
    def __str__(self):
        return self.ten


class Role(models.Model):
    ten =  models.CharField(max_length=255, unique=True)
    mausac = models. CharField(max_length=255, unique=True)
    staff = models.ForeignKey('User', on_delete=models.CASCADE)
    def __str__(self):
        return self.ten

class CostOfWork(models.Model):
    chiphi = models.IntegerField()
    songaycongtac = models.IntegerField()
    tiencongtac = models.IntegerField()
    tienkm = models.IntegerField()
    sokmdadi = models.IntegerField()
    thanhtien = models.IntegerField()
    ngaybatdau = models.DateTimeField(null=True)
    ngayketthuc = models.DateTimeField(null=True)
    ngaytao = models.DateTimeField(auto_created=True)

    staff = models.ForeignKey('User', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    nhanvienthamgia = models.ManyToManyField('User',related_name='nhanvienthamgiacongtac',blank=True)
    bophanthamgia = models.ManyToManyField('Part',related_name='bophanthamgiacongtac', blank=True, null=True)
    

class Comment(models.Model):
    noidung = models.TextField()
    ngaytao = models.DateTimeField(auto_created=True)

    category = models.ForeignKey('Categorys', on_delete=models.CASCADE)
    


 




    




