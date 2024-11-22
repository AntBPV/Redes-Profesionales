import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Post } from './posts';

@Injectable({
  providedIn: 'root',
})
export class PostService {
  private API_URL =
    'https://redesbackend-bvdwf3csceg5c8fr.eastus2-01.azurewebsites.net/api/post/list';

  constructor(private http: HttpClient) {}

  getPosts(): Observable<Post[]> {
    return this.http.get<Post[]>(this.API_URL);
  }

  detailPost(id: number): Observable<Post> {
    return this.http.get<Post>(`${this.API_URL}/${id}`);
  }

  createPost(postData: FormData): Observable<Post> {
    return this.http.post<Post>(this.API_URL, postData);
  }

  updatePost(id: number, formData: FormData): Observable<Post> {
    return this.http.put<Post>(`${this.API_URL}/${id}`, formData);
  }

  deletePost(id: number): Observable<any> {
    return this.http.delete(`${this.API_URL}/${id}`);
  }
}
