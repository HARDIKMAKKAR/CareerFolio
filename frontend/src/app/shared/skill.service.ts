import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class SkillService {
  private api = 'http://localhost:5000/api/skills'; // Node server


  forecastResult: any;

  setForecastResult(data: any) {
  this.forecastResult = data;
}

getForecastResult() {
  return this.forecastResult;
}


  recommendedSkillsData: any;

setRecommendedSkills(data: any) {
  this.recommendedSkillsData = data;
}

getRecommendedSkills() {
  return this.recommendedSkillsData;
}



  gapResult: any;

setGapResult(data: any) {
  this.gapResult = data;
}

getGapResult() {
  return this.gapResult;
}


predictedRole: string = '';

setPredictedRole(role: string) {
  this.predictedRole = role;
}

getPredictedRole() {
  return this.predictedRole;
}


  constructor(private http: HttpClient) {}

  recommend(skills: any[]): Observable<any> {
    return this.http.post<any>(`http://127.0.0.1:5001/recommend-skills`, { skills : skills });
  }

  predict(skills: any[]): Observable<any> {
    return this.http.post<any>(`http://127.0.0.1:5001/predict-career`, { skills : skills });
  }


  skill_gap_analysis(skills: any[] , targetRole : any): Observable<any> {
    return this.http.post<any>(`http://127.0.0.1:5001/api/skills/gap`, { skills : skills , target_role : targetRole });
  }

  forecast(skills: any[] , targetRole : any , exp:any , projects : any , certs : any , learning_rate : any): Observable<any> {
    return this.http.post<any>(`http://127.0.0.1:5001/forecast-growth`, { skills : skills , target_role : targetRole , exp : exp , projects : projects , certs : certs , learning_rate : learning_rate});
  }

}
