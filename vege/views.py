from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def receipes(request):
    if request.method == "POST":
        data=request.POST
        receipe_name=data.get('receipe_name')
        receip_image=request.FILES.get('receip_image')
        receipe_description=data.get('receipe_description')
    # to save the datat inside this model we use the below method.
        Receipe.objects.create(receip_image=receip_image,
                           receipe_description=receipe_description,
                           receipe_name = receipe_name)
    


        return redirect('/receipes/')
    # after saving this page redirects to this page only.




    queryset=Receipe.objects.all()
    context={'receipes':queryset}
    print(context)
    return render(request, 'receipe.html',context)


def delete_recipe(request,id):
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')
    
def update_recipe(request,id):
    queryset=Receipe.objects.get(id=id)
    context={'receipes':queryset}

    if request.method == "POST":
        data=request.POST
        receipe_name=data.get('receipe_name')
        receip_image=request.FILES.get('receip_image')
        receipe_description=data.get('receipe_description')

        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description
        
        if receip_image:
            queryset.receip_image=receip_image

        queryset.save()
        return redirect('/receipes/')

    return render(request,'update_recipe.html',context)
        