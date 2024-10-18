import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Login } from '../login';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  logins: Array<Login> =[];
  
  username: string = '';
  password: string = '';
  errorMessage: string = '';
  successMessage: string = '';
  
  profiles = [
    { username: 'pepe', password: '1234' },
    { username: 'admin', password: 'admin' },
    { username: 'user1', password: 'pass1' }
  ];

  constructor(private routerPath: Router) {}

  ngOnInit() {

  }


  enviarLogin() {
  
    const user = this.profiles.find(profile => 
      profile.username === this.username && profile.password === this.password
    );
    if (user) {
      this.successMessage = 'Inicio de sesión exitoso';
      this.errorMessage = ''; 
    } else {
      this.errorMessage = 'Usuario o contraseña incorrectos';
      this.successMessage = ''; 
    }
  }
}