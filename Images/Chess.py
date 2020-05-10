from tkinter import *
from PIL import ImageTk, Image

global turn , transparent_no , queen_no , horse_no , rook_no
global empty , count
global start , end
global castling
global initial_color_of_current_button , color_changed , code , initial_movement , initial_position
global capture1 , capture2 , capture3 , capture4 , capture5 , capture6 , capture7 , capture8
global supposed_position1 , supposed_position2 , supposed_position3 , supposed_position4 , supposed_position5 , supposed_position6 , supposed_position7 , supposed_position8 
global color_of_supposed_position1 , color_of_supposed_position2 , color_of_supposed_position3 , color_of_supposed_position4 , color_of_supposed_position5 , color_of_supposed_position6 , color_of_supposed_position7 , color_of_supposed_position8 
global color_of_supposed_position , supposed_position

count = 0
transparent_no = 64
castling = -1
code = color_changed = -1
initial_movement = initial_position = initial_color_of_current_button  = -1
start = end = -1
supposed_position1 = supposed_position2 = supposed_position3 = supposed_position4 = supposed_position5 = supposed_position6 = supposed_position7 = supposed_position8 = -1
color_of_supposed_position1 = color_of_supposed_position2 = color_of_supposed_position3 = color_of_supposed_position4 = color_of_supposed_position5 = color_of_supposed_position6 = color_of_supposed_position7 = color_of_supposed_position8 = -1
turn = empty = 0

color_of_supposed_position = [-1]*25
supposed_position = [-1]*25

color = ['white', 'dim grey', 'white', 'dim grey', 'white', 'dim grey', 'white', 'dim grey',
         'dim grey', 'white', 'dim grey', 'white', 'dim grey', 'white', 'dim grey', 'white',
         'white', 'dim grey', 'white', 'dim grey', 'white', 'dim grey', 'white', 'dim grey',
         'dim grey', 'white', 'dim grey', 'white', 'dim grey', 'white', 'dim grey', 'white',
         'white', 'dim grey', 'white', 'dim grey', 'white', 'dim grey', 'white', 'dim grey',
         'dim grey', 'white', 'dim grey', 'white', 'dim grey', 'white', 'dim grey', 'white',
         'white', 'dim grey', 'white', 'dim grey', 'white', 'dim grey', 'white', 'dim grey',
         'dim grey', 'white', 'dim grey', 'white', 'dim grey', 'white', 'dim grey', 'white',
         'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white',
         'white', 'white', 'white', 'white', 'white', 'white', 'white', 'dim grey',
         'dim grey', 'dim grey', 'dim grey', 'dim grey', 'dim grey', 'dim grey', 'dim grey', 'dim grey',
         'dim grey', 'dim grey', 'dim grey', 'dim grey', 'dim grey', 'dim grey', 'dim grey']

position = [0, 1, 2, 3, 4, 5, 6, 7,
            8, 9, 10, 11, 12, 13, 14, 15,
            16, 17, 18, 19, 20, 21, 22, 23,
            24, 25, 26, 27, 28, 29, 30, 31,
            32, 33, 34, 35, 36, 37, 38, 39,
            40, 41, 42, 43, 44, 45, 46, 47,
            48, 49, 50, 51, 52, 53, 54, 55,
            56, 57, 58, 59, 60, 61, 62, 63,
            64, 65, 66, 67, 68, 69, 70, 71,
            72, 73, 74, 75, 76, 77, 78, 79,
            80, 81, 82, 83, 84, 85, 86, 87,
            88, 89, 90, 91, 92, 93]

weights = [50,30,40,90,100,40,30,50,
           20,20,20,20,20,20,20,20,
           0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,
           -20,-20,-20,-20,-20,-20,-20,-20,
           -50,-30,-40,-90,-100,-40,-30,-50,
           0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,
           0,0,0,0,0,0]

movement = [2,1,1,1,2,1,1,2,
            2,2,2,2,2,2,2,2,
            0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,
            2,2,2,2,2,2,2,2,
            2,1,1,1,2,1,1,2,
            0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,
            0,0,0,0,0,0]

def ChessBoard():
    global turn
    master = Tk()
    master.title('Chess')
    master.geometry('496x496+10+10')
    transparent = ImageTk.PhotoImage(Image.open("transparent.png"))
    wk = ImageTk.PhotoImage(Image.open("white_king.png"))
    wq = ImageTk.PhotoImage(Image.open("white_queen.png"))
    wr = ImageTk.PhotoImage(Image.open("white_rook.png"))
    wb = ImageTk.PhotoImage(Image.open("white_bishop.png"))
    wkn = ImageTk.PhotoImage(Image.open("white_knight.png"))
    wp = ImageTk.PhotoImage(Image.open("white_pawn.png"))
    bk = ImageTk.PhotoImage(Image.open("black_king.png"))
    bq = ImageTk.PhotoImage(Image.open("black_queen.png"))
    br = ImageTk.PhotoImage(Image.open("black_rook.png"))
    bb = ImageTk.PhotoImage(Image.open("black_bishop.png"))
    bkn = ImageTk.PhotoImage(Image.open("black_knight.png"))
    bp = ImageTk.PhotoImage(Image.open("black_pawn.png"))
    button = [Button(master, image=br, width=50, height=50, bg=color[0],command = lambda:selected(master,0)),Button(master, image=bkn, width=50, height=50, bg=color[1],command = lambda:selected(master,1)),Button(master, image=bb, width=50, height=50, bg=color[2],command = lambda:selected(master,2)),Button(master, image=bq, width=50, height=50, bg=color[3],command = lambda:selected(master,3)),Button(master, image=bk, width=50, height=50, bg=color[4],command = lambda:selected(master,4)),Button(master, image=bb, width=50, height=50, bg=color[5],command = lambda:selected(master,5)),Button(master, image=bkn, width=50, height=50, bg=color[6],command = lambda:selected(master,6)),Button(master, image=br, width=50, height=50, bg=color[7],command = lambda:selected(master,7)),
              Button(master, image=bp, width=50, height=50, bg=color[8],command = lambda:selected(master,8)),Button(master, image=bp, width=50, height=50, bg=color[9],command = lambda:selected(master,9)),Button(master, image=bp, width=50, height=50, bg=color[10],command = lambda:selected(master,10)),Button(master, image=bp, width=50, height=50, bg=color[11],command = lambda:selected(master,11)),Button(master, image=bp, width=50, height=50, bg=color[12],command = lambda:selected(master,12)),Button(master, image=bp, width=50, height=50, bg=color[13],command = lambda:selected(master,13)),Button(master, image=bp, width=50, height=50, bg=color[14],command = lambda:selected(master,14)),Button(master, image=bp, width=50, height=50, bg=color[15],command = lambda:selected(master,15)),
              Button(master, image=transparent, width=50, height=50, bg=color[16],command = lambda:selected(master,16)),Button(master, image=transparent, width=50, height=50, bg=color[17],command = lambda:selected(master,17)),Button(master, image=transparent, width=50, height=50, bg=color[18],command = lambda:selected(master,18)),Button(master, image=transparent, width=50, height=50, bg=color[19],command = lambda:selected(master,19)),Button(master, image=transparent, width=50, height=50, bg=color[20],command = lambda:selected(master,20)),Button(master, image=transparent, width=50, height=50, bg=color[21],command = lambda:selected(master,21)),Button(master, image=transparent, width=50, height=50, bg=color[22],command = lambda:selected(master,22)),Button(master, image=transparent, width=50, height=50, bg=color[23],command = lambda:selected(master,23)),
              Button(master, image=transparent, width=50, height=50, bg=color[24],command=lambda:selected(master,24)),Button(master, image=transparent, width=50, height=50, bg=color[25],command = lambda:selected(master,25)),Button(master, image=transparent, width=50, height=50, bg=color[26],command = lambda:selected(master,26)),Button(master, image=transparent, width=50, height=50, bg=color[27],command = lambda:selected(master,27)),Button(master, image=transparent, width=50, height=50, bg=color[28],command = lambda:selected(master,28)),Button(master, image=transparent, width=50, height=50, bg=color[29],command = lambda:selected(master,29)),Button(master, image=transparent, width=50, height=50, bg=color[30],command = lambda:selected(master,30)),Button(master, image=transparent, width=50, height=50, bg=color[31],command = lambda:selected(master,31)),
              Button(master, image=transparent, width=50, height=50, bg=color[32],command = lambda:selected(master,32)),Button(master, image=transparent, width=50, height=50, bg=color[33],command = lambda:selected(master,33)),Button(master, image=transparent, width=50, height=50, bg=color[34],command = lambda:selected(master,34)),Button(master, image=transparent, width=50, height=50, bg=color[35],command = lambda:selected(master,35)),Button(master, image=transparent, width=50, height=50, bg=color[36],command = lambda:selected(master,36)),Button(master, image=transparent, width=50, height=50, bg=color[37],command = lambda:selected(master,37)),Button(master, image=transparent, width=50, height=50, bg=color[38],command = lambda:selected(master,38)),Button(master, image=transparent, width=50, height=50, bg=color[39],command = lambda:selected(master,39)),
              Button(master, image=transparent, width=50, height=50, bg=color[40],command = lambda:selected(master,40)),Button(master, image=transparent, width=50, height=50, bg=color[41],command = lambda:selected(master,41)),Button(master, image=transparent, width=50, height=50, bg=color[42],command = lambda:selected(master,42)),Button(master, image=transparent, width=50, height=50, bg=color[43],command = lambda:selected(master,43)),Button(master, image=transparent, width=50, height=50, bg=color[44],command = lambda:selected(master,44)),Button(master, image=transparent, width=50, height=50, bg=color[45],command = lambda:selected(master,45)),Button(master, image=transparent, width=50, height=50, bg=color[46],command = lambda:selected(master,46)),Button(master, image=transparent, width=50, height=50, bg=color[47],command = lambda:selected(master,47)),
              Button(master, image=wp, width=50, height=50, bg=color[48],command = lambda:selected(master,48)),Button(master, image=wp, width=50, height=50, bg=color[49],command = lambda:selected(master,49)),Button(master, image=wp, width=50, height=50, bg=color[50],command = lambda:selected(master,50)),Button(master, image=wp, width=50, height=50, bg=color[51],command = lambda:selected(master,51)),Button(master, image=wp, width=50, height=50, bg=color[52],command = lambda:selected(master,52)),Button(master, image=wp, width=50, height=50, bg=color[53],command = lambda:selected(master,53)),Button(master, image=wp, width=50, height=50, bg=color[54],command = lambda:selected(master,54)),Button(master, image=wp, width=50, height=50, bg=color[55],command = lambda:selected(master,55)),
              Button(master, image=wr, width=50, height=50, bg=color[56],command = lambda:selected(master,56)),Button(master, image=wkn, width=50, height=50, bg=color[57],command = lambda:selected(master,57)),Button(master, image=wb, width=50, height=50, bg=color[58],command = lambda:selected(master,58)),Button(master, image=wq, width=50, height=50, bg=color[59],command = lambda:selected(master,59)),Button(master, image=wk, width=50, height=50, bg=color[60],command = lambda:selected(master,60)),Button(master, image=wb, width=50, height=50, bg=color[61],command = lambda:selected(master,61)),Button(master, image=wkn, width=50, height=50, bg=color[62],command = lambda:selected(master,62)),Button(master, image=wr, width=50, height=50, bg=color[63],command = lambda:selected(master,63)),
              Button(master, image=transparent, width=50, height=50, bg=color[64],command = lambda:selected(master,64)),Button(master, image=transparent, width=50, height=50, bg=color[65],command = lambda:selected(master,65)),Button(master, image=transparent, width=50, height=50, bg=color[66],command = lambda:selected(master,66)),Button(master, image=transparent, width=50, height=50, bg=color[67],command = lambda:selected(master,67)),Button(master, image=transparent, width=50, height=50, bg=color[68],command = lambda:selected(master,68)),Button(master, image=transparent, width=50, height=50, bg=color[69],command = lambda:selected(master,69)),Button(master, image=transparent, width=50, height=50, bg=color[70],command = lambda:selected(master,70)),Button(master, image=transparent, width=50, height=50, bg=color[71],command = lambda:selected(master,71)),
              Button(master, image=transparent, width=50, height=50, bg=color[72],command = lambda:selected(master,72)),Button(master, image=transparent, width=50, height=50, bg=color[73],command = lambda:selected(master,73)),Button(master, image=transparent, width=50, height=50, bg=color[74],command = lambda:selected(master,74)),Button(master, image=transparent, width=50, height=50, bg=color[75],command = lambda:selected(master,75)),Button(master, image=transparent, width=50, height=50, bg=color[76],command = lambda:selected(master,76)),Button(master, image=transparent, width=50, height=50, bg=color[77],command = lambda:selected(master,77)),Button(master, image=transparent, width=50, height=50, bg=color[78],command = lambda:selected(master,78)),Button(master, image=transparent, width=50, height=50, bg=color[79],command = lambda:selected(master,79)),
              Button(master, image=transparent, width=50, height=50, bg=color[80],command = lambda:selected(master,80)),Button(master, image=transparent, width=50, height=50, bg=color[81],command = lambda:selected(master,81)),Button(master, image=transparent, width=50, height=50, bg=color[82],command = lambda:selected(master,82)),Button(master, image=transparent, width=50, height=50, bg=color[83],command = lambda:selected(master,83)),Button(master, image=transparent, width=50, height=50, bg=color[84],command = lambda:selected(master,84)),Button(master, image=transparent, width=50, height=50, bg=color[85],command = lambda:selected(master,85)),Button(master, image=transparent, width=50, height=50, bg=color[86],command = lambda:selected(master,86)),Button(master, image=transparent, width=50, height=50, bg=color[87],command = lambda:selected(master,87)),
              Button(master, image=transparent, width=50, height=50, bg=color[88],command = lambda:selected(master,88)),Button(master, image=transparent, width=50, height=50, bg=color[89],command = lambda:selected(master,89)),Button(master, image=transparent, width=50, height=50, bg=color[90],command = lambda:selected(master,90)),Button(master, image=transparent, width=50, height=50, bg=color[91],command = lambda:selected(master,91)),Button(master, image=transparent, width=50, height=50, bg=color[92],command = lambda:selected(master,92)),Button(master, image=transparent, width=50, height=50, bg=color[93],command = lambda:selected(master,93))]
    xc=yc=25
    for i in range(0,64):
        if i%8==0 and i>0:
            xc = 25
            yc += 56
        button[position[i]].place(x=xc,y=yc)
        if i>=0:
            xc += 56
    master.mainloop()

def selected (master,current_button):
    global start , end , turn , color_changed , initial_color_of_current_button , initial_movement , initial_position , castling
    global supposed_position1 , supposed_position2 , supposed_position3 , supposed_position4 , supposed_position5 , supposed_position6 , supposed_position7 , supposed_position8
    master.destroy()
    if turn%2 == 0:
        if position.index(current_button) != initial_position:
            if weights[position.index(current_button)] < 0 or position.index(current_button) in supposed_position or position.index(current_button) == supposed_position1 or position.index(current_button) == supposed_position2 or position.index(current_button) == supposed_position3 or position.index(current_button) == supposed_position4 or position.index(current_button) == supposed_position5 or position.index(current_button) == supposed_position6 or position.index(current_button) == supposed_position7 or position.index(current_button) == supposed_position8:
                if start == -1 and moveable(position.index(current_button),weights[position.index(current_button)]):
                    initial_position = position.index(current_button)
                    start = current_button
                    initial_movement = movement[position.index(current_button)]
                    highlight(start)
                elif start != -1:
                    color[start] = initial_color_of_current_button
                    start = position.index(start)
                    end = position.index(current_button)
                    weight = weights[start]
                    if castling == 1:
                        if position.index(current_button) == position.index(start) + 2:
                            castking = 1
                        else:
                            castling = -1
                    elif castling == 2:
                        if position.index(current_button) == position.index(start) - 2:
                            castking = 2
                        else:
                            castling = -1
                    elif castling == 3:
                        if position.index(current_button) == position.index(start) + 2:
                            castking = 1
                        elif position.index(current_button) == position.index(start) - 2:
                            castling = 2
                        else:
                            castling = -1
                    if end == supposed_position1 or end == supposed_position2 or end == supposed_position3 or end == supposed_position4 or end == supposed_position5 or end == supposed_position6 or end == supposed_position7 or end == supposed_position8:
                        swap(start,end,weight)
                        turn += 1
                        start = end = -1
                        color_changed = -1
                        initial_position = -1
                    elif end in supposed_position:
                        swap(start,end,weight)
                        turn += 1
                        start = end = -1
                        color_changed = -1
                        initial_position =-1
                else:
                    color[start] = initial_color_of_current_button
                    color_correction()
                    master = Tk()
                    master.title('Error')
                    master.geometry('100x100+192+215')
                    l = Label(master, text='Invalid Move')
                    b = Button(master, text='OK', width=5, height=2 , command = lambda:master.destroy())
                    l.pack()
                    b.pack()
                    master.mainloop()
                    empty = 0
                    color_changed = -1
                    initial_position = initial_color_of_current_position  = -1
                    supposed_position1 = supposed_position2 = supposed_position3 = supposed_position4 = supposed_position5 = supposed_position6 = supposed_position7 = supposed_position8 = -1
                    color_of_supposed_position1 = color_of_supposed_position2 = color_of_supposed_position3 = color_of_supposed_position4 = color_of_supposed_position5 = color_of_supposed_position6 = color_of_supposed_position7 = color_of_supposed_position8 = -1
            else:
                color[start] = initial_color_of_current_button
                color_correction()
                master = Tk()
                master.title('Error')
                master.geometry('100x100+192+215')
                l = Label(master, text='Invalid Choice')
                b = Button(master, text='OK', width=5, height=2 , command = lambda:master.destroy())
                l.pack()
                b.pack()
                master.mainloop()
                movement[start] = initial_movement
                start = end = -1
                empty = 0
                color_changed = -1
                initial_position = initial_color_of_current_position  = -1
                supposed_position1 = supposed_position2 = supposed_position3 = supposed_position4 = supposed_position5 = supposed_position6 = supposed_position7 = supposed_position8 = -1
                color_of_supposed_position1 = color_of_supposed_position2 = color_of_supposed_position3 = color_of_supposed_position4 = color_of_supposed_position5 = color_of_supposed_position6 = color_of_supposed_position7 = color_of_supposed_position8 = -1
        else:
            color[start] = initial_color_of_current_button
            color_correction()
            movement[start] = initial_movement
            start = end = -1
            empty = 0
            color_changed = -1
            initial_position = initial_color_of_current_position  = -1
            supposed_position1 = supposed_position2 = supposed_position3 = supposed_position4 = supposed_position5 = supposed_position6 = supposed_position7 = supposed_position8 = -1
            color_of_supposed_position1 = color_of_supposed_position2 = color_of_supposed_position3 = color_of_supposed_position4 = color_of_supposed_position5 = color_of_supposed_position6 = color_of_supposed_position7 = color_of_supposed_position8 = -1
    elif turn%2 == 1:
        if position.index(current_button) != initial_position:
            if weights[position.index(current_button)] > 0 or position.index(current_button) in supposed_position or position.index(current_button) == supposed_position1 or position.index(current_button) == supposed_position2 or position.index(current_button) == supposed_position3 or position.index(current_button) == supposed_position4 or position.index(current_button) == supposed_position5 or position.index(current_button) == supposed_position6 or position.index(current_button) == supposed_position7 or position.index(current_button) == supposed_position8:
                if start == -1 and moveable(position.index(current_button),weights[position.index(current_button)]):
                    initial_position = position.index(current_button)
                    start = current_button
                    initial_movement = movement[position.index(current_button)]
                    highlight(start)
                elif start != -1:
                    color[start] = initial_color_of_current_button
                    start = position.index(start)
                    end = position.index(current_button)
                    weight = weights[start]
                    if castling == 1:
                        if position.index(current_button) == position.index(start) + 2:
                            castking = 1
                        else:
                            castling = -1
                    elif castling == 2:
                        if position.index(current_button) == position.index(start) - 2:
                            castking = 2
                        else:
                            castling = -1
                    elif castling == 3:
                        if position.index(current_button) == position.index(start) + 2:
                            castking = 1
                        elif position.index(current_button) == position.index(start) - 2:
                            castling = 2
                        else:
                            castling = -1
                    if end == supposed_position1 or end == supposed_position2 or end == supposed_position3 or end == supposed_position4 or end == supposed_position5 or end == supposed_position6 or end == supposed_position7 or end == supposed_position8:
                        swap(start,end,weight)
                        turn += 1
                        start = end = -1
                        color_changed = -1
                        initial_position = -1
                    elif end in supposed_position:
                        swap(start,end,weight)
                        turn += 1
                        start = end = -1
                        color_changed = -1
                        initial_position =-1
                else:
                    color[start] = initial_color_of_current_button
                    color_correction()
                    master = Tk()
                    master.title('Error')
                    master.geometry('100x100+192+215')
                    l = Label(master, text='Invalid Choice')
                    b = Button(master, text='OK', width=5, height=2 , command = lambda:master.destroy())
                    l.pack()
                    b.pack()
                    master.mainloop()
                    empty = 0
                    color_changed = -1
                    initial_position = initial_color_of_current_position  = -1
                    supposed_position1 = supposed_position2 = supposed_position3 = supposed_position4 = supposed_position5 = supposed_position6 = supposed_position7 = supposed_position8 = -1
                    color_of_supposed_position1 = color_of_supposed_position2 = color_of_supposed_position3 = color_of_supposed_position4 = color_of_supposed_position5 = color_of_supposed_position6 = color_of_supposed_position7 = color_of_supposed_position8 = -1
            else:
                color[start] = initial_color_of_current_button
                color_correction()
                master = Tk()
                master.title('Error')
                master.geometry('100x100+192+215')
                l = Label(master, text='Invalid Move')
                b = Button(master, text='OK', width=5, height=2 , command = lambda:master.destroy())
                l.pack()
                b.pack()
                master.mainloop()
                movement[start] = initial_movement
                start = end = -1
                empty = 0
                color_changed = -1
                initial_position = initial_color_of_current_position  = -1
                supposed_position1 = supposed_position2 = supposed_position3 = supposed_position4 = supposed_position5 = supposed_position6 = supposed_position7 = supposed_position8 = -1
                color_of_supposed_position1 = color_of_supposed_position2 = color_of_supposed_position3 = color_of_supposed_position4 = color_of_supposed_position5 = color_of_supposed_position6 = color_of_supposed_position7 = color_of_supposed_position8 = -1
        else:
            color[start] = initial_color_of_current_button
            color_correction()
            movement[start] = initial_movement
            start = end = -1
            empty = 0
            color_changed = -1
            initial_position = initial_color_of_current_position  = -1
            supposed_position1 = supposed_position2 = supposed_position3 = supposed_position4 = supposed_position5 = supposed_position6 = supposed_position7 = supposed_position8 = -1
            color_of_supposed_position1 = color_of_supposed_position2 = color_of_supposed_position3 = color_of_supposed_position4 = color_of_supposed_position5 = color_of_supposed_position6 = color_of_supposed_position7 = color_of_supposed_position8 = -1
    ChessBoard()

def highlight(current_button):
    global initial_color_of_current_button , color_changed
    if current_button == start:
        initial_color_of_current_button = color[current_button]
        color[current_button] = "green"
    elif color_changed == 1 or color_changed == 2 or color_changed == 3 or color_changed == 4:
        color[current_button] = "red"
    elif color_changed == 6:
        color[current_button] = "cyan"
    else:
        color[current_button] = "yellow"
    if color_changed == -1:
        chess_piece_assumed_next_position(position.index(current_button))

def chess_piece_assumed_next_position(current_position):
    weight = weights[current_position]
    if weight == 20 or weight == -20:
        future_pawn_position(current_position,weight)
    elif weight == 30 or weight == -30:
        future_knight_position(current_position,weight)
    elif weight == 40 or weight == -40:
        future_bishop_position(current_position,weight)
    elif weight == 90 or weight == -90:
        future_queen_position(current_position,weight)
    elif weight == 50 or weight == -50:
        future_rook_position(current_position,weight)
    elif weight == 100 or weight == -100:
        future_king_position(current_position,weight)


def future_pawn_position(current_position,weight):
    global supposed_position1 , supposed_position2 , supposed_position3 , supposed_position4 , supposed_position5 , supposed_position6 , supposed_position7 , supposed_position8 
    global color_of_supposed_position1 , color_of_supposed_position2 , color_of_supposed_position3 , color_of_supposed_position4 , color_of_supposed_position5 , color_of_supposed_position6 , color_of_supposed_position7 , color_of_supposed_position8 , color_changed
    if movement[current_position] == 1 and weight == 20:#It checks if the piece is a black Pawn and has been moved.
        if checking(current_position,current_position+7,weight) and checking(current_position,current_position+9,weight):#Checking if the Piece has the ability to capture pieces place diagonal to it on both side.
            if weights[current_position+7] < 0 and weights[current_position+9] < 0 and weights[current_position+8] == 0:#The black pawn can move one block forward or capture the left or right piece.
                color_of_supposed_position1 = color[current_position+8]
                color_of_supposed_position2 = color[current_position+7]
                color_of_supposed_position3 = color[current_position+9]
                supposed_position1 = current_position+8
                supposed_position2 = current_position+7
                supposed_position3 = current_position+9
                highlight(position[supposed_position1])
                color_changed = 3
                highlight(position[supposed_position2])
                highlight(position[supposed_position3])
            elif weights[current_position+7] < 0 and weights[current_position+9] < 0 and weights[current_position+8] != 0:#The black pawn cannot move forward but it can capture the left or right piece.
                color_of_supposed_position1 = color[current_position+7]
                color_of_supposed_position2 = color[current_position+9]
                supposed_position1 = current_position+7
                supposed_position2 = current_position+9
                color_changed = 2
                highlight(position[supposed_position1])
                highlight(position[supposed_position2])
            elif weights[current_position+7] < 0 and weights[current_position+8] == 0: #The black pawn can move one block forward or capture the right piece.
                color_of_supposed_position1 = color[current_position+8]
                color_of_supposed_position2 = color[current_position+7]
                supposed_position1 = current_position+8
                supposed_position2 = current_position+7
                highlight(position[supposed_position1])
                color_changed = 2
                highlight(position[supposed_position2])
            elif weights[current_position+9] < 0  and weights[current_position+8] == 0:#The black pawn can move one block forward or capture the left piece.
                color_of_supposed_position1 = color[current_position+8]
                color_of_supposed_position2 = color[current_position+9]
                supposed_position1 = current_position+8
                supposed_position2 = current_position+9
                highlight(position[supposed_position1])
                color_changed = 2
                highlight(position[supposed_position2])
            elif weights[current_position+7] < 0 and weights[current_position+8] != 0:#The black pawn cannot move forward and it can capture the right piece.
                color_of_supposed_position1 = color[current_position+7]
                supposed_position1 = current_position+7
                color_changed = 1
                highlight(position[supposed_position1])
            elif weights[current_position+9] < 0 and weights[current_position+8] != 0:#The black pawn cannot move forward and it can capture the left piece.
                color_of_supposed_position1 = color[current_position+9]
                supposed_position1 = current_position+9
                color_changed = 3
                highlight(position[supposed_position1])
            elif weights[current_position+8] == 0:#The black pawn can only move one block forward.
                color_of_supposed_position1 = color[current_position+8]
                supposed_position1 = current_position+8
                highlight(position[supposed_position1])
                color_changed = 1
        elif checking(current_position,current_position+7,weight):#Checking if the Piece has the ability to capture pieces place diagonal to it on right side.
            if weights[current_position+7] < 0 and weights[current_position+8] == 0: #The black pawn can move one block forward or capture the right piece.
                color_of_supposed_position1 = color[current_position+8]
                color_of_supposed_position2 = color[current_position+7]
                supposed_position1 = current_position+8
                supposed_position2 = current_position+7
                highlight(position[supposed_position1])
                color_changed = 2
                highlight(position[supposed_position2])
            elif weights[current_position+7] < 0 and weights[current_position+8] != 0:#The black pawn cannot move forward and it can capture the right piece.
                color_of_supposed_position1 = color[current_position+7]
                supposed_position1 = current_position+7
                color_changed = 1
                highlight(position[supposed_position1])
            elif weights[current_position+8] == 0:#The black pawn can only move one block forward.
                color_of_supposed_position1 = color[current_position+8]
                supposed_position1 = current_position+8
                highlight(position[supposed_position1])
                color_changed = 1
        elif checking(current_position,current_position+9,weight):#Checking if the Piece has the ability to capture pieces place diagonal to it on left side.
            if weights[current_position+9] < 0 and weights[current_position+8] == 0:#The black pawn can move one block forward or capture the left piece.
                color_of_supposed_position1 = color[current_position+8]
                color_of_supposed_position2 = color[current_position+9]
                supposed_position1 = current_position+8
                supposed_position2 = current_position+9
                highlight(position[supposed_position1])
                color_changed = 2
                highlight(position[supposed_position2])
            elif weights[current_position+9] < 0 and weights[current_position+8] != 0:#The black pawn cannot move forward and it can capture the left piece.
                color_of_supposed_position1 = color[current_position+9]
                supposed_position1 = current_position+9
                color_changed = 1
                highlight(position[supposed_position1])
            elif weights[current_position+8] == 0:#The black pawn can only move one block forward.
                color_of_supposed_position1 = color[current_position+8]
                supposed_position1 = current_position+8
                color_changed = 1
                highlight(position[supposed_position1])
                color_changed = 1
    elif movement[current_position] == 2 and weight == 20:#It checks if the piece is a black Pawn and has never moved.
        if checking(current_position,current_position+7,weight) and checking(current_position,current_position+9,weight):#Checking if the Piece has the ability to capture pieces place diagonal to it on both side.
            if weights[current_position+7] < 0 and weights[current_position+9] < 0 and weights[current_position+8] == 0 and weights[current_position+16] == 0:#The black pawn can move one or two blocks forward or capture the left or right piece.
                color_of_supposed_position1 = color[current_position+8]
                color_of_supposed_position2 = color[current_position+16]
                color_of_supposed_position3 = color[current_position+7]
                color_of_supposed_position4 = color[current_position+9]
                supposed_position1 = current_position+8
                supposed_position2 = current_position+16
                supposed_position3 = current_position+7
                supposed_position4 = current_position+9
                highlight(position[supposed_position1])
                highlight(position[supposed_position2])
                color_changed = 4
                highlight(position[supposed_position3])
                highlight(position[supposed_position4])
                movement[current_position] = 1
            elif weights[current_position+7] < 0 and weights[current_position+9] < 0 and weights[current_position+8] == 0 and weights[current_position+16] != 0:#The black pawn can move only one blocks forward or capture the left or right piece.
                color_of_supposed_position1 = color[current_position+8]
                color_of_supposed_position2 = color[current_position+7]
                color_of_supposed_position3 = color[current_position+9]
                supposed_position1 = current_position+8
                supposed_position2 = current_position+7
                supposed_position3 = current_position+9
                highlight(position[supposed_position1])
                color_changed = 3
                highlight(position[supposed_position2])
                highlight(position[supposed_position3])
                movement[current_position] = 1
            elif weights[current_position+7] < 0 and weights[current_position+8] == 0 and weights[current_position+16] == 0:#The black pawn can move one or two blocks forward or capture the right piece.
                color_of_supposed_position1 = color[current_position+8]
                color_of_supposed_position2 = color[current_position+16]
                color_of_supposed_position3 = color[current_position+7]
                supposed_position1 = current_position+8
                supposed_position2 = current_position+16
                supposed_position3 = current_position+7
                highlight(position[supposed_position1])
                highlight(position[supposed_position2])
                color_changed = 3
                highlight(position[supposed_position3])
                movement[current_position] = 1
            elif weights[current_position+9] < 0 and weights[current_position+8] == 0 and weights[current_position+16] == 0:#The black pawn can move one or two blocks forward or capture the left piece.
                color_of_supposed_position1 = color[current_position+8]
                color_of_supposed_position2 = color[current_position+16]
                color_of_supposed_position3 = color[current_position+9]
                supposed_position1 = current_position+8
                supposed_position2 = current_position+16
                supposed_position3 = current_position+9
                highlight(position[supposed_position1])
                highlight(position[supposed_position2])
                color_changed = 3
                highlight(position[supposed_position3])
                movement[current_position] = 1
            elif weights[current_position+8] == 0 and weights[current_position+16] == 0:#The black pawn can move one or two blocks forward.
                color_of_supposed_position1 = color[current_position+8]
                color_of_supposed_position2 = color[current_position+16]
                supposed_position1 = current_position+8
                supposed_position2 = current_position+16
                highlight(position[supposed_position1])
                highlight(position[supposed_position2])
                color_changed = 2
                movement[current_position] = 1
            elif weights[current_position+8] == 0 and weights[current_position+16] != 0:#The black pawn can only move forward.
                color_of_supposed_position1 = color[current_position+8]
                supposed_position1 = current_position+8
                highlight(position[supposed_position1])
                color_changed = 1
                movement[current_position] = 1
        elif checking(current_position,current_position+7,weight):#Checking if the Piece has the ability to capture pieces place diagonal to it on right side.
            if weights[current_position+7] < 0 and weights[current_position+8] == 0 and weights[current_position+16] == 0:#The black pawn can move one or two blocks forward or capture the right piece.
                color_of_supposed_position1 = color[current_position+8]
                color_of_supposed_position2 = color[current_position+16]
                color_of_supposed_position3 = color[current_position+7]
                supposed_position1 = current_position+8
                supposed_position2 = current_position+16
                supposed_position3 = current_position+7
                highlight(position[supposed_position1])
                highlight(position[supposed_position2])
                color_changed = 3
                highlight(position[supposed_position3])
                movement[current_position] = 1
            elif weights[current_position+7] < 0 and weights[current_position+8] == 0 and weights[current_position+16] != 0: #The black pawn can move only one block forward or capture the right piece.
                color_of_supposed_position1 = color[current_position+8]
                color_of_supposed_position2 = color[current_position+7]
                supposed_position1 = current_position+8
                supposed_position2 = current_position+7
                highlight(position[supposed_position1])
                color_changed = 2
                highlight(position[supposed_position2])
                movement[current_position] = 1
            elif weights[current_position+7] < 0 and weights[current_position+8] != 0 : #The black pawn cannot move forward or capture the right piece.
                color_of_supposed_position1 = color[current_position+7]
                supposed_position1 = current_position+7
                color_changed = 1
                highlight(position[supposed_position1])
                movement[current_position] = 1
            elif weights[current_position+8] == 0 and weights[current_position+16] == 0:#The black pawn can move one or two blocks forward or capture the right piece.
                color_of_supposed_position1 = color[current_position+8]
                color_of_supposed_position2 = color[current_position+16]
                supposed_position1 = current_position+8
                supposed_position2 = current_position+16
                highlight(position[supposed_position1])
                highlight(position[supposed_position2])
                color_changed = 2
                movement[current_position] = 1
            elif weights[current_position+8] == 0 and weights[current_position+16] != 0:#The black pawn can move only one block forward.
                color_of_supposed_position1 = color[current_position+8]
                supposed_position1 = current_position+8
                highlight(position[supposed_position1])
                color_changed = 1
                movement[current_position] = 1
        elif checking(current_position,current_position+9,weight):
            if weights[current_position+9] < 0 and weights[current_position+8] == 0 and weights[current_position+16] == 0:#The black pawn can move one or two blocks forward or capture the left piece.
                color_of_supposed_position1 = color[current_position+8]
                color_of_supposed_position2 = color[current_position+16]
                color_of_supposed_position3 = color[current_position+9]
                supposed_position1 = current_position+8
                supposed_position2 = current_position+16
                supposed_position3 = current_position+9
                highlight(position[supposed_position1])
                highlight(position[supposed_position2])
                color_changed = 3
                highlight(position[supposed_position3])
                movement[current_position] = 1
            elif weights[current_position+9] < 0 and weights[current_position+8] == 0 and weights[current_position+16] != 0: #The black pawn can move one block forward or capture the left piece.
                color_of_supposed_position1 = color[current_position+8]
                color_of_supposed_position2 = color[current_position+9]
                supposed_position1 = current_position+8
                supposed_position2 = current_position+9
                highlight(position[supposed_position1])
                color_changed = 2
                highlight(position[supposed_position2])
                movement[current_position] = 1
            elif weights[current_position+9] < 0 and weights[current_position+8] != 0 : #The black pawn cannot move forward or capture the left piece.
                color_of_supposed_position1 = color[current_position+9]
                supposed_position1 = current_position+9
                color_changed = 1
                highlight(position[supposed_position1])
                movement[current_position] = 1
            elif weights[current_position+8] == 0 and weights[current_position+16] == 0:#The black pawn can move one or two places forward.
                color_of_supposed_position1 = color[current_position+8]
                color_of_supposed_position2 = color[current_position+16]
                supposed_position1 = current_position+8
                supposed_position2 = current_position+16
                highlight(position[supposed_position1])
                highlight(position[supposed_position2])
                color_changed = 2
                movement[current_position] = 1
            elif weights[current_position+8] == 0 and weights[current_position+16] != 0:#The black pawn can move only one block forward.
                color_of_supposed_position1 = color[current_position+8]
                supposed_position1 = current_position+8
                highlight(position[supposed_position1])
                color_changed = 1
                movement[current_position] = 1
    elif movement[current_position] == 1 and weight == -20:#It checks if the piece is a white Pawn and has been moved.
        if checking(current_position,current_position-7,weight) and checking(current_position,current_position-9,weight):#Checking if the Piece has the ability to capture pieces place diagonal to it on both side.
            if weights[current_position-7] > 0 and weights[current_position-9] > 0 and weights[current_position-8] == 0:#The white pawn can move one block forward or capture the left or right piece.
                color_of_supposed_position1 = color[current_position-8]
                color_of_supposed_position2 = color[current_position-7]
                color_of_supposed_position3 = color[current_position-9]
                supposed_position1 = current_position-8
                supposed_position2 = current_position-7
                supposed_position3 = current_position-9
                highlight(position[supposed_position1])
                color_changed = 3
                highlight(position[supposed_position2])
                highlight(position[supposed_position3])
            elif weights[current_position-7] > 0 and weights[current_position-9] > 0 and weights[current_position-8] != 0:#The white pawn cannot move forward but it can capture the left or right piece.
                color_of_supposed_position1 = color[current_position-7]
                color_of_supposed_position2 = color[current_position-9]
                supposed_position1 = current_position-7
                supposed_position2 = current_position-9
                color_changed = 2
                highlight(position[supposed_position1])
                highlight(position[supposed_position2])
            elif weights[current_position-7] > 0 and weights[current_position-8] == 0: #The white pawn can move one block forward or capture the right piece.
                color_of_supposed_position1 = color[current_position-8]
                color_of_supposed_position2 = color[current_position-7]
                supposed_position1 = current_position-8
                supposed_position2 = current_position-7
                highlight(position[supposed_position1])
                color_changed = 2
                highlight(position[supposed_position2])
            elif weights[current_position-9] > 0  and weights[current_position-8] == 0:#The white pawn can move one block forward or capture the left piece.
                color_of_supposed_position1 = color[current_position-8]
                color_of_supposed_position2 = color[current_position-9]
                supposed_position1 = current_position-8
                supposed_position2 = current_position-9
                highlight(position[supposed_position1])
                color_changed = 2
                highlight(position[supposed_position2])
            elif weights[current_position-7] > 0 and weights[current_position-8] != 0:#The white pawn cannot move forward and it can capture the right piece.
                color_of_supposed_position1 = color[current_position-7]
                supposed_position1 = current_position-7
                color_changed = 1
                highlight(position[supposed_position1])
            elif weights[current_position-9] > 0 and weights[current_position-8] != 0:#The white pawn cannot move forward and it can capture the left piece.
                color_of_supposed_position1 = color[current_position-9]
                supposed_position1 = current_position-9
                color_changed = 1
                highlight(position[supposed_position1])
            elif weights[current_position-8] == 0:#The white pawn can only move one block forward.
                color_of_supposed_position1 = color[current_position-8]
                supposed_position1 = current_position-8
                highlight(position[supposed_position1])
                color_changed = 1
        elif checking(current_position,current_position-7,weight):#Checking if the Piece has the ability to capture pieces place diagonal to it on right side.
            if weights[current_position-7] > 0 and weights[current_position-8] == 0: #The white pawn can move one block forward or capture the right piece.
                color_of_supposed_position1 = color[current_position-8]
                color_of_supposed_position2 = color[current_position-7]
                supposed_position1 = current_position-8
                supposed_position2 = current_position-7
                highlight(position[supposed_position1])
                color_changed = 2
                highlight(position[supposed_position2])
            elif weights[current_position-7] > 0 and weights[current_position-8] != 0:#The white pawn cannot move forward and it can capture the right piece.
                color_of_supposed_position1 = color[current_position-7]
                supposed_position1 = current_position-7
                color_changed = 1
                highlight(position[supposed_position1])
            elif weights[current_position-8] == 0:#The white pawn can only move one block forward.
                color_of_supposed_position1 = color[current_position-8]
                supposed_position1 = current_position-8
                highlight(position[supposed_position1])
                color_changed = 1
        elif checking(current_position,current_position-9,weight):#Checking if the Piece has the ability to capture pieces place diagonal to it on left side.
            if weights[current_position-9] > 0 and weights[current_position-8] == 0:#The white pawn can move one block forward or capture the left piece.
                color_of_supposed_position1 = color[current_position-8]
                color_of_supposed_position2 = color[current_position-9]
                supposed_position1 = current_position-8
                supposed_position2 = current_position-9
                highlight(position[supposed_position1])
                color_changed = 2
                highlight(position[supposed_position2])
            elif weights[current_position-9] > 0 and weights[current_position-8] != 0:#The white pawn cannot move forward and it can capture the left piece.
                color_of_supposed_position1 = color[current_position-9]
                supposed_position1 = current_position-9
                color_changed = 1
                highlight(position[supposed_position1])
            elif weights[current_position-8] == 0:#The white pawn can only move one block forward.
                color_of_supposed_position1 = color[current_position-8]
                supposed_position1 = current_position-8
                highlight(position[supposed_position1])
                color_changed = 1
    elif movement[current_position] == 2 and weight == -20:#It checks if the piece is a white Pawn and has never moved.
        if checking(current_position,current_position-7,weight) and checking(current_position,current_position-9,weight):#Checking if the Piece has the ability to capture pieces place diagonal to it on both side.
            if weights[current_position-7] > 0 and weights[current_position-9] > 0 and weights[current_position-8] == 0 and weights[current_position-16] == 0:#The white pawn can move one or two blocks forward or capture the left or right piece.
                color_of_supposed_position1 = color[current_position-8]
                color_of_supposed_position2 = color[current_position-16]
                color_of_supposed_position3 = color[current_position-7]
                color_of_supposed_position4 = color[current_position-9]
                supposed_position1 = current_position-8
                supposed_position2 = current_position-16
                supposed_position3 = current_position-7
                supposed_position4 = current_position-9
                highlight(position[supposed_position1])
                highlight(position[supposed_position2])
                color_changed = 4
                highlight(position[supposed_position3])
                highlight(position[supposed_position4])
                movement[current_position] = 1
            elif weights[current_position-7] > 0 and weights[current_position-9] > 0 and weights[current_position-8] == 0 and weights[current_position-16] != 0:#The white pawn can move only one blocks forward or capture the left or right piece.
                color_of_supposed_position1 = color[current_position-8]
                color_of_supposed_position2 = color[current_position-7]
                color_of_supposed_position3 = color[current_position-9]
                supposed_position1 = current_position-8
                supposed_position2 = current_position-7
                supposed_position3 = current_position-9
                highlight(position[supposed_position1])
                color_changed = 3
                highlight(position[supposed_position2])
                highlight(position[supposed_position3])
                movement[current_position] = 1
            elif weights[current_position-7] > 0 and weights[current_position-8] == 0 and weights[current_position-16] == 0:#The white pawn can move one or two blocks forward or capture the right piece.
                color_of_supposed_position1 = color[current_position-8]
                color_of_supposed_position2 = color[current_position-16]
                color_of_supposed_position3 = color[current_position-7]
                supposed_position1 = current_position-8
                supposed_position2 = current_position-16
                supposed_position3 = current_position-7
                highlight(position[supposed_position1])
                highlight(position[supposed_position2])
                color_changed = 3
                highlight(position[supposed_position3])
                movement[current_position] = 1
            elif weights[current_position-9] > 0 and weights[current_position-8] == 0 and weights[current_position-16] == 0:#The white pawn can move one or two blocks forward or capture the left piece.
                color_of_supposed_position1 = color[current_position-8]
                color_of_supposed_position2 = color[current_position-16]
                color_of_supposed_position3 = color[current_position-9]
                supposed_position1 = current_position-8
                supposed_position2 = current_position-16
                supposed_position3 = current_position-9
                highlight(position[supposed_position1])
                highlight(position[supposed_position2])
                color_changed = 3
                highlight(position[supposed_position3])
                movement[current_position] = 1
            elif weights[current_position-8] == 0 and weights[current_position-16] == 0:#The white pawn can move one or two blocks forward.
                color_of_supposed_position1 = color[current_position-8]
                color_of_supposed_position2 = color[current_position-16]
                supposed_position1 = current_position-8
                supposed_position2 = current_position-16
                highlight(position[supposed_position1])
                highlight(position[supposed_position2])
                color_changed = 2
                movement[current_position] = 1
            elif weights[current_position-8] == 0 and weights[current_position-16] != 0:#The white pawn can only move forward.
                color_of_supposed_position1 = color[current_position-8]
                supposed_position1 = current_position-8
                highlight(position[supposed_position1])
                color_changed = 1
                movement[current_position] = 1
        elif checking(current_position,current_position-7,weight):#Checking if the Piece has the ability to capture pieces place diagonal to it on right side.
            if weights[current_position-7] > 0 and weights[current_position-8] == 0 and weights[current_position-16] == 0:#The white pawn can move one or two blocks forward or capture the right piece.
                color_of_supposed_position1 = color[current_position-8]
                color_of_supposed_position2 = color[current_position-16]
                color_of_supposed_position3 = color[current_position-7]
                supposed_position1 = current_position-8
                supposed_position2 = current_position-16
                supposed_position3 = current_position-7
                highlight(position[supposed_position1])
                highlight(position[supposed_position2])
                color_changed = 3
                highlight(position[supposed_position3])
                movement[current_position] = 1
            elif weights[current_position-7] > 0 and weights[current_position-8] == 0 and weights[current_position-16] != 0: #The white pawn can move only one block forward or capture the right piece.
                color_of_supposed_position1 = color[current_position-8]
                color_of_supposed_position2 = color[current_position-7]
                supposed_position1 = current_position-8
                supposed_position2 = current_position-7
                highlight(position[supposed_position1])
                color_changed = 2
                highlight(position[supposed_position2])
                movement[current_position] = 1
            elif weights[current_position-7] > 0 and weights[current_position-8] != 0 : #The white pawn cannot move forward or capture the right piece.
                color_of_supposed_position1 = color[current_position-7]
                supposed_position1 = current_position-7
                color_changed = 1
                highlight(position[supposed_position1])
                movement[current_position] = 1
            elif weights[current_position-8] == 0 and weights[current_position-16] == 0:#The white pawn can move one or two blocks forward or capture the right piece.
                color_of_supposed_position1 = color[current_position-8]
                color_of_supposed_position2 = color[current_position-16]
                supposed_position1 = current_position-8
                supposed_position2 = current_position-16
                highlight(position[supposed_position1])
                highlight(position[supposed_position2])
                color_changed = 2
                movement[current_position] = 1
            elif weights[current_position-8] == 0 and weights[current_position-16] != 0:#The white pawn can move only one block forward.
                color_of_supposed_position1 = color[current_position-8]
                supposed_position1 = current_position-8
                highlight(position[supposed_position1])
                color_changed = 1
                movement[current_position] = 1
        elif checking(current_position,current_position-9,weight):
            if weights[current_position-9] > 0 and weights[current_position-8] == 0 and weights[current_position-16] == 0:#The white pawn can move one or two blocks forward or capture the left piece.
                color_of_supposed_position1 = color[current_position-8]
                color_of_supposed_position2 = color[current_position-16]
                color_of_supposed_position3 = color[current_position-9]
                supposed_position1 = current_position-8
                supposed_position2 = current_position-16
                supposed_position3 = current_position-9
                highlight(position[supposed_position1])
                highlight(position[supposed_position2])
                color_changed = 3
                highlight(position[supposed_position3])
                movement[current_position] = 1
            elif weights[current_position-9] > 0 and weights[current_position-8] == 0 and weights[current_position-16] != 0: #The white pawn can move one block forward or capture the left piece.
                color_of_supposed_position1 = color[current_position-8]
                color_of_supposed_position2 = color[current_position-9]
                supposed_position1 = current_position-8
                supposed_position2 = current_position-9
                highlight(position[supposed_position1])
                color_changed = 2
                highlight(position[supposed_position2])
                movement[current_position] = 1
            elif weights[current_position-9] > 0 and weights[current_position-8] != 0 : #The white pawn cannot move forward or capture the left piece.
                color_of_supposed_position1 = color[current_position-9]
                supposed_position1 = current_position-9
                color_changed = 1
                highlight(position[supposed_position1])
                movement[current_position] = 1
            elif weights[current_position-8] == 0 and weights[current_position-16] == 0:#The white pawn can move one or two places forward.
                color_of_supposed_position1 = color[current_position+8]
                color_of_supposed_position2 = color[current_position+16]
                supposed_position1 = current_position+8
                supposed_position2 = current_position+16
                highlight(position[supposed_position1])
                highlight(position[supposed_position2])
                color_changed = 2
                movement[current_position] = 1
            elif weights[current_position-8] == 0 and weights[current_position-16] != 0:#The white pawn can move only one block forward.
                color_of_supposed_position1 = color[current_position-8]
                supposed_position1 = current_position-8
                highlight(position[supposed_position1])
                color_changed = 1
                movement[current_position] = 1

def future_knight_position(current_position,weight):
    global code
    color_changed = 5
    if weight == 30:
        code = 1
        L_black(current_position,current_position-17,weight)
        code = 2
        L_black(current_position,current_position-15,weight)
        code = 3
        L_black(current_position,current_position-6,weight)
        code = 4
        L_black(current_position,current_position+10,weight)
        code = 5
        L_black(current_position,current_position+17,weight)
        code = 6
        L_black(current_position,current_position+15,weight)
        code = 7
        L_black(current_position,current_position+6,weight)
        code = 8
        L_black(current_position,current_position-10,weight)
    elif weight == -30:
        code = 1
        L_white(current_position,current_position-17,weight)
        code = 2
        L_white(current_position,current_position-15,weight)
        code = 3
        L_white(current_position,current_position-6,weight)
        code = 4
        L_white(current_position,current_position+10,weight)
        code = 5
        L_white(current_position,current_position+17,weight)
        code = 6
        L_white(current_position,current_position+15,weight)
        code = 7
        L_white(current_position,current_position+6,weight)
        code = 8
        L_white(current_position,current_position-10,weight)
    color_changed = 5

def L_white(current_position,element,weight):
    global empty
    global color_changed ,color_of_supposed_position , supposed_position
    if checking(current_position,element,weight):
        if weights[element] > 0:
            color_of_supposed_position[empty] = color[position[element]]
            supposed_position[empty] = element
            color_changed = 1
            highlight(position[supposed_position[empty]])
        elif weights[element] == 0:
            color_of_supposed_position[empty] = color[position[element]]
            supposed_position[empty] = element
            highlight(position[supposed_position[empty]])
            color_changed = 1
    empty += 1
    color_changed = 5

def L_black(current_position,element,weight):
    global empty
    global color_changed ,color_of_supposed_position  , supposed_position
    if checking(current_position,element,weight):
        if weights[element] < 0:
            color_of_supposed_position[empty] = color[position[element]]
            supposed_position[empty] = element
            color_changed = 1
            highlight(position[supposed_position[empty]])
        elif weights[element] == 0:
            color_of_supposed_position[empty] = color[position[element]]
            supposed_position[empty] = element
            highlight(position[supposed_position[empty]])
            color_changed = 1
    empty += 1
    color_changed = 5
    

def future_bishop_position(current_position,weight):
    allignment_function(current_position,-9,weight)
    allignment_function(current_position,-7,weight)
    allignment_function(current_position,9,weight)
    allignment_function(current_position,7,weight)

def future_queen_position(current_position,weight):
    allignment_function(current_position,-8,weight)
    allignment_function(current_position,-7,weight)
    allignment_function(current_position,1,weight)
    allignment_function(current_position,9,weight)
    allignment_function(current_position,8,weight)
    allignment_function(current_position,7,weight)
    allignment_function(current_position,-1,weight)
    allignment_function(current_position,-9,weight)

def future_rook_position(current_position,weight):
    allignment_function(current_position,-8,weight)
    allignment_function(current_position,1,weight)
    allignment_function(current_position,8,weight)
    allignment_function(current_position,-1,weight)

def future_king_position(current_position,weight):
    global empty , color_changed , castling
    king_allignment_function(current_position,-8,weight)
    king_allignment_function(current_position,-7,weight)
    king_allignment_function(current_position,1,weight)
    king_allignment_function(current_position,9,weight)
    king_allignment_function(current_position,8,weight)
    king_allignment_function(current_position,7,weight)
    king_allignment_function(current_position,-1,weight)
    king_allignment_function(current_position,-9,weight)
    if movement[current_position] == 2:
        if (weights[current_position+1] == 0 and weights[current_position+2] == 0 and movement[current_position+3] == 2 and ((weights[current_position] > 0 and weights[current_position+3] > 0) or (weights[current_position] < 0 and weights[current_position+3] < 0))) and (weights[current_position-1] != 0 and weights[current_position-2] != 0 and weights[current_position-3] != 0):
            if checking_danger(current_position+2,weight):
                color_changed = 6
                aftercastlekingposition = current_position+2
                color_of_supposed_position[empty] = color[position[aftercastlekingposition]]
                supposed_position[empty] = aftercastlekingposition
                highlight(position[supposed_position[empty]])
                castling = 1
        elif weights[current_position-1] == 0 and weights[current_position-2] == 0 and weights[current_position-3] == 0 and movement[current_position-4] == 2 and ((weights[current_position] > 0 and weights[current_position-4] > 0) or (weights[current_position] < 0 and weights[current_position-4] < 0)) and (weights[current_position+1] != 0 and weights[current_position+2] != 0):
            if checking_danger(current_position-2,weight):
                color_changed = 6
                aftercastlekingposition = current_position-2
                color_of_supposed_position[empty] = color[position[aftercastlekingposition]]
                supposed_position[empty] = aftercastlekingposition
                highlight(position[supposed_position[empty]])
                castling = 2
        elif (weights[current_position-1] == 0 and weights[current_position-2] == 0 and weights[current_position-3] == 0 and movement[current_position-4] == 2) and (weights[current_position+1] == 0 and weights[current_position+2] == 0 and movement[current_position+3] == 2) and ((weights[current_position] > 0 and weights[current_position-4] > 0) or (weights[current_position] < 0 and weights[current_position-4] < 0)):
            if checking_danger(current_position+2,weight):
                color_changed = 6
                aftercastlekingposition = current_position+2
                color_of_supposed_position[empty] = color[position[aftercastlekingposition]]
                supposed_position[empty] = aftercastlekingposition
                highlight(position[supposed_position[empty]])
                castling = 3
            if checking_danger(current_position-2,weight):
                color_changed = 6
                aftercastlekingposition = current_position-2
                color_of_supposed_position[empty] = color[position[aftercastlekingposition]]
                supposed_position[empty] = aftercastlekingposition
                highlight(position[supposed_position[empty]])
                castling = 3
    color_changed = 5

def allignment_function(current_position,allignment,weight):
    global empty
    global color_changed
    if weight > 0:
        if weights[current_position+allignment] < 0 and checking(current_position,current_position+allignment,weight):
            color_of_supposed_position[empty] = color[position[current_position+allignment]]
            supposed_position[empty] = current_position+allignment
            color_changed = 1
            highlight(position[supposed_position[empty]])
            empty += 1
        elif weights[current_position+allignment] == 0 and checking(current_position,current_position+allignment,weight):
            color_of_supposed_position[empty] = color[position[current_position+allignment]]
            supposed_position[empty] = current_position+allignment
            highlight(position[supposed_position[empty]])
            color_changed = 0
            empty += 1
            allignment_function(current_position+allignment,allignment,weight)
    elif weight < 0:
        if weights[current_position+allignment] > 0 and checking(current_position,current_position+allignment,weight):
            color_of_supposed_position[empty] = color[position[current_position+allignment]]
            supposed_position[empty] = current_position+allignment
            color_changed = 1
            highlight(position[supposed_position[empty]])
            empty += 1
        elif weights[current_position+allignment] == 0 and checking(current_position,current_position+allignment,weight):
            color_of_supposed_position[empty] = color[position[current_position+allignment]]
            supposed_position[empty] = current_position+allignment
            highlight(position[supposed_position[empty]])
            color_changed = 0
            empty += 1
            allignment_function(current_position+allignment,allignment,weight)
    color_changed = 5

def king_allignment_function(current_position,allignment,weight):
    global empty
    global color_changed
    if weight > 0:
        if weights[current_position+allignment] < 0 and checking(current_position,current_position+allignment,weight) and checking_danger(current_position+allignment,weight):
            color_of_supposed_position[empty] = color[position[current_position+allignment]]
            color_changed = 1
            supposed_position[empty] = current_position+allignment
            highlight(position[supposed_position[empty]])
            empty += 1
        elif weights[current_position+allignment] == 0 and checking(current_position,current_position+allignment,weight) and checking_danger(current_position+allignment,weight):
            color_of_supposed_position[empty] = color[position[current_position+allignment]]
            supposed_position[empty] = current_position+allignment
            highlight(position[supposed_position[empty]])
            color_changed = 5
            empty += 1
    elif weight < 0:
        if weights[current_position+allignment] > 0 and checking(current_position,current_position+allignment,weight) and checking_danger(current_position+allignment,weight):
            color_of_supposed_position[empty] = color[position[current_position+allignment]]
            color_changed = 1
            supposed_position[empty] = current_position+allignment
            highlight(position[supposed_position[empty]])
            empty += 1
        elif weights[current_position+allignment] == 0 and checking(current_position,current_position+allignment,weight) and checking_danger(current_position+allignment,weight):
            color_of_supposed_position[empty] = color[position[current_position+allignment]]
            supposed_position[empty] = current_position+allignment
            highlight(position[supposed_position[empty]])
            color_changed = 5
            empty += 1
    color_changed = 5

def swap(current_position,final_position,weight):
    global transparent_no
    global color_of_supposed_position , supposed_position
    global castling , initial_color_of_current_position , start , end , supposed_position1 , supposed_position2 , supposed_position3 , supposed_position4 , supposed_position5 , supposed_position6 , supposed_position7 , supposed_position8 , capture
    global color_of_supposed_position1 , color_of_supposed_position2 , color_of_supposed_position3 , color_of_supposed_position4 , color_of_supposed_position5 , color_of_supposed_position6 , color_of_supposed_position7 , color_of_supposed_position8 , color_changed
    global color_changed , empty
    global initial_color_of_current_position
    global supposed_position1 , supposed_position2 , supposed_position3 , supposed_position4 , supposed_position5 , supposed_position6 , supposed_position7 , supposed_position8 , color_of_supposed_position1 , color_of_supposed_position2 , color_of_supposed_position3 , color_of_supposed_position4 , color_of_supposed_position5 , color_of_supposed_position6 , color_of_supposed_position7 , color_of_supposed_position8
    if castling == -1:
        if (weights[current_position] > 0 and weights[final_position] == 0) or (weights[current_position] < 0 and weights[final_position] == 0):
            color_correction()
            swap_position(current_position,final_position)
            swap_color(current_position,final_position)
            swap_movement(current_position,final_position)
            swap_weights(current_position,final_position)
        elif (weights[current_position] > 0 and weights[final_position] < 0) or (weights[current_position] < 0 and weights[final_position] > 0):
            color_correction()
            swap_position(current_position,final_position)
            swap_color(current_position,final_position)
            swap_movement(current_position,final_position)
            swap_weights(current_position,final_position)
            swap_position(current_position,transparent_no)
            swap_color(current_position,transparent_no)
            swap_movement(current_position,transparent_no)
            swap_weights(current_position,transparent_no)
            transparent_no += 1
    elif castling == 1:
        movement[current_position] = 1
        movement[current_position+3] = 1
        movement[current_position-4] = 1
        color_correction()
        swap_position(current_position+3,current_position+1)
        swap_color(current_position+3,current_position+1)
        swap_movement(current_position+3,current_position+1)
        swap_weights(current_position+3,current_position+1)
        swap_position(current_position,final_position)
        swap_color(current_position,final_position)
        swap_movement(current_position,final_position)
        swap_weights(current_position,final_position)
    elif castling == 2:
        movement[current_position] = 1
        movement[current_position-4] = 1
        movement[current_position+3] = 1        
        swap_position(current_position-4,current_position-1)
        swap_color(current_position-4,current_position-1)
        swap_movement(current_position-4,current_position-1)
        swap_weights(current_position-4,current_position-1)
        swap_position(current_position,final_position)
        swap_color(current_position,final_position)
        swap_movement(current_position,final_position)
        swap_weights(current_position,final_position)
    castling = -1
    empty = 0
    color_changed = -1
    initial_color_of_current_position  = -1
    supposed_position1 = supposed_position2 = supposed_position3 = supposed_position4 = supposed_position5 = supposed_position6 = supposed_position7 = supposed_position8 = -1
    color_of_supposed_position1 = color_of_supposed_position2 = color_of_supposed_position3 = color_of_supposed_position4 = color_of_supposed_position5 = color_of_supposed_position6 = color_of_supposed_position7 = color_of_supposed_position8 = -1
    color_of_supposed_position = [-1]*25
    supposed_position = [-1]*25
        
def swap_position(current_position,final_position):
    temp = position[current_position]
    position[current_position] = position[final_position]
    position[final_position] = temp

def swap_color(current_position,final_position):
    temp = color[position[current_position]]
    color[position[current_position]] = color[position[final_position]]
    color[position[final_position]] = temp

def swap_movement(current_position,final_position):
    temp = movement[current_position]
    movement[current_position] = movement[final_position]
    movement[final_position] = temp

def swap_weights(current_position,final_position):
    temp = weights[current_position]
    weights[current_position] = weights[final_position]
    weights[final_position] = temp
        


def color_correction():
    global initial_color_of_current_position , color_changed , supposed_position1 , supposed_position2 , supposed_position3 , supposed_position4 , supposed_position5 , supposed_position6 , supposed_position7 , supposed_position8
    global color_of_supposed_position1 , color_of_supposed_position2 , color_of_supposed_position3 , color_of_supposed_position4 , color_of_supposed_position5 , color_of_supposed_position6 , color_of_supposed_position7 , color_of_supposed_position8
    if color_changed == 1:
        color[position[supposed_position1]] = color_of_supposed_position1
        color_changed = 0
    elif color_changed == 2:
        color[position[supposed_position1]] = color_of_supposed_position1
        color[position[supposed_position2]] = color_of_supposed_position2
        color_changed = 0
    elif color_changed == 3:
        color[position[supposed_position1]] = color_of_supposed_position1
        color[position[supposed_position2]] = color_of_supposed_position2
        color[position[supposed_position3]] = color_of_supposed_position3
        color_changed = 0
    elif color_changed == 4:
        color[supposed_position1] = color_of_supposed_position1
        color[supposed_position2] = color_of_supposed_position2
        color[supposed_position3] = color_of_supposed_position3
        color[supposed_position4] = color_of_supposed_position4
        color_changed = 0
    elif color_changed == 5:
        for empty in range(0,25):
            if supposed_position[empty] != -1:
                color[position[supposed_position[empty]]] = color_of_supposed_position[empty]


def checking_danger(current_position,weight):#we have to check if the king can go to current position or not.
    global count
    if weight < 0:
        if weights[current_position-9] == 20 or weights[current_position-7] == 20 or weights[current_position-17] == 30 or weights[current_position-15] == 30 or weights[current_position-6] == 30 or weights[current_position+10] == 30 or weights[current_position+17] == 30 or weights[current_position+15] == 30 or weights[current_position+6] == 30 or weights[current_position-10] == 30:
            return False
        count = 0
        if white_danger(current_position,-8,weight):
            return False
        count = 0
        if white_danger(current_position,-7,weight):
            return False
        count = 0
        if white_danger(current_position,1,weight):
            return False
        count = 0
        if white_danger(current_position,9,weight):
            return False
        count = 0
        if white_danger(current_position,8,weight):
            return False
        count = 0
        if white_danger(current_position,7,weight):
            return False
        count = 0
        if white_danger(current_position,-1,weight):
            return False
        count = 0
        if white_danger(current_position,-9,weight):
            return False
        else:
            return True
    elif weight > 0:
        if weights[current_position+9] == -20 or weights[current_position+7] == -20 or weights[current_position-17] == -30 or weights[current_position-15] == -30 or weights[current_position-6] == -30 or weights[current_position+10] == -30 or weights[current_position+17] == -30 or weights[current_position+15] == -30 or weights[current_position+6] == -30 or weights[current_position-10] == -30:
            return False
        count = 0
        if black_danger(current_position,-8,weight):
            return False
        count = 0
        if black_danger(current_position,-7,weight):
            return False
        count = 0
        if black_danger(current_position,1,weight):
            return False
        count = 0
        if black_danger(current_position,9,weight):
            return False
        count = 0
        if black_danger(current_position,8,weight):
            return False
        count = 0
        if black_danger(current_position,7,weight):
            return False
        count = 0
        if black_danger(current_position,-1,weight):
            return False
        count = 0
        if black_danger(current_position,-9,weight):
            return False
        else:
            return True

def white_danger(checking_position,allignment,weight):
    global count
    if (weights[checking_position+allignment] == 0 or weights[checking_position+allignment] == weight) and checking(checking_position,checking_position+allignment,weight):
        count += 1
        if white_danger(checking_position+allignment,allignment,weight):
            return True
        else:
            return False
    elif weights[checking_position+allignment] < 0 and weights[checking_position+allignment] != weight:
        return False
    elif weights[checking_position+allignment] > 0:
        if weights[checking_position+allignment] == 100 and count == 0:
            return True
        elif weights[checking_position+allignment] == 90:
            return True
        elif weights[checking_position+allignment] == 50 and (allignment == 8 or allignment == -8 or allignment == 1 or allignment == -1):
            return True
        elif weights[checking_position+allignment] == 40 and (allignment == 7 or allignment == -7 or allignment == 9 or allignment == -9):
            return True
def black_danger(checking_position,allignment,weight):
    global count
    if (weights[checking_position+allignment] == 0 or weights[checking_position+allignment] == weight) and checking(checking_position,checking_position+allignment,weight):
        count += 1
        if white_danger(checking_position+allignment,allignment,weight):
            return True
        return False
    elif weights[checking_position+allignment] > 0 and weights[checking_position+allignment] != weight:
        return False
    elif weights[checking_position+allignment] < 0:
        if weights[checking_position+allignment] == -100 and count == 0:
            return True
        elif weights[checking_position+allignment] == -90:
            return True
        elif weights[checking_position+allignment] == -50 and (allignment == 8 or allignment == -8 or allignment == 1 or allignment == -1):
            return True
        elif weights[checking_position+allignment] == -40 and (allignment == 7 or allignment == -7 or allignment == 9 or allignment == -9):
            return True

def checking(current_position,future_position,weight):
    global code
    if weight == 20:
        if ((current_position >= 8 and current_position < 16) and (future_position >= 16 and future_position < 24)) or ((current_position >= 16 and current_position < 24) and (future_position >= 24 and future_position < 32)) or ((current_position >= 24 and current_position < 32) and (future_position >= 32 and future_position < 40)) or ((current_position >= 32 and current_position < 40) and (future_position >= 40 and future_position < 48)) or ((current_position >= 40 and current_position < 48) and (future_position >= 48 and future_position < 56)) or ((current_position >= 48 and current_position < 56) and (future_position >= 56 and future_position < 64)):
            return True
        else:
            return False
    elif weight == -20:
        if ((current_position >= 8 and current_position < 16) and (future_position >= 0 and future_position < 8)) or ((current_position >= 16 and current_position < 24) and (future_position >= 8 and future_position < 16)) or ((current_position >= 24 and current_position < 32) and (future_position >= 16 and future_position < 24)) or ((current_position >= 32 and current_position < 40) and (future_position >= 24 and future_position < 32)) or ((current_position >= 40 and current_position < 48) and (future_position >= 32 and future_position < 40)) or ((current_position >= 48 and current_position < 56) and (future_position >= 40 and future_position < 56)):
            return True
        else:
            return False
    if weight == 30 or weight == -30:
        if code == 1:
            if ((current_position >= 17 and current_position < 24) and (future_position >= 0 and future_position < 7)) or ((current_position >= 25 and current_position < 32) and (future_position >= 8 and future_position < 15)) or ((current_position >= 33 and current_position < 40) and (future_position >= 16 and future_position < 23)) or ((current_position >= 41 and current_position < 48) and (future_position >= 24 and future_position < 31)) or ((current_position >= 49 and current_position < 56) and (future_position >= 32 and future_position < 39)) or ((current_position >= 57 and current_position < 64) and (future_position >= 40 and future_position < 47)):
                return True
            else:
                return False
        if code == 2:
            if ((current_position >= 16 and current_position < 23) and (future_position >= 1 and future_position < 8)) or ((current_position >= 24 and current_position < 31) and (future_position >= 9 and future_position < 16)) or ((current_position >= 32 and current_position < 39) and (future_position >= 17 and future_position < 24)) or ((current_position >= 40 and current_position < 47) and (future_position >= 25 and future_position < 32)) or ((current_position >= 48 and current_position < 55) and (future_position >= 33 and future_position < 40)) or ((current_position >= 56 and current_position < 63) and (future_position >= 41 and future_position < 48)):
                return True
            else:
                return False
        if code == 3:
            if ((current_position >= 8 and current_position < 14) and (future_position >= 2 and future_position < 8)) or ((current_position >= 16 and current_position < 22) and (future_position >= 10 and future_position < 16)) or ((current_position >= 24 and current_position < 30) and (future_position >= 18 and future_position < 24)) or ((current_position >= 32 and current_position < 38) and (future_position >= 26 and future_position < 32)) or ((current_position >= 40 and current_position < 46) and (future_position >= 34 and future_position < 40)) or ((current_position >= 48 and current_position < 54) and (future_position >= 42 and future_position < 48)) or ((current_position >= 56 and current_position < 62) and (future_position >= 50 and future_position < 56)):
                return True
            else:
                return False
        if code == 4:
            if ((current_position >= 0 and current_position < 6) and (future_position >= 10 and future_position < 16)) or ((current_position >= 8 and current_position < 14) and (future_position >= 18 and future_position < 24)) or ((current_position >= 16 and current_position < 22) and (future_position >= 26 and future_position < 32)) or ((current_position >= 24 and current_position < 30) and (future_position >= 34 and future_position < 40)) or ((current_position >= 32 and current_position < 38) and (future_position >= 42 and future_position < 48)) or ((current_position >= 40 and current_position < 46) and (future_position >= 50 and future_position < 56)) or ((current_position >= 48 and current_position < 54) and (future_position >= 58 and future_position < 64)):
                return True
            else:
                return False
        if code == 5:
            if ((current_position >= 0 and current_position < 7) and (future_position >= 17 and future_position < 24)) or ((current_position >= 8 and current_position < 15) and (future_position >= 25 and future_position < 32)) or ((current_position >= 16 and current_position < 23) and (future_position >= 33 and future_position < 40)) or ((current_position >= 24 and current_position < 31) and (future_position >= 41 and future_position < 48)) or ((current_position >= 32 and current_position < 39) and (future_position >= 49 and future_position < 56)) or ((current_position >= 40 and current_position < 47) and (future_position >= 57 and future_position < 64)) :
                return True
            else:
                return False
        if code == 6:
            if ((current_position >= 1 and current_position < 8) and (future_position >= 16 and future_position < 23)) or ((current_position >= 9 and current_position < 15) and (future_position >= 24 and future_position < 31)) or ((current_position >= 17 and current_position < 24) and (future_position >= 32 and future_position < 39)) or ((current_position >= 25 and current_position < 32) and (future_position >= 40 and future_position < 47)) or ((current_position >= 33 and current_position < 40) and (future_position >= 48 and future_position < 55)) or ((current_position >= 41 and current_position < 48) and (future_position >= 56 and future_position < 63)) :
                return True
            else:
                return False
        if code == 7:
            if ((current_position >= 2 and current_position < 8) and (future_position >= 8 and future_position < 14)) or ((current_position >= 10 and current_position < 16) and (future_position >= 16 and future_position < 22)) or ((current_position >= 18 and current_position < 24) and (future_position >= 24 and future_position < 30)) or ((current_position >= 26 and current_position < 32) and (future_position >= 32 and future_position < 38)) or ((current_position >= 34 and current_position < 40) and (future_position >= 40 and future_position < 46)) or ((current_position >= 42 and current_position < 48) and (future_position >= 48 and future_position < 54)) or ((current_position >= 50 and current_position < 56) and (future_position >= 56 and future_position < 62)):
                return True
            else:
                return False
        if code == 8:
            if ((current_position >= 10 and current_position < 16) and (future_position >= 0 and future_position < 6)) or ((current_position >= 18 and current_position < 24) and (future_position >= 8 and future_position < 14)) or ((current_position >= 26 and current_position < 32) and (future_position >= 16 and future_position < 22)) or ((current_position >= 34 and current_position < 40) and (future_position >= 24 and future_position < 30)) or ((current_position >= 42 and current_position < 48) and (future_position >= 32 and future_position < 38)) or ((current_position >= 50 and current_position < 56) and (future_position >= 40 and future_position < 46)) or ((current_position >= 58 and current_position < 64) and (future_position >= 48 and future_position < 54)):
                return True
            else:
                return False
    if weight == 40 or weight == -40 :
        if (((current_position >= 0 and current_position < 8) and (future_position >= 8 and future_position < 16)) or ((current_position >= 8 and current_position < 16) and (future_position >= 16 and future_position < 24)) or ((current_position >= 16 and current_position < 24) and (future_position >= 24 and future_position < 32)) or ((current_position >= 24 and current_position < 32) and (future_position >= 32 and future_position < 40)) or ((current_position >= 32 and current_position < 40) and (future_position >= 40 and future_position < 48)) or ((current_position >= 40 and current_position < 48) and (future_position >= 48 and future_position < 56)) or ((current_position >= 48 and current_position < 56) and (future_position >= 56 and future_position < 64))) or (((current_position >= 8 and current_position < 16) and (future_position >= 0 and future_position < 8)) or ((current_position >= 16 and current_position < 24) and (future_position >= 8 and future_position < 16)) or ((current_position >= 24 and current_position < 32) and (future_position >= 16 and future_position < 24)) or ((current_position >= 32 and current_position < 40) and (future_position >= 24 and future_position < 32)) or ((current_position >= 40 and current_position < 48) and (future_position >= 32 and future_position < 40)) or ((current_position >= 48 and current_position < 56) and (future_position >= 40 and future_position < 56)) or ((current_position >= 56 and current_position < 64) and (future_position >= 48 and future_position < 56))):
            return True
        else:
            return False
    if (weight == 50 or weight == -50) and (current_position-future_position == 8 or current_position-future_position == -8):
        if (((current_position >= 0 and current_position < 8) and (future_position >= 8 and future_position < 16)) or ((current_position >= 8 and current_position < 16) and (future_position >= 16 and future_position < 24)) or ((current_position >= 16 and current_position < 24) and (future_position >= 24 and future_position < 32)) or ((current_position >= 24 and current_position < 32) and (future_position >= 32 and future_position < 40)) or ((current_position >= 32 and current_position < 40) and (future_position >= 40 and future_position < 48)) or ((current_position >= 40 and current_position < 48) and (future_position >= 48 and future_position < 56)) or ((current_position >= 48 and current_position < 56) and (future_position >= 56 and future_position < 64))) or (((current_position >= 8 and current_position < 16) and (future_position >= 0 and future_position < 8)) or ((current_position >= 16 and current_position < 24) and (future_position >= 8 and future_position < 16)) or ((current_position >= 24 and current_position < 32) and (future_position >= 16 and future_position < 24)) or ((current_position >= 32 and current_position < 40) and (future_position >= 24 and future_position < 32)) or ((current_position >= 40 and current_position < 48) and (future_position >= 32 and future_position < 40)) or ((current_position >= 48 and current_position < 56) and (future_position >= 40 and future_position < 48)) or ((current_position >= 56 and current_position < 64) and (future_position >= 48 and future_position < 56))):
            return True
    elif weight == 50 or weight == -50:
        if ((current_position >= 0 and current_position < 8) and (future_position >= 0 and future_position < 8)) or ((current_position >= 8 and current_position < 16) and (future_position >= 8 and future_position < 16)) or ((current_position >= 16 and current_position < 24) and (future_position >= 16 and future_position < 24)) or ((current_position >= 24 and current_position < 32) and (future_position >= 24 and future_position < 32)) or ((current_position >= 32 and current_position < 40) and (future_position >= 32 and future_position < 40)) or ((current_position >= 40 and current_position < 48) and (future_position >= 40 and future_position < 48)) or ((current_position >= 48 and current_position < 56) and (future_position >= 48 and future_position < 56)) or ((current_position >= 56 and current_position < 64) and (future_position >= 56 and future_position < 64)) :
            return True
        else:
            return False
    if weight == 90 or weight == -90 or weight == 100 or weight == -100:
        if (current_position-future_position == 7 or current_position-future_position == -7 or current_position-future_position == 8 or current_position-future_position == -8 or current_position-future_position == 9 or current_position-future_position == -9) and ((((current_position >= 0 and current_position < 8) and (future_position >= 8 and future_position < 16)) or ((current_position >= 8 and current_position < 16) and (future_position >= 16 and future_position < 24)) or ((current_position >= 16 and current_position < 24) and (future_position >= 24 and future_position < 32)) or ((current_position >= 24 and current_position < 32) and (future_position >= 32 and future_position < 40)) or ((current_position >= 32 and current_position < 40) and (future_position >= 40 and future_position < 48)) or ((current_position >= 40 and current_position < 48) and (future_position >= 48 and future_position < 56)) or ((current_position >= 48 and current_position < 56) and (future_position >= 56 and future_position < 64))) or (((current_position >= 8 and current_position < 16) and (future_position >= 0 and future_position < 8)) or ((current_position >= 16 and current_position < 24) and (future_position >= 8 and future_position < 16)) or ((current_position >= 24 and current_position < 32) and (future_position >= 16 and future_position < 24)) or ((current_position >= 32 and current_position < 40) and (future_position >= 24 and future_position < 32)) or ((current_position >= 40 and current_position < 48) and (future_position >= 32 and future_position < 40)) or ((current_position >= 48 and current_position < 56) and (future_position >= 40 and future_position < 48)) or ((current_position >= 56 and current_position < 64) and (future_position >= 48 and future_position < 56)))):
            return True
        elif (current_position-future_position == 1 or current_position-future_position == -1) and (((current_position >= 0 and current_position < 8) and (future_position >= 0 and future_position < 8)) or ((current_position >= 8 and current_position < 16) and (future_position >= 8 and future_position < 16)) or ((current_position >= 16 and current_position < 24) and (future_position >= 16 and future_position < 24)) or ((current_position >= 24 and current_position < 32) and (future_position >= 24 and future_position < 32)) or ((current_position >= 32 and current_position < 40) and (future_position >= 32 and future_position < 40)) or ((current_position >= 40 and current_position < 48) and (future_position >= 40 and future_position < 48)) or ((current_position >= 48 and current_position < 56) and (future_position >= 48 and future_position < 56)) or ((current_position >= 56 and current_position < 64) and (future_position >= 56 and future_position < 64))) :
            return True
        else:
            return False

def moveable(current_position,weight):
    if one_end_opposite(current_position,-8,weight) and second_end_opposite(current_position,8,weight):
        return False
    elif one_end_opposite(current_position,-7,weight) and second_end_opposite(current_position,7,weight):
        return False
    elif one_end_opposite(current_position,-1,weight) and second_end_opposite(current_position,1,weight):
        return False
    elif one_end_opposite(current_position,-9,weight) and second_end_opposite(current_position,9,weight):
        return False
    elif one_end_opposite(current_position,8,weight) and second_end_opposite(current_position,-8,weight):
        return False
    elif one_end_opposite(current_position,7,weight) and second_end_opposite(current_position,-7,weight):      
        return False
    elif one_end_opposite(current_position,1,weight) and second_end_opposite(current_position,-1,weight):
        return False
    elif one_end_opposite(current_position,9,weight) and second_end_opposite(current_position,-9,weight):
        return False
    else:
        return True

def one_end_opposite(current_position,allignment,weight):
    if weight > 0:
        if weights[current_position+allignment] == 0 and checking(current_position+allignment,current_position+allignment+allignment,weight):
            if one_end_opposite(current_position+allignment,allignment,weight):
                return True
            else:
                return False
        elif weights[current_position+allignment] == 100:
            return True
    elif weight < 0:
        if weights[current_position+allignment] == 0 and checking(current_position+allignment,current_position+allignment+allignment,weight):
            if one_end_opposite(current_position+allignment,allignment,weight):
                return True
            else:
                return False
        elif weights[current_position+allignment] == -100:
            return True
        else:
            return False

def second_end_opposite(current_position,allignment,weight):
    if weight > 0:
        if weights[current_position+allignment] == 0 and checking(current_position+allignment,current_position+allignment+allignment,weight):
            if second_end_opposite(current_position+allignment,allignment,weight):
                return True
            else:
                return False
        elif weights[current_position+allignment] == -90:
            return True
        elif weights[current_position+allignment] == -50 and (allignment == 8 or allignment == -8 or allignment == 1 or allignment == -1):
            return True
        elif weights[current_position+allignment] == -40 and (allignment == 7 or allignment == -7 or allignment == 9 or allignment == -9):
            return True
    elif weight < 0:
        if weights[current_position+allignment] == 0 and checking(current_position+allignment,current_position+allignment+allignment,weight):
            if second_end_opposite(current_position+allignment,allignment,weight):
                return True
            else:
                return False
        elif weights[current_position+allignment] == 90:
            return True
        elif weights[current_position+allignment] == 50 and (allignment == 8 or allignment == -8 or allignment == 1 or allignment == -1):
            return True
        elif weights[current_position+allignment] == 40 and (allignment == 7 or allignment == -7 or allignment == 9 or allignment == -9):
            return True
        
ChessBoard()
