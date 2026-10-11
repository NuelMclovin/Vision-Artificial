import { Injectable, signal } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class VisionDetectionService {
  // Imagen cargada por el usuario (cascarón de frontend)
  public readonly selectedImage = signal<string | null>(null);
  public readonly selectedFile = signal<File | null>(null);
  public readonly fileName = signal<string | null>(null);
  public readonly fileSize = signal<string | null>(null);

  public setImage(file: File, dataUrl: string): void {
    this.selectedFile.set(file);
    this.selectedImage.set(dataUrl);
    this.fileName.set(file.name);
    
    // Formatear tamaño en KB o MB
    const sizeInKb = file.size / 1024;
    const formatted = sizeInKb > 1024 
      ? (sizeInKb / 1024).toFixed(2) + ' MB' 
      : sizeInKb.toFixed(1) + ' KB';
    this.fileSize.set(formatted);
  }

  public clearImage(): void {
    this.selectedFile.set(null);
    this.selectedImage.set(null);
    this.fileName.set(null);
    this.fileSize.set(null);
  }
}
