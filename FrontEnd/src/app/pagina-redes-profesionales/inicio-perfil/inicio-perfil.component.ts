import { Component, OnInit } from '@angular/core';
import { RouterLink } from '@angular/router';
import { NgFor } from '@angular/common';
import { InicioPerfilService } from './inicio-perfil.service';
import { user } from '../redes-profesionales';
import { iniciarSesionService } from '../iniciar-sesion/iniciar-sesion.service'; // Asegúrate que la ruta sea correcta

@Component({
  selector: 'app-inicio-perfil',
  standalone: true,
  imports: [RouterLink, NgFor],
  templateUrl: './inicio-perfil.component.html',
  styleUrl: './inicio-perfil.component.css'
})
export class InicioPerfilComponent implements OnInit {
  nombreUsuario: string = '';
  fotoUsuario: string = '';
  usuarioActual: user | null = null;

  constructor(private usuarioService: InicioPerfilService) {}

  ngOnInit(): void {

    this.usuarioService.usuario$.subscribe(usuario => {
      this.usuarioActual = usuario;
    });

    this.usuarioService.nombreUsuario$.subscribe(nombre => {
      this.nombreUsuario = nombre;
    });

    this.usuarioService.fotoUsuario$.subscribe(foto => {
      this.fotoUsuario = foto;
    });
  }
}