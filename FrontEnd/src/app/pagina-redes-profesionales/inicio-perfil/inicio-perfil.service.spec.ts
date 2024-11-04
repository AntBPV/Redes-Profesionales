import { TestBed } from '@angular/core/testing';

import { InicioPerfilService } from './inicio-perfil.service';

describe('InicioPerfilService', () => {
  let service: InicioPerfilService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(InicioPerfilService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
