from .models import Aluno,Cadastro
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 


####################
def alunoView(request):
    alunos_list = Aluno.objects.all()
    return render(request, 'main/alunos.html', {'alunos_list': alunos_list})
####################

def alunoIDview(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    print(aluno)
    return render(request, 'main/alunoID.html', {'aluno':aluno})
####################

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print('name:', name)
        print('Email:', email)
        print('Message:', message)
    return render(request, 'main/aula-teste.html')

#####################

# atenção: essas importações estão aqui apenas para uma melhor visualização!

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import AlunoForm

class AlunoCreateView(CreateView):
    model = Aluno
    form_class = AlunoForm
    success_url = reverse_lazy('aluno-lista') # url para redirecionar após a criação do objeto
    template_name = 'main/aluno_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

######################################
# exemplo com função!

from django.shortcuts import render, redirect
from django.urls import reverse

def aluno_create_view(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.user = request.user
            aluno.save()
            return redirect(reverse('aluno-lista'))
    else:
        form = AlunoForm()
    
    return render(request, 'aluno_form.html', {'form': form})
#########################################

class AlunoUpdateView(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'main/aluno_form.html'
    success_url = reverse_lazy('aluno-lista')

#########################################

def deleteAluno(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    aluno.delete()
    return redirect('/')

def novo_formulario(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('inputpassword')
        print('Email:', email)
        print('Password:', password)
    return render(request, 'main/novo.formulario.html')

def cadastro_endereco (request):
    if request.method == 'POST':
        email = request.POST.get('inputEmail4')
        password = request.POST.get('inputPassword4')
        address = request.POST.get('inputAddress')
        address2 = request.POST.get('inputAddress2')
        city = request.POST.get('inputCity')
        state = request.POST.get('inputState')
        zip = request.POST.get('inputZip')
        
        cadastro = Cadastro(email=email,password=password,
                            address=address,address2=address2,city=city,state=state,zip=zip)
        cadastro.save()
    
    return render(request, 'main/endereco.html')
        



