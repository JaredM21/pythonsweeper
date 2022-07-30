from tkinter import Button, Label
import random
import settings
import ctypes
import sys

class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_obj = None
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_obj = None
        self.x = x
        self.y = y

        #append the object to the cell.all list
        Cell.all.append(self)

    def create_btn_obj(self, location):
        btn = Button( #Instantiation of button class
            location,
            width=12,
            height=4,
            #text=f'{self.x}, {self.y}' #Displays coordinate
        )
        btn.bind('<Button-1>', self.left_click)
        btn.bind('<Button-3>', self.right_click)
        self.cell_btn_obj = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells Left: {Cell.cell_count}",
            width=12,
            height=4,
            font=("", 40)
        )
        Cell.cell_count_label_obj = lbl


    
    def left_click(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj  in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You won!', 'Game Over', 0)


        self.cell_btn_obj.unbind('<Button-1>')
        self.cell_btn_obj.unbind('<Button-3>')

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell


    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells


    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter


    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_obj.configure(text=self.surrounded_cells_mines_length)
            #Replace text of cell count label with the new count
            if Cell.cell_count_label_obj:
                Cell.cell_count_label_obj.configure(text=f'Cells Left: {Cell.cell_count}')
            self.cell_btn_obj.configure(
                bg='SystemButtonFace'
            )


        #Mark Cell as opened
        self.is_opened = True


    def get_cell_by_axis(self, x , y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def show_mine(self):
        self.cell_btn_obj.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 0)
        sys.exit()
        

    def right_click(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_obj.configure(
                bg='orange'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_obj.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate = False


    @staticmethod
    def radomize_mines():
        my_list = ['']
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
            )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f'Cell({self.x}, {self.y})'