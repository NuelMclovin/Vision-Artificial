import { Injectable, signal, effect, inject } from '@angular/core';
import { AccessibilityTheme, TextScale } from '../models/seal.models';
import { SpeechService } from './speech.service';
import { SoundEffectsService } from './sound-effects.service';

@Injectable({
  providedIn: 'root'
})
export class AccessibilityService {
  private speech = inject(SpeechService);
  private sounds = inject(SoundEffectsService);

  public readonly theme = signal<AccessibilityTheme>('liquid-glass');
  public readonly textScale = signal<TextScale>('normal');
  public readonly autoSpeech = signal<boolean>(true);
  public readonly opticalMagnifier = signal<boolean>(false);
  public readonly zoomLevel = signal<number>(1.0); // 1.0x, 1.5x, 2.0x

  constructor() {
    effect(() => {
      const currentTheme = this.theme();
      if (typeof document !== 'undefined') {
        if (currentTheme === 'high-contrast') {
          document.body.classList.add('high-contrast-mode');
        } else {
          document.body.classList.remove('high-contrast-mode');
        }
      }
    });

    effect(() => {
      const scale = this.textScale();
      if (typeof document !== 'undefined') {
        document.body.classList.remove('text-size-large', 'text-size-xlarge');
        if (scale === 'large') {
          document.body.classList.add('text-size-large');
        } else if (scale === 'extra-large') {
          document.body.classList.add('text-size-xlarge');
        }
      }
    });
  }

  public toggleTheme(): void {
    this.sounds.playTactileClick();
    const nextTheme = this.theme() === 'liquid-glass' ? 'high-contrast' : 'liquid-glass';
    this.theme.set(nextTheme);
    const msg = nextTheme === 'high-contrast' 
      ? 'Modo de alto contraste asistivo activado.' 
      : 'Modo visual Vidrio Líquido y Neumorfismo activado.';
    this.speech.speak(msg);
  }

  public cycleTextScale(): void {
    this.sounds.playTactileClick();
    const current = this.textScale();
    let next: TextScale = 'normal';
    let label = 'Tamaño de texto estándar.';

    if (current === 'normal') {
      next = 'large';
      label = 'Tamaño de texto grande.';
    } else if (current === 'large') {
      next = 'extra-large';
      label = 'Tamaño de texto extra grande para baja visión.';
    } else {
      next = 'normal';
      label = 'Tamaño de texto normal.';
    }

    this.textScale.set(next);
    this.speech.speak(label);
  }

  public toggleAutoSpeech(): void {
    this.sounds.playTactileClick();
    const nextVal = !this.autoSpeech();
    this.autoSpeech.set(nextVal);
    const msg = nextVal 
      ? 'Lectura por voz automática activada.' 
      : 'Lectura por voz en modo manual.';
    this.speech.speak(msg);
  }

  public toggleMagnifier(): void {
    this.sounds.playTactileClick();
    const next = !this.opticalMagnifier();
    this.opticalMagnifier.set(next);
    const msg = next ? 'Lupa óptica activada.' : 'Lupa óptica desactivada.';
    this.speech.speak(msg);
  }

  public cycleZoom(): void {
    this.sounds.playTactileClick();
    const current = this.zoomLevel();
    let next = 1.0;
    if (current === 1.0) next = 1.5;
    else if (current === 1.5) next = 2.0;
    else next = 1.0;
    
    this.zoomLevel.set(next);
    this.speech.speak(`Aumento de lente al ${next * 100} por ciento.`);
  }
}

