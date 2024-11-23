import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { PostCreateComponent } from './post-create/post-create.component';

@NgModule({
  declarations: [],
  imports: [CommonModule, HttpClientModule, FormsModule],
  exports: [],
})
export class PostsModule {}
