import pygame

running = True


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]

        # значения по умолчанию
        self.left = 0
        self.top = 0
        self.cell_size = 20
        self.board_width = len(self.board[0]) * self.cell_size
        self.board_height = len(self.board) * self.cell_size

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, sc):
        cell_left = self.left
        cell_top = self.top
        for i in self.board:
            for j in i:
                pygame.draw.rect(sc, pygame.Color('white'), (cell_left, cell_top, self.cell_size, self.cell_size),
                                 1)
                if j:
                    pygame.draw.rect(sc, pygame.Color('green'), (cell_left + 1, cell_top + 1, self.cell_size - 2, self.cell_size - 2))
                cell_left += self.cell_size
            cell_top += self.cell_size
            cell_left = self.left

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        cube_board_x = self.board_width // self.width
        # print(self.board_width, self.board_height)
        cube_board_y = self.board_height // self.height
        # print(cube_board_x, cube_board_y)
        if self.left <= mouse_pos[0] <= self.left + self.board_width \
                and self.top <= mouse_pos[1] <= self.top + self.board_height:
            mouse_in_cube_x = (mouse_pos[0] // cube_board_x)
            mouse_in_cube_y = (mouse_pos[-1] // cube_board_y)
            # print(mouse_in_cube_x, mouse_in_cube_y)
            return mouse_in_cube_y, mouse_in_cube_x
        else:
            return None

    def on_click(self, cell):
        if cell is not None:
            self.board[cell[0]][cell[-1]] = 1


class Life(Board):
    def next_move(self):
        # count = 0
        for i in range(len(self.board)):
            for j in range(i):
                # print(self.board[i][j])
                if self.board[i][j]:
                    # # print(1)
                    # if self.board[i-1][j] or self.board[i][j-1] or self.board[i+1][j] or self.board[i][j+1]:
                    #     # if self.board[i][j + 1] or self.board[i][j-1]
                    #     print(self.board[i][j])

# a.next_move()

if __name__ == '__main__':
    pygame.init()
    size = (500, 500)
    screen = pygame.display.set_mode(size)
    # board = Board(25, 25)
    life = Life(25, 25)
    # life.next_move()
    pygame.display.flip()
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                life.get_click(event.pos)
        life.render(screen)
        life.next_move()
        pygame.display.flip()
    pygame.quit()
