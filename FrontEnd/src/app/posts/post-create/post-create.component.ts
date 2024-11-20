import { Component, OnInit } from '@angular/core';
import { Post } from '../posts';
import { PostService } from '../post.service';
import {
  FormArray,
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-post-create',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './post-create.component.html',
  styleUrl: './post-create.component.css',
})
export class PostCreateComponent implements OnInit {
  postForm!: FormGroup;
  selectedImage: File | null = null;

  constructor(
    private formBuilder: FormBuilder,
    private postService: PostService,
    private router: Router
  ) {}

  ngOnInit() {
    this.postForm = this.formBuilder.group({
      text: ['', [Validators.required, Validators.minLength(20)]],
      image: [null],
    });
  }

  onFileSelected(event: any) {
    const file = event.target.files[0];
    if (file) {
      this.selectedImage = file;
    }
  }

  createPost() {
    if (this.postForm.valid) {
      const formData = new FormData();
      formData.append('text', this.postForm.get('text')?.value);

      formData.append('UserProfile', '1');

      if (this.selectedImage) {
        formData.append('image', this.selectedImage);
      }

      this.postService.createPost(formData).subscribe({
        next: (createdPost) => {
          alert('Publicación creada exitosamente');
          this.router.navigate(['/posts']);
        },
        error: (error) => {
          console.error('Error al crear publicación:', error);
          alert('Error al crear la publicación. Revisa los datos enviados.');
        },
      });
    } else {
      alert('Por favor, completa correctamente el formulario.');
    }
  }
}
