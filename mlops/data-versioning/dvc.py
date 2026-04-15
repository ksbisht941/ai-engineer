import pandas as pd
import os

# ── Base data (V1) ────────────────────────────────────────────────────────────
data = {
    "product_id":    ["P001", "P002", "P003"],
    "product_name":  ["Laptop", "Headphones", "Mouse"],
    "category":      ["Electronics", "Electronics", "Accessories"],
    "transaction":   ["sell", "purchase", "sell"],
    "quantity":      [2, 5, 10],
    "unit_price":    [999.99, 49.99, 19.99],
    "total_amount":  [1999.98, 249.95, 199.90],
}
df = pd.DataFrame(data)

# # ── V2: append first new row ───────────────────────────────────────────────────
# new_row_v2 = {
#     "product_id":   "P004",
#     "product_name": "Keyboard",
#     "category":     "Accessories",
#     "transaction":  "purchase",
#     "quantity":     7,
#     "unit_price":   39.99,
#     "total_amount": 279.93,
# }
# df.loc[len(df)] = new_row_v2

# # ── V3: append second new row ─────────────────────────────────────────────────
# new_row_v3 = {
#     "product_id":   "P005",
#     "product_name": "Monitor",
#     "category":     "Electronics",
#     "transaction":  "sell",
#     "quantity":     3,
#     "unit_price":   299.99,
#     "total_amount": 899.97,
# }
# df.loc[len(df)] = new_row_v3

# ── Output ────────────────────────────────────────────────────────────────────
DATA_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(DATA_DIR, "sample_data.csv")

df.to_csv(file_path, index=False)
print(f"CSV file saved to {file_path}")