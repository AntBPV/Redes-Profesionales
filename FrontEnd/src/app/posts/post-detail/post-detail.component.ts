import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';
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

  constructor(
    private route: ActivatedRoute,
    private postService: PostService
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
}
