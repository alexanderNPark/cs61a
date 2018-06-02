def self_apply(f):
    return f(f)

d = self_apply(lambda x:5)
print(d)