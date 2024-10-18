import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { PublicacionesComponent } from './redesprofecionales/publicaciones/publicaciones.component';
import { Routes } from '@angular/router';

 export const routes: Routes = [
  { path: '', redirectTo: '/publicaciones', pathMatch: 'full' },  // Redireccionar a publicaciones al cargar
  { path: 'publicaciones', component: PublicacionesComponent }    // Ruta para publicaciones
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }