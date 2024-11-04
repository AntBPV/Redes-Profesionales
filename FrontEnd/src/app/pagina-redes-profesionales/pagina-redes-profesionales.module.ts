import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {HttpClientModule} from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { PublicacionesComponent } from './publicaciones/publicaciones.component';
import { CrearPublicacionesComponent } from './crear-publicaciones/crear-publicaciones.component';

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    HttpClientModule
  ]
})
export class PaginaRedesProfesionalesModule { }
