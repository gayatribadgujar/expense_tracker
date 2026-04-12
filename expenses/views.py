from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, ExpenseForm
from .models import Expense


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('expense_list')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'expenses/signup.html', {'form': form})


@login_required(login_url='/login/')
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date', '-id')
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})


@login_required(login_url='/login/')
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()

    return render(request, 'expenses/add_expense.html', {'form': form})

@login_required(login_url='/login/')
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)

    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')

    return render(request, 'expenses/delete_expense.html', {'expense': expense})