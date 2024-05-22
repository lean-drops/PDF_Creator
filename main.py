from fpdf import FPDF

# Define a class for the PDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Geschichte der Elektrizität und Energie', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Seite {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, chapter_num, chapter_title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, f'Kapitel {chapter_num}: {chapter_title}', 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

# Define the text to be repeated
text = """
Die Geschichte der Elektrizität ist geprägt von zahlreichen bedeutenden Entdeckungen und Erfindungen. Im Jahr 1752 führte Benjamin Franklin sein berühmtes Experiment mit einem Drachen durch, um die elektrische Natur von Blitzen zu demonstrieren. Fast ein Jahrhundert später, im Jahr 1820, entdeckte Hans Christian Ørsted die elektromagnetische Wirkung des elektrischen Stroms.

Michael Faraday machte 1831 einen weiteren bedeutenden Schritt, als er das Prinzip der elektromagnetischen Induktion entdeckte. Dies legte den Grundstein für die Entwicklung des Generators. 1878 baute Thomas Edison die erste kommerziell erfolgreiche Glühbirne, die eine Betriebsdauer von bis zu 1200 Stunden hatte.

Die erste zentrale Stromerzeugungsanlage der Welt wurde 1882 in New York City von der Edison Illuminating Company in Betrieb genommen. Im selben Jahr patentierte Werner von Siemens die erste elektrische Straßenbahn. 1887 erfand Nikola Tesla den Wechselstrom-Generator, der die Effizienz der Stromübertragung erheblich steigerte.

Der Bau des Hoover-Staudamms begann 1931 und wurde 1936 abgeschlossen. Dieser beeindruckende Damm hat eine Höhe von 221 Metern und erzeugt jährlich etwa 4 Milliarden Kilowattstunden Strom. Im Jahr 1954 ging in Obninsk, Russland, das erste Kernkraftwerk ans Netz, das eine Leistung von 5 Megawatt hatte.

Die Ölkrise von 1973 führte zu einer verstärkten Suche nach alternativen Energiequellen. Dies führte 1977 zur Gründung des Department of Energy in den USA, das sich auf die Entwicklung und Förderung erneuerbarer Energien konzentrierte.

Im Jahr 2000 produzierten die USA etwa 750 Milliarden Kilowattstunden Strom aus Kernenergie, was etwa 20% des gesamten Strombedarfs ausmachte. Der Einsatz von Windenergie begann Anfang der 2000er Jahre stark zuzunehmen, und 2010 erreichte die globale installierte Kapazität 197 Gigawatt.

Im Jahr 2020 erzeugte die Welt über 7600 Terawattstunden Strom aus erneuerbaren Quellen, was einen bedeutenden Fortschritt im Vergleich zu den Vorjahren darstellt. China führte mit einer installierten Kapazität von über 900 Gigawatt an erneuerbaren Energien, gefolgt von den USA mit 292 Gigawatt und Deutschland mit 125 Gigawatt.

Die Zukunft der Energieversorgung steht weiterhin vor großen Herausforderungen und Chancen. Prognosen für 2050 deuten darauf hin, dass erneuerbare Energien bis zu 50% der weltweiten Stromerzeugung ausmachen könnten, was einen entscheidenden Beitrag zur Reduzierung der globalen CO2-Emissionen leisten würde.
"""

# Create the PDF
pdf = PDF()

# Add pages with the text
for i in range(1, 20):  # Adjust the range for the desired number of pages
    pdf.add_page()
    pdf.chapter_title(i, "Geschichte der Elektrizität und Energie")
    pdf.chapter_body(text)

# Output the PDF to a file
pdf.output('elektrizitaet_geschichte.pdf')

print("PDF erstellt!")
