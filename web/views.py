
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Count
from taggit.models import Tag 

from .models import Categorie, Page, Post,Conatct,Comments
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator
from django.contrib import messages
#html api's
def post_list(request,tag_slug=None):

    category=request.GET.get('category')
    
    
    if category== None:
        posts = Post.published.all()

        paginator = Paginator(posts, 10) # 10 posts in each page
        page = request.GET.get('page')
        try:
           posts = paginator.page(page)
        except PageNotAnInteger:
        # If page is not an integer deliver the first page
           posts = paginator.page(1)
        except EmptyPage:
        # If page is out of range deliver last page of results
           posts = paginator.page(paginator.num_pages)
           
    else:
        posts = Post.objects.filter(category__name=category)
        
    
    categories=Categorie.objects.all()
    tag = None
    if tag_slug:
        posts = Post.published.all()
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    
        
    return render(request,'post_list.html',{'posts':posts,'categories':categories,'tag':tag})
def post_detail(request, slug):
    categories=Categorie.objects.all()
    post=get_object_or_404(Post,slug=slug,status='published')
    
    post.views=post.views + 1
    post.save()
    post_tags_ids = post.tags.values_list('id', flat=True) 
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:6]
    if request.method=='POST':
        
        comment=request.POST['comment']
        slug=request.POST['slug']
        user=request.user
        parentsno=request.POST['ps']
        if parentsno=="":
            comment=Comments(user=user,post=post,comment=comment)
            comment.save()
            messages.success(request,"Your Comment has been successfully posted.")
        else:
            parent=Comments.objects.get(comment_sno=parentsno)
            comment=Comments(user=user,post=post,comment=comment,parent=parent)
            comment.save()
            messages.success(request,"Your Reply has been successfully posted.")
    
        
        return redirect(slug)
    else:
        
        comments=Comments.objects.filter(post=post,parent=None)
        replies=Comments.objects.filter(post=post).exclude(parent=None)

        replydict={}
        for reply in replies:
            if reply.parent.comment_sno not in replydict.keys():
                replydict[reply.parent.comment_sno]=[reply]
            else:
                replydict[reply.parent.comment_sno].append(reply)
                print(replydict)

        
    return render(request, 'post_detail.html',{'categories':categories,'post':post,'comments':comments,'replydict':replydict,'similar_posts':similar_posts})
    
def contact(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        question=request.POST['question']
        if len(fname)<2 or len(email)<3 or len(question)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Conatct(fname=fname, email=email,question=question)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
        contact=Conatct(fname=fname, email=email, lname=lname, question=question)

        contact.save()
        
        

    return render(request,'contact.html')
def search(request):
    query=request.GET['query']
    posts= Post.objects.filter(title__icontains=query)
    params={'posts': posts}
    return render(request, 'search.html', params)
#request api's
def handlesignup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        name=request.POST['name']
        
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('/')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('/')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= name
        myuser.last_name= username
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('/')

    else:
        return HttpResponse("404 - Not found")

def loginhandle(request):
    if request.method=='POST':
        loginusername=request.POST['lusername']
        loginpassword=request.POST['lpass']
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Loged In")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials, Please try again")


    return redirect('/')

def logouthandle(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('/')
def page(request,slug):
    page=get_object_or_404(Page,slug=slug,status='published')

    return render(request,'page.html',{'page':page})






    



         
  
