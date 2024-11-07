import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Post } from './posts';

@Injectable({
  providedIn: 'root',
})
export class PostService {
  private API_URL = 'http://127.0.0.1:8000/api/post/list';

  constructor(private http: HttpClient) {}

  getPosts(): Observable<Post[]> {
    return this.http.get<Post[]>(this.API_URL);
  }

  detailPost(id: number): Observable<Post> {
    return this.http.get<Post>(`${this.API_URL}/${id}`);
  }

  createPost(post: Post): Observable<Post> {
    return this.http.post<Post>(this.API_URL, post);
  }

  updatePost(id: number, post: Post): Observable<Post> {
    return this.http.put<Post>(`${this.API_URL}/${id}`, post);
  }

  deletePost(id: number): Observable<any> {
    return this.http.delete(`${this.API_URL}/${id}`);
  }
}
