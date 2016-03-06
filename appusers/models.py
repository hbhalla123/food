from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils import timezone
# Create your models here.
class MyUser(AbstractUser):
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
    profile_pic = models.ImageField(upload_to = 'profile_pics/', blank = True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=GENDER_CHOICES[0][0])
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(max_length=15,validators=[phone_regex], blank=True) # validators should be a list
    dob = models.DateField(blank=True, null=True)
    street_address = models.CharField(max_length = 100, null=True, blank=True)
    city = models.CharField( blank=True, null=True, max_length=255)
    pincode = models.CharField(max_length=8, default="0000000")
    following = models.ManyToManyField("self", symmetrical = False, related_name = "followers")
    email_id=models.EmailField(max_length=255)
    #pinned_photo=models.ForeignKey(Pinned_Photo,null=True,blank=True)
    #pinned_recipe=models.ForeignKey(Pinned_Recipe,null=True,blank=True)

    
    def image_tag(self):
        if self.profile_pic:
            return '<img height="40px" width="40px" src="/media/%s">' % self.profile_pic
        else:
            return ''
        image_tag.short_description = 'Image'
        image_tag.allow_tags = 'True'
    
    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "username__icontains", "first_name__icontains", "last_name__icontains")

class UserProfile(models.Model):
    user = models.OneToOneField(MyUser)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=timezone.now())
      
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural=u'User profiles'
		
"""African=0
American=1
Argentinian=2
Brazilian=3
Cajun=4
Caribbean=5
Chinese=6
Cuban=7
EastIndian=8
Egyptian=9
Ethiopian=10
French=11
Filipino=12
German=13
Greek=14
Hawaiian=15
Indonesian=16
Italian=17
Iranian=18
Irish=19
Japanese=20
Korean=21
Lebanese=22   
Mediterranean=23
Mexican=24
Mongolian=25
Mughlai=26
NorthIndian=27
Polish=28
Portuguese=29
Scottish=30
SeaFood=31
Spanish=32
SouthIndian=33
Swedish=34
Thai=35
Turkish=36
Vietnamese=37
WestIndian=38
    """
CUISINES_CHOICES = (
       ("African","African"),("American","American"),("Argentinian","Argentinian"),("Brazilian","Brazilian"),("Cajun","Cajun"),("Caribbean","Caribbean"),("Chinese","Chinese"),("Cuban","Cuban"),("EastIndian","EastIndian"),("Egyptian","Egyptian"),("Ethiopian","Ethiopian"),("French","French"),("Filipino","Filipino"),("German","German"),("Greek","Greek"),("Hawaiian","Hawaiian"),("Indonesian","Indonesian"),("Italian","Italian"),("Iranian","Iranian"),("Irish","Irish"),("Japanese","Japanese"),("Korean","Korean"),("Lebanese","Lebanese"),("Mediterranean","Mediterranean"),("Mexican","Mexican"),("Mongolian","Mongolian"),("Mughlai","Mughlai"),("NorthIndian","NorthIndian"),("Polish","Polish"),("Portuguese","Portuguese"),("Scottish","Scottish"),("SeaFood","SeaFood"),("Spanish","Spanish"),("SouthIndian","SouthIndian"),("Swedish","Swedish"),("Thai","Thai"),("Turkish","Turkish"),("Vietnamese","Vietnamese"),("WestIndian","WestIndian"),
)    
        
class cuisine_choice(models.Model):
    cuisines=models.CharField(choices=CUISINES_CHOICES , max_length=25,default='NorthIndian')
    def __str__(self):
        return self.cuisines
       # choices_dict = dict(CUISINES_CHOICES)
        #return choices_dict[self.cuisines]
    
    
        
class UserInfo(models.Model):
    user=models.OneToOneField(MyUser)
    info=models.CharField(max_length=300 , null=True)
    recommended_dish=models.CharField(max_length=100 ,null=True)
    fav_restro=models.CharField(max_length=100 , null=True)
    disliked_food=models.CharField(max_length=50 ,null=True)
    favourite_cuisine=models.CharField(max_length=30,choices=CUISINES_CHOICES,default='none')
    def __str__(self):
        return self.user.username
	


    
    

class Connection(models.Model):
    user1 = models.ForeignKey(MyUser, limit_choices_to={'is_active': True}, related_name = 'connection_user1')
    user2 = models.ForeignKey(MyUser, limit_choices_to={'is_active': True}, related_name = 'connection_user2')
    
    class Meta:
        unique_together=('user1','user2')
        verbose_name = 'Connection'
        verbose_name_plural = 'Connections'
        
    def __str__(self):
        return self.user2.username	

	
	
	
	

    
		
		