import { Routes } from '@angular/router';
import {InicioComponent} from './pagina-redes-profesionales/inicio/inicio.component';
import {IniciarSesionComponent} from './pagina-redes-profesionales/iniciar-sesion/iniciar-sesion.component';
import { Component } from '@angular/core';
import {RegistrarseComponent} from './pagina-redes-profesionales/registrarse/registrarse.component';
import { PruebaComponent } from './pagina-redes-profesionales/prueba/prueba.component';
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
    {
        path:'prueba',
        component:PruebaComponent
    }

];
