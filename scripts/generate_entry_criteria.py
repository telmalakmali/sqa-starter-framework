from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# Output file path
output_path = "../qa/entry_criteria.pdf"

# Layout settings
LEFT_MARGIN = 72
RIGHT_MARGIN = 72
TOP_MARGIN = 800
BOTTOM_MARGIN = 72
LINE_HEIGHT = 20            # More spacing between rows
CHECKBOX_SIZE = 11
INDENT = 20

# Entry Criteria Content
sections = {
    "1. Requirements, Acceptance Criteria, and Scope": [
        "User stories, requirements, or feature specifications are documented",
        "Acceptance criteria are clear and testable",
        "Edge cases and non-functional expectations are identified",
        "Scope boundaries are defined",
        "Changes to requirements are reviewed",
        "Stakeholders agree on success conditions",
    ],
    "2. Build and Environment Readiness": [
        "Latest build is deployed and stable",
        "Deployment steps completed successfully",
        "No build failures",
        "Environment configuration is correct",
        "Access and permissions provided",
        "Logs and monitoring tools available",
    ],
    "3. Test Data and Test Accounts": [
        "Test data prepared and valid",
        "Boundary and negative test values prepared",
        "Test accounts created",
        "External dependencies configured",
        "Mocks/stubs available if required",
    ],
    "4. Test Planning and Documentation": [
        "Test plan or checklist completed",
        "Test approach reviewed",
        "Risks and assumptions identified",
        "Required tools are ready",
        "Traceability between requirements and tests completed",
    ],
    "5. Communication and Readiness": [
        "Developer walkthrough completed",
        "Known limitations communicated",
        "Testing timelines agreed",
        "Defect assignment rules understood",
        "Communication channels confirmed",
        "Prior blockers reviewed",
    ],
    "6. Defect Status and Blockers": [
        "No critical unresolved defects",
        "No environment issues blocking testing",
        "Dependencies from other teams ready",
        "No merge conflicts affecting the build",
    ],
    "7. Compliance and Quality Checks": [
        "Security considerations reviewed",
        "Data privacy rules understood",
        "Code review completed",
        "Feature flags configured",
        "Logging/monitoring active",
    ],
}

# PDF Generator
def create_pdf():
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    # ---- Title (centered) ----
    title = "Entry Criteria Checklist"
    c.setFont("Helvetica-Bold", 20)
    title_width = c.stringWidth(title, "Helvetica-Bold", 20)
    title_x = (width - title_width) / 2
    y = TOP_MARGIN
    c.drawString(title_x, y, title)

    # Subtitle
    y -= 26
    c.setFont("Times-Italic", 11)
    subtitle = "QA readiness checklist for starting testing"
    sub_width = c.stringWidth(subtitle, "Times-Italic", 11)
    sub_x = (width - sub_width) / 2
    c.drawString(sub_x, y, subtitle)

    y -= 40  # spacing before sections

    # ---- Content Sections ----
    for section_title, items in sections.items():

        # Section Header
        c.setFont("Helvetica-Bold", 13)
        c.drawString(LEFT_MARGIN, y, section_title)
        y -= 22

        c.setFont("Times-Roman", 11)

        # Checklist items
        for item in items:

            # Checkbox aligned perfectly with text
            checkbox_x = LEFT_MARGIN
            checkbox_y = y - (CHECKBOX_SIZE / 2) + 3  # FIXED ALIGNMENT

            c.rect(checkbox_x, checkbox_y, CHECKBOX_SIZE, CHECKBOX_SIZE)

            text_x = checkbox_x + CHECKBOX_SIZE + 8
            c.drawString(text_x, y, item)

            y -= LINE_HEIGHT

            # If page bottom reached → new page
            if y < BOTTOM_MARGIN:
                c.showPage()
                y = TOP_MARGIN

                # Redraw continuation header on new page
                c.setFont("Helvetica-Bold", 16)
                c.drawString(LEFT_MARGIN, y, "Entry Criteria Checklist (cont.)")
                y -= 30
                c.setFont("Times-Roman", 11)

        y -= 12  # extra spacing between sections

    # Save PDF
    c.save()
    print("PDF created successfully at:", output_path)

# Run generator
if __name__ == "__main__":
    create_pdf()
