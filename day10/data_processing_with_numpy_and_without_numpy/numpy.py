import csv
import time
import numpy as np

# loading the data
with open("sales.csv", newline="") as f:
    data = list(csv.DictReader(f))
# verifiying the data
# print("Rows:", len(data))
# print("Columns:", list(data[0].keys()))

# finding duplicate orders
seen = set()
duplicates = []
for row in data:
    if row["order_id"] in seen:
        duplicates.append(row["order_id"])
    seen.add(row["order_id"])
print(
    "------------------------------------------------------------------finding duplicates------------------------------------------------------------------------"
)

print("Duplicate orders:", duplicates)
print("with Duplicate orders tot length:", len(data))

# removeing duplicated order id
seen = set()
unique_data = []

for row in data:
    if row["order_id"] not in seen:
        unique_data.append(row)
    seen.add(row["order_id"])
print(
    "------------------------------------------------------------------removed duplicates & serialized data------------------------------------------------------------------------"
)

print("Duplicate orders serialized : ", len(unique_data))

# clean data and Calculating revenue
for row in unique_data:
    row["quantity"] = int(row["quantity"])
    row["unit_price"] = float(row["unit_price"])
    row["discount_pct"] = float(row["discount_pct"] or 0)
    row["payment_method"] = row["payment_method"] or "Unknown"

    row["revenue"] = (
        row["quantity"] * row["unit_price"] * (1 - row["discount_pct"] / 100)
    )

print(
    "------------------------------------------------------------------clean data and Calculating revenue------------------------------------------------------------------------"
)

print(unique_data[:3])

print(
    "------------------------------------------------------------------Without numpy------------------------------------------------------------------------"
)
# descriptive analysis without numpy
revenue = [row["revenue"] for row in unique_data]
n = len(revenue)
print("total_length ", len(revenue))
print("total_sum ", sum(revenue))
print("max_num", max(revenue))
print("min_num", min(revenue))
print("average", sum(revenue) / n)
print("range", max(revenue) - min(revenue))

# descriptive analysis with numpy
arr = np.array(revenue)
print(
    "------------------------------------------------------------------With numpy------------------------------------------------------------------------"
)

print("count:", arr.size)
print("total:", np.sum(arr))
print("average:", np.mean(arr))
print("median:", np.median(arr))
print("minimum:", np.min(arr))
print("maximum:", np.max(arr))
print("range:", np.ptp(arr))
print("std:", np.std(arr))

print(
    "------------------------------------------------------------------revenue by product,city,category------------------------------------------------------------------------"
)

for col in ["product", "city", "category"]:
    result = {}

    for row in unique_data:
        key = row[col]
        result[key] = result.get(key, 0) + row["revenue"]

    print(f"\nRevenue by {col}:")
    print(sorted(result.items(), key=lambda x: x[1], reverse=True))

print(
    "------------------------------------------------------------------Comparission of execution time------------------------------------------------------------------------"
)

start = time.perf_counter()
sum(revenue)
python_time = time.perf_counter() - start

start = time.perf_counter()
np.sum(arr)
numpy_time = time.perf_counter() - start

print("Pure Python time:", python_time)
print("NumPy time:", numpy_time)
