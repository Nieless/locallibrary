from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='book-list'),
    url(r'book/add/$', views.BookCreate.as_view(), name='book-add'),
    url(r'book/update/(?P<pk>\d+)$', views.BookUpdateView.as_view(), name='book-update'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^book/delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book-delete'),
    url(r'^books/$', views.BookSearchView.as_view(), name='book-search'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='author-list'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'^profile/(?P<user_id>\d+)$', views.UserProfile.as_view(), name='user-profile'),
]
