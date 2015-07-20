from django.shortcuts import render, redirect
from .forms import UserCreationForm, AccountForm


def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserCreationForm(data=request.POST)
        account_form = AccountForm(data=request.POST)
        # the url if the registration is completed
        next = request.POST.get('next', 'home')

        # If the two forms are valid...
        if user_form.is_valid() and account_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            account = account_form.save(commit=False)
            account.user = user

            # Now we save the UserProfile model instance.
            account.save()

            # Update our variable to tell the template registration was successful.
            registered = True

            # Redirect to homepage
            return redirect(next)

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            # print(user_form.errors, account_form.errors)
            pass

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserCreationForm()
        account_form = AccountForm()
        next = request.GET.get('next', 'home')

    # Render the template depending on the context.
    return render(request, 'accounts/register.html', {
        'user_form': user_form,
        'account_form': account_form,
        'registered': registered,
        'next': next,
    })
