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
        leftMargin=32,
        rightMargin=32,
        topMargin=28,
        bottomMargin=28
    )

    story = []
    styles = getSampleStyleSheet()

    # Estilos tipográficos
    institution_badge = ParagraphStyle(
        'InstBadge',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#2563eb'),
        spaceAfter=2
    )

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#0f172a')
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#475569')
    )

    heading2_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#1e293b'),
        spaceBefore=6,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#334155')
    )

    body_bold_style = ParagraphStyle(
        'BodyBoldCustom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#1e293b')
    )

    link_box_style = ParagraphStyle(
        'LinkBoxStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#15803d')
    )

    caption_style = ParagraphStyle(
        'CaptionStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=10,
        alignment=1, # Center
        textColor=colors.HexColor('#64748b')
    )

    # 1. ENCABEZADO INSTITUCIONAL
    story.append(Paragraph("INSTITUTO POLITÉCNICO NACIONAL • ESCUELA SUPERIOR DE CÓMPUTO (ESCOM)", institution_badge))
    story.append(Paragraph("NutriVision AI — Reporte de Interfaz y Dataset NOM-051", title_style))
    story.append(Paragraph("Plataforma de Visión Artificial para asistencia a personas con debilidad visual", subtitle_style))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#2563eb'), spaceBefore=0, spaceAfter=6))

    # 2. METADATOS: ALUMNOS, MATERIA, SEMESTRE, GRUPO, TECNOLOGÍAS
    meta_data = [
        [
            Paragraph("<b>Alumnos:</b><br/>• Mejia Perez Emanuel Esau<br/>• Ana Andrea Dominguez Jimenez", body_style),
            Paragraph("<b>Materia:</b> Visión Artificial<br/><b>Semestre:</b> 5° Semestre &nbsp;&nbsp;|&nbsp;&nbsp; <b>Grupo:</b> 5BV1", body_style)
        ],
        [
            Paragraph("<b>Frontend:</b> Angular 22, TypeScript, SCSS<br/><b>Estilo UI:</b> Neumorphism 2.0 & Liquid Glass", body_style),
            Paragraph("<b>Backend (Inferencia):</b> Python (FastAPI, OpenCV, YOLO)<br/><b>Entregable:</b> Cascarón Frontend & Enlace Dataset", body_style)
        ]
    ]
    t_meta = Table(meta_data, colWidths=[274, 274])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 6))

    # 3. SECCIÓN: ENLACE AL DATASET
    story.append(Paragraph("1. Dataset de Entrenamiento y Validación (NOM-051)", heading2_style))
    dataset_html = """
    <b>Liga del Dataset en Google Drive:</b><br/>
    <a href="https://drive.google.com/drive/folders/1uWbUXPamx7q5xCZVcEs3IdejmHt3pVDR" color="#15803d"><u>https://drive.google.com/drive/folders/1uWbUXPamx7q5xCZVcEs3IdejmHt3pVDR</u></a>
    <br/>
    <font size="7.8" color="#166534">
    Repositorio con imágenes de productos comerciales en México que contienen sellos frontales de advertencia oficiales (Exceso de Azúcares, Calorías, Sodio, Grasas Saturadas, Grasas Trans, Edulcorantes y Cafeína).
    </font>
    """
    t_dataset = Table([[Paragraph(dataset_html, link_box_style)]], colWidths=[548])
    t_dataset.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f0fdf4')),
        ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor('#86efac')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_dataset)
    story.append(Spacer(1, 6))

    # 4. SECCIÓN: EVIDENCIA DE LA INTERFAZ
    story.append(Paragraph("2. Evidencia de la Interfaz Interactiva (Cascarón Frontend)", heading2_style))
    story.append(Paragraph(
        "Se desarrolló el cascarón de la interfaz en Angular con estética Liquid Glass y Neumorphism 2.0. "
        "En la captura se evidencia la carga de un producto real (<i>Barra2.jpg</i>, 1.48 MB) donde se aprecian con nitidez los sellos en el empaque, junto con la estructura de resultados lista para recibir la respuesta del backend en Python.",
        body_style
    ))
    story.append(Spacer(1, 4))

    img_path = "captura_interfaz.png"
    if os.path.exists(img_path):
        img_width = 548
        img_height = 230
        img = Image(img_path, width=img_width, height=img_height)
        t_img = Table([[img]], colWidths=[548])
        t_img.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ('LEFTPADDING', (0,0), (-1,-1), 3),
            ('RIGHTPADDING', (0,0), (-1,-1), 3),
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc'))
        ]))
        story.append(t_img)
        story.append(Spacer(1, 3))
        story.append(Paragraph("<b>Figura 1:</b> Cascarón de NutriVision AI con carga del producto real <i>Barra2.jpg</i> y panel estructurado para inferencia con backend en Python.", caption_style))

    story.append(Spacer(1, 6))

    # 5. ESPECIFICACIONES TÉCNICAS
    story.append(Paragraph("3. Arquitectura y Vinculación con el Backend en Python", heading2_style))
    specs_data = [
        [
            Paragraph("<b>Visor Óptico (Frontend Angular):</b><br/>Área de carga mediante selector de archivos o <i>drag & drop</i>. Enmarca la imagen con estética Liquid Glass y píldora con nombre y tamaño de archivo.", body_style),
            Paragraph("<b>Panel de Resultados y Conexión Backend:</b><br/>Cascarón estructurado con botón neumórfico 2.0 <i>'Analizar con Visión Artificial'</i> preparado para enviar la imagen vía HTTP POST hacia el servidor en Python.", body_style)
        ],
        [
            Paragraph("<b>Backend en Python (Próxima Etapa):</b><br/>Servicio en Python (FastAPI/OpenCV) para segmentación, extracción de regiones de interés (ROI) y clasificación de octágonos con YOLOv8.", body_style),
            Paragraph("<b>Accesibilidad para Discapacidad Visual:</b><br/>Modo Alto Contraste Asistivo (amarillo/negro), escalas de fuente dinámicas y estructura para síntesis de voz (Web Speech API).", body_style)
        ]
    ]
    t_specs = Table(specs_data, colWidths=[269, 269])
    t_specs.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_specs)

    doc.build(story)
    print(f"PDF generado exitosamente: {pdf_filename}")

if __name__ == "__main__":
    create_report()
