from django.db import models
from appusers.models import MyUser

# Create your models here.
class HashTag(models.Model):
    name = models.CharField(max_length = 100)
    count = models.IntegerField(default = 0)
    def __str__(self):
        return '#' + self.name
    
class Recipe(models.Model):
    cuisine_choices = (
    ("African","African"),("American","American"),("Argentinian","Argentinian"),("Brazilian","Brazilian"),("Cajun","Cajun"),("Caribbean","Caribbean"),("Chinese","Chinese"),("Cuban","Cuban"),("EastIndian","EastIndian"),("Egyptian","Egyptian"),("Ethiopian","Ethiopian"),("French","French"),("Filipino","Filipino"),("German","German"),("Greek","Greek"),("Hawaiian","Hawaiian"),("Indonesian","Indonesian"),("Italian","Italian"),("Iranian","Iranian"),("Irish","Irish"),("Japanese","Japanese"),("Korean","Korean"),("Lebanese","Lebanese"),("Mediterranean","Mediterranean"),("Mexiacan","Mexiacan"),("Mongolian","Mongolian"),("Mughlai","Mughlai"),("NorthIndian","NorthIndian"),("Polish","Polish"),("Portuguese","Portuguese"),("Scottish","Scottish"),("SeaFood","SeaFood"),("Spanish","Spanish"),("SouthIndian","SouthIndian"),("Swedish","Swedish"),("Thai","Thai"),("Turkish","Turkish"),("Vietnamese","Vietnamese"),("WestIndian","WestIndian"),
    
    )
    by=models.ForeignKey(MyUser)
    photo=models.ImageField(upload_to='recipe_images/')
    on=models.DateTimeField(auto_now_add = True)
    cuisine=models.CharField(max_length=30,choices=cuisine_choices,default='none')
    title=models.TextField(max_length=100)
    likers = models.ManyToManyField(MyUser, related_name = 'recipe_liked')
    pinners=models.ManyToManyField(MyUser,related_name='recipe_pinned',blank=True)
    reporters=models.ManyToManyField(MyUser,related_name='recipes_reported',through='Report_Recipe')
    pin_points=models.IntegerField(default=0)
    points=models.IntegerField(default=0)
    ingredients=models.TextField(max_length=1000)
    method=models.TextField(max_length=2000)
    prep_time=models.DurationField(null=True,blank=True)
    cook_time=models.DurationField()

    
    def __str__(self):
        return self.title

    
class Report_Recipe(models.Model):
    by=models.ForeignKey(MyUser,related_name='reported_recipe',on_delete=models.CASCADE)
    on=models.DateTimeField(auto_now_add = True)
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    report_reasons = (
        ('This recipe is a spam or a scam', 'This recipe is spam or a scam'),
        ('This recipe puts people at risk', 'This recipe puts people at risk'),
        ("This recipe shouldn't be on foodchaps", "This recipe shouldn't be on foodchaps"),
    )
    reason=models.CharField(max_length=40,choices=report_reasons,default="none")
    def __str__(self):
        return self.reason

   
    
class Photo(models.Model):
    cuisine_choices = (
    ("African","African"),("American","American"),("Argentinian","Argentinian"),("Brazilian","Brazilian"),("Cajun","Cajun"),("Caribbean","Caribbean"),("Chinese","Chinese"),("Cuban","Cuban"),("EastIndian","EastIndian"),("Egyptian","Egyptian"),("Ethiopian","Ethiopian"),("French","French"),("Filipino","Filipino"),("German","German"),("Greek","Greek"),("Hawaiian","Hawaiian"),("Indonesian","Indonesian"),("Italian","Italian"),("Iranian","Iranian"),("Irish","Irish"),("Japanese","Japanese"),("Korean","Korean"),("Lebanese","Lebanese"),("Mediterranean","Mediterranean"),("Mexican","Mexican"),("Mongolian","Mongolian"),("Mughlai","Mughlai"),("NorthIndian","NorthIndian"),("Polish","Polish"),("Portuguese","Portuguese"),("Scottish","Scottish"),("SeaFood","SeaFood"),("Spanish","Spanish"),("SouthIndian","SouthIndian"),("Swedish","Swedish"),("Thai","Thai"),("Turkish","Turkish"),("Vietnamese","Vietnamese"),("WestIndian","WestIndian"),
    
    )
    image = models.ImageField(upload_to = 'uploads/')
    place=models.CharField(max_length = 100,default='none')
    by = models.ForeignKey(MyUser, related_name = 'photos_uploaded')
    on = models.DateTimeField(auto_now_add = True)
    description = models.TextField(max_length = 120, null = True)
    likers = models.ManyToManyField(MyUser, related_name = 'photos_liked')
    reporters=models.ManyToManyField(MyUser,related_name='photos_reported',through='Report_Photo')
    cuisine=models.CharField(max_length=30,choices=cuisine_choices,default='none')
    pinners=models.ManyToManyField(MyUser,related_name='photos_pinned',blank=True)
    pin_points=models.IntegerField(default=0)
    points=models.IntegerField(default=0)
    user_tags = models.ManyToManyField(MyUser, related_name = 'photos_tagged_in')
    hash_tags = models.ManyToManyField(HashTag,related_name='tagged_photos')
    public=models.BooleanField(default=True)
	
    def __str__(self):
        return self.description
    
         
class Report_Photo(models.Model):
    reportedby=models.ForeignKey(MyUser,related_name='reported_photo',on_delete=models.CASCADE)
    photo=models.ForeignKey(Photo,on_delete=models.CASCADE)
    on=models.DateTimeField(auto_now_add = True)
    report_reasons = (
        ('This photo is a spam or a scam', 'This photo is spam or a scam'),
        ('This photo puts people at risk', 'This photo puts people at risk'),
        ("This photo shouldn't be on foodchaps", "This photo shouldn't be on foodchaps"),
    )
    reason=models.CharField(max_length=30,choices=report_reasons,default='none')
    def __str__(self):
        return self.reason        
   #class Meta:
        #auto_created = True
    
 
        
  
    
    

class Comment(models.Model):
    by = models.ForeignKey(MyUser)
    photo = models.ForeignKey(Photo)
    on = models.DateTimeField(auto_now_add = True)
    text = models.CharField(max_length = 100)

    def __str__(self):
        return self.text



class Recipe_Comment(models.Model):
    by = models.ForeignKey(MyUser)
    recipe = models.ForeignKey(Recipe)
    on = models.DateTimeField(auto_now_add = True)
    text = models.CharField(max_length = 100)

    def __str__(self):
        return self.text    

    



    
    
    
    
#class Pinned_Photo(models.Model):
#    by=models.ForeignKey(MyUser)
   # photo=models.ForeignKey(Photo)
  #  on=models.DateTimeField(auto_now_add = True)
 #   points=models.IntegerField(default=0)
    
#class Pinned_Recipe(models.Model):
    #by=models.ForeignKey(MyUser)
    #recipe=models.ForeignKey(Recipe)
    #on=models.DateTimeField(auto_now_add = True)    
    #points=models.IntegerField(default=0)
