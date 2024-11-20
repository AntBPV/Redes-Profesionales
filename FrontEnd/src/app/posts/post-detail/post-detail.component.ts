import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterModule, Router } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import { NgIf } from '@angular/common';
import { Post } from '../posts';
import { PostService } from '../post.service';

@Component({
  selector: 'app-post-detail',
  standalone: true,
  imports: [NgIf, RouterModule],
  templateUrl: './post-detail.component.html',
  styleUrl: './post-detail.component.css',
})
export class PostDetailComponent implements OnInit {
  post: Post | null = null;
  baseUrl = 'http://127.0.0.1:8000';

  constructor(
    private route: ActivatedRoute,
    private postService: PostService,
    private router: Router
  ) {}

  ngOnInit() {
    this.getPostDetail();
  }

  getPostDetail() {
    const id = Number(this.route.snapshot.paramMap.get('id'));

    this.postService.detailPost(id).subscribe(
      (data) => {
        this.post = data;
      },
      (error) => {
        console.error('Error fetching post details:', error);
      }
    );
  }
  getImageUrl(imagePath: string | File | null): string {
    if (!imagePath) return '';

    if (typeof imagePath === 'string') {
      return `${this.baseUrl}${imagePath}`;
    } else {
      return URL.createObjectURL(imagePath);
    }
  }

  deletePost() {
    if (this.post && this.post.id) {
      const confirmDelete = confirm(
        '¿Estás seguro de eliminar esta publicación?'
      );
      if (confirmDelete) {
        this.postService.deletePost(this.post.id).subscribe(
          () => {
            this.router.navigate(['/posts']);
          },
          (error) => {
            console.error('Error deleting post', error);
          }
        );
      }
    }
  }

  goBack() {
    this.router.navigate(['/posts']);
  }

  goToUpdate() {
    if (this.post && this.post.id) {
      this.router.navigate(['/update-post', this.post.id]);
    }
  }
}
