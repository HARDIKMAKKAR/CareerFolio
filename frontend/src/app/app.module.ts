import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { UploadComponent } from './upload/upload.component';
import { ErrorComponent } from './error/error.component';
import { SignupComponent } from './signup/signup.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HeaderComponent } from './header/header.component';
import { HttpClient, HttpClientModule, provideHttpClient } from '@angular/common/http';
import { DashboardComponent } from './dashboard/dashboard.component';
import { OutputComponent } from './output/output.component';
import { ForecastResultComponent } from './forecast-result/forecast-result.component';
import { RecommendResultComponent } from './recommend-result/recommend-result.component';
import { GapResultComponent } from './gap-result/gap-result.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    LoginComponent,
    UploadComponent,
    ErrorComponent,
    SignupComponent,
    HeaderComponent,
    DashboardComponent,
    OutputComponent,
    ForecastResultComponent,
    RecommendResultComponent,
    GapResultComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [provideHttpClient()],
  bootstrap: [AppComponent]
})
export class AppModule { }
