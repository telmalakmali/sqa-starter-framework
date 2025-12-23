from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

output_path = "../qa/entry_criteria.pdf"

# Layout Settings
LEFT_MARGIN = 72
RIGHT_MARGIN = 72
TOP_MARGIN = 800
BOTTOM_MARGIN = 72
LINE_HEIGHT = 20
CHECKBOX_SIZE = 11

# Exit Criteria Sections
sections = {
    "1. Test Execution": [
        "All planned test cases or checklists have been executed",
        "High-risk areas have been covered",
        "Regression tests for impacted areas are completed",
    ],
    "2. Defect Resolution": [
        "All critical defects are fixed and retested",
        "All major defects are fixed and retested",
        "Medium and minor defects are resolved or accepted for future release",
        "No open issues block core functionality",
    ],
    "3. Acceptance Criteria & Quality Benchmarks": [
        "All acceptance criteria defined in requirements are met",
        "No unexpected behaviour in core workflows",
        "Performance is acceptable for this release",
        "Usability is acceptable for the team",
    ],
    "4. Documentation Completion": [
        "Test results are recorded and stored",
        "Known issues are documented and communicated",
        "Release notes or defect summaries are prepared (if required)",
    ],
    "5. Build Stability Verification": [
        "Final build is stable in the test environment",
        "No recurring crashes or environment issues",
        "Integrations with other systems/modules function correctly",
    ],
    "6. Stakeholder Approval": [
        "QA engineer confirms testing is complete",
        "Product owner or team lead approves release readiness",
        "Remaining risks are communicated and accepted",
    ],
}

def create_pdf():
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    # ---- Title (centered) ----
    title = "Exit Criteria Checklist"
    c.setFont("Helvetica-Bold", 20)
    title_width = c.stringWidth(title, "Helvetica-Bold", 20)
    title_x = (width - title_width) / 2
    y = TOP_MARGIN
    c.drawString(title_x, y, title)

    # Subtitle
    y -= 26
    c.setFont("Times-Italic", 11)
    subtitle = "QA completion requirements before release"
    sub_width = c.stringWidth(subtitle, "Times-Italic", 11)
    sub_x = (width - sub_width) / 2
    c.drawString(sub_x, y, subtitle)

    y -= 40

    # ---- Checklist Sections ----
    for section_title, items in sections.items():
        c.setFont("Helvetica-Bold", 13)
        c.drawString(LEFT_MARGIN, y, section_title)
        y -= 22

        c.setFont("Times-Roman", 11)

        for item in items:
            # Checkbox (aligned)
            checkbox_x = LEFT_MARGIN
            checkbox_y = y - (CHECKBOX_SIZE / 2) + 3
            c.rect(checkbox_x, checkbox_y, CHECKBOX_SIZE, CHECKBOX_SIZE)

            # Text
            text_x = checkbox_x + CHECKBOX_SIZE + 8
            c.drawString(text_x, y, item)

            y -= LINE_HEIGHT

            # Auto page break
            if y < BOTTOM_MARGIN:
                c.showPage()
                y = TOP_MARGIN
                c.setFont("Helvetica-Bold", 16)
                c.drawString(LEFT_MARGIN, y, "Exit Criteria Checklist (cont.)")
                y -= 30
                c.setFont("Times-Roman", 11)

        y -= 12

    c.save()
    print("PDF created successfully at:", output_path)


if __name__ == "__main__":
    create_pdf()
