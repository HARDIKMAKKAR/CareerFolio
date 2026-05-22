import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {

  title = 'app';

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.warmUpServices();
  }

  warmUpServices() {

    // Wake Backend
    this.http.get('https://careerfolio-xtnw.onrender.com/')
      .subscribe({
        next: () => console.log('✅ Backend awake'),
        error: () => console.log('⚠️ Backend wake failed')
      });

    // Wake ML Service
    this.http.get('https://careerfolio-ml-service.onrender.com/')
      .subscribe({
        next: () => console.log('✅ ML service awake'),
        error: () => console.log('⚠️ ML service wake failed')
      });
  }
}