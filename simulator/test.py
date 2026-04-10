import sys
def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    max_len = max(len(lines1), len(lines2))

    for i in range(max_len):
        line1 = lines1[i].strip() if i < len(lines1) else "<NO LINE>"
        line2 = lines2[i].strip() if i < len(lines2) else "<NO LINE>"

        if line1 != line2:
            print(f"❌ Mismatch at line {i+1}")
            print(f"Your Output : {line1}")
            print(f"Expected    : {line2}")
            return

    print("✅ Files match perfectly!")

data_file = sys.argv[1]
out_file = sys.argv[2]
compare_files(data_file,out_file)
