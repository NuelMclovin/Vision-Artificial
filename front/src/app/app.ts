import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './components/header/header.component';
import { ScannerViewportComponent } from './components/scanner-viewport/scanner-viewport.component';
import { ResultsPanelComponent } from './components/results-panel/results-panel.component';
import { AccessibilityService } from './core/services/accessibility.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    HeaderComponent,
    ScannerViewportComponent,
    ResultsPanelComponent
  ],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  public accessibility = inject(AccessibilityService);
}
