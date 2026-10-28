print("=========================")
print(" Custom Ride Builder ")
print("=========================")

print("Choose your Vehicle")
print("1. Car")
print("2. Bike")
choice=int(input("Enter your choice 1 or 2 ?"))

if choice==1:
    print("Pick your car type")
    print("1. Haval")
    print("2. City")
    car_type=int(input("What type of car ? (1/2)"))

    if car_type==1:
        print("You chose Haval.")
        print("You should choose this car because it is better if you want to go to northern areas,long drives,bumpy roads or for travelling.Offers premium features (panoramic sunroofs, heads-up displays, heated/massaging seats) as standard equipment for a fraction of the cost of mainstream competitors.")
    elif car_type==2:
        print("You chose City.The Honda City is considered a good and popular car because it combines a spacious cabin, reliable engine performance, and high fuel economy into an affordable subcompact package")
    else:
        print("Wrong Choice!")

elif choice==2:
    print("Pick your bike type")
    print("1. Honda")
    print("2. Yamaha")
    bike_type=int(input("What type of bike do you want? (1/2)"))

    if bike_type==1:
        print("You chose Honda.Honda motorcycles are well-regarded because the company started as an engine manufacturer, focusing heavily on durability, smooth performance, and ease of maintenance.")
    elif bike_type==2:
        print("You chose Yamaha.they combine high reliability, agile and balanced handling, and strong racing-derived performance across a wide lineup of bikes.")
    else:
        print("Wrong Choice!")

else:
    print("Invalid input")