votes = {
    'tammy': '57124',
    'bafu': '12873',
    'kengyu': '21643',
    'khfeng': '1234',
    'penk': '21863',
    'phoebe': '68241',
    'joseph': '21864',
    'gerald': '21846'
}

ops = [votes[p] for p in votes]
nvotes = len(max(ops, key=len))

results = {}
for p in votes:
    v = votes[p]
    for i in range(0, len(v)):
        o = v[i]
        if o not in results:
            results[o] = 0
        results[o] += (nvotes - i)

sorted_results = sorted(results.items(), key=lambda o: o[1], reverse=True)

print('DT42 Voting Results')
print('-------------------')
for r in sorted_results:
    print('Option %s won %i points' % (r[0], r[1]))
