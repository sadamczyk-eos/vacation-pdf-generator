#!/usr/bin/env python3

import argparse
from fpdf import FPDF, XPos, YPos
from datetime import date

class PDF(FPDF):
    full_name = 'Adamczyk, Sebastian'

    def generate(self, args):
        self.add_page()

        self.set_font(family='Helvetica', size=16, style='B')
        self.set_fill_color(200)
        self.cell(txt='Urlaubsantrag', fill=True, h=6, new_x=XPos.LMARGIN)
        self.set_font(size=12, style='')

        self.set_y(50)
        self.write(txt='Name / Vorname: ')
        self.set_font(style='B')
        self.cell(txt=self.full_name, new_x=XPos.LMARGIN)
        self.set_font(style='')

        self.set_y(self.get_y() + 15)
        self.write(txt='Anspruch zum Zeitpunkt des Antrags: ')
        self.set_font(style='B')
        self.cell(txt=args.available_vacation_days + ' Tage', new_x=XPos.LMARGIN)
        self.set_font(style='')

        self.set_y(self.get_y() + 10)
        self.write(txt='Ich beantrage Urlaub vom ')
        self.set_font(style='B')
        self.write(txt=args.date_from)
        self.set_font(style='')
        self.write(txt=' bis ')
        self.set_font(style='B')
        self.cell(txt=args.date_to, new_x=XPos.LMARGIN)
        self.set_font(style='')

        self.set_y(self.get_y() + 10)
        self.write(txt='Insgesamt: ')
        self.set_font(style='B')
        self.cell(txt=args.planned_vacation_days + ' Tag(e)', new_x=XPos.LMARGIN)
        self.set_font(style='')

        self.set_y(self.get_y() + 10)
        self.write(txt='Verbleibender Resturlaub: ')
        self.set_font(style='B')
        self.cell(txt=str(int(args.available_vacation_days) - int(args.planned_vacation_days)) + ' Tage', new_x=XPos.LMARGIN)
        self.set_font(style='')

        self.set_y(self.get_y() + 30)
        self.cell(txt='Osnabrück, ' + date.today().strftime('%d.%m.%Y'), border='B', w=60)
        self.set_y(self.get_y() - 10)
        self.set_x(105)
        self.cell(link=self.image('./signature.png', w=37), border='B', w=60, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_y(self.get_y() + 1)
        self.cell(txt='Ort, Datum')
        self.set_x(105)
        self.cell(txt='Unterschrift Antragsteller', new_x=XPos.LMARGIN)

        self.set_y(self.get_y() + 30)
        self.cell(txt='Der Antrag wird genehmigt', h=6)
        self.set_x(80)
        self.cell(txt='X', border=1, fill=True, h=6, w=6, align='C', new_x=XPos.LMARGIN)

        self.set_y(self.get_y() + 10)
        self.cell(txt='Der Antrag wird abgelehnt', h=6)
        self.set_x(80)
        self.cell(txt=' ', border=1, fill=True, h=6, w=6, align='C', new_x=XPos.LMARGIN)

        self.set_y(self.get_y() + 30)
        self.cell(txt=' ', border='B', w=60)
        self.set_x(105)
        self.cell(txt=' ', border='B', w=60, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_y(self.get_y() + 1)
        self.cell(txt='Ort, Datum')
        self.set_x(105)
        self.cell(txt='Unterschrift Vorgesetzter', new_x=XPos.LMARGIN)

def generate():
    parser = argparse.ArgumentParser(
        prog='Vacation',
        description='Generate vacation PDF'
    )
    parser.add_argument('date_from')
    parser.add_argument('date_to')
    parser.add_argument('available_vacation_days')
    parser.add_argument('planned_vacation_days')

    pdf = PDF('P', 'mm', 'A4')
    pdf.set_author('Sebastian Adamczyk')
    pdf.set_title('Urlaubsantrag')
    pdf.set_margins(20, 20, 20)
    pdf.set_line_width(0.1)
    pdf.generate(parser.parse_args())
    pdf.output('out/vacation.pdf')

if __name__ == "__main__":
    generate()
