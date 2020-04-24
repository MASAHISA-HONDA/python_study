from enum import Enum
from typing import List,NamedTuple,Callable,Optional
import random
from math import sqrt
##from generic_search import dfs,bfs,node_to_pathastar,Node

class Cell(str,Enum):
    EMPYT = " "
    BLOKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"

class MazeLocation(NamedTuple):
    row:int
    column:int

class Maze:
    def __init__(self,rows:int=10,columns:int=10,sparseness:float=0.2,\
    start:MazeLocation=MazeLocation(0,0),goal:MazeLocation=MazeLocation(9,9)) -> None:
        #基本的なインスタンス変数初期化
        self.rows:int = rows
        self._columns:int = columns
