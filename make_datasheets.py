from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


out = Path("assets/datasheets")
out.mkdir(parents=True, exist_ok=True)

grades = {
    "pg-64-22-datasheet.pdf": (
        "PG 64-22",
        "General paving binder for standard traffic and regional climate requirements.",
    ),
    "pg-70-22-datasheet.pdf": (
        "PG 70-22",
        "Enhanced high-temperature performance for heavier traffic and tougher service conditions.",
    ),
    "pg-76-22-datasheet.pdf": (
        "PG 76-22",
        "Polymer modified binder for premium rutting resistance and demanding pavement sections.",
    ),
}

rows = [
    ("Flash Point", "deg C", "Min. 230", "AASHTO T48"),
    ("Viscosity @135 deg C", "Pa.s", "Max. 3.0", "AASHTO T316"),
    ("Dynamic Shear, original binder", "kPa", "Min. 1.0", "AASHTO T315"),
    ("Mass change, RTFO residue", "%Wt", "Max. 1.0", "AASHTO T240"),
    ("Dynamic Shear, RTFO residue", "kPa", "Min. 2.2", "AASHTO T315"),
    ("PAV Temperature", "deg C", "100", "AASHTO R28"),
    ("Dynamic Shear, PAV residue", "kPa", "Max. 5000", "AASHTO T315"),
    ("Creep Stiffness, S value", "MPa", "Max. 300", "AASHTO T313"),
    ("Creep Stiffness, M value", "", "Min. 0.30", "AASHTO T313"),
    ("Direct Tension failure strain", "%", "Min. 1.0", "AASHTO T314"),
]

for filename, (grade, description) in grades.items():
    pdf = canvas.Canvas(str(out / filename), pagesize=letter)
    width, height = letter
    pdf.setFillColor(colors.white)
    pdf.rect(0, 0, width, height, fill=1, stroke=0)
    pdf.setFillColor(colors.HexColor("#08213f"))
    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawString(0.7 * inch, height - 0.72 * inch, f"Polysan {grade}")
    pdf.setFont("Helvetica", 10.5)
    pdf.drawString(0.7 * inch, height - 0.98 * inch, "Product Data Sheet | Polymer Modified Asphalt Binder")
    pdf.setStrokeColor(colors.HexColor("#d7ecff"))
    pdf.setLineWidth(1)
    pdf.line(0.65 * inch, height - 1.22 * inch, 7.85 * inch, height - 1.22 * inch)

    y = height - 1.62 * inch
    pdf.setFillColor(colors.HexColor("#08213f"))
    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(0.7 * inch, y, "Applications")
    pdf.setFont("Helvetica", 10)
    pdf.drawString(0.7 * inch, y - 0.25 * inch, description)

    y -= 0.75 * inch
    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(0.7 * inch, y, "Specification Summary")
    y -= 0.28 * inch
    pdf.setFont("Helvetica-Bold", 8.5)
    columns = [0.7 * inch, 3.8 * inch, 4.55 * inch, 5.7 * inch]
    pdf.setFillColor(colors.HexColor("#f8fbff"))
    pdf.rect(0.65 * inch, y - 0.07 * inch, 7.2 * inch, 0.24 * inch, fill=1, stroke=0)
    pdf.setFillColor(colors.HexColor("#08213f"))
    for x, header in zip(columns, ["Characteristics", "Unit", "Limits", "Test Methods"]):
        pdf.drawString(x, y, header)
    y -= 0.15 * inch
    pdf.line(0.7 * inch, y, 7.7 * inch, y)
    y -= 0.22 * inch
    pdf.setFont("Helvetica", 8.5)
    for index, row in enumerate(rows):
        if index % 2:
            pdf.setFillColor(colors.HexColor("#f8fbff"))
            pdf.rect(0.65 * inch, y - 0.07 * inch, 7.2 * inch, 0.2 * inch, fill=1, stroke=0)
        pdf.setFillColor(colors.HexColor("#08213f"))
        for x, value in zip(columns, row):
            pdf.drawString(x, y, value)
        y -= 0.24 * inch

    y -= 0.2 * inch
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(0.7 * inch, y, "Batch Results")
    pdf.setFont("Helvetica", 9)
    pdf.drawString(
        0.7 * inch,
        y - 0.24 * inch,
        "Actual result values are reported on the certified laboratory COA for each production batch.",
    )
    pdf.setStrokeColor(colors.HexColor("#d7ecff"))
    pdf.line(0.65 * inch, 0.85 * inch, 7.85 * inch, 0.85 * inch)
    pdf.setFillColor(colors.HexColor("#4b6681"))
    pdf.drawString(0.7 * inch, 0.6 * inch, "Polysan | Origin Baltimore Terminals | Baltimore, MD")
    pdf.save()
