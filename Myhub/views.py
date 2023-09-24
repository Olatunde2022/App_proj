from django.shortcuts import render,redirect, reverse
from django.contrib import messages
from .models import Blog, Todo
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
# def Index(request):
#     return render(request, 'Myhub/index.html')
def Login(request): 
    if request.method == 'POST':
        form = request.POST
        username = form.get('username')
        password = form.get('password')
        if not username or not password:
            messages.error(request, 'There is error in your login details, kindly check and try again')
            return render(request, 'login.html')
        user_exist = User.objects.filter(username= username).exists()
        if not user_exist:
            messages.error(request, 'username is not exist')
            return render(request, 'Myhub/login.html')      
        user_isvalid = auth.authenticate(username=username, password= password)
        if not user_isvalid:
            messages.error(request, 'Your login details is not correct')
            return render(request, 'Myhub/login.html')
        user = User.objects.get(username=username)
        user = auth.login(request, user)
        messages.success(request, 'login successfully')
        return redirect(reverse( 'homepage'))      
    return render(request, 'Myhub/login.html')

def Logout(request):
    if not request.user.is_authenticated:
        return redirect(reverse('homepage'))
    auth.logout(request) 
    messages.success(request, 'Logout succesfully')
    return redirect (reverse('homepage'))   
    
    
def Home(request):
    blogs = Blog.objects.all()
    todos = Todo.objects.all()
    context = {"blogs": blogs, "todos":todos}
    return render(request, 'Myhub/index.html', context)
    
def Signup(request):
    if request.method =="POST" :
        form = request.POST 
        username = form.get('username') 
        email = form.get('email')  
        password = form.get('password')  
        confirm_password = form.get('confirm_password')
        if not username or not email or not password or not confirm_password:
            messages.error(request,'Imcomplete Details' )
            return render(request, 'Myhub/signup.html')
        if password != confirm_password:
            messages.error(request, 'Passwords are not match')
            return render(request, 'Myhub/signup.html')
        if len(password) < 8:
            messages.error(request, 'Password must be a minimum of 8 character')
            return render(request, 'Myhub/signup.html')
        user_exists = User.objects.filter(username=username).exists()
        if user_exists:
            messages.error(request, 'Username already taken')
            return render(request, 'Myhub/signup.html')
        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            messages.error(request, 'The email address already taken')
            return render(request, 'Myhub/signup.html')
        user = User.objects.create(username=username, email =email, password =password)
        user.set_password(password)
        user.save()
        return redirect(reverse('loginpage'))
    return render(request, 'Myhub/signup.html')
   
   
def product(request, num):
    context = {"num": num}
    return render(request, 'Myhub/products.html', context) 

def createBlog(request): 
    if not request.user.is_authenticated:
        return redirect(reverse('loginpage'))
    if request.method =="POST" :
        form = request.POST
     
        title = form.get('title')
        body = form.get('body')
        image = request.FILES.get('image')
        rating = form.get('rating')
        owner = request.user
        try:
            new_blog = Blog.objects.create(title=title, body=body,image=image, rating=rating, owner=owner)
            new_blog.save()
            messages.success(request, "Your blog has been created succesfully")
            return redirect(reverse('homepage'))
        except:
            messages.error(request, "There is incomplete in the form field")
            return render(request, 'Myhub/createblog.html')
        # if not rating or not img:
        #     messages.error(request, "There is imcomplete in the form field")
        #     return render(request, 'Myhub/createblog.html')
        
        # new_blog = Blog.objects.create(title=title, body=body,image=img, rating=rating)
        #     # print(new_blog)
        # new_blog.save()
        # messages.success(request, "Your blog has been created succesfully")
        # return redirect(reverse('loginpage'))
    return render(request, 'Myhub/createblog.html') 

def eachBlog(request,id):
    fetch_blog = Blog.objects.get(id =id)
    print(f'The blog title: {fetch_blog.title}')
    context={"item": fetch_blog}
    return render(request, 'Myhub/ojekab_blog.html', context)

def editBlog(request, id):
    if not request.user.is_authenticated:
        return redirect(reverse('loginpage'))
    blog_exist = Blog.objects.filter(id=id).exists()
    if not blog_exist:
        messages.error(request, 'Blog is not found')
        return redirect(reverse('homepage'))
    blog_obj = Blog.objects.get(id=id)
    if request.user !=blog_obj.owner:
        messages.error(request, 'Unathorized action')
        return redirect(reverse('homepage'))
    context ={"blog": blog_obj}
    return render(request, 'Myhub/editblog.html', context)


def MyTodo(request):
    if not request.user.is_authenticated:
        return redirect(reverse('loginpage'))
    owner = request.user
    if request.method == 'POST':
        form = request.POST                
        title =form.get('title')
        date = form.get('date')
        body = form.get('body')
        scale_of_importance = form.get('scale')       
        try:
            new_todo = Todo.objects.create(title=title, date=date, body=body,owner=owner, scale_of_importance=scale_of_importance)
            new_todo.save()
            message= messages.success(request, "New Todo has been created succesfully")
            print(message)
            return redirect(reverse('homepage'))
        except:
            messages.error(request, "There is an empty field, kindly check")
            return render(request, 'Myhub/createTodo.html')
    
        # if not body :
        #     messages.error(request, "There is imcomplete in the form field")
        #     return render(request, 'Myhub/createTodo.html')
        
        # new_todo = Todo.objects.create(title=title, date=date, body=body, scale=scale_of_importance)
        #     # print(new_blog)
        # new_todo.save()
        # messages.success(request, "Your todo has been created succesfully")
        # return redirect(reverse('loginpage'))
    return render(request, 'Myhub/createTodo.html')



def eachTodo(request, id):
    fetch_todo = Todo.objects.get(id=id)
    print(f'The todo title: {fetch_todo.title}')
    context={"item": fetch_todo}
    return render(request, 'Myhub/todopage.html', context)
