import time
txt = "The quick brown fox jumps over the lazy dog."
input("Press Enter to start...")
start = time.time()
typed = input(f"\nType this:\n{txt}\n\n")
end = time.time()
wpm = (len(txt.split()) / (end - start)) * 60
accuracy = sum(typed[i] == txt[i] for i in range(min(len(typed), len(txt)))) / len(txt) * 100
print(f"\nSpeed: {wpm:.2f} WPM | Accuracy: {accuracy:.2f}%")
