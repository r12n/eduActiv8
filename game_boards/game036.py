# -*- coding: utf-8 -*-

import random
import pygame

import classes.board
import classes.extras as ex
import classes.game_driver as gd
import classes.level_controller as lc


class Board(gd.BoardGame):
    def __init__(self, mainloop, speaker, config, screen_w, screen_h):
        self.lvlc = mainloop.xml_conn.get_level_count(mainloop.m.game_dbid, mainloop.config.user_age_group)
        self.level = lc.Level(self, mainloop, self.lvlc[0], self.lvlc[1])
        gd.BoardGame.__init__(self, mainloop, speaker, config, screen_w, screen_h, 11, 6)

    def create_game_objects(self, level=1):
        self.board.draw_grid = False
        self.allow_unit_animations = False
        self.allow_teleport = False
        self.vis_buttons = [1, 1, 1, 1, 1, 0, 1, 1, 1]
        self.mainloop.info.hide_buttonsa(self.vis_buttons)
        s = 100
        v = 255
        h = random.randrange(0, 255, 5)
        color0 = ex.hsv_to_rgb(h, 40, 230)
        font_color = ex.hsv_to_rgb(h, 255, 140)

        data = [11, 5]
        data.extend(
            self.mainloop.xml_conn.get_level_data(self.mainloop.m.game_dbid, self.mainloop.config.user_age_group,
                                                  self.level.lvl))
        self.chapters = self.mainloop.xml_conn.get_chapters(self.mainloop.m.game_dbid,
                                                            self.mainloop.config.user_age_group)
        self.data = data
        self.layout.update_layout(data[0], data[1])
        self.board.level_start(data[0], data[1], self.layout.scale)
        signs = ["+", " ", "-"]
        self.ship_id = -1
        self.total = 0

        # get random numbers until sum of all numbers is over 1 (does not prevent negative numbers in mid calculation)
        self.num_list = []
        self.sign_list = []
        expr = []

        t = 0
        while len(self.num_list) < data[4]:
            nbr = random.randint(1, data[3])
            if len(self.num_list) > 0:
                sgn = random.randint(0, 1)
                if sgn == 0:
                    temp = t + nbr
                else:
                    temp = t - nbr
            else:
                temp = nbr
            if 0 < temp < data[5]:
                t = temp
                if data[4] > len(self.num_list) > 0:  # data[4]:
                    self.sign_list.append(signs[sgn*2])
                    expr.append(str(signs[sgn*2]))
                self.num_list.append(nbr)
                expr.append(str(nbr))

        self.eval_string = ''.join(expr)
        self.eval_string = self.eval_string.strip()
        self.total = eval(self.eval_string )

        color = ((255, 255, 255))

        # create table to store 'binary' solution
        self.solution_grid = [0 for x in range(data[0])]
        self.expression = [" " for x in range(data[0])]

        # find position of first door square
        xd = (data[0] - data[2]) // 2

        # add objects to the board
        h = random.randrange(0, 255, 5)
        number_color = ex.hsv_to_rgb(h, s, v)  # highlight 1

        for i in range(0, data[4]):
            x2 = xd + i * 2 - 1
            caption = str(self.num_list[i])
            self.board.add_unit(x2, 2, 1, 1, classes.board.Label, caption, number_color, "", data[6])
            self.board.units[i].font_color = ex.hsv_to_rgb(h, 255, 140)
            self.solution_grid[x2] = 1
            self.expression[x2] = str(self.num_list[i])
            if i < data[4] - 1:
                self.solution_grid[x2 + 1] = 1
                self.expression[x2 + 1] = self.sign_list[i]

        self.board.add_unit(x2 + 1, 2, 1, 1, classes.board.Label, "=", number_color, "", data[6])
        self.board.units[-1].font_color = ex.hsv_to_rgb(h, 255, 140)
        self.board.add_unit(x2 + 2, 2, 1, 1, classes.board.Label, str(self.total), number_color, "", data[6])
        self.board.units[-1].font_color = ex.hsv_to_rgb(h, 255, 140)
        # signs = ["<","=",">"]*(data[4]-1)

        if h > 125:
            h = random.randrange(0, h - 25, 5)
        else:
            h = random.randrange(h + 25, 255, 5)
        number_color = ex.hsv_to_rgb(h, s, v)  # highlight 1

        indu = len(self.board.units)
        inds = len(self.board.ships)
        self.door_indexes = []
        for i in range(0, data[4] - 1):
            self.board.add_unit(xd + i * 2 + 1 - 1, 1, 1, 3, classes.board.Letter, signs, number_color, "", data[6])
            self.board.ships[i].font_color = ex.hsv_to_rgb(h, 255, 140)
            self.board.add_door(xd + i * 2 + 1 - 1, 2, 1, 1, classes.board.Door, "", color, "")
            self.board.units[indu + i].door_outline = True

            self.board.units[indu + i].checkable = True
            self.board.units[indu + i].init_check_images()
            self.door_indexes.append(indu + i)
            self.board.ships[inds + i].readable = False
            self.board.all_sprites_list.move_to_front(self.board.units[indu + i])
        """
        instruction = self.d["Drag the slider"]
        self.board.add_unit(0, 5, 11, 1, classes.board.Letter, instruction, color0, "", 7)
        self.board.ships[-1].immobilize()
        self.board.ships[-1].font_color = font_color

        self.board.ships[-1].speaker_val = self.dp["Drag the slider"]
        self.board.ships[-1].speaker_val_update = False
        """
        self.changed_since_check = True  # to make it possible to confirm if numbers are equal
        self.outline_all(0, 1)

    def show_info_dialog(self):
        self.mainloop.dialog.show_dialog(3, self.d["Drag the slider"])

    def auto_check_reset(self):
        for each in self.board.units:
            if each.is_door:
                each.update_me = True
                each.set_display_check(None)

    def handle(self, event):
        gd.BoardGame.handle(self, event)  # send event handling up

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.auto_check_reset()

    def update(self, game):
        game.fill((255, 255, 255))
        gd.BoardGame.update(self, game)  # rest of painting done by parent

    def check_result(self):
        all_true = True
        for i in range(len(self.board.ships)):
            # calculate the active value based on grid_y of the slider
            if self.board.ships[i].grid_y != 1:
                value = self.board.ships[i].value[2 - self.board.ships[i].grid_y]
                self.expression[self.board.ships[i].grid_x] = value
                if value == self.sign_list[i]:
                    self.board.units[self.door_indexes[i]].set_display_check(True)
                else:
                    self.board.units[self.door_indexes[i]].set_display_check(False)
            else:
                self.board.units[self.door_indexes[i]].set_display_check(False)
                all_true = False

        if all_true:
            eval_string = ''.join(self.expression)
            eval_string.strip()
            if eval(eval_string) == self.total:
                #in case there's more than one solution
                for i in range(len(self.board.ships) - 1):
                    self.board.units[self.door_indexes[i]].set_display_check(True)
                self.level.next_board()

        self.mainloop.redraw_needed[0] = True

