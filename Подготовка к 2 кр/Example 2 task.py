def late(*args, hyper=3):
    ans = {}
    for elem in args:
        count = len(elem) // hyper
        if len(elem) % hyper != 0:
            count += 1
        if count not in ans:
            ans[count] = []
        ans[count].append(elem)
    sorted_ans = {k: sorted(ans[k]) for k in sorted(ans)}
    return sorted_ans

if __name__ == '__main__':
    lines = [
        'People', 'starships',
        'fight', 'trade',
        'farthest', 'reaches', 'Galaxy'
    ]
    print(late(*lines, hyper=4))
    lines = ['However', 'usually', 'took', 'thousands', 'years', 'least', 'nearest', 'anywhere']
    print(late(*lines, hyper=4))


# предполагаемый вывод:
# {2: ['Galaxy', 'People', 'farthest', 'fight', 'reaches', 'trade'], 3: ['starships']}
# {1: ['took'], 2: ['However', 'anywhere', 'least', 'nearest', 'usually', 'years'], 3: ['thousands']}