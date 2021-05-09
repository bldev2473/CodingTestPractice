def get_lis_list(seq):
  result = []
  
  try:
    for i in range(len(seq)):
      # 각각의 요소들을 시작점으로 LIS를 찾아서 넣는 2차원 리스트
      lis_list = []
      
      # 기준 원소
      pivot = seq[i]
      lis_list.append(pivot)
      print('pivot: ', pivot)
      
      for sub_i in range(i + 1, len(seq)):
      
        # 기준 원소 보다 크면 (증가하면)
        if pivot < seq[sub_i]:
          lis_list.append(seq[sub_i])
          # 기준 원소를 마지막 비교 원소로
          pivot = seq[sub_i]
          
      print('lis_list: ', lis_list)
      
      result.append(lis_list)
  except Exception as e:
    print(e)
  return result