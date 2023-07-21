from django.urls import path, reverse_lazy
from .views import Homepage, CriarConta, FuturasCompras, HomepageLogin, Saldo, recebimentos, Relatorios, EditarPerfil, despesas, saldoAtual, excluir_item_futuras_compras, criar_relatorio, relatorio_delete, Error
from django.contrib.auth import views as auth_views

app_name='conta'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('criarconta/', CriarConta.as_view(), name='criarconta'),
    path('futurascompras/', FuturasCompras.as_view(), name='futurascompras'),
    path('sempreseguro/', HomepageLogin.as_view(), name='homepagelogin'),
    path('despesas/', despesas, name='despesas'),
    path('saldo/<int:pk>/', Saldo.as_view(), name='saldo'),
    path('recebimentos/',recebimentos , name='recebimentos'),
    path('relatorios/', Relatorios.as_view(), name='relatorios'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='homepage.html'), name='logout'),
    path('editarperfil/<int:pk>/', EditarPerfil.as_view(), name='editarperfil'),
    path('mudarsenha/',auth_views.PasswordChangeView.as_view(template_name='editarperfil.html', success_url=reverse_lazy('conta:homepagelogin')), name='mudarsenha'),
    path('saldoatual/', saldoAtual, name='saldoatual'),
    path('excluiritem/<int:item_id>/', excluir_item_futuras_compras, name='excluir_item' ),
    path('criar_relatorio/', criar_relatorio, name='criar_relatorio'),
    path('excluir-relatorio/<int:relatorio_id>/', relatorio_delete, name='saldo_delete'),
    path('error/', Error.as_view(), name='error')


]