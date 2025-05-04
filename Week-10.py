# SOAL NO 1
def compare(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()
    maxlen = max(len(lines1), len(lines2))
    hasil = []
    total_beda = 0
    for i in range(maxlen):
        line1 = lines1[i].strip() if i < len(lines1) else ""
        line2 = lines2[i].strip() if i < len(lines2) else ""

        if line1 != line2:
            total_beda += 1
            print(f"Beda pada baris ke-{i+1}:")
            print(f"  file1: {line1}")
            print(f"  file2: {line2}")

    print(f"Total beda ada : {total_beda} baris")
compare("file1.txt", "file2.txt")


# SOAL NO 2
with open("soal.txt", "r") as file :
    print("Nama file : soal.txt")
    for line in file :
        soal, jawaban = line.strip().split("|")
        print(soal.strip())
        jawaban_input = input("Jawaban Kamu : ").strip()
        if jawaban_input.lower() == jawaban.strip().lower() :
            print("Jawaban benar!\n")
        else:
            print("Jawaban salah!\n")
