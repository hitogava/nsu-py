a = [1,2,3]
b = ["a", "b"]
result = [(a[i],b[i]) for i in range(min(len(a),len(b)))]
