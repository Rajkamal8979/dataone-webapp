from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import generics
from .models import *
from .serializers import *
from webapp.forms import userform
# class directorlist(APIView):
#     def get(self,request):
#         director1=director.objects.all()
#         serializer=directorserializer(director1,many=True)
#         return Response(serializer.data)

# class leadactorslist(APIView):
#     def get(self,request):
#         actor=leadactors.objects.all()
#         serializer=leadactorsserializer(actor,many=True)
#         return Response(serializer.data)
def delete_movie(request,id):
    #pk=request.id
    mov=movie.objects.get(id=id)
    mov.delete()
    return redirect("movie")

def edit_movie(request,id):
    mov = get_object_or_404(movie, pk=id)
    if request.method == "POST":
        form = userform(request.POST, instance=mov)
        if form.is_valid():
            mov = form.save(commit=False)
            mov.save()
            return redirect("movie")
    else:
        form = userform(instance=mov)
    return render(request, 'webapp/create.html', {'form': form})
    # #pk=request.id
    # mov=movie.objects.get(id=id)
    # #mov.delete()
    # return redirect("new")

def details(request):
	details= movie.objects.all()
    #actor=movie.actors.all()
	return render(request,'webapp/list.html',{'movie':details})

class movielist(generics.ListCreateAPIView):
    #def get(self,request):
    queryset=movie.objects.all()
    #serializer=movieserializer(movies,many=True)
    serializer_class=movieserializer
        #return Response(serializer.data)
class directorlist(generics.ListCreateAPIView):
    #def get(self,request):
    queryset=director.objects.all()
    #serializer=movieserializer(movies,many=True)
    serializer_class=directorserializer
class leadactorslist(generics.ListCreateAPIView):
    #def get(self,request):
    queryset=leadactors.objects.all()
    #serializer=movieserializer(movies,many=True)
    serializer_class=leadactorsserializer


def test(request):
    if request.method=='POST':
        form=userform(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m()
            return redirect("movie")
    else:
        form=userform()
        context = {"form": form}
    #     #return HttpResponse("Saved")
    # # else:
    return  render(request, 'webapp/create.html',context)
    #       'form': userform(),
    #       })





# Create your views here.
