from django.shortcuts import render, redirect
from .models import ServiceModel, PackageModel
from .forms import ConsultingForm
from django.forms import HiddenInput

# Create your views here.


def homePage(request):
    servs = ServiceModel.objects.all()
    context = {'service': servs}
    return render(request, 'base/home.html', context)

def bookingconsultingPage(request):
    """Views for booking or consullting """
    t = request.GET.get('t')
    if(t=='consult'):
        form = ConsultingForm()
        if request.method == 'POST':
            form = ConsultingForm(request.POST)
            if form.is_valid:
                print('hi')
                data = form.save(commit = False)
                data.save()
                return redirect('home')

    else:
        q = request.GET.get('q')
        form = ConsultingForm()
        q = ServiceModel.objects.get(serv_name=q)
        form = ConsultingForm(initial={'service_insterested': q})
        form.fields['service_insterested'].widget = HiddenInput()
        form.fields['customer_name'].required = True
        form.fields['company_name'].required = True
        form.fields['email'].required = True

        if request.method == 'POST':
            form = ConsultingForm(request.POST)
            if form.is_valid:
                print('hi')
                data = form.save(commit=False)
                data.save()
                return redirect('home')

    context = {'forms':form}

    return render(request, 'base/book_consult.html', context)

def servicePage(request,pk):
    service = ServiceModel.objects.get(id=pk)

    try:
        package = PackageModel.objects.get(id=pk)

    except:
        package = None
    context = {'service': service, 'package': package}

    return render(request, 'base/serv_page.html', context)
