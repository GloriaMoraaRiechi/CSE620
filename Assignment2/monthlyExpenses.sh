#!/bin/bash

# Get the input from the user
read -p "Enter your Monthly Income: " monthlyIncome
read -p "Enter your monthly Housing Expense: " housing
read -p "Enter your monthly Transportation Expense: " transportation
read -p "Enter your monthly Food Expense: " food
read -p "Enter your monthly Utilities Expense: " utilities
read -p "Enter your monthly Personal Insurance Expense: " insurance
read -p "Enter your monthly Healthcare Expense: " healthcare
read -p "Enter your monthly Cash contributions Expense: " cashContributions
read -p "Enter your monthly Education Expense: " apparelAndServices
read -p "Enter the size of your family: " familySize

# FUNCTION TO CALCULATE THE TOTAL EXPENSES
calculateTotalExpenses(){
	totalExpenses=0
	for expense in "$@"; do
		local totalExpenses=$((totalExpenses + expense))
	done
	echo $totalExpenses
}


expenses=($housing $transportation $food $utilities $insurance $healthcare $cashContributions $apparelAndServices)
TOTALEXPENSES=$(calculateTotalExpenses "${expenses[@]}")

echo "Your total monthly expenses are: \$${TOTALEXPENSES}"

# CALCULATING CASH AVAILABLE FOR THE MONTH
availableCash=$((monthlyIncome - TOTALEXPENSES))
echo "Your remaining cash is: " $availableCash

# FUNCTION TO COMPARE EXPENSES WITH ANOTHER FAMILY, 2022
compareAverage(){
    familySize=$1
    TOTALEXPENSES=$2

    # 2022 average monthly expenses of dufferent families
    case $familySize in
        1) avgExpenses=3693 ;;
        2) avgExpenses=6372 ;;
        3) avgExpenses=7189 ;;
        4) avgExpenses=8640 ;;
        5) avgExpenses=8068 ;;

        *) echo "The family size data is not available for comparison" ; return ;;
    esac

    if [[ $TOTALEXPENSES -gt avgExpenses ]] ; then
        echo "Your expenses exceed the average for a family of size $familySize in 2022."
    else
        echo "Your expenses are below the average for a family of size $familySize in 2022."
    fi
}
compareAverage $familySize $TOTALEXPENSES
