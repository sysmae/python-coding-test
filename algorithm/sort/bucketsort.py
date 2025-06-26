class BucketSortWithLogs:
    def __init__(self):
        self.step_count = 0
    
    def bucket_sort(self, arr, log=True):
        """
        버킷 정렬을 수행하는 메인 함수
        
        Args:
            arr: 정렬할 배열
            log: 로그 출력 여부
        
        Returns:
            정렬된 배열
        """
        if log:
            print("=" * 60)
            print("버킷 정렬(Bucket Sort) 시작")
            print("=" * 60)
            print(f"입력 배열: {arr}")
            print(f"배열 크기: {len(arr)}")
        
        if not arr or len(arr) <= 1:
            if log:
                print("배열이 비어있거나 원소가 1개입니다. 정렬 종료.")
            return arr
        
        # 최댓값과 최솟값 찾기
        min_val = min(arr)
        max_val = max(arr)
        
        if log:
            print(f"최솟값: {min_val}")
            print(f"최댓값: {max_val}")
            print(f"값의 범위: {max_val - min_val}")
            print()
        
        # 1단계: 버킷 생성
        buckets = self.create_buckets(arr, min_val, max_val, log)
        
        # 2단계: 원소 분배
        self.distribute_elements(arr, buckets, min_val, max_val, log)
        
        # 3단계: 각 버킷 정렬
        self.sort_buckets(buckets, log)
        
        # 4단계: 버킷 병합
        sorted_array = self.merge_buckets(buckets, log)
        
        if log:
            print(f"\n최종 정렬 결과: {sorted_array}")
            print("버킷 정렬 완료!")
            print("=" * 60)
        
        return sorted_array
    
    def create_buckets(self, arr, min_val, max_val, log=True):
        """
        1단계: 버킷 생성
        """
        self.step_count += 1
        if log:
            print(f"[1단계] 버킷 생성")
            print("-" * 30)
        
        n = len(arr)
        buckets = [[] for _ in range(n)]
        
        if log:
            print(f"버킷 개수: {n}개 (배열 크기와 동일)")
            print(f"각 버킷의 범위 계산:")
            
            if max_val != min_val:
                bucket_range = (max_val - min_val) / n
                print(f"버킷 범위 = (최댓값 - 최솟값) / 버킷개수")
                print(f"         = ({max_val} - {min_val}) / {n}")
                print(f"         = {bucket_range:.2f}")
            else:
                print("모든 값이 동일하므로 버킷 하나만 사용")
            
            print(f"생성된 빈 버킷들: {buckets}")
            print()
        
        return buckets
    
    def distribute_elements(self, arr, buckets, min_val, max_val, log=True):
        """
        2단계: 원소 분배
        """
        self.step_count += 1
        if log:
            print(f"[2단계] 원소 분배")
            print("-" * 30)
            print("각 원소를 해당하는 버킷에 배치합니다.")
        
        n = len(arr)
        
        for i, num in enumerate(arr):
            if max_val == min_val:
                bucket_index = 0
            else:
                # 버킷 인덱스 계산: (원소값 - 최솟값) / 버킷범위
                bucket_range = (max_val - min_val) / n
                bucket_index = int((num - min_val) / bucket_range)
                # 최댓값이 마지막 버킷을 초과하지 않도록 조정
                if bucket_index == n:
                    bucket_index = n - 1
            
            buckets[bucket_index].append(num)
            
            if log:
                print(f"  원소 {i+1}: {num}")
                print(f"    버킷 인덱스 계산: ({num} - {min_val}) / {(max_val - min_val) / n:.2f} = {bucket_index}")
                print(f"    버킷[{bucket_index}]에 {num} 추가")
                print(f"    현재 버킷[{bucket_index}]: {buckets[bucket_index]}")
        
        if log:
            print(f"\n2단계 완료 - 모든 원소 분배 결과:")
            for i, bucket in enumerate(buckets):
                if bucket:  # 비어있지 않은 버킷만 출력
                    print(f"  버킷[{i}]: {bucket}")
            print()
    
    def sort_buckets(self, buckets, log=True):
        """
        3단계: 각 버킷 정렬
        """
        self.step_count += 1
        if log:
            print(f"[3단계] 각 버킷 정렬")
            print("-" * 30)
            print("각 버킷의 원소들을 개별적으로 정렬합니다.")
        
        for i, bucket in enumerate(buckets):
            if len(bucket) > 1:
                if log:
                    print(f"\n  버킷[{i}] 정렬:")
                    print(f"    정렬 전: {bucket}")
                
                # 삽입 정렬 사용 (작은 배열에 효율적)
                bucket.sort()
                
                if log:
                    print(f"    정렬 후: {bucket}")
            elif len(bucket) == 1:
                if log:
                    print(f"\n  버킷[{i}]: {bucket} (원소 1개, 정렬 불필요)")
        
        if log:
            print(f"\n3단계 완료 - 모든 버킷 정렬 결과:")
            for i, bucket in enumerate(buckets):
                if bucket:
                    print(f"  버킷[{i}]: {bucket}")
            print()
    
    def merge_buckets(self, buckets, log=True):
        """
        4단계: 버킷 병합
        """
        self.step_count += 1
        if log:
            print(f"[4단계] 버킷 병합")
            print("-" * 30)
            print("정렬된 버킷들을 순서대로 합칩니다.")
        
        sorted_array = []
        
        for i, bucket in enumerate(buckets):
            if bucket:
                if log:
                    print(f"  버킷[{i}] {bucket}를 결과에 추가")
                sorted_array.extend(bucket)
                if log:
                    print(f"    현재 결과: {sorted_array}")
        
        if log:
            print(f"\n4단계 완료 - 최종 정렬된 배열: {sorted_array}")
        
        return sorted_array
    
    def demonstrate_step_by_step(self, test_arrays):
        """
        여러 테스트 케이스로 단계별 시연
        """
        print("버킷 정렬 단계별 시연")
        print("=" * 80)
        
        for i, arr in enumerate(test_arrays, 1):
            print(f"\n테스트 케이스 {i}: {arr}")
            self.step_count = 0
            sorted_result = self.bucket_sort(arr.copy(), log=True)
            
            print(f"정렬 전: {arr}")
            print(f"정렬 후: {sorted_result}")
            print(f"총 단계 수: {self.step_count}")
            
            if i < len(test_arrays):
                print("\n" + "="*80)

# 버킷 정렬 성능 분석 클래스
class BucketSortAnalyzer:
    def __init__(self):
        pass
    
    def analyze_complexity(self):
        """
        버킷 정렬의 시간 복잡도 분석
        """
        print("버킷 정렬 시간 복잡도 분석")
        print("=" * 50)
        
        print("각 단계별 시간 복잡도:")
        steps = [
            ("1단계: 버킷 생성", "O(n)"),
            ("2단계: 원소 분배", "O(n)"),
            ("3단계: 각 버킷 정렬", "O(k × (n/k)²) = O(n²/k)"),
            ("4단계: 버킷 병합", "O(n)")
        ]
        
        for step, complexity in steps:
            print(f"  {step}: {complexity}")
        
        print()
        print("전체 시간 복잡도:")
        print("- 최선의 경우 (균등 분포): O(n)")
        print("- 평균의 경우: O(n + k)")
        print("- 최악의 경우 (모든 원소가 한 버킷): O(n²)")
        print()
        print("공간 복잡도: O(n + k)")
    
    def compare_with_other_sorts(self):
        """
        다른 정렬 알고리즘과의 비교
        """
        print("\n정렬 알고리즘 비교")
        print("=" * 60)
        
        algorithms = [
            ("버킷 정렬", "평균 O(n)", "O(n+k)", "안정", "균등분포 가정"),
            ("계수 정렬", "O(n+k)", "O(k)", "안정", "정수, 제한된 범위"),
            ("기수 정렬", "O(d(n+k))", "O(n+k)", "안정", "고정 길이 키"),
            ("병합 정렬", "O(n log n)", "O(n)", "안정", "범용"),
            ("퀵 정렬", "평균 O(n log n)", "O(log n)", "불안정", "범용")
        ]
        
        print("알고리즘\t시간복잡도\t\t공간복잡도\t안정성\t적용 조건")
        print("-" * 80)
        
        for name, time, space, stable, condition in algorithms:
            print(f"{name}\t{time}\t\t{space}\t\t{stable}\t{condition}")

# 실제 사용 예시 및 테스트
def main():
    """
    버킷 정렬 학습용 메인 함수
    """
    # 버킷 정렬 객체 생성
    bucket_sort = BucketSortWithLogs()
    analyzer = BucketSortAnalyzer()
    
    # 테스트 케이스들
    test_arrays = [
        [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434],  # 소수 (균등분포)
        [29, 25, 3, 49, 9, 37, 21, 43],                 # 정수
        [5, 2, 8, 1, 9, 3],                             # 작은 정수
        [0.1, 0.5, 0.3, 0.7, 0.2, 0.8, 0.4, 0.6]      # 균등분포 소수
    ]
    
    # 단계별 시연
    bucket_sort.demonstrate_step_by_step(test_arrays[:2])
    
    # 복잡도 분석
    print("\n")
    analyzer.analyze_complexity()
    analyzer.compare_with_other_sorts()
    
    # 간단한 사용 예시
    print("\n간단한 사용 예시:")
    print("=" * 30)
    simple_array = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
    print(f"정렬 전: {simple_array}")
    sorted_array = bucket_sort.bucket_sort(simple_array, log=False)
    print(f"정렬 후: {sorted_array}")

# 버킷 정렬의 적용 조건 시연
def demonstrate_distribution_effect():
    """
    데이터 분포가 버킷 정렬 성능에 미치는 영향 시연
    """
    print("\n데이터 분포와 버킷 정렬 성능")
    print("=" * 40)
    
    bucket_sort = BucketSortWithLogs()
    
    print("1. 균등 분포 (이상적):")
    uniform_data = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    bucket_sort.bucket_sort(uniform_data, log=False)
    
    print("\n2. 편향 분포 (비효율적):")
    skewed_data = [0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17]
    bucket_sort.bucket_sort(skewed_data, log=False)
    
    print("\n분석:")
    print("- 균등 분포: 각 버킷에 비슷한 수의 원소가 들어가 효율적")
    print("- 편향 분포: 특정 버킷에 원소가 몰려 비효율적")

if __name__ == "__main__":
    main()
    demonstrate_distribution_effect()
