import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

# Target Carousel Dimensions: 4:5 Aspect Ratio (1080px x 1350px equivalent in points)
# 1080 / 1.3333 = 810 pt width, 1350 / 1.3333 = 1012.5 pt height
PAGE_WIDTH = 810
PAGE_HEIGHT = 1012.5

# Color Palette (Minimal Modern Dark Mode)
BG_COLOR = colors.HexColor("#0f172a")        # Deep Dark Slate
CARD_BG = colors.HexColor("#1e293b")         # Obsidian Card Surface
BORDER_COLOR = colors.HexColor("#334155")    # Subtle Slate Border
ACCENT_CYAN = colors.HexColor("#38bdf8")     # Soft Cyan
ACCENT_BLUE = colors.HexColor("#6366f1")     # Soft Indigo
ACCENT_GREEN = colors.HexColor("#34d399")    # Emerald Accent
TEXT_WHITE = colors.HexColor("#f8fafc")      # Pure White Title
TEXT_MUTED = colors.HexColor("#94a3b8")      # Readable Secondary Text
TEXT_DIM = colors.HexColor("#64748b")        # Darker Muted Text
CODE_BG = colors.HexColor("#090d16")         # Pure dark for code blocks

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_decorations(self, page_count):
        # Draw Background
        self.setFillColor(BG_COLOR)
        self.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)
        
        # Subtle top accent bar
        self.setFillColor(ACCENT_CYAN)
        self.rect(0, PAGE_HEIGHT - 6, PAGE_WIDTH, 6, fill=True, stroke=False)
        
        # Footer Bar
        self.setStrokeColor(BORDER_COLOR)
        self.setLineWidth(1)
        self.line(50, 60, PAGE_WIDTH - 50, 60)
        
        # Footer Text
        self.setFont("Helvetica-Bold", 12)
        self.setFillColor(TEXT_WHITE)
        self.drawString(50, 38, "Bharath Krishnan")
        
        self.setFont("Helvetica", 11)
        self.setFillColor(TEXT_MUTED)
        self.drawString(175, 38, "•   Software Engineering Intern   •   AI Coding Tutor Project")
        
        page_str = f"Slide {self._pageNumber} of {page_count}"
        self.setFont("Helvetica-Bold", 11)
        self.setFillColor(ACCENT_CYAN)
        self.drawRightString(PAGE_WIDTH - 50, 38, page_str)

def build_pdf(filename="AI_Coding_Tutor_LinkedIn_Carousel.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=(PAGE_WIDTH, PAGE_HEIGHT),
        leftMargin=55,
        rightMargin=55,
        topMargin=50,
        bottomMargin=80
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Typography Styles
    badge_style = ParagraphStyle(
        'BadgeStyle',
        fontName='Helvetica-Bold',
        fontSize=11,
        textColor=ACCENT_CYAN,
        spaceAfter=15,
        textTransform='uppercase'
    )
    
    title_style = ParagraphStyle(
        'MainTitle',
        fontName='Helvetica-Bold',
        fontSize=34,
        leading=42,
        textColor=TEXT_WHITE,
        spaceAfter=15
    )
    
    subtitle_style = ParagraphStyle(
        'SubTitle',
        fontName='Helvetica',
        fontSize=17,
        leading=25,
        textColor=TEXT_MUTED,
        spaceAfter=30
    )

    section_header_style = ParagraphStyle(
        'SectionHeader',
        fontName='Helvetica-Bold',
        fontSize=26,
        leading=34,
        textColor=TEXT_WHITE,
        spaceAfter=20
    )
    
    body_style = ParagraphStyle(
        'BodyTextCustom',
        fontName='Helvetica',
        fontSize=14,
        leading=22,
        textColor=TEXT_MUTED,
        spaceAfter=12
    )

    body_white = ParagraphStyle(
        'BodyWhite',
        fontName='Helvetica',
        fontSize=14,
        leading=22,
        textColor=TEXT_WHITE,
        spaceAfter=10
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        fontName='Courier',
        fontSize=12,
        leading=18,
        textColor=ACCENT_GREEN
    )

    story = []

    # -------------------------------------------------------------------------
    # SLIDE 1: COVER
    # -------------------------------------------------------------------------
    story.append(Spacer(1, 100))
    story.append(Paragraph("INTERNSHIP PROJECT SHOWCASE", badge_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Building an AI Coding Tutor<br/>From Scratch", title_style))
    story.append(Spacer(1, 15))
    story.append(Paragraph(
        "How I engineered a full-stack educational app (React + Django REST + Gemini AI) "
        "to turn raw error messages into structured, beginner-friendly learning experiences.",
        subtitle_style
    ))
    story.append(Spacer(1, 40))
    
    # Hero Card
    hero_content = [
        [Paragraph("<font color='#38bdf8'><b>THE INTERNSHIP MISSION</b></font>", body_white)],
        [Paragraph(
            "Beginners learning Python often get stuck on cryptic error messages. "
            "My goal was to build a tool that doesn't just fix code, but teaches the developer "
            "<i>why</i> it broke and how to master the underlying concept.",
            body_style
        )]
    ]
    hero_table = Table(hero_content, colWidths=[PAGE_WIDTH - 110])
    hero_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 25),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,0), 5),
    ]))
    story.append(hero_table)
    story.append(PageBreak())

    # -------------------------------------------------------------------------
    # SLIDE 2: THE PROBLEM & WHY I BUILT IT
    # -------------------------------------------------------------------------
    story.append(Paragraph("01. THE PROBLEM", badge_style))
    story.append(Paragraph("Why Standard Debugging Fails Beginners", section_header_style))
    story.append(Spacer(1, 15))
    
    card1_data = [
        [Paragraph("<b>1. Raw Tracebacks are Intimidating</b>", body_white)],
        [Paragraph("Messages like <code>IndentationError: unexpected unindent</code> or <code>KeyError: 'id'</code> confuse early learners without providing context or actionable guidance.", body_style)]
    ]
    t1 = Table(card1_data, colWidths=[PAGE_WIDTH - 110])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 20),
    ]))
    story.append(t1)
    story.append(Spacer(1, 20))

    card2_data = [
        [Paragraph("<b>2. Generic AI Chat Dumps Answers</b>", body_white)],
        [Paragraph("Asking standard LLM chatbots often returns a full refactored script. The beginner copies & pastes it without understanding the root bug.", body_style)]
    ]
    t2 = Table(card2_data, colWidths=[PAGE_WIDTH - 110])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 20),
    ]))
    story.append(t2)
    story.append(Spacer(1, 20))

    card3_data = [
        [Paragraph("<b>3. The Internship Solution: Guided AI Feedback</b>", ParagraphStyle('GreenHeader', parent=body_white, textColor=ACCENT_GREEN))],
        [Paragraph("Build a dedicated tutor interface that breaks down feedback into 6 distinct sections: Analysis, Mistakes, Simple Explanation, Corrected Snippet, Core Concept, and Practice Exercises.", body_style)]
    ]
    t3 = Table(card3_data, colWidths=[PAGE_WIDTH - 110])
    t3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
        ('BOX', (0,0), (-1,-1), 1.5, ACCENT_GREEN),
        ('PADDING', (0,0), (-1,-1), 20),
    ]))
    story.append(t3)
    story.append(PageBreak())

    # -------------------------------------------------------------------------
    # SLIDE 3: SYSTEM ARCHITECTURE
    # -------------------------------------------------------------------------
    story.append(Paragraph("02. ARCHITECTURE", badge_style))
    story.append(Paragraph("Decoupled Full-Stack System", section_header_style))
    story.append(Spacer(1, 10))
    
    # Diagram Table
    diag_data = [
        [
            Paragraph("<font color='#38bdf8'><b>REACT 19 FRONTEND</b></font><br/><font color='#94a3b8' size=11>Vite + Tailwind CSS<br/>Code Editor & Prism Highlighter</font>", TA_CENTER_style if 'TA_CENTER_style' in locals() else ParagraphStyle('C1', parent=body_style, alignment=TA_CENTER)),
            Paragraph("<font color='#6366f1'><b>DJANGO REST API</b></font><br/><font color='#94a3b8' size=11>Python 3.12 + DRF<br/>Endpoint: /api/analyze/</font>", ParagraphStyle('C2', parent=body_style, alignment=TA_CENTER)),
            Paragraph("<font color='#34d399'><b>GEMINI 2.5 FLASH</b></font><br/><font color='#94a3b8' size=11>Google Gemini API<br/>System Prompt Guardrails</font>", ParagraphStyle('C3', parent=body_style, alignment=TA_CENTER))
        ]
    ]
    diag_table = Table(diag_data, colWidths=[220, 220, 220])
    diag_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CODE_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 20),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(diag_table)
    story.append(Spacer(1, 25))

    arch_bullets = [
        [Paragraph("<b>Frontend (Client Layer):</b> Built with React 19 and Tailwind CSS. Features a clean code editor component with live syntax highlighting and responsive glassmorphism UI.", body_style)],
        [Paragraph("<b>Backend (API Layer):</b> Django REST Framework handles incoming code payloads, CORS verification, environment secrets, and forwards requests to Gemini AI.", body_style)],
        [Paragraph("<b>AI Layer (Intelligence):</b> Uses <code>gemini-2.5-flash</code> with strict system instructions to guarantee a structured 6-section educational response.", body_style)]
    ]
    arch_table = Table(arch_bullets, colWidths=[PAGE_WIDTH - 110])
    arch_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 18),
        ('LINEBELOW', (0,0), (-1,-2), 0.5, BORDER_COLOR),
    ]))
    story.append(arch_table)
    story.append(PageBreak())

    # -------------------------------------------------------------------------
    # SLIDE 4: PROMPT ENGINEERING & GUARDRAILS
    # -------------------------------------------------------------------------
    story.append(Paragraph("03. AI INTEGRATION", badge_style))
    story.append(Paragraph("Enforcing Structured AI Responses", section_header_style))
    story.append(Spacer(1, 10))

    story.append(Paragraph(
        "Raw AI outputs are unpredictable. To turn an LLM into a reliable tutor, "
        "I engineered a strict system prompt inside <code>backend/api/analyzer.py</code> "
        "that forces the output into a predictable 6-section schema:",
        body_style
    ))
    story.append(Spacer(1, 15))

    code_snippet = (
        "<font color='#6366f1'># Excerpt from CodeAnalyzer (backend/api/analyzer.py)</font><br/>"
        "<font color='#f8fafc'>SYSTEM_PROMPT = \"\"\"</font><br/>"
        "You are an expert, patient Python tutor for absolute beginners.<br/>"
        "Analyze the provided code and return EXACTLY these 6 sections:<br/>"
        "<font color='#38bdf8'>1. CODE ANALYSIS</font> - High-level summary of intent<br/>"
        "<font color='#38bdf8'>2. MISTAKES FOUND</font> - Bullet points of errors<br/>"
        "<font color='#38bdf8'>3. BEGINNER EXPLANATION</font> - Simple plain-English breakdown<br/>"
        "<font color='#38bdf8'>4. CORRECTED CODE</font> - Clean, idiomatic Python block<br/>"
        "<font color='#38bdf8'>5. KEY CONCEPT</font> - Core computer science rule<br/>"
        "<font color='#38bdf8'>6. PRACTICE EXERCISES</font> - 2 tailored mini-challenges<br/>"
        "<font color='#f8fafc'>\"\"\"</font>"
    )
    
    code_table = Table([[Paragraph(code_snippet, code_style)]], colWidths=[PAGE_WIDTH - 110])
    code_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CODE_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 20),
    ]))
    story.append(code_table)
    story.append(Spacer(1, 20))

    story.append(Paragraph(
        "<b>Why this matters:</b> By enforcing markdown structural headers, the React frontend can reliably render each section using custom components and Prism syntax highlighting without parsing errors.",
        body_style
    ))
    story.append(PageBreak())

    # -------------------------------------------------------------------------
    # SLIDE 5: USER EXPERIENCE & INTERFACE DESIGN
    # -------------------------------------------------------------------------
    story.append(Paragraph("04. USER EXPERIENCE", badge_style))
    story.append(Paragraph("Minimalist, Developer-First UI", section_header_style))
    story.append(Spacer(1, 15))

    ux_card1 = [
        [Paragraph("<font color='#38bdf8'><b>1. Minimal Visual Noise</b></font>", body_white)],
        [Paragraph("Designed with Tailwind CSS using dark slate palette (<code>#0f172a</code>) and soft glassmorphism containers to keep focus entirely on code comprehension.", body_style)]
    ]
    u1 = Table(ux_card1, colWidths=[PAGE_WIDTH - 110])
    u1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 20),
    ]))
    story.append(u1)
    story.append(Spacer(1, 20))

    ux_card2 = [
        [Paragraph("<font color='#6366f1'><b>2. Reactive Markdown & Syntax Highlighting</b></font>", body_white)],
        [Paragraph("Integrated <code>react-markdown</code> and <code>react-syntax-highlighter (Prism)</code> so AI-generated code blocks render with crisp, color-coded syntax.", body_style)]
    ]
    u2 = Table(ux_card2, colWidths=[PAGE_WIDTH - 110])
    u2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 20),
    ]))
    story.append(u2)
    story.append(Spacer(1, 20))

    ux_card3 = [
        [Paragraph("<font color='#34d399'><b>3. Active Learning Practice Loops</b></font>", body_white)],
        [Paragraph("Rather than passive reading, every analysis includes interactive practice questions so the user immediately applies what they just learned.", body_style)]
    ]
    u3 = Table(ux_card3, colWidths=[PAGE_WIDTH - 110])
    u3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 20),
    ]))
    story.append(u3)
    story.append(PageBreak())

    # -------------------------------------------------------------------------
    # SLIDE 6: LESSONS LEARNED
    # -------------------------------------------------------------------------
    story.append(Paragraph("05. INTERNSHIP LESSONS", badge_style))
    story.append(Paragraph("3 Key Takeaways from the Build", section_header_style))
    story.append(Spacer(1, 15))

    l1 = [
        [Paragraph("<font color='#38bdf8'><b>1. Guardrails make LLMs reliable software components</b></font>", body_white)],
        [Paragraph("An AI API call without strict system prompts is unpredictable. Adding structured schemas transforms an generative LLM into a dependable API backend.", body_style)]
    ]
    lt1 = Table(l1, colWidths=[PAGE_WIDTH - 110])
    lt1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 20),
    ]))
    story.append(lt1)
    story.append(Spacer(1, 20))

    l2 = [
        [Paragraph("<font color='#6366f1'><b>2. Clean API boundaries simplify frontend state</b></font>", body_white)],
        [Paragraph("Decoupling Django REST from React allowed me to isolate loading states, handle error boundaries gracefully, and test API responses independently.", body_style)]
    ]
    lt2 = Table(l2, colWidths=[PAGE_WIDTH - 110])
    lt2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 20),
    ]))
    story.append(lt2)
    story.append(Spacer(1, 20))

    l3 = [
        [Paragraph("<font color='#34d399'><b>3. Developer Experience is User Experience</b></font>", body_white)],
        [Paragraph("Thoughtful details—like syntax highlighting, subtle micro-animations, and structured section layout—make a huge difference in learning engagement.", body_style)]
    ]
    lt3 = Table(l3, colWidths=[PAGE_WIDTH - 110])
    lt3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 20),
    ]))
    story.append(lt3)
    story.append(PageBreak())

    # -------------------------------------------------------------------------
    # SLIDE 7: PROJECT HANDOFF & REPO CTA
    # -------------------------------------------------------------------------
    story.append(Paragraph("06. INTERNSHIP HANDOFF", badge_style))
    story.append(Paragraph("Project Completed & Pushed to GitHub", section_header_style))
    story.append(Spacer(1, 15))

    final_card = [
        [Paragraph("<font color='#34d399'><b>PROJECT STATUS: SHIPPED</b></font>", body_white)],
        [Paragraph("The full-stack AI Coding Tutor codebase, Django API setup, React client, and technical documentation are complete and published.", body_style)],
        [Spacer(1, 10)],
        [Paragraph("<font color='#38bdf8'><b>GITHUB REPOSITORY</b></font>", body_white)],
        [Paragraph("<code>github.com/bharathkrish2608/ai-coding-tutor</code>", code_style)],
        [Spacer(1, 10)],
        [Paragraph("<b>What's included in the repository:</b><br/>"
                   "• Complete Django REST backend & Gemini API integration<br/>"
                   "• React 19 + Vite frontend with Tailwind styling<br/>"
                   "• Detailed technical setup guide & system prompt schemas", body_style)]
    ]
    ft = Table(final_card, colWidths=[PAGE_WIDTH - 110])
    ft.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
        ('BOX', (0,0), (-1,-1), 1.5, ACCENT_CYAN),
        ('PADDING', (0,0), (-1,-1), 25),
    ]))
    story.append(ft)
    story.append(Spacer(1, 30))

    closing_text = Paragraph(
        "<font color='#f8fafc'><b>Thank you for reading!</b></font><br/>"
        "<font color='#94a3b8'>If you're interested in AI developer tools or full-stack web applications, "
        "feel free to check out the repo or connect with me here on LinkedIn.</font>",
        ParagraphStyle('Closing', parent=body_style, alignment=TA_CENTER)
    )
    story.append(closing_text)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully generated: {filename}")

if __name__ == "__main__":
    build_pdf()
