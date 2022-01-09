
def main():
    print("First Module Name, __name__: \t", __name__);



if __name__ == "__main__":
    print("Executed Directly ...")
    main()
else: 
    print("Imported and Executed Indirectly ...")
    main()
