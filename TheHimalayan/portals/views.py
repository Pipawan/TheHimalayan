from django.views.generic import ListView
from django.shortcuts import render
from datetime import datetime
from portals.forms import SignUpForm
from . import forms
from portals.models import Post
from portals.forms import CommentForm, ContactForm,FeedBackForm
from django.contrib.auth.decorators import login_required
from portals.models import Post, PoliticalNewsPost, ScienceNewsPost, InternationalNewsPost, SportsNewsPost, BreakingNewsPost
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect

# Create your views here.


def home_view(request):
    now = datetime.now()
    date_time = now.strftime("%d-%m-%Y %H:%M:%S")
    week_day = now.strftime("%A")
    return render(request, 'portals/home.html', {"date_time": date_time, "week_day": week_day})


def About(request):
    return render(request, 'portals/about.html')


def Breaking_news(request):
    post_list = BreakingNewsPost.objects.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page')
    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'portals/breaking_news.html', {'post_list': post_list})


# def contact(request):
#     return render(request, 'portals/contact.html')


def political_news_view(request):
    post_list = PoliticalNewsPost.objects.all()
    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page')
    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'sub_portals/politics.html', {'post_list': post_list})


def science_news_view(request):
    post_list = ScienceNewsPost.objects.all()
    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page')
    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'sub_portals/science.html', {'post_list': post_list})


def sports_news_view(request):
    post_list = SportsNewsPost.objects.all()
    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page')
    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'sub_portals/sports.html', {'post_list': post_list})


def international_list_view(request):
    post_list = InternationalNewsPost.objects.all()
    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page')
    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'sub_portals/international.html', {'post_list': post_list})


class PostView(ListView):
    model = Post
    paginate_by = 1


def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(Post, status='published',
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    comments = post.comments.filter(active=True)
    csubmit = False
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            csubmit = True
    else:
        form = CommentForm()

    return render(request, 'sub_portals/post_detail.html', {'post': post, 'form': form, 'csubmit': csubmit, 'comments': comments})

# Auth session
def thanks_view(request):
    return render(request, 'aut_h/thanks.html')

@login_required
def contact_view(request):
  form = FeedBackForm()
  if request.method == 'POST':
    form = FeedBackForm(request.POST)
    if form.is_valid():
      print('Validation complete  printing feedback info')
      print("Student Name:", form.cleaned_data['name'])
      print("Student email :", form.cleaned_data['email'])
      print("Student subject :", form.cleaned_data['subject'])
      print("Student message:", form.cleaned_data['message'])
      return thanks_view(request)
  return render(request, 'portals/contact.html', {'form': form})


@login_required
def ok(request):
    return render(request, 'contact.html')


def logout_view(request):
    return render(request, 'aut_h/logout.html')


def login_view(request):
    return render(request, 'aut_h/login.html')


def Signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request, 'aut_h/sign_up.html', {'form': form})
