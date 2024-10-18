import { Component } from '@angular/core';

@Component({
  selector: 'app-publicaciones',
  templateUrl: './publicaciones.component.html',
  styleUrls: ['./publicaciones.component.css']
})
export class PublicacionesComponent {
  titulo = 'Explorando el mundo del desarrollo web';
  contenido = 'Hoy vamos a explorar las tendencias más importantes en el mundo del desarrollo web, incluyendo frameworks como Angular, React y más.';
  autor = 'Juan Pérez';
  fechaPublicacion = new Date().toLocaleDateString();

  meGusta() {
    console.log('Le diste Me Gusta a la publicación');
  }

  compartir() {
    console.log('Compartiste la publicación');
  }
}