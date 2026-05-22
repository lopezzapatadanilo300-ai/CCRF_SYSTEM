from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('login/',        views.login_view, name='login'),
    path('logout/',       views.logout_view, name='logout'),
    path('dashboard/',    views.dashboard_view, name='dashboard'),
    # Sedes y usuarios
    path('sedes/', views.sedes_list, name='sedes_list'),
    path('sedes/nueva/', views.sede_form, name='sede_nueva'),
    path('sedes/<int:pk>/editar/', views.sede_form, name='sede_editar'),
    path('usuarios/', views.usuarios_list, name='usuarios_list'),
    path('usuarios/nuevo/', views.usuario_form, name='usuario_nuevo'),
    path('usuarios/<int:pk>/toggle/', views.usuario_toggle, name='usuario_toggle'),
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    # Miembros
    path('miembros/', views.miembros_list, name='miembros_list'),
    path('miembros/nuevo/', views.miembro_form, name='miembro_nuevo'),
    path('miembros/<int:pk>/editar/', views.miembro_form, name='miembro_editar'),
    path('miembros/<int:pk>/toggle/', views.miembro_toggle, name='miembro_toggle'),
    # Finanzas
    path('finanzas/', views.finanzas_list, name='finanzas_list'),
    path('finanzas/nuevo/', views.finanza_form, name='finanza_nueva'),
    path('finanzas/<int:pk>/eliminar/', views.finanza_eliminar, name='finanza_eliminar'),
    path( 'finanzas/editar/<int:pk>/', views.finanza_editar, name='finanza_editar'),
    # Inventario
    path('inventario/', views.inventario_list, name='inventario_list'),
    path('inventario/nuevo/', views.inventario_form, name='inventario_nuevo'),
    path('inventario/<int:pk>/', views.inventario_detalle, name='inventario_detalle'),
    path('inventario/<int:pk>/enviar/', views.inventario_enviar, name='inventario_enviar'),
    path('inventario/<int:pk>/revisar/', views.inventario_revisar, name='inventario_revisar'),
    path('inventario/<int:pk>/pdf/', views.inventario_exportar_pdf, name='inventario_pdf'),
    path('inventario/<int:pk>/excel/', views.inventario_exportar_excel, name='inventario_excel'),
    # Reportes
    path('reportes/',   views.reportes_view, name='reportes'),
    path('reportes/ranking/', views.ranking_view, name='ranking'),
    path('reportes/exportar/pdf/', views.exportar_pdf, name='exportar_pdf'),
    path('reportes/exportar/excel/', views.exportar_excel, name='exportar_excel'),
]