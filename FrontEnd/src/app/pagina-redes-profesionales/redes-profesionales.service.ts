import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';
import { Observable, of} from 'rxjs';
import { user } from './redes-profesionales';
import { PublicacionesComponent } from './publicaciones/publicaciones.component';
import { publicaciones } from './redes-profesionales';

const API_URL=''

@Injectable({
  providedIn: 'root'
})
export class redesProfesionalesService {

  
  constructor(private http:HttpClient) { }

  obtenerUsuarios(): Observable<user[]>{
    return this.http.get<user[]>(API_URL);
  }

  crearUsuario(newUser:user):Observable<user>{
    return this.http.post<user>('', newUser)
  } 

  obtenerUsuario(id:Number): Observable<user>{
    return this.http.get<user>(''+'consultar/'+id)
  }

  obtenerPublicaciones(): Observable<publicaciones[]>{
    return this.http.get<publicaciones[]>(API_URL);
  }

  crearPublicacion(newUser:publicaciones):Observable<publicaciones>{
    return this.http.post<publicaciones>('', newUser)
  } 

}
