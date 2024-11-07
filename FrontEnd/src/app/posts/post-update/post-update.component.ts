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
  post: Post = new Post(1, 1, 1, 1, '', '');
  idPost: string = '';

  constructor(
    private formBuilder: FormBuilder,
    private router: ActivatedRoute,
    private postService: PostService
  ) {}

  ngOnInit() {
    this.router.params.subscribe((params) => {
      this.idPost = params['id'];

      this.postService.detailPost(parseInt(this.idPost)).subscribe((pst) => {
        this.post = pst;
        this.initForm();
      });
    });
  }

  initForm() {
    this.postForm = this.formBuilder.group({
      user: [
        this.post?.user || '',
        [Validators.required, Validators.minLength(1)],
      ],
      UserProfile: [
        this.post?.UserProfile || '',
        [Validators.required, Validators.minLength(1)],
      ],
      EnterpriseProfile: [
        this.post?.EnterpriseProfile || '',
        [Validators.required, Validators.minLength(1)],
      ],
      image: [
        this.post?.image || '',
        [Validators.required, Validators.minLength(1)],
      ],
      text: [
        this.post?.text || '',
        [Validators.required, Validators.minLength(20)],
      ],
    });
  }

  updatePost(post: Post) {
    this.postService.updatePost(this.post.id, post).subscribe((ps) => {
      alert('Publicacion Actualizada');
    });
  }
}
