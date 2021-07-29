"""
File: my_drawing.py
Name: HJ
----------------------
This file uses campy module to draw on a GWindow object
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon, GArc, GLine
from campy.graphics.gwindow import GWindow

# Global variables
window = GWindow(width=500, height=700, title='New Look')


def main():
    """
    mimic Dior's classic iconic 'New Look' by campy module
    """
    background = GRect(500, 800)
    background.filled = True
    background.fill_color = 'silver'
    background.color = 'silver'
    window.add(background)
    vintage_hat()
    a_line_skirt()
    bar_jacket()
    hand_on_waist()
    button()
    label = GLabel('DIOR', 125, 560)
    label.font = 'Times-120'
    label.color = 'goldenrod'
    window.add(label, 100, 730)


def vintage_hat():
    """
    shape the hat with GArc and GPolygon
    """
    arc = GArc(220, 123, -203, 180)
    arc.filled = True
    arc.fill_color = 'burlywood'
    arc.color = 'burlywood'
    window.add(arc, 172, 30)
    hat = GPolygon()
    hat.add_vertex((110, 45))
    hat.add_vertex((275, -62))
    hat.add_vertex((390, 93))
    hat.filled = True
    hat.fill_color = 'burlywood'
    hat.color = 'burlywood'
    window.add(hat)
    l_brim = GPolygon()
    l_brim.add_vertex((110, 45))
    l_brim.add_vertex((200, 30))
    l_brim.add_vertex((185, 94))
    l_brim.filled = True
    l_brim.fill_color ='burlywood'
    l_brim.color = 'burlywood'
    window.add(l_brim)
    r_brim = GPolygon()
    r_brim.add_vertex((310, 80))
    r_brim.add_vertex((390, 93))
    r_brim.add_vertex((323, 112))
    r_brim.filled = True
    r_brim.fill_color = 'burlywood'
    r_brim.color = 'burlywood'
    window.add(r_brim)


def a_line_skirt():
    """
    draw the skirt and its pleats with GPolygon and GRect
    """
    skirt = GPolygon()
    skirt.add_vertex((240, 480))
    skirt.add_vertex((120, 800))
    skirt.add_vertex((510, 800))
    skirt.add_vertex((425, 480))
    skirt.filled = True
    skirt.fill_color = 'darkgrey'
    skirt.color = 'darkgrey'
    window.add(skirt)
    pleat0 = GPolygon()
    pleat0.add_vertex((430, 500))
    pleat0.add_vertex((450, 800))
    pleat0.add_vertex((453, 800))
    pleat0.add_vertex((453, 590))
    pleat0.filled = True
    pleat0.fill_color = 'dimgrey'
    pleat0.color = 'dimgrey'
    window.add(pleat0)
    pleat1 = GPolygon()
    pleat1.add_vertex((355, 480))
    pleat1.add_vertex((355, 800))
    pleat1.add_vertex((420, 800))
    pleat1.add_vertex((400, 480))
    pleat1.filled = True
    pleat1.fill_color = 'dimgray'
    pleat1.color = 'dimgray'
    window.add(pleat1)
    pleat2 = GPolygon()
    pleat2.add_vertex((335, 480))
    pleat2.add_vertex((338, 800))
    pleat2.add_vertex((340, 800))
    pleat2.add_vertex((342, 480))
    pleat2.filled = True
    pleat2.fill_color = 'dimgrey'
    pleat2.color = 'dimgrey'
    window.add(pleat2)
    pleat3 = GRect(15, 500)
    pleat3.filled = True
    pleat3.fill_color = 'dimgrey'
    pleat3.color = 'dimgrey'
    window.add(pleat3, 290, 450)
    pleat4 = GRect(5, 500)
    pleat4.filled = True
    pleat4.fill_color = 'dimgrey'
    pleat4.color = 'dimgrey'
    window.add(pleat4, 250, 450)
    pleat5 = GPolygon()
    pleat5.add_vertex((230, 430))
    pleat5.add_vertex((210, 800))
    pleat5.add_vertex((240, 800))
    pleat5.add_vertex((230, 430))
    pleat5.filled = True
    pleat5.fill_color = 'dimgrey'
    pleat5.color = 'dimgrey'
    window.add(pleat5)
    pleat6 = GPolygon()
    pleat6.add_vertex((170, 740))
    pleat6.add_vertex((170, 800))
    pleat6.add_vertex((183, 800))
    pleat6.add_vertex((190, 620))
    pleat6.filled = True
    pleat6.fill_color = 'dimgrey'
    pleat6.color = 'dimgrey'
    window.add(pleat6)


def bar_jacket():
    """
    combine chest, waist, arm, sleeve, collars, hips and hems into a whole piece of bar jacket by GPolygon, GOval
    """
    chest = GPolygon()
    chest.add_vertex((140, 175))
    chest.add_vertex((135, 185))
    chest.add_vertex((120, 290))
    chest.add_vertex((310, 260))
    chest.add_vertex((232, 210))
    chest.add_vertex((240, 190))
    chest.add_vertex((205, 185))
    chest.add_vertex((205, 150))
    chest.filled = True
    chest.fill_color = 'seashell'
    chest.color = 'seashell'
    window.add(chest)
    waist = GPolygon()
    waist.add_vertex((125, 290))
    waist.add_vertex((310, 430))
    waist.add_vertex((325, 430))
    waist.add_vertex((325, 255))
    waist.add_vertex((318, 238))
    waist.add_vertex((308, 255))
    waist.filled = True
    waist.fill_color = 'seashell'
    waist.color = 'seashell'
    window.add(waist)
    arm = GPolygon()
    arm.add_vertex((125, 220))
    arm.add_vertex((8, 358))
    arm.add_vertex((66, 345))
    arm.add_vertex((140, 280))
    arm.filled = True
    arm.fill_color = 'seashell'
    arm.color = 'seashell'
    window.add(arm)
    wrinkle = GPolygon()
    wrinkle.add_vertex((135, 218))
    wrinkle.add_vertex((122, 220))
    wrinkle.add_vertex((100, 260))
    wrinkle.filled = True
    wrinkle.fill_color = 'seashell'
    wrinkle.color = 'seashell'
    window.add(wrinkle)
    sleeve = GPolygon()
    sleeve.add_vertex((5, 355))
    sleeve.add_vertex((70, 350))
    sleeve.add_vertex((167, 435))
    sleeve.add_vertex((130, 465))
    sleeve.filled = True
    sleeve.fill_color = 'seashell'
    sleeve.color = 'seashell'
    window.add(sleeve)
    armpit = GPolygon()
    armpit.add_vertex((155, 268))
    armpit.add_vertex((128, 292))
    armpit.add_vertex((135, 310))
    armpit.filled = True
    armpit.fill_color = 'silver'
    armpit.color = 'silver'
    window.add(armpit)
    l_collar = GPolygon()
    l_collar.add_vertex((230, 130))
    l_collar.add_vertex((215, 145))
    l_collar.add_vertex((215, 180))
    l_collar.add_vertex((245, 185))
    l_collar.add_vertex((240, 210))
    l_collar.add_vertex((305, 250))
    l_collar.filled = True
    l_collar.fill_color = 'seashell'
    l_collar.color = 'seashell'
    window.add(l_collar)
    r_collar = GPolygon()
    r_collar.add_vertex((290, 170))
    r_collar.add_vertex((315, 190))
    r_collar.add_vertex((310, 205))
    r_collar.add_vertex((320, 220))
    r_collar.add_vertex((305, 250))
    r_collar.filled = True
    r_collar.fill_color = 'seashell'
    r_collar.color = 'seashell'
    window.add(r_collar)
    l_hem = GPolygon()
    l_hem.add_vertex((300, 360))
    l_hem.add_vertex((205, 430))
    l_hem.add_vertex((185, 570))
    l_hem.add_vertex((375, 500))
    l_hem.filled = True
    l_hem.fill_color = 'seashell'
    l_hem.color = 'seashell'
    hips = GOval(80, 150)
    hips.filled = True
    hips.fill_color = 'seashell'
    hips.color = 'seashell'
    window.add(hips, 205, 360)
    window.add(l_hem)
    r_hem = GPolygon()
    r_hem.add_vertex((300, 350))
    r_hem.add_vertex((370, 390))
    r_hem.add_vertex((440, 465))
    r_hem.add_vertex((340, 500))
    r_hem.filled = True
    r_hem.fill_color = 'seashell'
    r_hem.color = 'seashell'
    window.add(r_hem)


def hand_on_waist():
    """
    draw wrist, hand, and fingers by GPolygon
    """
    wrist = GPolygon()
    wrist.add_vertex((179, 425))
    wrist.add_vertex((150, 460))
    wrist.add_vertex((194, 460))
    wrist.add_vertex((194, 440))
    wrist.filled = True
    window.add(wrist)
    hand = GPolygon()
    hand.add_vertex((179, 460))
    hand.add_vertex((194, 460))
    hand.add_vertex((215, 415))
    hand.add_vertex((210, 380))
    hand.filled = True
    window.add(hand)
    forefinger = GPolygon()
    forefinger.add_vertex((240, 360))
    forefinger.add_vertex((240, 368))
    forefinger.add_vertex((210, 395))
    forefinger.add_vertex((210, 380))
    forefinger.filled = True
    window.add(forefinger)
    middle_finger = GPolygon()
    middle_finger.add_vertex((255, 370))
    middle_finger.add_vertex((255, 377))
    middle_finger.add_vertex((210, 400))
    middle_finger.add_vertex((210, 385))
    middle_finger.filled = True
    window.add(middle_finger)
    ring_finger = GPolygon()
    ring_finger.add_vertex((245, 382))
    ring_finger.add_vertex((245, 387))
    ring_finger.add_vertex((210, 410))
    ring_finger.add_vertex((210, 400))
    ring_finger.filled = True
    window.add(ring_finger)
    little_finger = GPolygon()
    little_finger.add_vertex((238, 392))
    little_finger.add_vertex((238, 397))
    little_finger.add_vertex((210, 420))
    little_finger.add_vertex((210, 410))
    little_finger.filled = True
    window.add(little_finger)


def button():
    """
    put the buttons on the sleeve and chest by GOval
    """
    c_1 = GOval(8, 8)
    c_1.filled = True
    c_1.fill_color = 'white'
    c_1.color = 'white'
    window.add(c_1, 98, 433)
    c_2 = GOval(8, 8)
    c_2.filled = True
    c_2.fill_color = 'white'
    c_2.color = 'white'
    window.add(c_2, 110, 445)
    c_3 = GOval(8, 8)
    c_3.filled = True
    c_3.fill_color = 'white'
    c_3.color = 'white'
    window.add(c_3, 290, 258)
    c_4 = GOval(8, 8)
    c_4.filled = True
    c_4.fill_color = 'white'
    c_4.color = 'white'
    window.add(c_4, 290, 285)
    c_5 = GOval(8, 8)
    c_5.filled = True
    c_5.fill_color = 'white'
    c_5.color = 'white'
    window.add(c_5, 290, 311)
    c_6 = GOval(8, 8)
    c_6.filled = True
    c_6.fill_color = 'white'
    c_6.color = 'white'
    window.add(c_6, 290, 338)
    c_7 = GOval(8, 8)
    c_7.filled = True
    c_7.fill_color = 'white'
    c_7.color = 'white'
    window.add(c_7, 295, 360)





if __name__ == '__main__':
    main()
