import { Routes } from '@angular/router';
import { InicioComponent} from './pagina-redes-profesionales/inicio/inicio.component';
import { IniciarSesionComponent} from './pagina-redes-profesionales/iniciar-sesion/iniciar-sesion.component';
import { Component } from '@angular/core';
import { RegistrarseComponent} from './pagina-redes-profesionales/registrarse/registrarse.component';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { PublicacionesComponent } from './pagina-redes-profesionales/publicaciones/publicaciones.component';
import { CrearPublicacionesComponent } from './pagina-redes-profesionales/crear-publicaciones/crear-publicaciones.component';
import { InicioPerfilComponent } from './pagina-redes-profesionales/inicio-perfil/inicio-perfil.component';

export const routes: Routes = [
    {
        path:'',
        component:InicioComponent
    },
    {
        path:'iniciarSesion',
        component:IniciarSesionComponent
    },
    {
        path:'Registrarse',
        component:RegistrarseComponent
    },

    {   path: 'publicacion',
        component:InicioPerfilComponent 
    },
    { path: 'inicioPerfil', component:InicioPerfilComponent },

    { path: 'crearPublicaciones', component:CrearPublicacionesComponent }, 

    { path: 'publicaciones', component: PublicacionesComponent },
  


];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
