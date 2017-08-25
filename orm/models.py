from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=30)
    alamat = models.TextField()
    tanggal_lahir = models.DateField(auto_now=False, auto_now_add=False)
    photo = models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'profile'


class Jurnal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jurnals')
    nama = models.CharField(max_length=30)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'jurnal'
        ordering = ['-id']


class Transaksi(models.Model):
    jurnal = models.ForeignKey(Jurnal, on_delete=models.CASCADE, related_name='transaksis')
    tanggal = models.DateField(auto_now=False, auto_now_add=False)
    uraian = models.TextField()
    debt = models.FloatField(blank=True, default=0.0)
    kredit = models.FloatField(blank=True, default=0.0)

    def __str__(self):
        return self.uraian

    class Meta:
        db_table = 'transaksi'
        ordering = ['-id']
