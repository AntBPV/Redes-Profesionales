import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { RouterLink, Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { redesProfesionalesService } from '../redes-profesionales.service';
import { user } from '../redes-profesionales';
import { catchError } from 'rxjs/operators';
import { of } from 'rxjs';

@Component({
  selector: 'app-iniciar-sesion',
  templateUrl: './iniciar-sesion.component.html',
  styleUrls: ['./iniciar-sesion.component.css'],
  standalone: true,
  imports: [RouterLink, CommonModule, ReactiveFormsModule]
})
export class IniciarSesionComponent implements OnInit {
  loginForm: FormGroup;
  errorLogin: string = '';
  loginExitoso: boolean = false; 

  constructor(
    private routerPath: Router, 
    private redesProfesionalesService: redesProfesionalesService,
    private formBuilder: FormBuilder
  ) {
    this.loginForm = this.formBuilder.group({
      username: ['', [Validators.required]],
      password: ['', [Validators.required]]
    });
  }

  ngOnInit(): void {

  }

  onSubmit() {
    this.errorLogin = '';
    this.loginExitoso = false;

    if (this.loginForm.valid) {
      const username = this.loginForm.get('username')?.value;
      const password = this.loginForm.get('password')?.value;


      this.redesProfesionalesService.obtenerUsuarios()
        .pipe(
          catchError(error => {
            this.errorLogin = 'Error al intentar iniciar sesión. Intente nuevamente.';
            console.error('Error de inicio de sesión:', error);
            return of([]);
          })
        )
        .subscribe(
          (usuarios) => {
            const usuarioEncontrado = usuarios.find(
              usuario => 
                usuario.username === username && 
                usuario.password === password
            );

            if (usuarioEncontrado) {
              this.loginExitoso = true; 
              localStorage.setItem('usuarioActual', JSON.stringify(usuarioEncontrado));
              
              setTimeout(() => {
                this.routerPath.navigate(['/prueba']); 
              }, 2000); 
            } else {
              this.errorLogin = 'Credenciales incorrectas. Por favor, intenta de nuevo.';
            }
          }
        );
    }
  }
}