import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { VisionDetectionService } from '../../core/services/vision-detection.service';
import { SoundEffectsService } from '../../core/services/sound-effects.service';
import { SpeechService } from '../../core/services/speech.service';

@Component({
  selector: 'app-results-panel',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './results-panel.component.html',
  styleUrl: './results-panel.component.scss'
})
export class ResultsPanelComponent {
  public vision = inject(VisionDetectionService);
  public sounds = inject(SoundEffectsService);
  public speech = inject(SpeechService);

  public onAnalyzeClick(): void {
    this.sounds.playTactileClick();
    this.speech.speak('Imagen lista. Conecte su backend de Python para realizar la inferencia de sellos.');
  }
}
