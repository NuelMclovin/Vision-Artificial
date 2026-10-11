import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, HRFlowable
)

def create_report():
    pdf_filename = "NutriVision_Reporte_Interfaz_Dataset.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    story = []
    styles = getSampleStyleSheet()

    # Estilos tipográficos personalizados
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#0f172a')
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#475569')
    )

    institution_badge = ParagraphStyle(
        'InstBadge',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=colors.HexColor('#2563eb')
    )

    heading2_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#1e293b'),
        spaceBefore=10,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#334155'),
        alignment=4 # Justified
    )

    link_box_style = ParagraphStyle(
        'LinkBoxStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#15803d')
    )

    caption_style = ParagraphStyle(
        'CaptionStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11,
        alignment=1, # Center
        textColor=colors.HexColor('#64748b')
    )

    # 1. ENCABEZADO
    story.append(Paragraph("INSTITUTO POLITÉCNICO NACIONAL • ESCOM • VISIÓN ARTIFICIAL", institution_badge))
    story.append(Spacer(1, 4))
    story.append(Paragraph("NutriVision AI — Reporte de Interfaz y Dataset NOM-051", title_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("Asistente visual para detección y lectura de sellos de advertencia en productos comerciales", subtitle_style))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#2563eb'), spaceBefore=0, spaceAfter=10))

    # 2. TABLA DE METADATOS
    meta_data = [
        [
            Paragraph("<b>Materia:</b> Visión Artificial (6° Semestre)", body_style),
            Paragraph("<b>Estilo UI:</b> Neumorphism 2.0 & Liquid Glass", body_style)
        ],
        [
            Paragraph("<b>Entregable:</b> Cascarón Frontend & Enlace Dataset", body_style),
            Paragraph("<b>Stack:</b> Angular 22, TypeScript, SCSS", body_style)
        ]
    ]
    t_meta = Table(meta_data, colWidths=[270, 270])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#e2e8f0')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#f1f5f9')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 10))

    # 3. SECCIÓN: ENLACE AL DATASET
    story.append(Paragraph("1. Dataset de Entrenamiento y Validación (NOM-051)", heading2_style))
    dataset_html = """
    <b>Acceso al Dataset en Google Drive:</b><br/>
    <a href="https://drive.google.com/drive/folders/1uWbUXPamx7q5xCZVcEs3IdejmHt3pVDR" color="#15803d"><u>https://drive.google.com/drive/folders/1uWbUXPamx7q5xCZVcEs3IdejmHt3pVDR</u></a>
    <br/><br/>
    <font size="8.5" color="#166534">
    El repositorio contiene imágenes recopiladas de productos comerciales mexicanos con sellos oficiales de advertencia (Exceso de Azúcares, Exceso de Calorías, Exceso de Sodio, Exceso de Grasas Saturadas, Grasas Trans, Edulcorantes y Cafeína).
    </font>
    """
    t_dataset = Table([[Paragraph(dataset_html, link_box_style)]], colWidths=[540])
    t_dataset.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f0fdf4')),
        ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#86efac')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(t_dataset)
    story.append(Spacer(1, 10))

    # 4. SECCIÓN: EVIDENCIA DE LA INTERFAZ
    story.append(Paragraph("2. Evidencia de la Interfaz Interactiva (Cascarón Frontend)", heading2_style))
    story.append(Paragraph(
        "Se implementó el cascarón de la interfaz frontend con arquitectura modular por componentes. "
        "En la captura se evidencia la carga exitosa de un producto real (<i>Barra2.jpg</i>, 1.48 MB) donde se aprecian con claridad los sellos de advertencia en el empaque, junto con la estructura lista para recibir la inferencia del backend.",
        body_style
    ))
    story.append(Spacer(1, 6))

    img_path = "captura_interfaz.png"
    if os.path.exists(img_path):
        # Ancho disponible: 540 puntos (7.5 pulgadas)
        img_width = 540
        # Relación de aspecto de la captura (aprox 1100x480 -> 2.3:1)
        img_height = 235
        img = Image(img_path, width=img_width, height=img_height)
        t_img = Table([[img]], colWidths=[540])
        t_img.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 4),
            ('RIGHTPADDING', (0,0), (-1,-1), 4),
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc'))
        ]))
        story.append(t_img)
        story.append(Spacer(1, 4))
        story.append(Paragraph("<b>Figura 1:</b> Cascarón de NutriVision AI con carga y previsualización de producto comercial real y panel estructurado para inferencia.", caption_style))

    story.append(Spacer(1, 10))

    # 5. DESCRIPCIÓN DE COMPONENTES
    story.append(Paragraph("3. Especificaciones del Diseño Frontend", heading2_style))
    specs_data = [
        [
            Paragraph("<b>Visor Óptico Inteligente:</b><br/>Dropzone interactivo que permite arrastrar y soltar o seleccionar fotos de empaques. Enmarca la imagen con bordes de cristal líquido y permite cambiar o descartar el archivo.", body_style),
            Paragraph("<b>Panel de Resultados (Cascarón):</b><br/>Estructura con tarjetas neumórficas 2.0 y botón <i>'Analizar con Visión Artificial'</i>, preparado para consumir la API REST en Python (FastAPI/YOLO).", body_style)
        ],
        [
            Paragraph("<b>Estilo Liquid Glass:</b><br/>Superficies translúcidas con desenfoque óptico (<i>backdrop-filter</i>), doble bisel especular y sensación de grosor milimétrico.", body_style),
            Paragraph("<b>Neumorphism 2.0 & Accesibilidad:</b><br/>Contraste selectivo en contornos para usuarios con baja visión, modo Alto Contraste y escalado de fuentes dinámico.", body_style)
        ]
    ]
    t_specs = Table(specs_data, colWidths=[265, 265])
    t_specs.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#e2e8f0')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_specs)

    doc.build(story)
    print(f"PDF generado exitosamente: {pdf_filename}")

if __name__ == "__main__":
    create_report()
