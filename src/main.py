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
        self.cell(text='Urlaubsantrag', fill=True, h=6, new_x=XPos.LMARGIN)
        self.set_font(size=12, style='')

        self.set_y(50)
        self.write(text='Name / Vorname: ')
        self.set_font(style='B')
        self.cell(text=self.full_name, new_x=XPos.LMARGIN)
        self.set_font(style='')

        self.set_y(self.get_y() + 15)
        self.write(text='Anspruch zum Zeitpunkt des Antrags: ')
        self.set_font(style='B')
        self.cell(text=args.available_vacation_days + ' Tage', new_x=XPos.LMARGIN)
        self.set_font(style='')

        self.set_y(self.get_y() + 10)
        self.write(text='Ich beantrage Urlaub vom ')
        self.set_font(style='B')
        self.write(text=args.date_from)
        self.set_font(style='')
        self.write(text=' bis ')
        self.set_font(style='B')
        self.cell(text=args.date_to, new_x=XPos.LMARGIN)
        self.set_font(style='')

        self.set_y(self.get_y() + 10)
        self.write(text='Insgesamt: ')
        self.set_font(style='B')
        self.cell(text=args.planned_vacation_days + ' Tag(e)', new_x=XPos.LMARGIN)
        self.set_font(style='')

        self.set_y(self.get_y() + 10)
        self.write(text='Verbleibender Resturlaub: ')
        self.set_font(style='B')
        self.cell(text=str(int(args.available_vacation_days) - int(args.planned_vacation_days)) + ' Tage', new_x=XPos.LMARGIN)
        self.set_font(style='')

        self.set_y(self.get_y() + 30)
        self.cell(text='Osnabrück, ' + date.today().strftime('%d.%m.%Y'), border='B', w=60)
        self.set_y(self.get_y() - 10)
        self.set_x(105)
        self.cell(link=self.image('./signature.png', w=37), border='B', w=60, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_y(self.get_y() + 1)
        self.cell(text='Ort, Datum')
        self.set_x(105)
        self.cell(text='Unterschrift Antragsteller', new_x=XPos.LMARGIN)

        self.set_y(self.get_y() + 30)
        self.cell(text='Der Antrag wird genehmigt', h=6)
        self.set_x(80)
        self.cell(text='X', border=1, fill=True, h=6, w=6, align='C', new_x=XPos.LMARGIN)

        self.set_y(self.get_y() + 10)
        self.cell(text='Der Antrag wird abgelehnt', h=6)
        self.set_x(80)
        self.cell(text=' ', border=1, fill=True, h=6, w=6, align='C', new_x=XPos.LMARGIN)

        self.set_y(self.get_y() + 30)
        self.cell(text=' ', border='B', w=60)
        self.set_x(105)
        self.cell(text=' ', border='B', w=60, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_y(self.get_y() + 1)
        self.cell(text='Ort, Datum')
        self.set_x(105)
        self.cell(text='Unterschrift Vorgesetzter', new_x=XPos.LMARGIN)

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
    args = parser.parse_args()
    pdf.generate(args)
    pdf.output('out/urlaub_sebastian-adamczyk_' + args.date_from + '-' + args.date_to + '.pdf')

if __name__ == "__main__":
    generate()
