from django.urls import path
from blog.views import iletisim, anasayfa, kategori, yazilarim, detay, yazi_ekle, yazi_guncelle, yazi_sil, yorum_sil

urlpatterns = [
    path('', anasayfa, name='anasayfa'),
    path('iletisim', iletisim, name='iletisim'),
    path('kategori/<slug:kategoriSlug>', kategori, name='kategori'),
    path('yazilarim', yazilarim, name='yazilarim'),
    path('detay/<slug:slug>', detay, name='detay'),
    path('yazi-sil/<slug:slug>', yazi_sil, name='yazi_sil'),
    path('yorum-sil/<slug:slug>', yorum-sil, name='yorum-sil'),
    path('yazi-ekle', yazi_ekle, name='yazi-ekle'),
    path('yazi-guncelle/<slug:slug>', yazi_guncelle, name='yazi-guncelle'),

]
