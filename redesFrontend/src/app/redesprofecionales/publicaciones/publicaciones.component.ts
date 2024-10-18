import { Component } from '@angular/core';
import { NgFor } from '@angular/common';

@Component({
  selector: 'app-publicaciones',
  standalone: true,
  imports: [NgFor],
  templateUrl: './publicaciones.component.html',
  styleUrls: ['./publicaciones.component.css']

})
export class PublicacionesComponent {
  publicaciones = [
    {
      autor: 'Juan Pérez',
      titulo: 'Mi primera publicación',
      contenido: 'Este es el contenido de mi primera publicación. Es un texto breve pero informativo.',
      fechaPublicacion: new Date().toLocaleDateString()
    },
    {
      autor: 'María López',
      titulo: 'Consejos para mejorar tu productividad',
      contenido: 'Aquí te dejo algunos consejos útiles para mejorar tu productividad día a día. Recuerda enfocarte en lo importante.',
      fechaPublicacion: new Date().toLocaleDateString()
    },
    {
      autor: 'Carlos Ramírez',
      titulo: 'Las tendencias tecnológicas del 2024',
      contenido: 'Este año veremos avances en inteligencia artificial, computación cuántica, y muchas otras tecnologías emergentes.',
      fechaPublicacion: new Date().toLocaleDateString()
    },
    {
      autor: 'Juan Pérez',
      titulo: 'Mi primera publicación',
      contenido: 'Este es el contenido de mi primera publicación. Es un texto breve pero informativo.',
      fechaPublicacion: new Date().toLocaleDateString()
    },
    {
      autor: 'Juan Pérez',
      titulo: 'Mi primera publicación',
      contenido: 'Este es el contenido de mi primera publicación. Es un texto breve pero informativo.',
      fechaPublicacion: new Date().toLocaleDateString()
    },
    {
      autor: 'Juan Pérez',
      titulo: 'Mi primera publicación',
      contenido: 'Este es el contenido de mi primera publicación. Es un texto breve pero informativo.',
      fechaPublicacion: new Date().toLocaleDateString()
    },
    {
      autor: 'Juan Pérez',
      titulo: 'Mi primera publicación',
      contenido: 'Este es el contenido de mi primera publicación. Es un texto breve pero informativo.',
      fechaPublicacion: new Date().toLocaleDateString()
    },
    {
      autor: 'Juan Pérez',
      titulo: 'Mi primera publicación',
      contenido: 'Este es el contenido de mi primera publicación. Es un texto breve pero informativo.',
      fechaPublicacion: new Date().toLocaleDateString()
    },
    {
      autor: 'Juan Pérez',
      titulo: 'Mi primera publicación',
      contenido: 'Este es el contenido de mi primera publicación. Es un texto breve pero informativo.',
      fechaPublicacion: new Date().toLocaleDateString()
    },
  ];
}