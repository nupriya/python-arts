import matplotlib.pyplot as plt
from illusions import moving_squares, cafe_wall, rotating_snake
from utils.save_image import save

def show_menu():
    print("\n🎨 Optical Illusion Generator")
    print("1. Moving Squares")
    print("2. Cafe Wall Illusion")
    print("3. Rotating Snake")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        img = moving_squares.generate()
        plt.imshow(img, cmap='gray')
        plt.axis('off')
        plt.show()

    elif choice == "2":
        fig, ax = plt.subplots()
        cafe_wall.generate(ax)
        ax.set_aspect('equal')
        ax.axis('off')
        plt.gca().invert_yaxis()
        plt.show()

    elif choice == "3":
        fig, ax = plt.subplots()
        rotating_snake.generate(ax)
        ax.set_aspect('equal')
        ax.axis('off')
        plt.show()

    elif choice == "4":
        break

    else:
        print("Invalid choice")

    save_option = input("Save image? (y/n): ")
    if save_option.lower() == 'y':
        save(plt.gcf())