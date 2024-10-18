import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { PublicacionesComponent } from './redesprofecionales/publicaciones/publicaciones.component';
import { Routes } from '@angular/router';



 export const routes: Routes = [
  { path: '', redirectTo: '/publicaciones', pathMatch: 'full' },  
  { path: 'publicaciones', component: PublicacionesComponent }    
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }