from django.db import models
from django.conf import settings


# Create your models here.


class Location(models.Model):
    cityImg = models.ImageField(upload_to='cityImg/',
                           
                           width_field='widthField',
                           height_field='heightField')
    heightField = models.IntegerField(default=0)
    widthField = models.IntegerField(default=0)
    city = models.CharField(max_length=120) #choices=CITYNAME)
    state = models.CharField(max_length=120) #choices=STATENAME)
    country = models.CharField(max_length=120)

    def __str__(self):
        return '%s - %s' % (self.city, self.state)

    class Meta:
        unique_together = ('city','state')
        verbose_name_plural = "Location"



class Category(models.Model):
	name = models.CharField(max_length=120, unique=True)
	desc = models.TextField(blank=True)
	catImg = models.FileField(upload_to='catImg/')
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Categories"



class SubCategory(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    desc = models.TextField(blank=True)
    subCatImg = models.FileField(upload_to='subCatImg/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "SubCategories"



class Profile(models.Model):

   
    name = models.CharField(max_length=120, unique=True)
    # slug = models.SlugField(unique=True, blank=True)
    designation = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=120, unique=True)
    dob = models.CharField(max_length=120, unique=True)
    email = models.EmailField(blank=True)
    contact = models.CharField(max_length=14)
    interests = models.CharField(max_length=300)
    profilepic = models.ImageField(upload_to='profilepic/', height_field='heightField', width_field='widthField')
    coverpic = models.ImageField(upload_to='coverpic/', height_field='heightField', width_field='widthField')
    heightField = models.IntegerField(default=0)
    widthField = models.IntegerField(default=0)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    heightField = models.IntegerField(default=0)
    widthField = models.IntegerField(default=0)
  
    def __str__(self):
        return self.name
    class Meta:
    	verbose_name_plural = "Profile"     


# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.name)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Profile.objects.filter(slug=slug).order_by("-id")
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s" %(slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug

