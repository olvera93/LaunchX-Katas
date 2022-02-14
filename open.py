def main():
    try:
        open("config.txt")
    except FileNotFoundError:
        print("Couln't find the the config.txt file!")
if __name__ == "__main__":
    main()


