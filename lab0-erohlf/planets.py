def weight_on_planets():
   # write your code here
    earth = int(input("What do you weigh on earth? "))   
    mars = earth*0.38
    jupiter = earth*2.34
    print("\nOn Mars you would weigh {0} pounds.\nOn Jupiter you would weigh {1} pounds.".format(mars,jupiter))  
   
if __name__ == '__main__':
    weight_on_planets()
