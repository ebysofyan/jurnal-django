from django.db import models
from jurnal.models import Jurnal

# Create your models here.
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