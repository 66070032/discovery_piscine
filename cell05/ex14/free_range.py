import sys

if len(sys.argv) == 3:
    start_num = int(sys.argv[1])
    end_num = int(sys.argv[2])

    num_array = list(range(start_num, end_num + 1))
    print(num_array)
else:
    print("none")
