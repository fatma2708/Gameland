from django.shortcuts import render, redirect
from .forms import UserInfoForm
from .models import Agence  
from django.shortcuts import render, redirect, get_object_or_404
# Import your model
def user_info_view(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_info_table')  
    else:
        form = UserInfoForm()


    user_infos = Agence.objects.all()
    return render(request, 'user_info_form.html', {'form': form, 'user_infos': user_infos})
def update_user_view(request, pk):
    user_info = get_object_or_404(Agence, pk=pk)
    if request.method == 'POST':
        form = UserInfoForm(request.POST, instance=user_info)
        if form.is_valid():
            form.save()
            return redirect('user_info_table')  
    else:
        form = UserInfoForm(instance=user_info)
    return render(request, 'user_info_form.html', {'form': form})

def delete_user_view(request, pk):
    user_info = get_object_or_404(Agence, pk=pk)
    if request.method == 'POST':
        user_info.delete()
        return redirect('user_info_table')
    return render(request, 'delete_user_confirm.html', {'user_info': user_info})


def user_info_table(request):
    user_infos = Agence.objects.all()
    return render(request, 'user_info_table.html', {'user_infos': user_infos})

