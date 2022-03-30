from django.shortcuts import redirect, render
from .models import Product, Category, Comment
from orders.forms import CartAddForm
from .forms import CommentCreateForm, CommentReplyForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required




def product_category_list(request):
    
    context={
        'products': Product.objects.all(),
        'categoris': Category.objects.all(),
        }
    return render(request, 'store/index.html', context)

def list_category(request, slug):
    form = CartAddForm()
    category = Category.objects.get(slug=slug)
    context = {
        'products': Product.objects.filter(category=category),
        'title': category.title,
        'form': form,
    }
    return render(request, 'store/list.html', context)


def product_detail(request, product_id):
    if request.method == 'GET':
        form = CartAddForm()
        product = Product.objects.get(id=product_id)
        comments = product.product_comments.filter(is_reply=False)
        context = {
            'product': product,
            'title': product.category.title,
            'form': form,
            'comments': comments,
            'comment_form': CommentCreateForm,
            'reply_form': CommentReplyForm,
        }
        return render(request, 'store/product-detail.html', context)

    elif request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            product = Product.objects.get(id=product_id)
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.product = product
            new_comment.save()
            messages.success(request, 'نظر شما با موفقیت ثبت شد', 'success')
            return redirect('store:detail', product.id)


def all_products(request):
    form = CartAddForm()
    context = {
        'products': Product.objects.all(),
        'title': 'کل محصولات سایت',
        'form': form,
    }
    if request.GET.get('search'):
        context['products'] = Product.objects.filter(title__contains=request.GET['search'])
    return render(request, 'store/list.html', context)


def about(request):
    return render(request, 'store/about.html')


@login_required
def add_reply(request, product_id, comment_id):
    if request.method == 'POST':
        reply_form = CommentReplyForm(request.POST)
        product = Product.objects.get(id=product_id)
        comment = Comment.objects.get(id=comment_id)
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.author = request.user
            reply.product = product
            reply.reply = comment
            reply.is_reply = True
            reply.save()
            messages.success(request, 'نظر شما با موفقیت ثبت شد', 'success')
        return redirect('store:detail', product.id)
    