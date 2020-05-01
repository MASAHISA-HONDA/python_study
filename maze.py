from enum import Enum
from typing import List,NamedTuple,Callable,Optional
import random
from math import sqrt
##from generic_search import dfs,bfs,node_to_pathastar,Node

class Cell(str,Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"

class MazeLocation(NamedTuple):
    row:int
    column:int

class Maze:
    #10×10の迷路を作成
    #sparsenessで障害物の散布度を調整
    def __init__(self,rows:int=10,columns:int=10,sparseness:float=0.1,\
        start=MazeLocation(0,0),goal=MazeLocation(9,9)) -> None:
            #基本的なインスタンス変数初期化
            self.rows:int = rows
            self._columns:int = columns
            self.start:MazeLocation = start
            self.goal:MazeLocation = goal
            #空のセルを設定
            self._grid:List[List[Cell]] = \
            [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
            #障害物設定
            self._randomly_fill(rows,columns,sparseness)
            #スタートとゴール
            self._grid[start.row][start.column] = Cell.START
            self._grid[goal.row][goal.column] = Cell.GOAL
        
    def _randomly_fill(self,rows:int,columns:int,sparseness:float):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0,1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED#ランダムにBLOCKEDを配置

    #整地
    def __str__(self) -> str:
        output:str = ""
        for row in self._grid:
            output += "".join([c.value for c in row]) + "\n"#文字列を連結
        return output

    #ゴールチェック
    #GOALしたらTrueを返す
    def goal_test(self,ml:MazeLocation) -> bool:
        return ml == self.goal

    #移動関数
    def successors(self,ml:MazeLocation) ->List[MazeLocation]:
        locations = List[MazeLocation] = []


maze:Maze = Maze()
print(maze)

