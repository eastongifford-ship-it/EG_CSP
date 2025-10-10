// eg 7th budget calculaotr

#include <stdio.h>

int main() {
    float income, rent, utilities, groceries, transportation;
    float total_expenses, savings, leftover;

    
    printf("Enter your monthly income: $");
    scanf("%f", &income);

    printf("Enter your monthly Rent/Mortgage: $");
    scanf("%f", &rent);

    printf("Enter your monthly Utilities: $");
    scanf("%f", &utilities);

    printf("Enter your monthly Groceries: $");
    scanf("%f", &groceries);

    printf("Enter your monthly Transportation: $");
    scanf("%f", &transportation);

    
    total_expenses = rent + utilities + groceries + transportation;
    savings = income * 0.20; 
    leftover = income - total_expenses - savings;

    
    printf("\n--- Monthly Budget Summary ---\n");
    printf("Income: $%.2f\n", income);
    printf("Rent/Mortgage: $%.2f (%.2f%%)\n", rent, (rent / income) * 100);
    printf("Utilities: $%.2f (%.2f%%)\n", utilities, (utilities / income) * 100);
    printf("Groceries: $%.2f (%.2f%%)\n", groceries, (groceries / income) * 100);
    printf("Transportation: $%.2f (%.2f%%)\n", transportation, (transportation / income) * 100);
    printf("Recommended Savings: $%.2f (%.2f%%)\n", savings, (savings / income) * 100);
    printf("Leftover to spend: $%.2f (%.2f%%)\n", leftover, (leftover / income) * 100);

    return 0;
}