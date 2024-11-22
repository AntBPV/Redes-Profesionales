import { Component, OnInit } from '@angular/core';
import {
  FormArray,
  FormBuilder,
  FormGroup,
  FormsModule,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { Router } from '@angular/router';
import { ActivatedRoute } from '@angular/router';
import { Post } from '../posts';
import { PostService } from '../post.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-post-update',
  standalone: true,
  imports: [ReactiveFormsModule, FormsModule, CommonModule],
  templateUrl: './post-update.component.html',
  styleUrl: './post-update.component.css',
})
export class PostUpdateComponent implements OnInit {
  postForm!: FormGroup;
  post: Post | null = null;
  selectedImage: File | null = null;
  idPost: string = '';
  currentImage: string | null = null;
  baseUrl =
    'https://redesbackend-bvdwf3csceg5c8fr.eastus2-01.azurewebsites.net';

  constructor(
    private formBuilder: FormBuilder,
    private route: ActivatedRoute,
    private postService: PostService,
    private router: Router
  ) {}

  ngOnInit() {
    this.route.params.subscribe((params) => {
      this.idPost = params['id'];

      this.postService.detailPost(parseInt(this.idPost)).subscribe((pst) => {
        this.post = pst;
        this.initForm();
      });
    });
  }

  initForm() {
    this.postForm = this.formBuilder.group({
      text: [
        this.post?.text || '',
        [Validators.required, Validators.minLength(20)],
      ],
      image: [this.currentImage], // Inicializar con la imagen actual
    });
  }

  onFileSelected(event: any) {
    if (event.target.files.length > 0) {
      this.selectedImage = event.target.files[0];
    }
  }

  updatePost() {
    if (this.postForm.valid && this.post) {
      const formData = new FormData();

      formData.append('text', this.postForm.get('text')?.value);

      if (this.selectedImage) {
        formData.append('image', this.selectedImage);
      }

      this.postService.updatePost(this.post.id, formData).subscribe({
        next: (updatedPost) => {
          alert('Publicación actualizada exitosamente');
          this.router.navigate(['/posts']); // O a donde necesites
        },
        error: (error) => {
          console.error('Error al actualizar publicación:', error);
          alert('Error al actualizar la publicación');
        },
      });
    } else {
      this.postForm.markAllAsTouched();
    }
  }

  getImageUrl(imagePath: string | File | null): string {
    if (!imagePath) return '';

    if (typeof imagePath === 'string') {
      return `${this.baseUrl}${imagePath}`;
    } else {
      return URL.createObjectURL(imagePath);
    }
  }

  goBack() {
    this.router.navigate(['/posts', this.post?.id]);
  }
}
