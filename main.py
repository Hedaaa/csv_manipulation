import pandas as p
import matplotlib.pyplot as plt

# Enzo : Owners
# Mathis : Sales
# Me : Transactions (txns)

def txns_graph():
    data = p.read_csv('nft_sales.csv')
    x = data['Txns']
    y = data[]
    plt.plot()
    
def main():
    txns_graph()
    

if __name__ == "__main__":
    main()