def solution(sequence):
    answer = 0
    
    m_sequence = [num if i%2==0 else -num for i,num in enumerate(sequence)]
    p_sequence = [num if i%2==1 else -num for i,num in enumerate(sequence)]
    
    for i in range(len(sequence)-1) :
        m_sequence[i+1] = max(m_sequence[i]+m_sequence[i+1], m_sequence[i+1])
        p_sequence[i+1] = max(p_sequence[i]+p_sequence[i+1], p_sequence[i+1])

    return max(max(m_sequence), max(p_sequence))