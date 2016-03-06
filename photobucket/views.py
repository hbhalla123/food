from django.forms import ModelForm
from photobucket.models import *
from django.shortcuts import render, get_object_or_404, redirect
from appusers.models import *
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect ,HttpResponse
from django.contrib.auth.decorators import login_required
import re
from django.template import RequestContext
from django.views.decorators.http import require_http_methods
from django.views.generic import View
from django.utils import timezone
from django.conf import settings
from pusher import Pusher
from pusherable.mixins import PusherDetailMixin, PusherUpdateMixin
from pusherable.mixins import PusherMixin
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from itertools import chain
from friends.models import Friendship
from django.template import loader
from django.template import Context
from django.template.loader import get_template
from photobucket.template import render_block_to_string
from django.template.loader import render_to_string
# Create your views here.


class photoForm(ModelForm):
	class Meta:
		model = Photo
		fields = ['image','description','cuisine','place','public']


class commentForm(ModelForm):
	class Meta:
		model=Comment
		fields = '__all__'
		exclude = ['by','on','photo']
        
class RecipeForm(ModelForm):
    class Meta:
        model=Recipe
        fields=['photo','cuisine','title','ingredients','prep_time','cook_time','method']
        
class ReportphotoForm(ModelForm):
    class Meta:
        model=Report_Photo
        fields='__all__'
        exclude=['reportedby','on','photo']
        
class ReportrecipeForm(ModelForm):
    class Meta:
        model=Report_Recipe
        fields='__all__'
        exclude=['by','on','recipe']
        
class commentForm(ModelForm):
	class Meta:
		model=Comment
		fields = '__all__'
		exclude = ['by','on','photo']
		
class signupForm(ModelForm):
	class Meta:
		model=MyUser
		fields = '__all__'
		exclude = ['profile_pic','following']
		
@login_required	
@require_http_methods(["GET"])
def home(request):
    user=request.user
    photo=Photo.objects.all()
    recipe=Recipe.objects.all()
    j=[]
    print("aaj")
    if not Friendship.objects.friends_for_user(request.user) and not UserInfo.objects.filter(user=request.user).exists() and not request.is_ajax():
        print("piyu")
        data=sorted(
    chain(photo,recipe),
    key=lambda instance: instance.on,reverse=True)
        form3=photoForm()
       # obj=get_object_or_404(Comment,pk=1)
        reportform=ReportphotoForm()
        reportformrec=ReportrecipeForm()
        return render(request,'home.html',{"item_list":data[:5],'form3' : form3,'user':user,'reportform':reportform,'reportformrec':reportformrec,'home':True})      
        
    if Friendship.objects.friends_for_user(request.user) and not UserInfo.objects.filter(user=request.user).exists():
        friends = Friendship.objects.friends_for_user(request.user)
        for i in range(photo.count()):
            author=photo[i].by
            for friend in friends:
                if author == friend and author != user:
                    j.insert(i,1)
                else:
                    j.insert(i,0)
        for i in range(photo.count(),recipe.count()+photo.count()):
            for friend in friends:
                if author == friend :
                    j.insert(i,1)
                else:
                    j.insert(i,0)
    if UserInfo.objects.filter(user=request.user).exists() and not Friendship.objects.friends_for_user(request.user):
        userinfo=UserInfo.objects.get(user=request.user)
        for i in range(photo.count()):
            print(userinfo)
            cuisine=photo[i].cuisine
            if cuisine==userinfo.favourite_cuisine:
                j.insert(i,1)
             #   print(j[i])
            else:
                j.insert(i,0)
        for i in range(photo.count(),recipe.count()+photo.count()):
            #print(i)
            cuisine=recipe[i-photo.count()].cuisine
            #print(cuisine)
            if cuisine==userinfo.favourite_cuisine :
                j.insert(i,1)
             #   print(j[i])
            else:
                j.insert(i,0)        
    if UserInfo.objects.filter(user=request.user).exists() and Friendship.objects.friends_for_user(request.user):
        userinfo=UserInfo.objects.get(user=request.user)
        friends = Friendship.objects.friends_for_user(request.user)
        for i in range(photo.count()):
            #print(i)
            cuisine=photo[i].cuisine
            author=photo[i].by
            #print(cuisine)
            if cuisine==userinfo.favourite_cuisine :
                j.insert(i,1)
             #   print(j[i])
            else:
                j.insert(i,0)
       
            for friend in friends:
                if author == friend and author != user:
                    j[i]=j[i]+1     
        for i in range(photo.count(),recipe.count()+photo.count()):
            #print(i)
            cuisine=recipe[i-photo.count()].cuisine
            #print(cuisine)
            if cuisine==userinfo.favourite_cuisine :
                j.insert(i,1)
             #   print(j[i])
            else:
                j.insert(i,0)
            for friend in friends:
                if author == friend :
                    j[i]=j[i]+1
    if request.is_ajax():
        print("reach")
        obj=request.GET.get('feedobj')
        print('wow')
        print(obj)
        if request.GET.get('storytype')=="photo":
            lastobj=Photo.objects.get(id=obj)
        else:
            lastobj=Recipe.objects.get(id=obj)
        print("kii")
        print(lastobj.on)
        time=lastobj.on
        photo=Photo.objects.all().filter(on__lte=time)
        recipe=Recipe.objects.all().filter(on__lte=time)        
        data=sorted(
    chain(photo,recipe),
    key=lambda instance: instance.on,reverse=True)
        print(len(data))
        form3=photoForm()
        user=request.user
        reportform=ReportphotoForm()
        reportformrec=ReportrecipeForm()
        if len(data)<=0:
        #obj1=get_object_or_404(Comment,pk=1)
    #context = RequestContext(request,{'item_list':data ,'form3' : form3,'user':user,'obj':obj1,'reportform':reportform})    
            #rendered = "<p>No more stories</p>"
            return HttpResponse("<p>No more stories</p>", content_type="text/plain")
        else:
            rendered = render_to_string('content.html',{"item_list":data[1:6],'form3':form3,'user':user,'reportform':reportform,'reportformrec':reportformrec,'home':True})
            return HttpResponse(rendered)
            
    else: 
            #if count>=6:
        feed=[]
        count=0
        for i in range(photo.count()):
            
            if j[i]>=1:
                feed.insert(count,photo[i])
                count=count+1
        for i in range(photo.count(),recipe.count()+photo.count()):
            if j[i]>=1:
                feed.insert(count,recipe[i-photo.count()])
                count=count+1
        form3=photoForm()
        data=sorted(
    feed,
    key=lambda instance: instance.on,reverse=True)
#        obj=get_object_or_404(Comment,pk=1)
        reportform=ReportphotoForm()
        reportformrec=ReportrecipeForm()
        recipeform=RecipeForm()
        #l=len(feed)-1
        if len(feed)>0:
            lastobj=feed[-1]                         
            time=lastobj.on
            photoaja=Photo.objects.all().filter(on__lte=time)
            recipeaja=Recipe.objects.all().filter(on__lte=time)
            myfeed=sorted(
    chain(data,photoaja,recipeaja),
    key=lambda instance: instance.on,reverse=True)
            return render(request,'home.html',{"item_list":set(myfeed[:5]),'form3' : form3,'user':user,'reportform':reportform,'form2':recipeform,'reportformrec':reportformrec,'home':True})        
        else:
            data=sorted(
    chain(photo,recipe),
    key=lambda instance: instance.on,reverse=True)
            form3=photoForm()
       # obj=get_object_or_404(Comment,pk=1)
            reportform=ReportphotoForm()
            reportformrec=ReportrecipeForm()
            return render(request,'home.html',{"item_list":set(data[:5]),'form3' : form3,'user':user,'reportform':reportform,'reportformrec':reportformrec,'home':True})      
            
              


def photosort(request):
    userphoto=Photo.objects.filter(by=request.user)
    userrecipe=Recipe.objects.filter(by=request.user)
    data=sorted(
    chain(userphoto, userrecipe),
    key=lambda instance: instance.on,reverse=True)
    user=request.user
    return render(request,'home.html',{"item_list":data,'user':user,'userphoto':True})         

def addphoto(request):
    print("here")
    print(request)
    if request.method == 'POST':
        form = photoForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            print("Hey")
            
            photo=form.save(commit=False)
            photo.by = MyUser.objects.get(username=request.user.username)
            photo.save()
            print(photo.id)
            pat=re.compile(r"#(\w+)")
            tag=pat.findall(photo.description)
            #desc=photo.description
            #desc=desc.replace(str(pat),'<a href="tagsearch/?q=">tag</a>')
            #print(desc)
            #photo.description=desc
            print(len(tag))
            print(tag)
            for index in range(len(tag)):
                found=HashTag.objects.filter(name = tag[index])
                print(found)
                if not found:
                    hash=HashTag(name=tag[index])
                    hash.count+=1
                    hash.save()
                    print(hash.name)
                    link='<a class="chip" href="/tagsearch/?q='+ hash.name + '">' + hash.name + '</a>'
                    print(link)
                    print("oye")
                    photo.description=photo.description.replace(hash.name,link)
                    photo.save()
                    print(photo)
                    photo_added=get_object_or_404(Photo,pk=photo.id)
                    photo_added.hash_tags.add(hash)
					
                else:
                    photo_added=get_object_or_404(Photo,pk=photo.id)
                    hash=HashTag(name=tag[index])
                    link='<a class="chip" href="/tagsearch/?q='+ hash.name + '">' + hash.name + '</a>'
                    print(link)
                    print("toye")
                    photo.description=photo.description.replace(hash.name,link)
                    photo.save()
                    photo_added.hash_tags.add(HashTag.objects.get(name = tag[index]))
                    foundtag=HashTag.objects.get(name = tag[index])
                    foundtag.count=foundtag.count+1
				
            return redirect('/userphoto/')
    return redirect('/home/')




class PusherCommentMixin(PusherMixin):
    pusher_event_name = "comment"

@login_required	
@require_http_methods(["POST"])
def addcomment(request):
    print("booo")
    if request.method == 'POST':
        if(request.POST.get('text')):
            print("hooo")
            photo1=get_object_or_404(Photo,pk=request.POST.get('photo'))
            user=MyUser.objects.get(username=request.user.username)
            texty=request.POST.get('text')
            photoId=photo1.id
            comment=Comment(by=user,photo=photo1,text=texty)
            comment.save()
            return HttpResponse()
        else:
            return HttpResponse('<p>Please enter some text</p>')
        
    else:
        return HttpResponse('<p>Page not found</p>')
           # def render_to_response(self, context, **response_kwargs):

            #    channel = photo1.format(pk=self.object.pk)
             #   event_data = {'user': self.request.user.username}
              #  pusher.trigger(
               # [channel, ], 
                #"comment", 
                #event_data
                #)

                #return super(addcomment, self.render_to_response(context, **response_kwargs)
    #return HttpResponse()
def addcomment_recipe(request):
    print("booo")
    if request.method == 'POST':
        if(request.POST.get('text')):
            print("hooo")
            recipe1=get_object_or_404(Recipe,pk=request.POST.get('recipe'))
            user=MyUser.objects.get(username=request.user.username)
            texty=request.POST.get('text')
            recipeId=recipe1.id
            print("heyy")
            comment=Recipe_Comment(by=user,recipe=recipe1,text=texty)
            print(comment)
            comment.save()
            return HttpResponse()
        else:
            return HttpResponse()
            

@login_required                       
def addrecipe(request):
    if request.method=='POST':
        print("heyy")
        recipe_form=RecipeForm(request.POST , request.FILES)
        print("keyy")
        if recipe_form.is_valid():
                print("jii")
                recipe=recipe_form.save(commit=False)
                recipe.by=MyUser.objects.get(username=request.user.username)
                recipe.save()
                recipe=Recipe.objects.all()
                return redirect('/userphoto/')
@login_required                         
def user_recipe(request):
    if request.method=='GET':
        recipe=Recipe.objects.filter(by=request.user)
        recipe_form=RecipeForm()                 
        return render(request,'recipe.html',{'recipe' : recipe,'recipe_form':recipe_form})
    

		
@login_required	
def pinlist(request):
    user=request.user
    pinnedphoto=user.photos_pinned.all()
    pinnedrecipe=user.recipe_pinned.all()
    pinned=sorted(
    chain(pinnedphoto,pinnedrecipe),
    key=lambda instance: instance.on)
    return render(request,'home.html',{"item_list":pinned,'user':user})
    
    
@login_required   
def recipelist(request):
    if request.method=='GET':
        recipe=Recipe.objects.all()
        recipe_form=RecipeForm()
        return render(request,'recipe.html',{'recipe' : recipe,'recipe_form':recipe_form})
    

                             
                             
def thanks(request):
	return render(request,'thanku.html')


    
	
@login_required
def vote(request):
    photo=get_object_or_404(Photo,pk=request.POST.get('photo'))
    photo.points+=1
    photo.save()
    print("hii")
    user=request.user
    user.photos_liked.add(photo)
    user.save()
    result=photo.points
    return HttpResponse(result) 

@login_required
def voterecipe(request):
    print("yeaa")
    recipe=get_object_or_404(Recipe,pk=request.POST.get('recipe'))
    recipe.points+=1
    recipe.save()
    print("hii")
    user=request.user
    user.recipe_liked.add(recipe)
    print("biii")
    user.save()
    result=recipe.points
    return HttpResponse(result) 



	
@login_required
def pin_photo(request):
    photo=get_object_or_404(Photo,pk=request.POST.get('photo'))
    photo.pin_points+=1
    photo.save()
    print("hii")
    user=request.user
    user.photos_pinned.add(photo)
    user.save()
    result=photo.pin_points
    return HttpResponse(result) 

@login_required
def pin_recipe(request):
    recipe=get_object_or_404(Recipe,pk=request.POST.get('recipe'))
    recipe.pin_points+=1
    recipe.save()
    print("hii")
    user=request.user
    user.recipe_pinned.add(recipe)
    user.save()
    result=recipe.pin_points
    return HttpResponse(result) 

		
@login_required
def delete_photo(request):
	photo=get_object_or_404(Photo,pk=request.POST.get('photo'))
    if photo.by==request.user:
        photo.delete()
        return HttpResponse()
	return HttpResponse()

@login_required
def delete_recipe(request):
    print("hoo")
    recipe=get_object_or_404(Recipe,pk=request.POST.get('recipe'))
    print("boo")
    print(recipe)
    if recipe.by==request.user:
        recipe.delete()
        return HttpResponse()
    print("Wow")
    return HttpResponse()



@login_required
@require_http_methods(["POST"])
def reportphoto(request):
    print(request.POST)
    photo=get_object_or_404(Photo,pk=request.POST.get('photo_id'))
    user=request.user
    #user.photos_reported.add(photo)
    #user.save()
    reportform=ReportphotoForm(request.POST)
    print(reportform)
    if reportform.is_valid():
        print("jii")
        report=reportform.save(commit=False)
        rep=Report_Photo(reason=report.reason,reportedby=user,photo=photo)
        rep.save()
        #report=reportform.save(commit=False)
        #report.by=request.user
        #report.photo=photo
        print("lii")
        #report.save()
        print("hogya")
        return redirect('/home/')
    

@login_required
@require_http_methods(["POST"])
def reportrecipe(request):
    print(request.POST)
    #recipe=Recipe.objects.get(pk=request.POST.get('recipe_id'))
    print("done")
    recipe=get_object_or_404(Recipe,pk=request.POST.get('recipe_id'))
    user=request.user
    #user.photos_reported.add(photo)
    #user.save()
   # r=request.POST.get('reason')
#    data={'reason':'r'}
 #   print(r)
    reportform=ReportrecipeForm(request.POST)
    print(reportform)
    if reportform.is_valid():
        print("jii")
        report=reportform.save(commit=False)
        report.by=MyUser.objects.get(username=request.user.username)
        report.recipe=recipe
        print("lii")
        report.save()
        print("hogya")
        return HttpResponseRedirect('/home/')







#class PusherMixin(object):

 #   def render_to_response(self, context, **response_kwargs):

  #      channel = "{model}_{pk}".format(
   #         model=self.object._meta.model_name,
   #         pk=self.object.pk
     #   )
      #  event_data = self.__object_to_json_serializable(self.object)      
#
 #       pusher = Pusher(app_id=settings.PUSHER_APP_ID,
  #                      key=settings.PUSHER_KEY,
   #                     secret=settings.PUSHER_SECRET)
    #    pusher.trigger(
   #         [channel, ],
    #        self.pusher_event_name,
     #       event_data
      #  )
#
        #return super(PusherMixin, self).render_to_response(context, **response_kwargs)    
 #       def __object_to_json_serializable(self, object):
  #      model_dict = model_to_dict(object)
   #     json_data = json.dumps(model_dict, cls=DjangoJSONEncoder)
    #    data = json.loads(json_data)
     #   return data
    
