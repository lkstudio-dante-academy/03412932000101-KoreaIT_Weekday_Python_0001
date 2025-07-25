import os
import sys

import random
from Example.Example_20.Sorting import sortValues_ByBubble, sortValues_ByInsertion, sortValues_ByMerge

"""
정렬 (Sorting) 이란?
- 데이터를 특정 기준에 따라 순서를 재배치하는 것을 의미한다. (+ 즉, 정렬은 데이터의 탐색을 위해 데이터의 순서를
변경한다는 것을 알 수 있다.)

정렬 알고리즘은 크게 안정 정렬과 불안정 정렬로 구분된다.

안정 정렬 vs 불안정 정렬
- 안정 정렬은 정렬 기준 이외에 데이터의 순서가 변경되지 않는 반면 불안정 정렬은 정렬 기준 이외에 데이터가
순서가 변경 될 수 있다는 차이점이 존재한다. (+ 즉, 안정 정렬은 정렬 이전의 데이터 순서가 유지 된다는 것을
알 수 있다.)

안정 정렬 알고리즘 종류
- 버블 정렬 (Bubble Sort)
- 삽입 정렬 (Insertion Sort)
- 병합 정렬 (Merge Sort)
"""


# Example 20 (정렬 - 1)
def start(args):
	oListValues = [random.randrange(1, 100) for i in range(0, 10)]
	
	print("=====> 리스트 - 정렬 전 <=====")
	print(oListValues)
	
	# sortValues_ByBubble(oListValues)
	# sortValues_ByInsertion(oListValues)
	sortValues_ByMerge(oListValues)
	
	print("\n=====> 리스트 - 정렬 후 <=====")
	print(oListValues)
