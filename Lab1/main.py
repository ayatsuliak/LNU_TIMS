import matplotlib.pyplot as plt
#x = [2, 1, 4, 5, 2, 5, 3, 4, 6, 6, 5] #to do with random(50) and from console
x = []
lenght = int(input("Введіть довжину масиву значень: "))
print("Введіть ваші значення: ")
for i in range(lenght):
    x.append(int(input()))
print("Введіть який саме розподіл: ")
print(" 1 - звичайний\n", "2 - інтервальний")
num = input()
if num == '1':
    variation = sorted(x) #to do without func
    x_max = 0
    for i in x:
        if i > x_max:
            x_max = i

    x_min = x_max
    for i in x:
        if i < x_min:
            x_min = i

    for i in x:
        for j in x:
            if i < j:
                temp = i
                i = j
                j = temp
    # print(x)
    variation_without_repetition = []
    for i in variation:
        if i in variation_without_repetition:
            continue
        else:
            variation_without_repetition.append(i)

    variation_counts = []
    for i in variation_without_repetition:
        first = i
        count = 0
        for j in variation:
            if j == first:
                count += 1
        variation_counts.append(count)

    n_max = 0
    for i in variation_counts:
        if i > n_max:
            n_max = i

    n_min = n_max
    for i in variation_counts:
        if i < n_min:
            n_min = i

    print("xi: | ", end="")
    for i in variation_without_repetition:
        print(f"{i} | ", end="")

    print("\nni: | ", end="")
    for i in variation_counts:
        print(f"{i} | ", end="")

    sum = 0
    for i in variation_counts:
        sum += i

    variational_relative_frequencies = []
    print("\nwi: | ", end="")
    for i in variation_counts:
        variational_relative_frequencies.append((i/sum))
        print(f"{i/sum} | ", end="")

    #to empire func and draw
    print("\n 1 - полігон і діаграма частот \n", "2 - полігон і діаграма відносних частот\n", "exit - вихід")

    str = input("Enter which graphic: ")
    while(str != 'exit'):
        if str == '1':
            fig, ax = plt.subplots(2)
            ax[0].set_title("Полігон частот")
            ax[0].set_xlim(0, x_max + 1)
            ax[0].set_ylim(0, n_max + 1)
            ax[0].set_xlabel("xi")
            ax[0].set_ylabel("ni")
            ax[0].plot(variation_without_repetition, variation_counts, color="red", marker="o")

            ax[1].set_title("Діаграма частот")
            ax[1].set_xlabel("xi")
            ax[1].set_ylabel("ni")
            ax[1].set_xlim(0, x_max + 1)
            ax[1].set_ylim(0, n_max + 1)
            ax[1].bar(variation_without_repetition, variation_counts, edgecolor="black", width=0.001)
            fig.tight_layout()
            plt.show()
        elif str == '2':
            fig, ax = plt.subplots(2)
            ax[0].set_title("Полігон відносних частот")
            ax[0].set_xlim(0, x_max + 1)
            ax[0].set_ylim(0, 1.000)
            ax[0].set_xlabel("xi")
            ax[0].set_ylabel("wi")
            ax[0].plot(variation_without_repetition, variational_relative_frequencies, color="blue", marker="o")

            ax[1].set_title("Діаграма відносних частот")
            ax[1].set_xlabel("xi")
            ax[1].set_ylabel("wi")
            ax[1].set_xlim(0, x_max + 1)
            ax[1].set_ylim(0, 1.000)
            ax[1].bar(variation_without_repetition, variational_relative_frequencies, edgecolor="green", width=0.001)
            fig.tight_layout()
            plt.show()
        str = input("Enter which graphic: ")






# fig, ax = plt.subplots(2, 2)
# ax[0, 0].set_title("Полігон частот")
# ax[0, 0].set_xlim(0, x_max + 1)
# ax[0, 0].set_ylim(0, n_max + 1)
# ax[0, 0].set_xlabel("xi")
# ax[0, 0].set_ylabel("ni")
# ax[0, 0].plot(variation_without_repetition, variation_counts, color="red", marker="o")
#
# ax[0, 1].set_title("Діаграма частот")
# ax[0, 1].set_xlabel("xi")
# ax[0, 1].set_ylabel("ni")
# ax[0, 1].set_xlim(0, x_max + 1)
# ax[0, 1].set_ylim(0, n_max + 1)
# ax[0, 1].bar(variation_without_repetition, variation_counts, edgecolor="black", width=0.001)
#
# ax[1, 0].set_title("Полігон відносних частот")
# ax[1, 0].set_xlim(0, x_max + 1)
# ax[1, 0].set_ylim(0, 1.000)
# ax[1, 0].set_xlabel("xi")
# ax[1, 0].set_ylabel("wi")
# ax[1, 0].plot(variation_without_repetition, variational_relative_frequencies, color="blue", marker="o")
#
# ax[1, 1].set_title("Діаграма відносних частот")
# ax[1, 1].set_xlabel("xi")
# ax[1, 1].set_ylabel("wi")
# ax[1, 1].set_xlim(0, x_max + 1)
# ax[1, 1].set_ylim(0, 1.000)
# ax[1, 1].bar(variation_without_repetition, variational_relative_frequencies, edgecolor="green", width=0.001)
# fig.tight_layout()



#plt.show()