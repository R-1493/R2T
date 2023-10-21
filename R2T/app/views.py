from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerSignUpForm, TranslatorSignUpForm, LoginForm
from.models import Customer, Appointment, User, Translatorr , Product
from django.contrib.auth import login
import json
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views import View
#====================================================================================================
#Star home page View
#====================================================================================================
def home(request):
    return render(request,'Pages/Home.html')#for show the log in or sign up choice page 
#====================================================================================================
#End home page View
#====================================================================================================

'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''

#====================================================================================================
#Start signUp View
#====================================================================================================

def index(request):
    return render(request,'Pages/SignUp.html')

#====================================================================================================
#End signUp View
#====================================================================================================
'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''

#====================================================================================================
#Start CustomerProfile View
#====================================================================================================

def CustomerProfile_View(request):
    return render(request,'Customers/Profile.html')

def TranslatorProfile_View(request):
    return render(request,'Translator/Profile.html')

#====================================================================================================
#End CustomerProfile View
#====================================================================================================

'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% '''

#====================================================================================================
#Start CustomerProfile View
#====================================================================================================

def CustomerChat_View(request):
    return render(request,'Pages/CustomerChat.html')

#====================================================================================================
#End CustomerProfile View
#====================================================================================================

'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% '''

#====================================================================================================
#Star sign Up View
#====================================================================================================
#**Start customer and translator sign up View  the are the same code it for going to deffrent forms **
def CustomerSignUp_View(request):
    form=CustomerSignUpForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user=form.save()
        login(request, user)
        return redirect('customer_Home_Page')
    return render(request,'Customers/SignUp.html', {'form':form})

def TranslatorSignUp_View(request):
    form=TranslatorSignUpForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user=form.save()
        login(request, user)
        return redirect('translator_Home_Page')
    return render(request,'Translator/SignUp.html', {'form':form})
#====================================================================================================
#End sign Up View
#====================================================================================================

'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''

#====================================================================================================
#Star Hame Pages View
#====================================================================================================
#***************************The has same functiond put the go to deffrent Html **********************

def CustomerHomePage_View(request):    
    if request.method == 'POST':
        Second_Language = request.POST.get('textfield', None)
        try:
            pro=Translatorr.objects.filter(Second_Language=Second_Language)
            x={'pro': pro}  
            return render(request,'Homes/representationOfTranslators.html', x)#for show the customer Home page                         
        except Translatorr.DoesNotExist :
            return HttpResponse("no such user")
    else:
        return render(request, 'Customers/HomePage.html')

def TranslatorHomePage_View(request):
    return render(request,'Translator/HomePage.html')#for show the customer Home page 
#====================================================================================================
#End Hame Pages View
#====================================================================================================

'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''

#====================================================================================================
#Star Send request View
#====================================================================================================

def witePage_View(request):
        return render(request,'Homes/whitePage.html')

#====================================================================================================
#End Send request View
#====================================================================================================

'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% '''

#====================================================================================================
#Star log in view
#====================================================================================================
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
def login_view(request):
    model=User
    template_name='login.html'
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            formm = LoginForm(request.POST or None)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_customer:
                login(request, user)
                return redirect('customer_Home_Page')
            elif user is not None and user.is_translator:
                login(request, user)
                return redirect('translator_Home_Page')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    else:
        form = AuthenticationForm()
    return render(request, 'Pages/Login.html', {'form': form})
#====================================================================================================
#End log in view
#====================================================================================================

'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% '''

#====================================================================================================
#Start Machine translation
#====================================================================================================

def Translatortranslate_app(request):
      return render(request, 'Translator/translate.html')

def Customerstranslate_app(request):
      return render(request, 'Customers/translate.html')

#====================================================================================================
#End Machine translation
#====================================================================================================

#====================================================================================================
#Start Session
#====================================================================================================
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RoomSerializer,MessageSerializer, UserSerializer
from django.shortcuts import render, redirect
from .models import Room, Message 
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
import random
import time

def CustomerChat_View(request):
    translators = User.objects.filter(is_translator=True)
    print(translators)
    return render(request,'Customers/ChatList.html',{'translators':translators})

def TranslatorChat_View(request):
       customers =User.objects.filter(is_customer=True)
       print(customers)
       return render(request,'Translator/ChatList.html',{'customers':customers})
   
def room(request, room):
    room_details = Room.objects.get(roomID=room)
    current_user  = request.user 
    currentuser_typeT = current_user.is_translator # if the user is translator 
    currentuser_typeC = current_user.is_customer # if the user iscustomer 
    username = request.GET.get('username')
    if currentuser_typeT:
       receiver = room_details.customer
    elif currentuser_typeC:
       receiver = room_details.translator
    return render(request, 'Pages/Room.html', {
        'receiver':receiver,
        'username': username,
        'room': room,
        'room_details': room_details
    })
#-------------------------------------------
#check for user AND Customer
#-------------------------------------------
def checkview(request ):
    listID = request.POST['list_id']
    uselistname = User.objects.get(id = listID)
    userlist = uselistname.username
    current_user  = request.user #to get the user
    currentuser = current_user.username #for storing user NAME
    currentuser_typeT = current_user.is_translator # if the user is translator 
    currentuser_typeC = current_user.is_customer # if the user iscustomer 
    #for storing user id as str
    fiId = str(current_user.id)
    if currentuser_typeT:#chacks if the user iscustomer 
        translator = current_user.username
        room = fiId #14
        room =room + listID #13
       # print('\n\ntranslator', currentuser_typeT,'\n')
        if Room.objects.filter(roomID=room).exists():
            return redirect('/'+room+'/')
        #the creat will not be her it gona be when the reacust finsh
        else:
            new_room = Room.objects.create(roomID=room , translator=translator , customer = userlist)
            new_room.save()
            return redirect('/'+room+'/')
    elif currentuser_typeC: # if the user is translator
        customer = current_user.username
        room = listID #14
        room =room +fiId #13
        #print('\ncustomer', currentuser_typeC,'\n\n')
        if Room.objects.filter(roomID=room).exists():
            return redirect('/'+room+'/')
        #the creat will not be her it gona be when the reacust finsh
        else:
            new_room = Room.objects.create(roomID=room ,customer=customer , translator=userlist )
            new_room.save()
            return redirect('/'+room+'/')

def send(request ):
    message = request.POST['message']
    current_user = request.user
    username = current_user.username
    room_id = request.POST['room_id']
    new_message = Message.objects.create(value=message, sender=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    room_details = Room.objects.get(roomID=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

def VideoCall(request, room ):
    room_details = Room.objects.get(roomID=room)
    currentuser  = request.user 
    currentuser_typeT = currentuser.is_translator # if the user is translator 
    currentuser_typeC = currentuser.is_customer # if the user iscustomer 
    if currentuser_typeT:
       receiver = room_details.customer
    elif currentuser_typeC:
       receiver = room_details.translator
    return render(request, 'Pages/VideoCall.html',{'currentuser':currentuser , 'receiver':receiver })


@api_view(['GET'])

def getRoom(requset):
    name = Room.objects.all()
    serializer = RoomSerializer(name , many = True)
    return Response(serializer.data)

@api_view(['GET'])

def getMassage(requset):
    name = Message.objects.all()
    serializer = MessageSerializer(name , many = True)
    return Response(serializer.data)


@api_view(['GET'])

def getUser(requset):
    name = User.objects.all()
    serializer = UserSerializer(name , many = True)
    return Response(serializer.data)


#====================================================================================================
#End Session
#====================================================================================================
