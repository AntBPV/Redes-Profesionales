import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { RouterLink, Router } from '@angular/router';
import { redesProfesionalesService } from '../redes-profesionales.service';
import { user } from '../redes-profesionales';
import { catchError } from 'rxjs/operators';
import { of } from 'rxjs';

@Component({
  selector: 'app-registrarse',
  standalone: true,
  imports: [
    ReactiveFormsModule,
    CommonModule,
    RouterLink 
  ],
  templateUrl: './registrarse.component.html',
  styleUrl: './registrarse.component.css'
})
export class RegistrarseComponent implements OnInit {
  registerForm: FormGroup;
  mensajeExito: boolean = false;
  mensajeError: string = '';

  constructor(
    private fb: FormBuilder,
    private redesService: redesProfesionalesService,
    private router: Router
  ) {
    this.registerForm = this.fb.group({
      username: ['', [Validators.required, Validators.minLength(3)]],
      password: ['', [Validators.required, Validators.minLength(6)]], 
      confirmPassword: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.email]],
    }, { validators: this.passwordMatchValidator }); 
  }

  passwordMatchValidator(form: FormGroup) {
    const password = form.get('password');
    const confirmPassword = form.get('confirmPassword');
    
    if (password && confirmPassword && password.value !== confirmPassword.value) {
      return { passwordMismatch: true };
    }
    return null;
  }

  onSubmit() {
    this.mensajeError = '';
    this.mensajeExito = false;

    if (this.registerForm.valid) {
      const newUser = new user(
        0, // El ID será generado por el backend
        this.registerForm.value.username,
        this.registerForm.value.password,
        this.registerForm.value.email
      );

      this.redesService.crearUsuario(newUser)
        .pipe(
          catchError(error => {
            this.mensajeError = 'Error al registrar usuario. Intente nuevamente.';
            console.error('Error de registro:', error);
            return of(null);
          })
        )
        .subscribe(
          (usuarioCreado) => {
            if (usuarioCreado) {
              this.mensajeExito = true;
              setTimeout(() => {
                this.router.navigate(['/iniciarSesion']);
              }, 3000);
            }
          }
        );
    }
  }

  ngOnInit(): void {
  }
}