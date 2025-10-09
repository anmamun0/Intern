from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm
from django.http import HttpResponse
# GET → List all blogs
def blog_list(request):
   
    blogs = Blog.objects.all().order_by('-created_at')
    blog = Blog.objects.all().first()
    # Model এর meta তথ্য
    # meta = blog._meta

    # print("Model Name:", meta.model_name)
    # print("App Label:", meta.app_label)
    # print("DB Table:", meta.db_table)
    # print("Object Name:", meta.object_name)
    # print("Verbose Name:", meta.verbose_name)
    # print("Verbose Name Plural:", meta.verbose_name_plural)
    # print("Label:", meta.label)
    # print("Label Lower:", meta.label_lower)

    # print("\nAll Fields:")
    # for field in meta.get_fields():
    #     print(f"  {field.name} ({field.get_internal_type()})")
    
    # print("\nAll Fields with details:--------------------------\n")
    # for field in meta.get_fields():
    #     print(f"\nField Name: {field.name}")
    #     print(f"  Type: {field.get_internal_type()} (এই ফিল্ডের ধরন)")
    #     print(f"  Column: {getattr(field, 'column', None)} (DB column নাম)")
    #     print(f"  Verbose Name: {field.verbose_name} (Admin panel এ ব্যবহার হয়)")
    #     print(f"  Help Text: {field.help_text} (User কে বোঝানোর জন্য)")
    #     print(f"  Primary Key: {field.primary_key} (এইটা কি primary key?)")
    #     print(f"  Null: {field.null} (DB তে NULL allow?)")
    #     print(f"  Blank: {field.blank} (Form এ ফাকা allow?)")
    #     print(f"  Default: {field.default} (User কিছু না দিলে default মান)")
    #     print(f"  Unique: {field.unique} (মান unique হতে হবে?)")
    #     print(f"  Choices: {field.choices} (নির্দিষ্ট option লিস্ট)")
    #     print(f"  Is Relation: {field.is_relation} (Relation field?)")
    #     print(f"  Related Model: {field.related_model} (যদি relation থাকে)")
    # print("\n --------------------------\n")
    # print(Blog._meta.get_fields()[0].get_internal_type())

    # print("->> ",list(blog))
    return render(request, 'blog_list.html', {'blogs': blogs})
    return HttpResponse("Check your console")

# POST → Create new blog
# @login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,  initial={'title': 'Mamun'})

        # print('--->',form.changed_data )
        print("tesing ,,, ")
        if form.is_valid():
            blog = form.save(commit=False) 
            blog.save()  
        return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog_form.html', {'form': form})
