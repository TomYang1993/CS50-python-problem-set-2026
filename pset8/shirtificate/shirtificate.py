from fpdf import FPDF


def main():
    name = input("Name: ")

    pdf = FPDF(orientation="portrait", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font("helvetica", "B", 24)
    pdf.cell(0, 20, "CS50 Shirtificate", align="C")

    pdf.image("shirtificate.png", x=20, y=40, w=170)

    pdf.set_xy(0, 70)
    pdf.set_font("helvetica", "B", 18)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 20, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
