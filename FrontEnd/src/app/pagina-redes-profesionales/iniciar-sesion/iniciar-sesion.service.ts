import { Injectable } from '@angular/core';
import { BehaviorSubject} from 'rxjs';
import {user} from '../redes-profesionales'


@Injectable({
  providedIn: 'root'
})
export class iniciarSesionService {
  private usuarioActualSubject = new BehaviorSubject<user | null>(null);
  usuarioActual$ = this.usuarioActualSubject.asObservable();

  constructor() {
    const usuarioGuardado = localStorage.getItem('usuarioActual');
    if (usuarioGuardado) {
      this.usuarioActualSubject.next(JSON.parse(usuarioGuardado));
    }
  }

  setUsuarioActual(usuario: user) {
    localStorage.setItem('usuarioActual', JSON.stringify(usuario));
    this.usuarioActualSubject.next(usuario);
  }

  getUsuarioActual() {
    return this.usuarioActualSubject.value;
  }

  logout() {
    localStorage.removeItem('usuarioActual');
    this.usuarioActualSubject.next(null);
  }
}