import { Component, ElementRef, ViewChild, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { VisionDetectionService } from '../../core/services/vision-detection.service';
import { AccessibilityService } from '../../core/services/accessibility.service';
import { SoundEffectsService } from '../../core/services/sound-effects.service';

@Component({
  selector: 'app-scanner-viewport',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './scanner-viewport.component.html',
  styleUrl: './scanner-viewport.component.scss'
})
export class ScannerViewportComponent {
  @ViewChild('fileInput') fileInputRef!: ElementRef<HTMLInputElement>;

  public vision = inject(VisionDetectionService);
  public accessibility = inject(AccessibilityService);
  public sounds = inject(SoundEffectsService);

  public isDragging = signal<boolean>(false);

  public triggerFileInput(): void {
    this.sounds.playTactileClick();
    if (this.fileInputRef) {
      this.fileInputRef.nativeElement.click();
    }
  }

  public onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.handleFile(input.files[0]);
    }
  }

  public onDragOver(event: DragEvent): void {
    event.preventDefault();
    this.isDragging.set(true);
  }

  public onDragLeave(): void {
    this.isDragging.set(false);
  }

  public onDrop(event: DragEvent): void {
    event.preventDefault();
    this.isDragging.set(false);
    if (event.dataTransfer && event.dataTransfer.files.length > 0) {
      this.handleFile(event.dataTransfer.files[0]);
    }
  }

  private handleFile(file: File): void {
    if (!file.type.startsWith('image/')) return;
    this.sounds.playScanTone();
    const reader = new FileReader();
    reader.onload = (e) => {
      const result = e.target?.result as string;
      this.vision.setImage(file, result);
    };
    reader.readAsDataURL(file);
  }

  public onRemoveImage(): void {
    this.sounds.playTactileClick();
    this.vision.clearImage();
    if (this.fileInputRef) {
      this.fileInputRef.nativeElement.value = '';
    }
  }
}
