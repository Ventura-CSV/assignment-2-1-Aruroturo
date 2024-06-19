def main():
   # Comlete your code here
   # Use m_perc , f_perc, nb_perc for your results
   #input number of males
    men_num = int(input("Enter The Number of Male Students: "))
    # input number of females
    fem_num = int(input("Enter The Number of Female Students: "))
    #input number of non binary
    nonb_num = int(input(" Enter The Number of Non-binary Students: "))
    #Computer caculates the total number of all students
    total_peeps = men_num + fem_num + nonb_num
   # This is the percentage caculation of the males
    m_perc = (men_num / total_peeps) * 100
    # This is the percentage calculation of the females
    f_perc = (fem_num / total_peeps) * 100
# this is the percentage caculation of the non binary
    nb_perc = (nonb_num / total_peeps) * 100
# This entire section is the output of our information
    print(f"The total Number of Students: t\t{total_peeps}")
    print(f"The Number of Males, Femals and Non-binary: \t{men_num} \t{fem_num} \t{nonb_num}")
    print(f"The Percentage of Males, Females and Non-Binary \t {m_perc:.2f}% \t{f_perc:.2f}% \t{nb_perc:.2f}%")


if __name__ == '__main__':
    main()