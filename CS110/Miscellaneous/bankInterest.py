def main():
    principal = eval(input('Enter the starting principal'))
    apr = eval(input('Enter the interest  (as 0.00)'))

    for i in range(10):
        #print(i)
        principal = principal * (1 + apr)

    print('After 10 years, the investment is', principal)

main()
