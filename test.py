# By Dominic Eggerman

# Imports
import pandas as pd


# Test optimization
if __name__ == "__main__":
    # Read file
    pipes = pd.read_excel("Sample Pipe Rates.xlsx", sheet_name="Pipes")
    caps = pd.read_excel("Sample Pipe Rates.xlsx", sheet_name="Capacities")

    # Parameters
    to_sell = 80000

    # Join frames
    df = pipes.set_index("Pipeline").join(caps.set_index("Pipeline"))

    # Calculate optimization
    df["Deliverable"] = df["Lease Capacity"] - (df["Lease Capacity"] * df["Fuel"])
    df["Cost"] = df["Lease Capacity"] * df["Rate"]
    df["Sale"] = df["Deliverable"] * df["Price"]
    df["Total Profit"] = df["Sale"] - df["Cost"]
    df["Profit per Unit"] = df["Total Profit"] / df["Lease Capacity"]

    # Optimize
    df.sort_values(by="Profit per Unit", ascending=False, inplace=True)

    # Find sale volumes
    sold = []
    for vol in df["Lease Capacity"].values:
        # Break if no volume remaining
        if to_sell - vol <= 0:
            sold.append(to_sell)
            break
        # Append and update
        sold.append(vol)
        to_sell = to_sell - vol

    # Append sold volumes to df
    sold = pd.DataFrame(sold, columns=["Vol Sold"])
    df = df.reset_index().join(sold)

    # Calculate total profit
    df.dropna(axis=0, inplace=True)
    print(df["Total Profit"].sum())

    # Print
    print(df)