import math

import numpy as np
import random
import time

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
weight = np.array([
    [0,10, 3, 7, 7, 3,10, 0],
    [10,3, 2, 5, 5, 2, 3,10],
    [3, 2, 6, 6, 6, 6, 2, 3],
    [7, 5, 6, 4, 4, 6, 5, 7],
    [7, 5, 6, 4, 4, 6, 5, 7],
    [3, 2, 6, 6, 6, 6, 2, 3],
    [10,3, 2, 5, 5, 2, 3,10],
    [0,10, 3, 7, 7, 3, 10,0],
])


# don't change the class name


def finalsearch(chessboard, color, chessboard_size):
    idx = np.where(chessboard == COLOR_NONE)
    idx = list(zip(idx[0], idx[1]))
    for i in range(len(idx)):
        if chessboard[idx[i][0]][idx[i][1]] == COLOR_NONE:
            num = 1
            while idx[i][0] - num >= 0 and chessboard[idx[i][0] - num][idx[i][1]] == -color:
                num = num + 1
            if idx[i][0] - num >= 0 and chessboard[idx[i][0] - num][idx[i][1]] == color:
                for j in range(1, num):
                    chessboard[idx[i][0] - j][idx[i][1]] = color
            num = 1
            while idx[i][0] + num < chessboard_size and chessboard[idx[i][0] + num][idx[i][1]] == -color:
                num = num + 1
            if idx[i][0] + num < chessboard_size and chessboard[idx[i][0] + num][idx[i][1]] == color:
                for j in range(1, num):
                    chessboard[idx[i][0] + j][idx[i][1]] = color
            num = 1
            while idx[i][1] - num >= 0 and chessboard[idx[i][0]][idx[i][1] - num] == -color:
                num = num + 1
            if idx[i][1] - num >= 0 and chessboard[idx[i][0]][idx[i][1] - num] == color:
                for j in range(1, num):
                    chessboard[idx[i][0]][idx[i][1] - j] = color
            num = 1
            while idx[i][1] + num < chessboard_size and chessboard[idx[i][0]][idx[i][1] + num] == -color:
                num = num + 1
            if idx[i][1] + num < chessboard_size and chessboard[idx[i][0]][idx[i][1] + num] == color:
                for j in range(1, num):
                    chessboard[idx[i][0]][idx[i][1] + num] = color
            num = 1
            while idx[i][0] - num >= 0 and idx[i][1] + num < chessboard_size and chessboard[idx[i][0] - num][
                idx[i][1] + num] == -color:
                num = num + 1
            if idx[i][0] - num >= 0 and idx[i][1] + num < chessboard_size and chessboard[idx[i][0] - num][
                idx[i][1] + num] == color:
                for j in range(1, num):
                    chessboard[idx[i][0] - num][idx[i][1] + num] = color
            num = 1
            while idx[i][0] - num >= 0 and idx[i][1] - num >= 0 and chessboard[idx[i][0] - num][
                idx[i][1] - num] == -color:
                num = num + 1
            if idx[i][0] - num >= 0 and idx[i][1] - num >= 0 and chessboard[idx[i][0] - num][idx[i][1] - num] == color:
                for j in range(1, num):
                    chessboard[idx[i][0] - num][idx[i][1] - num] = color
            num = 1
            while idx[i][0] + num < chessboard_size and idx[i][1] + num < chessboard_size and \
                    chessboard[idx[i][0] + num][idx[i][1] + num] == -color:
                num = num + 1
            if idx[i][0] + num < chessboard_size and idx[i][1] + num < chessboard_size and \
                    chessboard[idx[i][0] + num][idx[i][1] + num] == color:
                for j in range(1, num):
                    chessboard[idx[i][0] + num][idx[i][1] + num] = color
            num = 1
            while idx[i][0] + num < chessboard_size and idx[i][1] - num >= 0 and chessboard[idx[i][0] + num][
                idx[i][1] - num] == -color:
                num = num + 1
            if idx[i][0] + num < chessboard_size and idx[i][1] - num >= 0 and chessboard[idx[i][0] + num][
                idx[i][1] - num] == color:
                for j in range(1, num):
                    chessboard[idx[i][0] + num][idx[i][1] - num] = color
    idxx = np.where(chessboard == color)
    idxx = list(zip(idxx[0], idxx[1]))
    idxy = np.where(chessboard == -color)
    idxy = list(zip(idxy[0], idxy[1]))
    if len(idxx) > len(idxy):
        return math.inf
    elif len(idxx) == len(idxy):
        return 0
    else:
        return -math.inf


def search(chessboard, level, pos, change, color, chessboard_size, start, timeout, alpha, beta):
    if time.time() - timeout > timeout - 0.2:
        return 0
    chessboard[pos[0]][pos[1]] = color
    ptr = 0
    while change > 0:
        if change & 1 == 1:
            num = 1
            if ptr == 0:
                while chessboard[pos[0] + num][pos[1] - num] == -color:
                    chessboard[pos[0] + num][pos[1] - num] = color
                    num = num + 1
            elif ptr == 1:
                while chessboard[pos[0] + num][pos[1] + num] == -color:
                    chessboard[pos[0] + num][pos[1] + num] = color
                    num = num + 1
            elif ptr == 2:
                while chessboard[pos[0] - num][pos[1] - num] == -color:
                    chessboard[pos[0] - num][pos[1] - num] = color
                    num = num + 1
            elif ptr == 3:
                while chessboard[pos[0] - num][pos[1] + num] == -color:
                    chessboard[pos[0] - num][pos[1] + num] = color
                    num = num + 1
            elif ptr == 4:
                while chessboard[pos[0]][pos[1] + num] == -color:
                    chessboard[pos[0]][pos[1] + num] = color
                    num = num + 1
            elif ptr == 5:
                while chessboard[pos[0]][pos[1] - num] == -color:
                    chessboard[pos[0]][pos[1] - num] = color
                    num = num + 1
            elif ptr == 6:
                while chessboard[pos[0] + num][pos[1]] == -color:
                    chessboard[pos[0] + num][pos[1]] = color
                    num = num + 1
            else:
                while chessboard[pos[0] - num][pos[1]] == -color:
                    chessboard[pos[0] - num][pos[1]] = color
                    num = num + 1
        ptr = ptr + 1
        change = change >> 1
    # return 0
    color = -color
    candidate_list = []
    wei = []
    changelist = []
    idx = np.where(chessboard == COLOR_NONE)
    idx = list(zip(idx[0], idx[1]))
    if len(idx) == 0:
        win = list(zip(np.where(chessboard == color)[0], np.where(chessboard == color)[1]))
        if win < chessboard_size * chessboard_size / 2:
            value = -math.inf
        elif win == chessboard_size * chessboard_size / 2:
            value = 0
        else:
            value = math.inf
        if level % 2 == 1:
            value = -value
        return value
    for i in range(len(idx)):
        change = 0
        totnum = 0
        num = 1
        while idx[i][0] - num >= 0 and chessboard[idx[i][0] - num][idx[i][1]] == -color:
            num = num + 1
        if idx[i][0] - num >= 0 and chessboard[idx[i][0] - num][idx[i][1]] == color:
            totnum += num - 1
            if num != 1:
                change += 1
        change *= 2
        num = 1
        while idx[i][0] + num < chessboard_size and chessboard[idx[i][0] + num][idx[i][1]] == -color:
            num = num + 1
        if idx[i][0] + num < chessboard_size and chessboard[idx[i][0] + num][idx[i][1]] == color:
            totnum += num - 1
            if num != 1:
                change += 1
        change *= 2
        num = 1
        while idx[i][1] - num >= 0 and chessboard[idx[i][0]][idx[i][1] - num] == -color:
            num = num + 1
        if idx[i][1] - num >= 0 and chessboard[idx[i][0]][idx[i][1] - num] == color:
            totnum += num - 1
            if num != 1:
                change += 1
        change *= 2
        num = 1
        while idx[i][1] + num < chessboard_size and chessboard[idx[i][0]][idx[i][1] + num] == -color:
            num = num + 1
        if idx[i][1] + num < chessboard_size and chessboard[idx[i][0]][idx[i][1] + num] == color:
            totnum += num - 1
            if num != 1:
                change += 1
        change *= 2
        num = 1
        while idx[i][0] - num >= 0 and idx[i][1] + num < chessboard_size and chessboard[idx[i][0] - num][
            idx[i][1] + num] == -color:
            num = num + 1
        if idx[i][0] - num >= 0 and idx[i][1] + num < chessboard_size and chessboard[idx[i][0] - num][
            idx[i][1] + num] == color:
            totnum += num - 1
            if num != 1:
                change += 1
        change *= 2
        num = 1
        while idx[i][0] - num >= 0 and idx[i][1] - num >= 0 and chessboard[idx[i][0] - num][
            idx[i][1] - num] == -color:
            num = num + 1
        if idx[i][0] - num >= 0 and idx[i][1] - num >= 0 and chessboard[idx[i][0] - num][idx[i][1] - num] == color:
            totnum += num - 1
            if num != 1:
                change += 1
        change *= 2
        num = 1
        while idx[i][0] + num < chessboard_size and idx[i][1] + num < chessboard_size and \
                chessboard[idx[i][0] + num][idx[i][1] + num] == -color:
            num = num + 1
        if idx[i][0] + num < chessboard_size and idx[i][1] + num < chessboard_size and \
                chessboard[idx[i][0] + num][idx[i][1] + num] == color:
            totnum += num - 1
            if num != 1:
                change += 1
        change *= 2
        num = 1
        while idx[i][0] + num < chessboard_size and idx[i][1] - num >= 0 and chessboard[idx[i][0] + num][
            idx[i][1] - num] == -color:
            num = num + 1
        if idx[i][0] + num < chessboard_size and idx[i][1] - num >= 0 and chessboard[idx[i][0] + num][
            idx[i][1] - num] == color:
            totnum += num - 1
            if num != 1:
                change += 1
        if totnum > 0:
            candidate_list.append(idx[i])
            if len(idx) > 40:
                wei.append(weight[idx[i][0]][idx[i][1]] - 0.5 * totnum)
            else:
                wei.append(weight[idx[i][0]][idx[i][1]] - totnum)
            changelist.append(change)
    if len(wei) == 0:
        idxx = np.where(chessboard == color)
        idxx = list(zip(idxx[0], idxx[1]))
        if level % 2 == 1:
            value = -8
        else:
            value = 8
        value += search(chessboard, level + 1, idxx[0], 0, color, chessboard_size, start, timeout, alpha, beta)
        return value
    else:
        if level % 2 == 1:
            value = math.inf
        else:
            value = -math.inf
        for i in range(len(wei)):
            if (level < 3 and len(idx) > 20) or len(idx) <= 20:
                num = search(chessboard, level + 1, candidate_list[i], changelist[i], color, chessboard_size, start,
                             timeout, alpha, beta)
            else:
                num = 0
            if level % 2 == 0:
                if wei[i] + num > value:
                    value = wei[i] + num
                if value >= beta:
                    return value
                alpha = max(alpha, value)
            if level % 2 == 1:
                if -wei[i] + num < value:
                    value = -wei[i] + num
                if value <= alpha:
                    return value
                beta = min(beta, value)
        return value


class AI(object):
    # chessboard_size, color, time_out passed from agent
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        # You are white or black
        self.color = color
        # the max time you should use, your algorithm's run time must not exceed the time limit.
        self.time_out = time_out
        # You need to add your decision to your candidate_list. The system will get the end of your candidate_list as your decision.
        self.candidate_list = []

    # The input is the current chessboard. Chessboard is a numpy array.

    def go(self, chessboard):
        # Clear candidate_list, must do this step
        self.candidate_list.clear()
        wei = []
        changelist = []
        # ==================================================================
        # Write your algorithm here
        # Here is the simplest sample:Random decision
        idx = np.where(chessboard == COLOR_NONE)
        idx = list(zip(idx[0], idx[1]))
        maxvalue = -math.inf
        maxpos = -1
        alpha = -math.inf
        beta = math.inf
        for i in range(len(idx)):
            change = 0
            totnum = 0
            num = 1
            while idx[i][0] - num >= 0 and chessboard[idx[i][0] - num][idx[i][1]] == -self.color:
                num = num + 1
            if idx[i][0] - num >= 0 and chessboard[idx[i][0] - num][idx[i][1]] == self.color:
                totnum += num - 1
                if num != 1:
                    change += 1
            change *= 2
            num = 1
            while idx[i][0] + num < self.chessboard_size and chessboard[idx[i][0] + num][idx[i][1]] == -self.color:
                num = num + 1
            if idx[i][0] + num < self.chessboard_size and chessboard[idx[i][0] + num][idx[i][1]] == self.color:
                totnum += num - 1
                if num != 1:
                    change += 1
            change *= 2
            num = 1
            while idx[i][1] - num >= 0 and chessboard[idx[i][0]][idx[i][1] - num] == -self.color:
                num = num + 1
            if idx[i][1] - num >= 0 and chessboard[idx[i][0]][idx[i][1] - num] == self.color:
                totnum += num - 1
                if num != 1:
                    change += 1
            change *= 2
            num = 1
            while idx[i][1] + num < self.chessboard_size and chessboard[idx[i][0]][idx[i][1] + num] == -self.color:
                num = num + 1
            if idx[i][1] + num < self.chessboard_size and chessboard[idx[i][0]][idx[i][1] + num] == self.color:
                totnum += num - 1
                if num != 1:
                    change += 1
            change *= 2
            num = 1
            while idx[i][0] - num >= 0 and idx[i][1] + num < self.chessboard_size and chessboard[idx[i][0] - num][
                idx[i][1] + num] == -self.color:
                num = num + 1
            if idx[i][0] - num >= 0 and idx[i][1] + num < self.chessboard_size and chessboard[idx[i][0] - num][
                idx[i][1] + num] == self.color:
                totnum += num - 1
                if num != 1:
                    change += 1
            change *= 2
            num = 1
            while idx[i][0] - num >= 0 and idx[i][1] - num >= 0 and chessboard[idx[i][0] - num][
                idx[i][1] - num] == -self.color:
                num = num + 1
            if idx[i][0] - num >= 0 and idx[i][1] - num >= 0 and chessboard[idx[i][0] - num][
                idx[i][1] - num] == self.color:
                totnum += num - 1
                if num != 1:
                    change += 1
            change *= 2
            num = 1
            while idx[i][0] + num < self.chessboard_size and idx[i][1] + num < self.chessboard_size and \
                    chessboard[idx[i][0] + num][idx[i][1] + num] == -self.color:
                num = num + 1
            if idx[i][0] + num < self.chessboard_size and idx[i][1] + num < self.chessboard_size and \
                    chessboard[idx[i][0] + num][idx[i][1] + num] == self.color:
                totnum += num - 1
                if num != 1:
                    change += 1
            change *= 2
            num = 1
            while idx[i][0] + num < self.chessboard_size and idx[i][1] - num >= 0 and chessboard[idx[i][0] + num][
                idx[i][1] - num] == -self.color:
                num = num + 1
            if idx[i][0] + num < self.chessboard_size and idx[i][1] - num >= 0 and chessboard[idx[i][0] + num][
                idx[i][1] - num] == self.color:
                totnum += num - 1
                if num != 1:
                    change += 1
            if totnum > 0:
                self.candidate_list.append(idx[i])
                if len(idx) > 40:
                    wei.append(weight[idx[i][0]][idx[i][1]] - 0.5 * totnum)
                else:
                    wei.append(weight[idx[i][0]][idx[i][1]] - totnum)
                changelist.append(change)

        for i in range(len(wei)):
            num = search(chessboard, 1, self.candidate_list[i], changelist[i], self.color, self.chessboard_size,
                         time.time(), self.time_out, alpha, beta)
            if wei[i] + num > maxvalue:
                maxpos = i
                maxvalue = wei[i] + num
            if maxvalue >= beta:
                break
            alpha = max(alpha, maxvalue)
        if maxpos != -1:
            self.candidate_list.append(self.candidate_list[maxpos])

# ==============Find new pos========================================
# Make sure that the position of your decision on the chess board is empty.
# If not, the system will return error.
# Add your decision into candidate_list, Records the chessboard
# You need to add all the positions which are valid
# candidate_list example: [(3,3),(4,4)]
# You need append your decision at the end of the candidate_list,
# candidate_list example: [(3,3),(4,4),(4,4)]
# we will pick the last element of the candidate_list as the position you choose.
# In above example, we will pick (4,4) as your decision.
# If there is no valid position, you must return an empty list.
