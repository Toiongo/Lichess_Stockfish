from stockfish import Stockfish
from selenium import webdriver
import pgn_to_fen
import re
import os

driver = webdriver.Chrome()
clear = lambda: os.system('cls')
pgnConverter = pgn_to_fen.PgnToFen()
moves = []

def getElementByClassName(class_name):
    try:
        el = driver.find_element_by_class_name(class_name)
        return el
    except:
        return None

stockfish = Stockfish("C:\\Stockfish\\stockfish.exe",
 parameters = 
 {
    "Write Debug Log": "false",
    "Contempt": 0,
    "Min Split Depth": 0,
    "Threads": 1,
    "Ponder": "false",
    "Hash": 512,
    "MultiPV": 1,
    "Skill Level": 20,
    "Move Overhead": 0,
    "Slow Mover": 0,
    "UCI_Chess960": "false",
    #"SyzygyPath": "C:\\Stockfish\\syzygy",
}, depth=6)

driver.get("https://www.lichess.org")

def convert_and_print():
    pgnConverter.resetBoard()
    pgnConverter.pgnToFen(moves)
    stockfish.set_fen_position(pgnConverter.getFullFen())
    clear()
    print(stockfish.get_board_visual())
    print(stockfish.get_evaluation())
    print(stockfish.get_best_move())
    print(pgnConverter.getFullFen())

while True:
    if (getElementByClassName("a1t") is None):
        continue
    elif len(moves) < len(driver.find_elements_by_tag_name("u8t")):
        moves.append(getElementByClassName("a1t").text)
        convert_and_print()
    elif (len(moves) > len(driver.find_elements_by_tag_name("u8t"))) and len(driver.find_elements_by_tag_name("u8t")) == 1:
        pgnConverter.resetBoard()
        moves = [getElementByClassName("a1t").text]
        convert_and_print() 
    elif len(moves) > len(driver.find_elements_by_tag_name("u8t")):
        del moves[-1]
        convert_and_print()
