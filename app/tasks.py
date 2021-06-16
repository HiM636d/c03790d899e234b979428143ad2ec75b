from __future__ import absolute_import, unicode_literals
from celery import shared_task
import matplotlib.pyplot as plt
import numpy as np



            

@shared_task()
def get_plt(id):
    allowed_symbols=['t','1','2','3','4','5','6','7','8','9','0','+','-','*','/']
    f=function.objects.get(id=id)

    #checks to make sure the function entered is in valid format to avoid "injections" caused by eval()
    if all(c in allowed_symbols for c in f.function):
        date_now=datetime.now()
        
        from_date= datetime.now()-timedelta(days=f.interval) 
        #evaluating the variable t in seconds
        t= (date_now-from_date).total_seconds()
        # turning the function from string into real calculable function withthe t variable replaced with value
        y=eval(f.function)



        #plotting the chart in houurs
        fig=plt.figure()
        x=np.arange(0,t/3600,f.steps)
        y=(eval(f.function)/3600)
        plt.plot(x,y)

        #saving picture as id.png
        fig.savefig('./app/images/'+f.id+'.png')

        #populating the graph image field with the suitable png
        f.graph='./app/images/'+f.id+'.png'
        f.save()


    #in case the function is in wrong format,an error is returned    
    f.graph='./app/images/error.png'
    f.save()