from src.load_to_mysql import load_data
from src.train_model import train_model

def main():

    load_data()

    train_model()

    print("Pipeline completed")

if __name__ == "__main__":
    main()