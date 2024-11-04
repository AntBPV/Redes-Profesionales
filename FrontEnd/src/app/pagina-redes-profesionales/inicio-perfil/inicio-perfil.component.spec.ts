import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InicioPerfilComponent } from './inicio-perfil.component';

describe('InicioPerfilComponent', () => {
  let component: InicioPerfilComponent;
  let fixture: ComponentFixture<InicioPerfilComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [InicioPerfilComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(InicioPerfilComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
