import { Injectable, signal } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SpeechService {
  private synth: SpeechSynthesis | null = null;
  private currentUtterance: SpeechSynthesisUtterance | null = null;
  private spanishVoice: SpeechSynthesisVoice | null = null;

  public readonly isSpeaking = signal<boolean>(false);
  public readonly isPaused = signal<boolean>(false);
  public readonly currentText = signal<string>('');
  public readonly speechRate = signal<number>(1.0); // 0.8x a 1.2x

  constructor() {
    if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
      this.synth = window.speechSynthesis;
      this.initVoices();
      if (this.synth.onvoiceschanged !== undefined) {
        this.synth.onvoiceschanged = () => this.initVoices();
      }
    }
  }

  private initVoices(): void {
    if (!this.synth) return;
    const voices = this.synth.getVoices();
    // Priorizar voces en español de México (es-MX) o cualquier variante en español
    this.spanishVoice = 
      voices.find(v => v.lang.toLowerCase() === 'es-mx') ||
      voices.find(v => v.lang.toLowerCase().startsWith('es-')) ||
      voices.find(v => v.lang.toLowerCase().includes('es')) ||
      null;
  }

  public speak(text: string, force: boolean = true): void {
    if (!this.synth) {
      console.warn('SpeechSynthesis no es compatible en este navegador.');
      return;
    }

    if (force) {
      this.stop();
    }

    if (!text || text.trim().length === 0) return;

    this.currentText.set(text);
    const utterance = new SpeechSynthesisUtterance(text);
    
    if (this.spanishVoice) {
      utterance.voice = this.spanishVoice;
    }
    utterance.lang = 'es-MX';
    utterance.rate = this.speechRate();
    utterance.pitch = 1.0;

    utterance.onstart = () => {
      this.isSpeaking.set(true);
      this.isPaused.set(false);
    };

    utterance.onend = () => {
      this.isSpeaking.set(false);
      this.isPaused.set(false);
      this.currentText.set('');
    };

    utterance.onerror = () => {
      this.isSpeaking.set(false);
      this.isPaused.set(false);
      this.currentText.set('');
    };

    this.currentUtterance = utterance;
    this.synth.speak(utterance);
  }

  public stop(): void {
    if (!this.synth) return;
    this.synth.cancel();
    this.isSpeaking.set(false);
    this.isPaused.set(false);
    this.currentText.set('');
  }

  public togglePause(): void {
    if (!this.synth) return;
    if (this.isPaused()) {
      this.synth.resume();
      this.isPaused.set(false);
    } else if (this.isSpeaking()) {
      this.synth.pause();
      this.isPaused.set(true);
    }
  }

  public setRate(rate: number): void {
    this.speechRate.set(rate);
    if (this.isSpeaking() && this.currentText()) {
      const remainingText = this.currentText();
      this.speak(remainingText, true);
    }
  }
}

