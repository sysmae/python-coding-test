class CountingSortWithLogs:
    def __init__(self):
        self.step_count = 0
    
    def counting_sort(self, arr, log=True, return_indices=False):
        """
        계수 정렬을 수행하는 메인 함수
        
        Args:
            arr: 정렬할 배열
            log: 로그 출력 여부
            return_indices: True면 (값, 원래 인덱스) 쌍 반환
        
        Returns:
            정렬된 배열 또는 (값, 인덱스) 쌍 배열
        """
        if log:
            print("=" * 60)
            print("계수 정렬(Counting Sort) 시작")
            print("=" * 60)
            print(f"입력 배열: {arr}")
            print(f"배열 크기: {len(arr)}")
        
        if not arr:
            if log:
                print("빈 배열입니다. 정렬 종료.")
            return arr
        
        # 최댓값 찾기
        max_val = max(arr)
        min_val = min(arr)
        range_val = max_val - min_val + 1
        
        if log:
            print(f"최솟값: {min_val}")
            print(f"최댓값: {max_val}")
            print(f"값의 범위: {range_val}")
            print()
        
        # 1단계: 각 값의 개수 세기
        count_array = self.count_elements(arr, min_val, range_val, log)
        
        # 2단계: 누적합 계산
        cumulative_count = self.calculate_cumulative_sum(count_array, log)
        # (값, 인덱스) 쌍 정렬 지원
        if return_indices:
            indexed_arr = [(v, i) for i, v in enumerate(arr)]
            sorted_array = self.build_sorted_array_with_indices(indexed_arr, cumulative_count, min_val, log)
        else:
            sorted_array = self.build_sorted_array(arr, cumulative_count, min_val, log)
        
        if log:
            print(f"\n최종 정렬 결과: {sorted_array}")
            print("계수 정렬 완료!")
            print("=" * 60)
        
        return sorted_array
    
    def count_elements(self, arr, min_val, range_val, log=True):
        """
        1단계: 각 원소의 개수를 계산
        """
        self.step_count += 1
        if log:
            print(f"[1단계] 각 원소의 개수 계산")
            print("-" * 30)
        
        count = [0] * range_val
        
        if log:
            print(f"카운트 배열 초기화: {count}")
            print("각 원소의 개수 계산 중...")
        
        for i, num in enumerate(arr):
            count_index = num - min_val
            count[count_index] += 1
            
            if log:
                print(f"  단계 {i+1}: 원소 {num} 발견")
                print(f"    카운트 배열 인덱스: {count_index}")
                print(f"    count[{count_index}] = {count[count_index]}")
                print(f"    현재 카운트 배열: {count}")
        
        if log:
            print(f"\n1단계 완료 - 최종 카운트 배열: {count}")
            self.print_count_summary(count, min_val)
            print()
        
        return count
    
    def calculate_cumulative_sum(self, count, log=True):
        """
        2단계: 누적합 계산
        """
        self.step_count += 1
        if log:
            print(f"[2단계] 누적합 계산")
            print("-" * 30)
            print("누적합은 각 값이 정렬된 배열에서 들어갈 수 있는 최대 위치를 나타냅니다.")
            print(f"누적합 계산 전: {count}")
        
        cumulative = count[:]
        
        for i in range(1, len(cumulative)):
            old_value = cumulative[i]
            cumulative[i] += cumulative[i-1]
            
            if log:
                print(f"  누적합[{i}] = 누적합[{i-1}] + 원래값[{i}]")
                print(f"             = {cumulative[i-1]} + {old_value} = {cumulative[i]}")
        
        if log:
            print(f"\n2단계 완료 - 최종 누적합 배열: {cumulative}")
            print("누적합의 의미:")
            for i, val in enumerate(cumulative):
                if count[i] > 0:  # 실제 존재하는 값만 출력
                    print(f"  값 {i}: 최대 {val}번째 위치까지 배치 가능")
            print()
        
        return cumulative
    
    def build_sorted_array(self, arr, cumulative_count, min_val, log=True):
        """
        3단계: 정렬된 배열 생성 (값만)
        """
        self.step_count += 1
        if log:
            print(f"[3단계] 정렬된 배열 생성")
            print("-" * 30)
            print("원본 배열을 뒤에서부터 순회하여 안정 정렬을 보장합니다.")
        
        result = [0] * len(arr)
        working_cumulative = cumulative_count[:]
        
        if log:
            print(f"결과 배열 초기화: {result}")
            print(f"작업용 누적합 배열: {working_cumulative}")
            print()
        
        # 뒤에서부터 순회 (안정 정렬을 위해)
        for i in range(len(arr) - 1, -1, -1):
            element = arr[i]
            count_index = element - min_val
            position = working_cumulative[count_index] - 1
            
            if log:
                print(f"  원소 처리: arr[{i}] = {element}")
                print(f"    카운트 배열 인덱스: {count_index}")
                print(f"    현재 누적합 값: {working_cumulative[count_index]}")
                print(f"    배치 위치: {position} (인덱스는 0부터 시작)")
            
            result[position] = element
            working_cumulative[count_index] -= 1
            
            if log:
                print(f"    result[{position}] = {element}")
                print(f"    누적합[{count_index}] 감소: {working_cumulative[count_index]}")
                print(f"    현재 결과 배열: {result}")
                print()
        
        if log:
            print(f"3단계 완료 - 정렬된 배열: {result}")
        
        return result

    def build_sorted_array_with_indices(self, arr_with_indices, cumulative_count, min_val, log=True):
        """
        3단계: 정렬된 배열 생성 (값, 인덱스 쌍)
        """
        self.step_count += 1
        if log:
            print(f"[3단계] (값, 인덱스) 쌍 정렬된 배열 생성")
            print("-" * 30)
            print("원본 배열을 뒤에서부터 순회하여 안정 정렬을 보장합니다.")
        
        result = [None] * len(arr_with_indices)
        working_cumulative = cumulative_count[:]
        
        if log:
            print(f"결과 배열 초기화: {result}")
            print(f"작업용 누적합 배열: {working_cumulative}")
            print()
        
        for i in range(len(arr_with_indices) - 1, -1, -1):
            value, orig_idx = arr_with_indices[i]
            count_index = value - min_val
            position = working_cumulative[count_index] - 1
            
            if log:
                print(f"  원소 처리: arr[{i}] = ({value},{orig_idx})")
                print(f"    카운트 배열 인덱스: {count_index}")
                print(f"    현재 누적합 값: {working_cumulative[count_index]}")
                print(f"    배치 위치: {position} (인덱스는 0부터 시작)")
            
            result[position] = (value, orig_idx)
            working_cumulative[count_index] -= 1
            
            if log:
                print(f"    result[{position}] = ({value},{orig_idx})")
                print(f"    누적합[{count_index}] 감소: {working_cumulative[count_index]}")
                print(f"    현재 결과 배열: {result}")
                print()
        
        if log:
            print(f"3단계 완료 - (값, 인덱스) 쌍 정렬된 배열: {result}")
        
        return result

    def print_count_summary(self, count, min_val):
        """
        카운트 배열의 요약 정보 출력
        """
        print("각 값별 개수:")
        for i, cnt in enumerate(count):
            if cnt > 0:
                actual_value = i + min_val
                print(f"  값 {actual_value}: {cnt}개")
    
    def demonstrate_step_by_step(self, test_arrays):
        """
        여러 테스트 케이스로 단계별 시연
        """
        print("계수 정렬 단계별 시연")
        print("=" * 80)
        
        for i, arr in enumerate(test_arrays, 1):
            print(f"\n테스트 케이스 {i}: {arr}")
            self.step_count = 0
            sorted_result = self.counting_sort(arr.copy(), log=True)
            
            print(f"정렬 전: {arr}")
            print(f"정렬 후: {sorted_result}")
            print(f"총 단계 수: {self.step_count}")
            
            if i < len(test_arrays):
                print("\n" + "="*80)

# 계수 정렬 성능 분석 클래스
class CountingSortAnalyzer:
    def __init__(self):
        pass
    
    def analyze_complexity(self, test_cases):
        """
        다양한 케이스의 시간/공간 복잡도 분석
        """
        print("계수 정렬 복잡도 분석")
        print("=" * 50)
        print("케이스\t배열크기(n)\t값범위(k)\t시간복잡도\t공간복잡도")
        print("-" * 70)
        
        for i, (arr, description) in enumerate(test_cases, 1):
            n = len(arr)
            k = max(arr) - min(arr) + 1 if arr else 0
            time_complexity = f"O({n} + {k})"
            space_complexity = f"O({k})"
            
            print(f"{description}\t{n}\t\t{k}\t\t{time_complexity}\t{space_complexity}")
        
        print()
        print("분석 결과:")
        print("- n이 k보다 훨씬 클 때: 시간복잡도 ≈ O(n), 매우 효율적")
        print("- k가 n보다 훨씬 클 때: 시간복잡도 ≈ O(k), 비효율적")
        print("- 최적 사용 조건: k ≤ n 또는 k가 작은 상수")
    
    def compare_with_other_sorts(self):
        """
        다른 정렬 알고리즘과의 비교
        """
        print("\n정렬 알고리즘 비교")
        print("=" * 50)
        
        algorithms = [
            ("계수 정렬", "O(n+k)", "O(k)", "안정", "정수, 제한된 범위"),
            ("병합 정렬", "O(n log n)", "O(n)", "안정", "범용"),
            ("힙 정렬", "O(n log n)", "O(1)", "불안정", "범용"),
            ("퀵 정렬", "평균 O(n log n)", "O(log n)", "불안정", "범용"),
            ("기수 정렬", "O(d(n+k))", "O(n+k)", "안정", "고정 길이 키")
        ]
        
        print("알고리즘\t\t시간복잡도\t\t공간복잡도\t안정성\t적용 조건")
        print("-" * 80)
        
        for name, time, space, stable, condition in algorithms:
            print(f"{name}\t\t{time}\t\t{space}\t\t{stable}\t{condition}")

# 실제 사용 예시 및 테스트
def main():
    """
    계수 정렬 학습용 메인 함수
    """
    # 계수 정렬 객체 생성
    counting_sort = CountingSortWithLogs()
    analyzer = CountingSortAnalyzer()
    
    # 테스트 케이스들
    test_arrays = [
        [4, 2, 2, 8, 3, 3, 1],           # 기본 케이스
        [3, 1, 4, 1, 5, 9, 2, 6, 5],    # 더 긴 배열
        [5, 5, 5, 5],                    # 동일한 값들
        [1, 2, 3, 4, 5],                 # 이미 정렬됨
        [5, 4, 3, 2, 1],                 # 역순
        [0, 10, 5, 2, 8]                 # 0을 포함한 경우
    ]
    
    # 단계별 시연
    counting_sort.demonstrate_step_by_step(test_arrays[:3])
    
    # 복잡도 분석
    complexity_test_cases = [
        ([4, 2, 2, 8, 3, 3, 1], "작은배열"),
        ([1, 2, 3, 4, 5] * 100, "큰배열,작은범위"),
        ([i for i in range(1000)], "큰배열,큰범위"),
        ([1, 1000], "작은배열,큰범위")
    ]
    
    print("\n")
    analyzer.analyze_complexity(complexity_test_cases)
    analyzer.compare_with_other_sorts()
    
    # 간단한 사용 예시
    print("\n간단한 사용 예시:")
    print("=" * 30)
    simple_array = [3, 1, 4, 1, 5]
    print(f"정렬 전: {simple_array}")
    sorted_array = counting_sort.counting_sort(simple_array, log=False)
    print(f"정렬 후: {sorted_array}")

# 계수 정렬의 안정성 시연
def demonstrate_stability():
    """
    계수 정렬의 안정성(Stable Sort) 시연
    """
    print("\n계수 정렬의 안정성 시연")
    print("=" * 40)
    
    # 안정성을 확인하기 위한 특별한 데이터 구조
    class NumberWithIndex:
        def __init__(self, value, original_index):
            self.value = value
            self.original_index = original_index
        
        def __repr__(self):
            return f"({self.value},{self.original_index})"
    
    # 동일한 값을 가진 원소들
    original_data = [
        NumberWithIndex(3, 0),
        NumberWithIndex(1, 1), 
        NumberWithIndex(3, 2),
        NumberWithIndex(2, 3),
        NumberWithIndex(1, 4)
    ]
    
    print("원본 데이터 (값, 원래_인덱스):")
    print(original_data)
    
    # 값만 추출하여 계수 정렬 수행 (값, 인덱스) 쌍으로 정렬
    values = [item.value for item in original_data]
    counting_sort = CountingSortWithLogs()
    sorted_pairs = counting_sort.counting_sort(values, log=False, return_indices=True)
    
    print(f"\n정렬된 (값, 인덱스) 쌍: {sorted_pairs}")
    print("\n정렬 후 원본 데이터 순서:")
    print([original_data[pair[1]] for pair in sorted_pairs])
    print("\n안정 정렬의 특징:")
    print("- 동일한 값을 가진 원소들의 상대적 순서가 보존됨")
    print("- 값이 3인 원소들: (3,0)이 (3,2)보다 앞에 위치해야 함")
    print("- 값이 1인 원소들: (1,1)이 (1,4)보다 앞에 위치해야 함")

if __name__ == "__main__":
    main()
    demonstrate_stability()
