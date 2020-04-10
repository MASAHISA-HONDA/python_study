from __future__ import annotations
from typing import TypeVar,Iterable,Sequence,Generic,List,\
    Callable,Set,Deque,Dict,Any,Optional
from typing_extensions import Protocol
from heapq import heappush,heappop

T = TypeVar('T')

def liner_contains(iterable:Iterable[T], key:T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False

C = TypeVar('C',bound="Comparable")
class Comparable(Protocol):
    #def __eq__(self,other:Any) -> bool:

    #def __lt__(self:C, other:C) -> bool:

    def __gt__(self:C, other:C) -> bool:
        return (not self < other) and self != other 

    def __le__(self:C , other:C) -> bool:
        return self < other or self == other

    def __ge__(self:C , other:C) -> bool:
        return not self < other


def binary_contains(sequence:Sequence[C], key:C):
    low:int = 0
    high:int = len(sequence)-1

    while low <= high:
        mid:int = (low+high) // 2
        
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid -1
        else:
            return True

    return False

if __name__ == "__main__":
    print(liner_contains([1,2,5,3,4,2,3,5,6,7],5))
    print(binary_contains([1,2,5,3,4,2,3,5,6,7],9))
    print(binary_contains(["a","d","e","f","z"],"f"))
    print(binary_contains(["a","d","e","f","z"],"k"))
    print(binary_contains(["apple","bag","cat","document"],"cat"))
