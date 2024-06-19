def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc=3 , f_perc, nb_perc for your results
    ##################################################
    """
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
male_peeps = int(input("Enter The Number of Male Students: "))
    
female_peeps = int(input("Enter The Number of Female Students: "))
    
peeps = int(input(" Enter The Number of Non-binary Students: "))
    
total_peeps = male_peeps + female_peeps + peeps
   
m_perc = (male_peeps / total_peeps) * 100
    
f_perc = (female_peeps / total_peeps) * 100

nb_perc = (peeps / total_peeps) * 100

print(f"The total Number of Students: t\t{total_peeps}")

print(f"The Number of Males, Femals and Non-binary: \t{male_peeps} \t\t{female_peeps} \t\{peeps}")

print(f"The Percentage of Males, Females and Non-Binary \t {male_peeps:.2f}% \t\t{female_peeps:.2f}% \t\t{peeps:.2f}%")


if __name__ == '__main__':
    main()