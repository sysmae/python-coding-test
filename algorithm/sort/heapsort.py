def heapify(arr, n, i, log=False, step_count=None, indent=0):
    """
    힙 속성을 유지하기 위해 하위 트리를 재구성하는 함수
    
    arr: 정렬할 배열
    n: 배열의 크기
    i: 현재 노드 인덱스
    log: 로깅 활성화 여부
    step_count: 단계 카운터 (None이면 로깅하지 않음)
    indent: 재귀 호출 깊이를 표시하기 위한 들여쓰기 레벨
    """
    if step_count is not None:
        step_count[0] += 1
        current_step = step_count[0]
    else:
        current_step = None
    
    if log:
        indent_str = "  " * indent
        if current_step is not None:
            print(f"\n{indent_str}[단계 {current_step}] heapify 시작: 배열={arr[:n]}, 크기={n}, 현재 노드={i}")
        else:
            print(f"\n{indent_str}[로그] heapify 시작: 배열={arr[:n]}, 크기={n}, 현재 노드={i}")
    
    largest = i  # 현재 노드를 가장 큰 값으로 초기화
    left = 2 * i + 1  # 왼쪽 자식 노드 인덱스
    right = 2 * i + 2  # 오른쪽 자식 노드 인덱스
    
    # 왼쪽 자식이 루트보다 크면 largest 업데이트
    if left < n:
        if log:
            print(f"{indent_str}[로그] 왼쪽 자식 검사: arr[{left}]={arr[left]} vs arr[{largest}]={arr[largest]}")
        if arr[left] > arr[largest]:
            if log:
                print(f"{indent_str}[로그] 왼쪽 자식({arr[left]})이 현재 노드({arr[largest]})보다 큼")
            largest = left
    
    # 오른쪽 자식이 현재 largest보다 크면 largest 업데이트
    if right < n:
        if log:
            print(f"{indent_str}[로그] 오른쪽 자식 검사: arr[{right}]={arr[right]} vs arr[{largest}]={arr[largest]}")
        if arr[right] > arr[largest]:
            if log:
                print(f"{indent_str}[로그] 오른쪽 자식({arr[right]})이 현재 largest({arr[largest]})보다 큼")
            largest = right
    
    # largest가 현재 노드가 아니면 교환하고 재귀적으로 heapify 호출
    if largest != i:
        if log:
            print(f"{indent_str}[로그] 교환: arr[{i}]={arr[i]} <-> arr[{largest}]={arr[largest]}")
        arr[i], arr[largest] = arr[largest], arr[i]
        
        # 교환 후 배열 상태 출력
        if log:
            print(f"{indent_str}[로그] 교환 후 배열: {arr[:n]}")
            print_heap_structure(arr, n, indent_str)
            print(f"{indent_str}[로그] 재귀 호출: heapify(arr, {n}, {largest})")
        
        # 재귀적으로 영향받은 하위 트리에 대해 heapify 수행
        heapify(arr, n, largest, log, step_count, indent + 1)
    else:
        if log:
            print(f"{indent_str}[로그] 교환 필요 없음: 현재 노드가 이미 최대값")

def build_max_heap(arr, n, log=False, step_count=None):
    """
    배열을 최대 힙으로 구성하는 함수
    
    arr: 정렬할 배열
    n: 배열의 크기
    log: 로깅 활성화 여부
    step_count: 단계 카운터
    """
    if log:
        print("\n[로그] 최대 힙 구성 시작")
    
    # 마지막 비-리프 노드부터 루트까지 역순으로 heapify 수행
    for i in range(n // 2 - 1, -1, -1):
        if log:
            print(f"\n[로그] 최대 힙 구성 단계: i={i} (노드 값: {arr[i]})")
        heapify(arr, n, i, log, step_count)
    
    if log:
        print(f"\n[로그] 최대 힙 구성 완료: {arr[:n]}")
        print("\n최대 힙 구성 후 힙 구조:")
        print_heap_structure(arr, n)

def heap_sort(arr, log=False):
    """
    힙 정렬 함수
    
    arr: 정렬할 배열
    log: 로깅 활성화 여부
    """
    n = len(arr)
    step_count = [0] if log else None
    
    if log:
        print(f"[로그] 힙 정렬 시작: 초기 배열 = {arr}")
        print("\n초기 배열의 힙 구조:")
        print_heap_structure(arr, n)
    
    # 최대 힙 구성 (Build max heap)
    build_max_heap(arr, n, log, step_count)
    
    if log:
        print("\n[로그] 정렬 단계 시작")
    
    # 힙에서 요소를 하나씩 추출
    for i in range(n - 1, 0, -1):
        if log:
            print(f"\n[로그] 정렬 단계 {n-i}/{n-1}: 최대값 {arr[0]}을 마지막 위치({i})로 이동")
        
        # 루트(최대값)를 마지막 요소와 교환
        arr[i], arr[0] = arr[0], arr[i]
        
        if log:
            print(f"[로그] 교환 후 배열: {arr}")
            print(f"[로그] 힙 크기를 {i}로 줄이고 루트에서 heapify 수행")
            print_heap_structure(arr, i)  # 현재 힙 구조 출력 (크기 i)
        
        # 줄어든 힙에 대해 heapify 수행
        heapify(arr, i, 0, log, step_count)
    
    if log:
        print(f"\n[로그] 힙 정렬 완료: {arr}")
        print(f"[로그] 총 단계 수: {step_count[0]}")
    
    return arr

def print_heap_structure(arr, n, prefix=""):
    """
    힙 구조를 시각적으로 출력하는 함수
    
    arr: 배열
    n: 고려할 배열의 크기
    prefix: 출력 접두사
    """
    print(f"{prefix}힙 구조:")
    
    # 힙의 레벨 수 계산
    import math
    levels = math.ceil(math.log2(n + 1)) if n > 0 else 0
    
    # 각 레벨별로 노드 출력
    node_index = 0
    for level in range(levels):
        nodes_in_level = min(2**level, n - sum(2**i for i in range(level)))
        level_str = prefix
        
        # 들여쓰기 계산
        indent = 2**(levels - level - 1) - 1
        level_str += " " * indent
        
        # 현재 레벨의 노드 출력
        for _ in range(nodes_in_level):
            if node_index < n:
                # 노드 값 출력
                node_str = f"{arr[node_index]}"
                level_str += node_str
                
                # 노드 간 간격 계산
                if _ < nodes_in_level - 1:
                    space = 2**(levels - level) - 1
                    level_str += " " * space
                
                node_index += 1
        
        print(level_str)
    
    # 배열 형태로도 출력
    print(f"{prefix}배열 표현: {arr[:n]}")
    
    # 인덱스와 부모-자식 관계 출력
    print(f"{prefix}인덱스 관계:")
    for i in range(n):
        parent_idx = (i - 1) // 2 if i > 0 else None
        left_idx = 2 * i + 1 if 2 * i + 1 < n else None
        right_idx = 2 * i + 2 if 2 * i + 2 < n else None
        
        relation_str = f"{prefix}노드 {i}(값:{arr[i]}): "
        if parent_idx is not None:
            relation_str += f"부모={parent_idx}(값:{arr[parent_idx]}), "
        else:
            relation_str += "부모=없음, "
        
        if left_idx is not None:
            relation_str += f"왼쪽 자식={left_idx}(값:{arr[left_idx]}), "
        else:
            relation_str += "왼쪽 자식=없음, "
        
        if right_idx is not None:
            relation_str += f"오른쪽 자식={right_idx}(값:{arr[right_idx]})"
        else:
            relation_str += "오른쪽 자식=없음"
        
        print(relation_str)

# 테스트 함수
def test_heap_sort_with_detailed_logging():
    # 테스트 배열
    # 4 2 8 7 3 3 5 1 9
    test_arr = [4, 2, 8, 7, 3, 3, 5, 1, 9]
    print(f"정렬 전 배열: {test_arr}")
    
    # 로깅을 활성화하여 힙 정렬 수행
    heap_sort(test_arr, log=True)
    
    print(f"\n정렬 후 배열: {test_arr}")

# 테스트 실행
test_heap_sort_with_detailed_logging()
