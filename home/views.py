from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


peoples=[
    {
    'name':'raj',
    'age':25,
    'gender':'M'
    },
    {
    'name':'saurabh',
    'age':28,
    'gender':'M'
    },
    {
    'name':'surbhi',
    'age':25,
    'gender':'F'
    }
]

text="""
  Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio nobis aliquid, aspernatur iste fuga temporibus quod dicta maxime ut sit repudiandae explicabo, accusamus blanditiis voluptates? Sunt cupiditate enim et provident delectus a dicta fugit voluptas voluptatem. Quis a adipisci quibusdam nostrum eaque reprehenderit nobis amet perspiciatis inventore, excepturi ullam fugiat deleniti pariatur fuga quisquam? Alias, quas. Vel, magni eveniet ut harum eaque cupiditate sapiente atque reprehenderit fuga dolore deleniti voluptate suscipit quis rerum quae, aliquam pariatur. Cum distinctio tempora, minima accusantium, expedita sit at mollitia nihil facere quis assumenda maiores voluptas molestiae blanditiis, error reprehenderit corporis porro ipsa sint explicabo."""

def home(request):
    return render(request,"index.html",context={'peoples':peoples,'':text})

def success_page(request):
    print("*"*10)
    return HttpResponse("im the success page")