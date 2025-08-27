import sys
input = sys.stdin.readline

dataset = set()
for line in sys.stdin.readlines()[1:]:
    if line.split()[1] == "enter":
        dataset.add(line.split()[0])
    else: dataset.remove(line.split()[0])

result = sorted(dataset, reverse=True)
print("\n".join(result))