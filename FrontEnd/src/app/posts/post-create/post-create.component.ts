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

  constructor(
    private formBuilder: FormBuilder,
    private postService: PostService
  ) {}

  ngOnInit() {
    this.postForm = this.formBuilder.group({
      User: ['', [Validators.required, Validators.minLength(1)]],
      UserProfile: ['', [Validators.required, Validators.minLength(1)]],
      EnterpriseProfile: ['', [Validators.required, Validators.minLength(1)]],
      image: ['', [Validators.required, Validators.minLength(1)]],
      text: ['', [Validators.required, Validators.minLength(20)]],
    });
  }

  createPost(post: Post): void {
    this.postService.createPost(post).subscribe((createdPost) => {
      alert('Publicacion creada');
      this.postForm.reset();
    });
  }
}
