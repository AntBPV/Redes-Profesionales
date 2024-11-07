import { Component, OnInit } from '@angular/core';
import { Router, RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import { NgFor, NgIf } from '@angular/common';
import { Post } from '../posts';
import { PostService } from '../post.service';

@Component({
  selector: 'app-post-list',
  standalone: true,
  imports: [NgFor, NgIf, RouterModule],
  templateUrl: './post-list.component.html',
  styleUrl: './post-list.component.css',
})
export class PostListComponent implements OnInit {
  posts: Array<Post> = [];

  constructor(private routerPath: Router, private postService: PostService) {}

  ngOnInit() {
    this.getPosts();
  }

  getPosts() {
    this.postService.getPosts().subscribe(
      (data) => {
        this.posts = data;
        this.logPosts();
      },
      (error) => {
        console.error('Error fetching posts:', error);
      }
    );
  }

  logPosts() {
    console.log('Posts retrieved from the API:');
    this.posts.forEach((post) => {
      console.log(post);
    });
  }
}
