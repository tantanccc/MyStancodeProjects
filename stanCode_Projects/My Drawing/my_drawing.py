"""
File: my_drawing.py
Name: zoe
----------------------
TODO: Draw a cat
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: MyCat
    This is my cat called 'De De'.
    I hope one day in the future I can live as my cat, doing nothing just enjoy the life :D
    """
    window = GWindow(width=800, height=500, title='MyCat')

    label = GLabel('Live like a cat !', x=100, y=120)
    label.font = 'Helvetica-15-bold'
    label.color = 'black'
    window.add(label)

    poly1 = GPolygon()
    poly1.add_vertex((314.5, 175.51))
    poly1.add_vertex((365.06, 219.19))
    poly1.add_vertex((318.75, 216.55))
    window.add(poly1)
    poly1.filled = True
    poly1.fill_color = '#6F60AA'

    poly2 = GPolygon()
    poly2.add_vertex((318.75, 216.55))
    poly2.add_vertex((365.06, 219.19))
    poly2.add_vertex((366.78, 262.07))
    poly2.add_vertex((312.1, 261.84))
    poly2.add_vertex((296.5, 238.45))
    window.add(poly2)
    poly2.filled = True
    poly2.fill_color = '#AB5FA4'

    poly3 = GPolygon()
    poly3.add_vertex((296.5, 238.45))
    poly3.add_vertex((312.1, 261.84))
    poly3.add_vertex((290.31, 267.69))
    window.add(poly3)
    poly3.filled = True
    poly3.fill_color = '#B72AB1'

    poly4 = GPolygon()
    poly4.add_vertex((281.94, 282.02))
    poly4.add_vertex((281.94, 300.0191))
    poly4.add_vertex((274.949, 292.68))
    window.add(poly4)
    poly4.filled = True
    poly4.fill_color = '#874884'

    poly5 = GPolygon()
    poly5.add_vertex((290.31, 267.69))
    poly5.add_vertex((312.1, 261.84))
    poly5.add_vertex((335.828, 308.7325))
    poly5.add_vertex((296.39, 316.41))
    poly5.add_vertex((281.94, 300.0191))
    poly5.add_vertex((281.94, 282.02))
    window.add(poly5)
    poly5.filled = True
    poly5.fill_color = '#681B64'

    poly6 = GPolygon()
    poly6.add_vertex((312.1, 261.84))
    poly6.add_vertex((366.78, 262.07))
    poly6.add_vertex((335.828, 308.7325))
    window.add(poly6)
    poly6.filled = True
    poly6.fill_color = '#5B2759'

    poly7 = GPolygon()
    poly7.add_vertex((365.06, 219.19))
    poly7.add_vertex((417.15, 238.87))
    poly7.add_vertex((366.78, 262.07))
    window.add(poly7)
    poly7.filled = True
    poly7.fill_color = '#08456C'

    poly8 = GPolygon()
    poly8.add_vertex((366.78, 262.07))
    poly8.add_vertex((370.83, 330.75))
    poly8.add_vertex((335.828, 308.7325))
    window.add(poly8)
    poly8.filled = True
    poly8.fill_color = '#5B2759'

    poly9 = GPolygon()
    poly9.add_vertex((366.78, 262.07))
    poly9.add_vertex((412.87, 288.71))
    poly9.add_vertex((370.83, 330.75))
    window.add(poly9)
    poly9.filled = True
    poly9.fill_color = '#2F79A3'

    poly10 = GPolygon()
    poly10.add_vertex((366.78, 262.07))
    poly10.add_vertex((417.15, 238.87))
    poly10.add_vertex((412.87, 288.71))
    window.add(poly10)
    poly10.filled = True
    poly10.fill_color = '#158CCE'

    poly11 = GPolygon()
    poly11.add_vertex((417.15, 238.87))
    poly11.add_vertex((445.59, 242.08))
    poly11.add_vertex((412.87, 288.71))
    window.add(poly11)
    poly11.filled = True
    poly11.fill_color = '#2E7399'

    poly12 = GPolygon()
    poly12.add_vertex((445.59, 242.08))
    poly12.add_vertex((467.75, 288.55))
    poly12.add_vertex((412.87, 288.71))
    window.add(poly12)
    poly12.filled = True
    poly12.fill_color = '#345060'

    poly13 = GPolygon()
    poly13.add_vertex((412.87, 288.71))
    poly13.add_vertex((371.6, 366.21))
    poly13.add_vertex((370.83, 330.75))
    window.add(poly13)
    poly13.filled = True
    poly13.fill_color = '#317093'

    poly14 = GPolygon()
    poly14.add_vertex((412.87, 288.71))
    poly14.add_vertex((434.12, 368.35))
    poly14.add_vertex((371.6, 366.21))
    window.add(poly14)
    poly14.filled = True
    poly14.fill_color = '#0C6DA3'

    poly15 = GPolygon()
    poly15.add_vertex((412.87, 288.71))
    poly15.add_vertex((467.75, 288.55))
    poly15.add_vertex((434.12, 368.35))
    window.add(poly15)
    poly15.filled = True
    poly15.fill_color = '#4491BC'

    poly16 = GPolygon()
    poly16.add_vertex((434.12, 368.35))
    poly16.add_vertex((371.6, 366.21))
    poly16.add_vertex((355.242, 400.758))
    window.add(poly16)
    poly16.filled = True
    poly16.fill_color = '#34235E'

    poly17 = GPolygon()
    poly17.add_vertex((434.12, 368.35))
    poly17.add_vertex((355.242, 400.758))
    poly17.add_vertex((332.31, 451.66))
    window.add(poly17)
    poly17.filled = True
    poly17.fill_color = '#5F4D99'

    poly18 = GPolygon()
    poly18.add_vertex((371.6, 366.21))
    poly18.add_vertex((332.31, 451.66))
    poly18.add_vertex((313.051, 427.36))
    window.add(poly18)
    poly18.filled = True
    poly18.fill_color = '#3D335B'

    poly19 = GPolygon()
    poly19.add_vertex((292.41, 459.15))
    poly19.add_vertex((332.31, 451.66))
    poly19.add_vertex((313.051, 427.36))
    window.add(poly19)
    poly19.filled = True
    poly19.fill_color = '#422991'

    poly20 = GPolygon()
    poly20.add_vertex((292.41, 459.15))
    poly20.add_vertex((290.12, 443.41))
    poly20.add_vertex((313.051, 427.36))
    window.add(poly20)
    poly20.filled = True
    poly20.fill_color = '#6630B5'

    poly21 = GPolygon()
    poly21.add_vertex((445.59, 242.08))
    poly21.add_vertex((467.75, 288.55))
    poly21.add_vertex((553.05, 282.59))
    window.add(poly21)
    poly21.filled = True
    poly21.fill_color = '#186A92'

    poly22 = GPolygon()
    poly22.add_vertex((445.59, 242.08))
    poly22.add_vertex((586.68, 229.09))
    poly22.add_vertex((553.05, 282.59))
    window.add(poly22)
    poly22.filled = True
    poly22.fill_color = '#42BFA6'

    poly23 = GPolygon()
    poly23.add_vertex((434.12, 368.35))
    poly23.add_vertex((467.75, 288.55))
    poly23.add_vertex((553.05, 282.59))
    window.add(poly23)
    poly23.filled = True
    poly23.fill_color = '#1993A0'

    poly24 = GPolygon()
    poly24.add_vertex((434.12, 368.35))
    poly24.add_vertex((553.05, 282.59))
    poly24.add_vertex((493.13, 373.70))
    poly24.add_vertex((456.74, 376.15))
    window.add(poly24)
    poly24.filled = True
    poly24.fill_color = '#1C7B7F'

    poly25 = GPolygon()
    poly25.add_vertex((553.05, 282.59))
    poly25.add_vertex((493.13, 373.70))
    poly25.add_vertex((543.57, 365.75))
    window.add(poly25)
    poly25.filled = True
    poly25.fill_color = '#1DA875'

    poly26 = GPolygon()
    poly26.add_vertex((456.74, 376.15))
    poly26.add_vertex((484.26, 374.92))
    poly26.add_vertex((485.48, 408.86))
    window.add(poly26)
    poly26.filled = True
    poly26.fill_color = '#19AAAB'

    poly27 = GPolygon()
    poly27.add_vertex((493.13, 373.70))
    poly27.add_vertex((484.26, 374.92))
    poly27.add_vertex((485.48, 408.86))
    poly27.add_vertex((508.72, 440.35))
    window.add(poly27)
    poly27.filled = True
    poly27.fill_color = '#1AAA7D'

    poly28 = GPolygon()
    poly28.add_vertex((456.74, 376.15))
    poly28.add_vertex((508.72, 440.35))
    poly28.add_vertex((481.51, 435.46))
    window.add(poly28)
    poly28.filled = True
    poly28.fill_color = '#73D142'

    poly29 = GPolygon()
    poly29.add_vertex((472.95, 457.47))
    poly29.add_vertex((508.72, 440.35))
    poly29.add_vertex((481.51, 435.46))
    window.add(poly29)
    poly29.filled = True
    poly29.fill_color = '#72BF47'

    poly30 = GPolygon()
    poly30.add_vertex((472.95, 457.47))
    poly30.add_vertex((508.72, 440.35))
    poly30.add_vertex((514.53, 459.92))
    window.add(poly30)
    poly30.filled = True
    poly30.fill_color = '#DADD4A'

    poly31 = GPolygon()
    poly31.add_vertex((472.95, 457.47))
    poly31.add_vertex((481.51, 435.46))
    poly31.add_vertex((470.2, 450.13))
    window.add(poly31)
    poly31.filled = True
    poly31.fill_color = '#B4D622'

    poly32 = GPolygon()
    poly32.add_vertex((543.57, 365.75))
    poly32.add_vertex((553.05, 282.59))
    poly32.add_vertex((593.10, 381.04))
    window.add(poly32)
    poly32.filled = True
    poly32.fill_color = '#E2E21E'

    poly33 = GPolygon()
    poly33.add_vertex((629.79, 337.62))
    poly33.add_vertex((607.47, 285.96))
    poly33.add_vertex((553.05, 282.59))
    poly33.add_vertex((593.10, 381.04))
    window.add(poly33)
    poly33.filled = True
    poly33.fill_color = '#C9D92F'

    poly34 = GPolygon()
    poly34.add_vertex((586.68, 229.09))
    poly34.add_vertex((607.47, 285.96))
    poly34.add_vertex((553.05, 282.59))
    window.add(poly34)
    poly34.filled = True
    poly34.fill_color = '#D1D667'

    poly35 = GPolygon()
    poly35.add_vertex((586.68, 229.09))
    poly35.add_vertex((607.47, 285.96))
    poly35.add_vertex((671.06, 289.93))
    window.add(poly35)
    poly35.filled = True
    poly35.fill_color = '#F8EF44'

    poly36 = GPolygon()
    poly36.add_vertex((586.68, 229.09))
    poly36.add_vertex((655.93, 244.07))
    poly36.add_vertex((671.06, 289.93))
    window.add(poly36)
    poly36.filled = True
    poly36.fill_color = '#FBDC06'

    poly37 = GPolygon()
    poly37.add_vertex((629.79, 337.62))
    poly37.add_vertex((607.47, 285.96))
    poly37.add_vertex((671.06, 289.93))
    window.add(poly37)
    poly37.filled = True
    poly37.fill_color = '#F9CB08'

    poly38 = GPolygon()
    poly38.add_vertex((629.79, 337.62))
    poly38.add_vertex((643.55, 373.09))
    poly38.add_vertex((671.06, 289.93))
    window.add(poly38)
    poly38.filled = True
    poly38.fill_color = '#F7B82B'

    poly39 = GPolygon()
    poly39.add_vertex((629.79, 337.62))
    poly39.add_vertex((643.55, 373.09))
    poly39.add_vertex((630.24, 400.91))
    poly39.add_vertex((593.10, 381.04))
    window.add(poly39)
    poly39.filled = True
    poly39.fill_color = '#F4CF58'

    poly40 = GPolygon()
    poly40.add_vertex((630.24, 400.91))
    poly40.add_vertex((593.10, 381.04))
    poly40.add_vertex((610.83, 407.94))
    poly40.add_vertex((627.04, 409.17))
    window.add(poly40)
    poly40.filled = True
    poly40.fill_color = '#F58C21'

    poly41 = GPolygon()
    poly41.add_vertex((630.24, 400.91))
    poly41.add_vertex((643.55, 373.09))
    poly41.add_vertex((653.03, 412.22))
    window.add(poly41)
    poly41.filled = True
    poly41.fill_color = '#F47722'

    poly42 = GPolygon()
    poly42.add_vertex((630.24, 400.91))
    poly42.add_vertex((627.04, 409.17))
    poly42.add_vertex((653.03, 412.22))
    window.add(poly42)
    poly42.filled = True
    poly42.fill_color = '#A61E22'

    poly43 = GPolygon()
    poly43.add_vertex((608.08, 455.03))
    poly43.add_vertex((627.04, 409.17))
    poly43.add_vertex((653.03, 412.22))
    window.add(poly43)
    poly43.filled = True
    poly43.fill_color = '#E25827'

    poly44 = GPolygon()
    poly44.add_vertex((608.08, 455.03))
    poly44.add_vertex((627.04, 409.17))
    poly44.add_vertex((610.83, 407.94))
    poly44.add_vertex((578.12, 440.35))
    window.add(poly44)
    poly44.filled = True
    poly44.fill_color = '#BA1E51'

    poly45 = GPolygon()
    poly45.add_vertex((608.08, 455.03))
    poly45.add_vertex((571.39, 451.66))
    poly45.add_vertex((578.12, 440.35))
    window.add(poly45)
    poly45.filled = True
    poly45.fill_color = '#A1268C'

    poly46 = GPolygon()
    poly46.add_vertex((643.55, 373.09))
    poly46.add_vertex((671.06, 289.93))
    poly46.add_vertex((690.32, 343.13))
    poly46.add_vertex((697.20, 393.57))
    window.add(poly46)
    poly46.filled = True
    poly46.fill_color = '#D12127'

    poly47 = GPolygon()
    poly47.add_vertex((718.76, 360.55))
    poly47.add_vertex((690.32, 343.13))
    poly47.add_vertex((697.20, 393.57))
    window.add(poly47)
    poly47.filled = True
    poly47.fill_color = '#8B1721'

    poly48 = GPolygon()
    poly48.add_vertex((718.76, 360.55))
    poly48.add_vertex((715.55, 424.3))
    poly48.add_vertex((697.20, 393.57))
    window.add(poly48)
    poly48.filled = True
    poly48.fill_color = '#A32171'

    poly49 = GPolygon()
    poly49.add_vertex((718.76, 360.55))
    poly49.add_vertex((715.55, 424.3))
    poly49.add_vertex((739.39, 417.42))
    window.add(poly49)
    poly49.filled = True
    poly49.fill_color = '#75255A'

    poly50 = GPolygon()
    poly50.add_vertex((728.84, 451.36))
    poly50.add_vertex((715.09, 445.39))
    poly50.add_vertex((715.55, 424.3))
    poly50.add_vertex((739.39, 417.42))
    window.add(poly50)
    poly50.filled = True
    poly50.fill_color = '#5B1142'

    poly51 = GPolygon()
    poly51.add_vertex((655.93, 244.07))
    poly51.add_vertex((671.06, 289.93))
    poly51.add_vertex((684.82, 211.05))
    window.add(poly51)
    poly51.filled = True
    poly51.fill_color = '#FDD606'

    poly52 = GPolygon()
    poly52.add_vertex((721.05, 175.74))
    poly52.add_vertex((671.06, 289.93))
    poly52.add_vertex((684.82, 211.05))
    window.add(poly52)
    poly52.filled = True
    poly52.fill_color = '#FCE408'

    poly53 = GPolygon()
    poly53.add_vertex((691.70, 171.61))
    poly53.add_vertex((655.93, 244.07))
    poly53.add_vertex((684.82, 211.05))
    window.add(poly53)
    poly53.filled = True
    poly53.fill_color = '#E2D344'

    poly54 = GPolygon()
    poly54.add_vertex((684.82, 211.05))
    poly54.add_vertex((691.70, 171.61))
    poly54.add_vertex((691.24, 130.80))
    poly54.add_vertex((721.05, 175.74))
    window.add(poly54)
    poly54.filled = True
    poly54.fill_color = '#D3DA25'

    poly55 = GPolygon()
    poly55.add_vertex((690.78, 100.07))
    poly55.add_vertex((691.24, 130.80))
    poly55.add_vertex((721.05, 175.74))
    window.add(poly55)
    poly55.filled = True
    poly55.fill_color = '#71BE46'

    poly56 = GPolygon()
    poly56.add_vertex((691.70, 171.61))
    poly56.add_vertex((691.24, 130.80))
    poly56.add_vertex((671.98, 108.32))
    window.add(poly56)
    poly56.filled = True
    poly56.fill_color = '#1CAA73'

    poly57 = GPolygon()
    poly57.add_vertex((691.24, 130.80))
    poly57.add_vertex((690.78, 100.07))
    poly57.add_vertex((669.69, 90.9))
    poly57.add_vertex((671.98, 108.32))
    window.add(poly57)
    poly57.filled = True
    poly57.fill_color = '#11878B'

    poly58 = GPolygon()
    poly58.add_vertex((690.78, 100.07))
    poly58.add_vertex((669.69, 90.9))
    poly58.add_vertex((668.3, 78.97))
    window.add(poly58)
    poly58.filled = True
    poly58.fill_color = '#E0E04C'

    poly59 = GPolygon()
    poly59.add_vertex((649, 86.3))
    poly59.add_vertex((669.69, 90.9))
    poly59.add_vertex((668.3, 78.97))
    window.add(poly59)
    poly59.filled = True
    poly59.fill_color = '#0FB5B5'

    poly60 = GPolygon()
    poly60.add_vertex((649, 86.3))
    poly60.add_vertex((669.69, 90.9))
    poly60.add_vertex((671.98, 108.32))
    window.add(poly60)
    poly60.filled = True
    poly60.fill_color = '#115959'

    poly61 = GPolygon()
    poly61.add_vertex((649, 86.3))
    poly61.add_vertex((645.84, 66.13))
    poly61.add_vertex((668.3, 78.97))
    window.add(poly61)
    poly61.filled = True
    poly61.fill_color = '#78B548'

    poly62 = GPolygon()
    poly62.add_vertex((649, 86.3))
    poly62.add_vertex((645.84, 66.13))
    poly62.add_vertex((628.87, 78.97))
    window.add(poly62)
    poly62.filled = True
    poly62.fill_color = '#95AA1A'

    poly63 = GPolygon()
    poly63.add_vertex((649, 86.3))
    poly63.add_vertex((633, 99.15))
    poly63.add_vertex((628.87, 78.97))
    window.add(poly63)
    poly63.filled = True
    poly63.fill_color = '#9FAA63'

    poly64 = GPolygon()
    poly64.add_vertex((616.95, 104.2))
    poly64.add_vertex((633, 99.15))
    poly64.add_vertex((628.87, 78.97))
    window.add(poly64)
    poly64.filled = True
    poly64.fill_color = '#E0E04C'


if __name__ == '__main__':
    main()
