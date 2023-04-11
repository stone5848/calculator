from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def critical(request):

    if request.method == 'POST':
        bcri_per = int(request.POST['bcri_per'])
        bcri_dam = int(request.POST['bcri_dam'])

        acri_per = int(request.POST['acri_per'])
        acri_dam = int(request.POST['acri_dam'])

        before_damage = (100 * 100) + (bcri_dam-100) * bcri_per
        after_damage = (100 * 100) +  (acri_dam-100) * acri_per

        data = {
            'cri_per' : acri_per,
            'cri_dam' : acri_dam,
            'percent' : (after_damage - before_damage) / before_damage * 100
        }
        return render(request, 'main/critical.html', data)
    return render(request, 'main/critical.html')