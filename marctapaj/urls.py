from django.conf.urls import patterns, url

from marctapaj import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	# url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^category/add/$', views.AddCategoryView.as_view(), name='add_cat'),
	url(r'^category/edit/(?P<pk>\d+)$', views.EditCategoryView.as_view(), name='edit_cat'),
	url(r'^category/delete/(?P<pk>\d+)$', views.DeleteCategoryView.as_view(), name='del_cat'),
	url(r'^bookmark/add/$', views.AddBookmarkView.as_view(), name='add_bm'),
	url(r'^bookmark/(?P<bookmark_id>\d+)/note/add/$', views.AddNoteView.as_view(), name='add_note'),
	url(r'^note/(?P<pk>\d+)/edit/$', views.EditNoteView.as_view(), name='edit_note'),
	url(r'^note/(?P<pk>\d+)/delete/$', views.DeleteNoteView.as_view(), name='del_note'),
	url(r'^go/(?P<bookmark_id>\d+)/$', views.GoToBookmark.as_view(), name='go_to_bookmark')
)