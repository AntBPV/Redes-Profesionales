import { Routes } from '@angular/router';
import { PostListComponent } from './posts/post-list/post-list.component';
import { PostDetailComponent } from './posts/post-detail/post-detail.component';
import { PostCreateComponent } from './posts/post-create/post-create.component';
import { PostUpdateComponent } from './posts/post-update/post-update.component';

export const routes: Routes = [
  {
    path: '',
    component: PostListComponent,
  },
  {
    path: 'posts',
    component: PostListComponent,
  },
  {
    path: 'posts/:id',
    component: PostDetailComponent,
  },
  {
    path: 'create-post',
    component: PostCreateComponent,
  },
  {
    path: 'update-post/:id',
    component: PostUpdateComponent,
  },
];
