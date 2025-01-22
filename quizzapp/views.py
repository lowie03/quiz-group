<<<<<<< HEAD
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

from .forms import CreateUserForm

from django.http import HttpResponse

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def game(request):
    return render(request, 'game.html')

@login_required(login_url='login')
def end(request):
    return render(request, 'end.html')

@login_required(login_url='login')
def highscores(request):
    return render(request, 'highscores.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else: 
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')


        context = {'form':form}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else: 
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
=======
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views import View
# from .forms import CreateUserForm
# from .game import QuizGame

# class GameView(LoginRequiredMixin, View):
#     login_url = 'login'

#     def get(self, request):
#         game = QuizGame()
#         game.fetch_questions()
#         context = {'questions': game.questions}
#         return render(request, 'game.html', context)
    
# class BaseView(View):
#     def get(self, request):
#         return render(request, self.template_name)

# class IndexView(LoginRequiredMixin, BaseView):
#     login_url = 'login'
#     template_name = 'index.html'

# class GameView(LoginRequiredMixin, BaseView):
#     login_url = 'login'
#     template_name = 'game.html'

# class EndView(LoginRequiredMixin, BaseView):
#     login_url = 'login'
#     template_name = 'end.html'

# class HighscoresView(LoginRequiredMixin, BaseView):
#     login_url = 'login'
#     template_name = 'highscores.html'

# class RegisterView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('index')
#         form = CreateUserForm()
#         return render(request, 'register.html', {'form': form})

#     def post(self, request):
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, 'Account was created for ' + user)
#             return redirect('login')
#         return render(request, 'register.html', {'form': form})

# class LoginView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('index')
#         return render(request, 'login.html')

#     def post(self, request):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#         messages.info(request, 'Username or password is incorrect')
#         return render(request, 'login.html')

# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return redirect('login')
    



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import CreateUserForm
from .game import QuizGame

class BaseView(View):
    template_name = ''

    def get_template_name(self):
        return self.template_name

    def get_context_data(self, request):
        return {}

    def get(self, request):
        context = self.get_context_data(request)
        return render(request, self.get_template_name(), context)

class IndexView(LoginRequiredMixin, BaseView):
    login_url = 'login'
    template_name = 'index.html'

    def get_context_data(self, request):
        # Add any context data specific to the index view
        return {}

class GameView(LoginRequiredMixin, BaseView):
    login_url = 'login'
    template_name = 'game.html'

    def get_context_data(self, request):
        game = QuizGame()
        game.fetch_questions()
        return {'questions': game.questions}

class EndView(LoginRequiredMixin, BaseView):
    login_url = 'login'
    template_name = 'end.html'

    def get_context_data(self, request):
        # Add any context data specific to the end view
        return {}

class HighscoresView(LoginRequiredMixin, BaseView):
    login_url = 'login'
    template_name = 'highscores.html'

    def get_context_data(self, request):
        # Add any context data specific to the highscores view
        return {}

class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        form = CreateUserForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
        return render(request, 'register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        messages.info(request, 'Username or password is incorrect')
        return render(request, 'login.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')



# from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm

# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages

# from django.contrib.auth.decorators import login_required

# # Create your views here.

# from .forms import CreateUserForm

# from django.http import HttpResponse

# @login_required(login_url='login')
# def index(request):
#     return render(request, 'index.html')

# @login_required(login_url='login')
# def game(request):
#     return render(request, 'game.html')

# @login_required(login_url='login')
# def end(request):
#     return render(request, 'end.html')

# @login_required(login_url='login')
# def highscores(request):
#     return render(request, 'highscores.html')

# def registerPage(request):
#     if request.user.is_authenticated:
#         return redirect('index')
#     else:
#         form = CreateUserForm()

#         if request.method == 'POST':
#             form = CreateUserForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 user = form.cleaned_data.get('username')
#                 messages.success(request, 'Account was created for ' + user)

#                 return redirect('login')
#         context = {'form':form}
#         return render(request, 'register.html', context)

# def loginPage(request):
#     if request.user.is_authenticated:
#         return redirect('index')
#     else: 
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')

#             user = authenticate(request, username = username, password=password)

#             if user is not None:
#                 login(request, user)
#                 return redirect('index')
#             else:
#                 messages.info(request, 'Username or password is incorrect')

#         context = {}
#         return render(request, 'login.html', context)

# def logoutUser(request):
#     logout(request)
#     return redirect('login')


>>>>>>> b1fe81c (updates)
