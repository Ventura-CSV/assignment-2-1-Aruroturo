def main():
   # Comlete your code here
   # Use m_perc=3 , f_perc, nb_perc for your results
    men_num = int(input("Enter The Number of Male Students: "))
    
    fem_num = int(input("Enter The Number of Female Students: "))
    
    nonb_num = int(input(" Enter The Number of Non-binary Students: "))
    
    total_peeps = men_num + fem_num + nonb_num
   
    m_perc = (men_num / total_peeps) * 100
    
    f_perc = (fem_num / total_peeps) * 100

    nb_perc = (nonb_num / total_peeps) * 100

    print(f"The total Number of Students: t\t{total_peeps}")

    print(f"The Number of Males, Femals and Non-binary: \t{men_num} \t{fem_num} \t{nonb_num}")

    print(f"The Percentage of Males, Females and Non-Binary \t {m_perc:.2f}% \t{f_perc:.2f}% \t{nb_perc:.2f}%")


if __name__ == '__main__':
    main()