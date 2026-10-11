export enum SealType {
  CALORIAS = 'EXCESO CALORÍAS',
  AZUCARES = 'EXCESO AZÚCARES',
  GRASAS_SATURADAS = 'EXCESO GRASAS SATURADAS',
  GRASAS_TRANS = 'EXCESO GRASAS TRANS',
  SODIO = 'EXCESO SODIO',
  EDULCORANTES = 'CONTIENE EDULCORANTES - EVITAR EN NIÑOS',
  CAFEINA = 'CONTIENE CAFEÍNA - EVITAR EN NIÑOS'
}

export interface BoundingBox {
  x: number; // Porcentaje relativo 0 - 100
  y: number; // Porcentaje relativo 0 - 100
  width: number; // Porcentaje relativo 0 - 100
  height: number; // Porcentaje relativo 0 - 100
  label: string;
  confidence: number; // 0.0 - 1.0
}

export interface DetectedSeal {
  type: SealType;
  title: string;
  shortDescription: string;
  medicalRisk: string;
  impactGroup: 'diabetes' | 'hipertension' | 'cardiovascular' | 'infantil' | 'general';
  severityLevel: 'moderada' | 'alta' | 'critica';
  confidence: number;
  box?: BoundingBox;
}

export interface ProductDetectionResult {
  id: string;
  productName: string;
  category: string;
  imageUrl: string;
  timestamp: Date;
  sealsCount: number;
  hasChildrenWarning: boolean;
  seals: DetectedSeal[];
  audioScript: string;
  healthSummary: string;
  nutritionalScore: 'A' | 'B' | 'C' | 'D' | 'E'; // E = más de 3 sellos, A = 0 sellos
  healthRecommendations: string[];
}

export type AccessibilityTheme = 'liquid-glass' | 'high-contrast';
export type TextScale = 'normal' | 'large' | 'extra-large';

