# Create your views here.
from django.shortcuts import render_to_response

#set view default value
def object_list(request,model,template_name="here_it_is"):
    obj_list = model.objects.all();
    return render_to_response(template_name,{'object_list':obj_list})