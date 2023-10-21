from django.urls import path, include
from .views import *

urlpatterns = [   
    #Start home page for login and signup paths =====================================
    path('', home , name='home'),
    #End home page for login and signup paths =======================================

    #Start register page for signup as customer or translators paths ================
    path('register/', index, name='signUp'),
    #Start register page for signup as customer or translators paths ================

    #Start of sign up paths =========================================================
    path('customerSignUp', CustomerSignUp_View, name='customer_signup'),
    path('translatorSignUp', TranslatorSignUp_View, name='translator_signup' ),
    #End of sign up paths ===========================================================
    
    #Start of log in paths ==========================================================
    path('login/', login_view, name='login'),
    #End of log in paths ============================================================

    #Start of Home pages paths ======================================================
    path('customerHomePage', CustomerHomePage_View, name='customer_Home_Page'),
    path('translatorHomePage', TranslatorHomePage_View, name='translator_Home_Page' ),
    #End of Home pages paths =========================================================

    #Start of send request to the data paths ==========================================
    path('waitingPage', witePage_View, name = 'w'),
    #End of send request to the data paths ============================================

    #Start machine translation page paths =============================================
    path('ttranslate/', Translatortranslate_app, name='TMachineTranslation'), # Machine translation page
    path('ctranslate/', Customerstranslate_app, name='CMachineTranslation'), # Machine translation page

    #End machine translation page paths ===============================================

    #Start CustomerProfile page paths =============================================
    path('cProfile', CustomerProfile_View, name='CustomerProfile'),
    path('tProfile', TranslatorProfile_View, name='TranslatorProfile'),

    #End CustomerProfile page paths =============================================

    #Start CustomerChat page paths =============================================
    path('Chat', CustomerChat_View, name='CustomerChat'),
    #End CustomerChat page paths =============================================

    #Start TranslatorChat page paths =============================================
    path('TranslatorChat', TranslatorChat_View, name='TranslatorChat'),
    path('<int:room>/', room , name='room'),
    path('checkview', checkview , name='checkview'),
    path('send', send , name='send'),
    path('getMessages/<int:room>/', getMessages, name='getMessages'),
    path('<int:room>/VideoCall', VideoCall, name='VideoCall'),

    path('getRoom',getRoom),
    path('getMassage',getMassage),
    path('getUser',getUser)
    #Start Video Call===========================================================

    #Start payment ============================================
    
]

    

