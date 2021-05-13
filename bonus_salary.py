#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: May 11, 2021
# This program determines whether the number the user inputed was
# positive, negative, or 0


# this is the fucntion that does everything
def bonuses():
    salary = (input("What is your salary: "))
    years_worked = (input("How many years have you worked there: "))

    try:
        # try to turn salary into an integer
        salary = int(salary)

    except ValueError:
        # If an error arrises this gets printed to the user
        print("Salary must be a number")

    else:
        try:
            # try to turn years_worked into an integer
            years_worked = int(years_worked)

        except ValueError:
            # if this doesnt work tell the user that it must be a number
            print("Years worked must be a number")

        else:
            # if the number of years is more than 5
            if (years_worked >= 5):
                # calcualte the bonus and total salary
                bonus = salary * 0.05
                total = bonus + salary

                # tell them what their bonus and total salary is
                print("Your bonus is ${0:.2f}".format(bonus))
                print("Your total salary with this bonus is ${0:.2f}"
                      .format(total))

                # depending on how big their bonus is tell them the
                # kind of vacation they can afford
                # note: this is mostly just for one person,
                # and they are the averge costs.
                if (bonus >= 1274) and (bonus < 1659):
                    print("With a bonus of ${0:.2f} you can afford a 1 \
                    \nweek trip to Greece for 1 person".format(bonus))

                if (bonus >= 1659) and (bonus < 1882):
                    print("With a bonus of ${0:.2f} you can afford a 1 \
                    \nweek trip to Japan for 1 person".format(bonus))

                if (bonus >= 1882) and (bonus < 3765):
                    print("With a bonus of ${0:.2f} you can afford a 1 \
                    \nweek trip to Hawaii for 1 person".format(bonus))

                if (bonus >= 3765) and (bonus < 5000):
                    print("With a bonus of ${0:.2f} you can afford a 1 \
                    \nweek trip to Hawaii for 2 people".format(bonus))

                if (bonus >= 5000):
                    print("Wow thats a lot of money, please consider\
                    \ndonating some of that to a charity :)")
            else:
                print("Sorry, no bonus for you :(")


# initial bootup of the program
if __name__ == "__main__":
    bonuses()
