import sys

params = sys.argv[1:]
num_params = len(params)

if (num_params) == 0:
    print("none")
else:
    print(f"parameters: {num_params}")

    for word in params:
        print(f"{word}: {len(word)}")
