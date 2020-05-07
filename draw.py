# Investment plan
def main ():
     print("This program plots the growth of 10-years investment.")

     principal = input("Enter the initail principal:")
     apr = input("Enter the annualized interest rate: ")

     win = createLabeledWindow ()
     drawBar(win, 0 , principal)
     for year in range(1, 11):
          principal = principal * (1 + apr)
          drawBar (win, year, principal)


print("What is wrong with you")
   
     





     