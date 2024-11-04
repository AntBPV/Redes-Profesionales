import { Component } from '@angular/core';
import { Route,RouterLink } from '@angular/router';
import { NgFor } from '@angular/common';
import { redesProfesionalesService} from '../redes-profesionales.service';
import { PublicacionesService } from './publicaciones.service';
import { OnInit } from '@angular/core';


@Component({
  selector: 'app-publicaciones',
  standalone: true,
  imports: [RouterLink, NgFor],
  templateUrl: './publicaciones.component.html',
  styleUrl: './publicaciones.component.css'
})
export class PublicacionesComponent implements OnInit {
  publicaciones: any[] = [];

  constructor(private publicacionesService: PublicacionesService, private redesProfesionalesService:redesProfesionalesService) {}

  obtenerPublicaciones(){
    this.redesProfesionalesService.obtenerPublicaciones().subscribe(publicacion=>{
      this.publicaciones = publicacion;
      console.log(this.publicaciones)
    })
  }

  ngOnInit() {
    this.obtenerPublicaciones();


    this.publicacionesService.publicaciones$.subscribe(data => {
      this.publicaciones = data.map(publicacion => ({
        ...publicacion
      }));
    });
  }
}