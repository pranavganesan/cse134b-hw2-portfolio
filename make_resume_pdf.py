from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

styles = getSampleStyleSheet()
doc = SimpleDocTemplate("assets/resume-placeholder.pdf", pagesize=letter)
story = [
    Paragraph("Pranav Ganesan", styles["Title"]),
    Paragraph("prganesan@ucsd.edu &middot; github.com/pranavganesan", styles["Normal"]),
    Spacer(1, 14),
    Paragraph("Education", styles["Heading2"]),
    Paragraph("B.S. Computer Science, University of California San Diego (expected 2028)", styles["Normal"]),
    Spacer(1, 10),
    Paragraph("Skills", styles["Heading2"]),
    Paragraph("HTML5, CSS3, JavaScript/TypeScript, Python, Git", styles["Normal"]),
    Spacer(1, 10),
    Paragraph("Projects", styles["Heading2"]),
    Paragraph("Campus Event Finder, Habit Tracker, Recipe Box. See portfolio for details.", styles["Normal"]),
    Spacer(1, 14),
    Paragraph("This is a placeholder resume generated for HW2 Phase 1/2. A finished version will replace it by HW3.", styles["Italic"]),
]
doc.build(story)
print("resume placeholder written")
