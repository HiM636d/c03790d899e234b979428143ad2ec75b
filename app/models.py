from django.db import models
from app.tasks import get_plt
from django.db import models
from django.utils.safestring import mark_safe
from datetime import datetime,timedelta
from django.db import transaction
from django.utils.html import mark_safe


class Function(models.Model):

    function= models.CharField(max_length = 50)
    graph= models.ImageField(upload_to="images/", max_length=100,blank=True)
    interval=models.IntegerField(null=True)
    steps=models.IntegerField(null=True)
    updated=models.DateTimeField(auto_now=True)


    #overriding the save() method on transaction.commit, to fire the celery task after save
    def save(self,*args,**kwargs):
       
        transaction.on_commit(lambda : get_plt.delay(self.id))
        #calling the super to carry on with the default save() method
        super(Function,self).save(*args,**kwargs)


        #a function that marks it safe to display graph picture and specifies width/height
        @property
        def graph_preview(self):
            if self.graph:
                return mark_safe('<img src='{}' width='150' height='150' />.format(self.graph.url))
            return ""