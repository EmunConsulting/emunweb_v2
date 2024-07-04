from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('attach/', views.attach, name='attach'),
    path('my_documents/', views.my_documents, name='my_documents'),
    path('add_ref_id/', views.add_ref_id, name='add_ref_id'),
    path('add_fam_att/', views.add_fam_att, name='add_fam_att'),
    path('add_bir_cer/', views.add_bir_cer, name='add_bir_cer'),
    path('add_nat_id/', views.add_nat_id, name='add_nat_id'),
    path('add_wed_cer/', views.add_wed_cer, name='add_wed_cer'),
    path('add_emb_doc/', views.add_emb_doc, name='add_emb_doc'),
    path('add_med_doc/', views.add_med_doc, name='add_med_doc'),
    path('add_oth_doc/', views.add_oth_doc, name='add_oth_doc'),

    # Delete
    path('del_ref_id/<int:pk>', views.del_ref_id, name='del_ref_id'),
    path('del_fam_att/<int:pk>', views.del_fam_att, name='del_fam_att'),
    path('del_bir_cer/<int:pk>', views.del_bir_cer, name='del_bir_cer'),
    path('del_nat_id/<int:pk>', views.del_nat_id, name='del_nat_id'),
    path('del_wed_cer/<int:pk>', views.del_wed_cer, name='del_wed_cer'),
    path('del_emb_doc/<int:pk>', views.del_emb_doc, name='del_emb_doc'),
    path('del_med_doc/<int:pk>', views.del_med_doc, name='del_med_doc'),
    path('del_oth_doc/<int:pk>', views.del_oth_doc, name='del_oth_doc'),

]
