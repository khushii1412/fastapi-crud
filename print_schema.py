# print_schema.py
from blog_crud.database import engine
from blog_crud import models

output_path = "db_schema.txt"

with open(output_path, "w", encoding="utf-8") as f:
    f.write("=== Database Schema ===\n")
    for table in models.Base.metadata.sorted_tables:
        f.write(f"\nTable: {table.name}\n")
        for column in table.columns:
            f.write(f"  - {column.name} ({column.type})\n")

print(f"✅ Schema written to {output_path}")
