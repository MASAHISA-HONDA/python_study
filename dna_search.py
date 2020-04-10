from enum import IntEnum
from typing import Tuple,List
import time

Nucleotide: IntEnum = IntEnum('Nucleotide',('A','C','G','T'))

Codon = Tuple[Nucleotide,Nucleotide,Nucleotide]
Gene = List[Codon]

gene_str = "ACGGGTAGTCAGGCGATCGATCGACATCATCGACGATCGATCGATCGTCGATGCCTGATCGACGTA"

def string_to_gene(s :str) -> Gene:
    gene: Gene = []
    for i in range(0,len(s),3):
        if (i+2) >= len(s):
            return gene

        codon :Codon = (Nucleotide[s[i]],Nucleotide[s[i+1]],Nucleotide[s[i+2]])
        gene.append(codon)

    return gene

my_gene :Gene = string_to_gene(gene_str)


##線形探索
def liner_contains(gene: Gene, key_codon:Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    return False

#二分探索
def binary_contains(gene:Gene, key_codon:Codon) -> bool:
    low :int = 0
    high :int = len(gene)-1

    while low<=high:
        mid :int = (low+high)//2

        #検索値が中央より後ろの場合
        if gene[mid] < key_codon:
            low = mid+1
        #検索値が中央より前の場合
        elif gene[mid] > key_codon:
            high = mid-1
        #検索値が中央にある場合
        else:
            return True
        
    return False
        

acg :Codon = (Nucleotide.A,Nucleotide.C,Nucleotide.G)
gat :Codon = (Nucleotide.G,Nucleotide.A,Nucleotide.T)

start = time.time()
print(liner_contains(my_gene,acg))
print(liner_contains(my_gene,gat))
end = time.time()
print(round((end-start)*1000,5)) #[ms]

start = time.time()
my_sorted_gene :Gene = sorted(my_gene)
print(binary_contains(my_sorted_gene,acg))
print(binary_contains(my_sorted_gene,gat))
end = time.time()
print(round((end-start)*1000,5)) #[ms]