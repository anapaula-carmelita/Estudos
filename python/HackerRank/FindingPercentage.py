if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    soma = 0
    for m in student_marks[query_name]:
        soma += m
    soma = soma/len(student_marks[query_name])
    print(f"{soma:.2f}")
