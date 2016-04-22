from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View 
from django.shortcuts import get_object_or_404
from .forms import PostForm
from .models import Posts 
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Register(View):
	template = "register.html" 

	def get(self,request):

		if request.user.is_authenticated():
			return redirect("index")
		userform = UserCreationForm()
		context = {
			"userform":userform
		}
		return render(request, self.template, context)

	def post(self,request):
		userform = UserCreationForm(data=request.POST)
		if userform.is_valid():
			user = userform.save()
			return redirect("home:login")
		else:
			context = {
				"userform":userform
			}
			return render(request,self.template,context)

class Login(View):
	template = "login.html"

	def get(self,request):
		return render(request,self.template,{})

	def post(self,request):
		if request.user.is_authenticated():
			#messages.warning(request,"You're already logged in.")
			return redirect("index")

		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username,password=password)
		if user:
			if user.is_active:
				login(request,user)
				return redirect("index")
			else:
				return HttpResponse("your account is disabled")
		else:
			return HttpResponse("Invalid details")

class Index(View):
	template = "index.html"
	
	def get(self,request):
		posts_list = Posts.objects.all().order_by('-created_at')
		paginator = Paginator(posts_list, 10)

		page = request.GET.get('page')
		try:
			posts_list = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			posts_list = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			posts_list = paginator.page(paginator.num_pages)
		context = {
				"posts":posts_list
			}
   
		return render(request, self.template, context)

				

class Create(LoginRequiredMixin,View):
	template = "create.html"

	def get(self,request):
		postform = PostForm(initial={'user':request.user})
		context = {
			"form":postform
		}
		return render(request, self.template, context)
		
	def post(self,request):
		postform = PostForm(request.POST)
		# post = Posts.objects.get()
		# post = [p.to_jason() for p in post]
		
		if postform.is_valid():
			new_post = postform.save()
			return redirect("index")
			# return JsonResponse(new_post.to_json())
		# return JsonResponse({'post':post})
		

class Edit(View):
	template = "edit.html"

	def get(self,request,pk):
		news = get_object_or_404(Posts,slug=slug)
		form = PostForm(instance=news)

		context = {
			"form":form,
			"post":news
		}
		return render(request, self.template, context)

	def post(self,request,slug):
		news = get_object_or_404(Posts,slug=slug)
		form = PostForm(request.POST,instance=news)
		if form.is_valid():
			form.save()
			return redirect("index")
		else:
			context = {
				"form":form,
				"post":news
			}
			return render(request, self.template, context)

class Delete(View):
	def post(self,request,slug):
		news = get_object_or_404(Posts,slug=slug)
		news.delete()
		return redirect("index")

@login_required
def user_logout(request):
	# Since we know the user is logged in, we can now just log them out.
	logout(request)

	# Take the user back to the homepage.
	return redirect('index')
		