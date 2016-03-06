from django.conf.urls import patterns, include, url, static
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import CreateView
from photologue.models import Photo,Gallery
from photologue.views import PhotoListView, PhotoDetailView, GalleryListView, \
    GalleryDetailView, PhotoArchiveIndexView, PhotoDateDetailView, PhotoDayArchiveView, \
    PhotoYearArchiveView, PhotoMonthArchiveView, GalleryArchiveIndexView, GalleryYearArchiveView, \
    GalleryDateDetailView, GalleryDayArchiveView, GalleryMonthArchiveView

    
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foodlovers.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

url(r'^photo/comments/', include('django_comments.urls')),	
url(r'^photologue/photo/add/$', CreateView.as_view(model=Photo, success_url='/photologue/photolist',fields=('image','title','slug',)),
        name='add-photo'),
url(r'^photologue/gallery/add/$', CreateView.as_view(model=Gallery, success_url='/photologue/gallery',fields=('photos','title','slug','description',)),
        name='add-gallery'),		
url(r'^login/$', 'appusers.views.mylogin', name='login'),
   url(r'^logout/$', 'appusers.views.mylogout', name='logout'),
                       
        url(r'^friends/', include('friends.urls')),               
                       
                       
     url(r'^show_feed/$', 'appusers.views.show_feed', name='show_feed'),                   
                       
    url(r'^home/$', 'photobucket.views.home', name='home'),
        url(r'^feed/$', 'photobucket.views.home', name='home'),
                   
url(r'^home/users/(?P<user_id>[\d]+)/$','appusers.views.show_user_id',name='show_user_id'),
                       #rl(r'^login/$', 'appusers.views.register', name='register'),
	 url(r'^searchuser/$', 'appusers.views.autocomplete', name='autocomplete'),
	 url(r'^tagsearch/$', 'appusers.views.tagsearch', name='search'),
    url(r'^userphoto/tagsearch/$', 'appusers.views.tagsearch', name='search'),
                   
	 url(r'^addprofilepic/$', 'appusers.views.addprofilepic', name='addprofilepic'), 
	 url(r'^delprofilepic/$', 'appusers.views.delprofilepic', name='delprofilepic'), 
                       
	  url(r'^addphoto/$', 'photobucket.views.addphoto', name='addphoto'),
	  url(r'^addrecipe/$', 'photobucket.views.addrecipe', name='addrecipe'),
	  url(r'^recipes/$', 'photobucket.views.recipelist', name='recipelist'),
	  url(r'^myrecipes/$', 'photobucket.views.user_recipe', name='user_recipe'),
                       
     url(r"^notifications/", include("pinax.notifications.urls")),                  
      url(r'^friend_feed/$', 'appusers.views.friend_feed', name='friend_feed'),                 
	  url(r'^deletephoto/$', 'photobucket.views.delete_photo', name='delete_photo'),
	  url(r'^deleterecipe/$', 'photobucket.views.delete_recipe', name='delete_recipe'),
                       
      url(r'^reportphoto/$', 'photobucket.views.reportphoto', name='reportphoto'),                  
      url(r'^reportrecipe/$', 'photobucket.views.reportrecipe', name='reportrecipe'),                  
    url(r'^addcomment/$', 'photobucket.views.addcomment', name='addcomment'),
	  url(r'^addcommentrecipe/$', 'photobucket.views.addcomment_recipe', name='addcomment_recipe'),

    url(r'^thanku/$', 'photobucket.views.thanks', name='thanks'),
	url(r'^userphoto/$', 'photobucket.views.photosort', name='photosort'),
	url(r'^profile/$', 'appusers.views.profile', name='profile'),
	url(r'^vote/$', 'photobucket.views.vote', name='vote'),
    url(r'^voterecipe/$', 'photobucket.views.voterecipe', name='voterecipe'),
                   
	url(r'^pin_photo/$', 'photobucket.views.pin_photo', name='pin_photo'),
	url(r'^pin_recipe/$', 'photobucket.views.pin_recipe', name='pin_recipe'),

    url(r'^pinned/$', 'photobucket.views.pinlist', name='pinlist'),
              
                       
    (r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),                   
                       
                       
    url(r'^admin/', include(admin.site.urls)),
	url(r'^sign_up/', ('appusers.views.register_user')),
    url(r'^register_success/', ('appusers.views.register_success')),
    url(r'^accounts/confirm/(?P<activation_key>\w+)/', ('appusers.views.register_confirm')),
	url(r'^photologue/', include('photologue.urls')),
		url(r'^photologue/', include('photologue.urls', namespace='photologue')),	
	url(r'^addinfo/$', 'appusers.views.addinfo', name='addinfo'),
	url(r'^profile/edituserinfo/$', 'appusers.views.edituserinfo', name='edituserinfo'),
                       
	url(r'^facebook/$', include('django_facebook.urls')),
url(r'^accounts/', include('django_facebook.auth_urls')),
url('', include('social.apps.django_app.urls', namespace='social')),
)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 


