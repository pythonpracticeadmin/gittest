from django.shortcuts import render, HttpResponseRedirect
from .forms import menform
from .models import menmodel
from .serializer import menmodelapi

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class menapi_view(APIView):
    def get(self, r):
        apidata = menmodel.objects.all()
        menapi = menmodelapi(apidata, many=True)
        return Response(menapi.data)

    def post(self, r):
        serobj = menmodelapi(data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data, status=status.HTTP_201_CREATED)
        return Response(serobj.errors, status=status.HTTP_400_BAD_REQUEST)

class updatedeleteapi(APIView):
    def put(self, r, pk):
        obj = menmodel.objects.get(pk=pk)
        serobj = menmodelapi(obj, data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data, status=status.HTTP_201_CREATED)
        return Response(serobj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, r, pk):
        obj = menmodel.objects.get(pk=pk)
        obj.delete()
        return Response(obj.delete(), status=status.HTTP_200_OK)


def menhome(r):
    return render(r, 'men/men.html')


def men_form(r):
    if r.method == "POST":
        form = menform(r.POST, r.FILES)
        if form.is_valid():
            form.save()
    return render(r, 'men/menform.html', {'form':menform, 'data':menmodel.objects.all})


def mendata(r):
    return render(r, 'men/mendata.html', {'data':menmodel.objects.all()})

def men_update(r, id):
    obj = menmodel.objects.get(id=id)
    if r.method == "POST":
        form = menform(r.POST, r.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/men/data')
    return render(r, 'men/menupdate.html', {'obj':obj})

def men_delete(r, id):
    obj = menmodel.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect('/men/data')


