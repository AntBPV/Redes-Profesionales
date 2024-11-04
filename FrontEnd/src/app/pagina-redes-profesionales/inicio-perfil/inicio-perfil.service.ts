import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { iniciarSesionService } from '../iniciar-sesion/iniciar-sesion.service';
import { user } from '../redes-profesionales';

@Injectable({
  providedIn: 'root'
})
export class InicioPerfilService {
  private nombreSubject = new BehaviorSubject<string>('sebastian camilo papito ramos toro');
  private fotoSubject = new BehaviorSubject<string>('/lobo_con_audifonos.jpg');
  private usuarioSubject = new BehaviorSubject<user | null>(null);

  nombreUsuario$ = this.nombreSubject.asObservable();
  fotoUsuario$ = this.fotoSubject.asObservable();
  usuario$ = this.usuarioSubject.asObservable();

  constructor(private iniciarSesionService: iniciarSesionService) {

    this.iniciarSesionService.usuarioActual$.subscribe(usuario => {
      this.usuarioSubject.next(usuario);
      if (usuario) {
        this.nombreSubject.next(usuario.username); 

      }
    });
  }

  actualizarUsuario(nuevoNombre: string) {
    this.nombreSubject.next(nuevoNombre);
  }

  actualizarFoto(nuevaFoto: string) {
    this.fotoSubject.next(nuevaFoto);
  }

  getUsuarioActual(): user | null {
    return this.usuarioSubject.value;
  }
}