import { Component, OnInit } from '@angular/core';
import { Router,RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';
import { publicaciones } from '../redes-profesionales';
import { redesProfesionalesService } from '../redes-profesionales.service';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule, FormsModule } from '@angular/forms';
import { PublicacionesService } from '../publicaciones/publicaciones.service';
import { InicioPerfilService } from '../inicio-perfil/inicio-perfil.service';


@Component({
  selector: 'app-crear-publicaciones',
  standalone: true,
  imports: [RouterLink, 
            CommonModule, 
            ReactiveFormsModule,
            FormsModule],
  templateUrl: './crear-publicaciones.component.html',
  styleUrl: './crear-publicaciones.component.css'
})
export class CrearPublicacionesComponent implements OnInit {
  nuevaPublicacion: string = '';
  nombreUsuario:    string = '';
  fotoUsuario:      string = '';

  constructor(private publicacionesService: PublicacionesService,private usuarioService:InicioPerfilService, private redesProfesionalesService:redesProfesionalesService) {}


  agregarPublicacion() {
    if (this.nuevaPublicacion.trim()) {
      this.redesProfesionalesService.crearPublicacion({
        user:  this.nombreUsuario,
        image: this.fotoUsuario,
        text:  this.nuevaPublicacion,
        id: 0
      }).subscribe(()=>{
        this.nuevaPublicacion = '';
      })

      
      
      
      /*const publicacion = {
        nombreUsuario: this.nombreUsuario,
        fotoUsuario: this.fotoUsuario,
        contenido: this.nuevaPublicacion
      };
      this.publicacionesService.agregarPublicacion(publicacion);
      this.nuevaPublicacion = '';*/
    }
  }
  ngOnInit(): void {
    this.usuarioService.nombreUsuario$.subscribe(nombre => { 
      this.nombreUsuario = nombre;
    })
    this.usuarioService.fotoUsuario$.subscribe(foto => {
      this.fotoUsuario = foto;
    })
  }

}