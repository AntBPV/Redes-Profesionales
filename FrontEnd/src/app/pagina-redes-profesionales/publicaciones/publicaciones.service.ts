import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

interface Publicacion {
  nombreUsuario: string;
  fotoUsuario: string;
  contenido: string;
}

@Injectable({
  providedIn: 'root'
})
export class PublicacionesService {
  private publicaciones = new BehaviorSubject<Publicacion[]>([]);
  publicaciones$ = this.publicaciones.asObservable();

  agregarPublicacion(publicacion: Publicacion) {
    const currentPublicaciones = this.publicaciones.value;
    this.publicaciones.next([...currentPublicaciones, publicacion]);
  }
}