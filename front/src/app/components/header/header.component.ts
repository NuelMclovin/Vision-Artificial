import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AccessibilityService } from '../../core/services/accessibility.service';
import { SpeechService } from '../../core/services/speech.service';
import { VisionDetectionService } from '../../core/services/vision-detection.service';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss'
})
export class HeaderComponent {
  public accessibility = inject(AccessibilityService);
  public speech = inject(SpeechService);
  public vision = inject(VisionDetectionService);
}

