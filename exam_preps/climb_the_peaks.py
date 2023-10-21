from collections import deque

daily_portions = deque([int(el) for el in input().split(', ')])
daily_staminas = deque([int(el) for el in input().split(', ')])

peaks_list = [('Vihren', 80),
              ('Kutelo', 90),
              ('Banski Suhodol', 100),
              ('Polezhan', 60),
              ('Kamenitza', 70)]

climbed_peaks = []

for day in range(1, 8):
    current_portion = daily_portions.pop()
    current_stamina = daily_staminas.popleft()
    current_energy = current_portion + current_stamina

    if current_energy >= peaks_list[0][1]:
        climbed_peaks.append(peaks_list[0][0])
        peaks_list.pop(0)

    if len(peaks_list) == 0:
        break

if len(peaks_list) == 0:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")

else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if climbed_peaks:
    print("Conquered peaks:")
    for peak in climbed_peaks:
        print(peak)

