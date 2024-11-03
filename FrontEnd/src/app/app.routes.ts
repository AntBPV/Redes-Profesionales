import { Routes } from '@angular/router';
import {InicioComponent} from './pagina-redes-profesionales/inicio/inicio.component';
import {IniciarSesionComponent} from './pagina-redes-profesionales/iniciar-sesion/iniciar-sesion.component';
import { Component } from '@angular/core';
import {RegistrarseComponent} from './pagina-redes-profesionales/registrarse/registrarse.component';

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


];
