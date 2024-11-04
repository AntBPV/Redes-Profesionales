import { TestBed } from '@angular/core/testing';

import { redesProfesionalesService } from './redes-profesionales.service';

describe('RedesProfesionalesService', () => {
  let service: redesProfesionalesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(redesProfesionalesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
