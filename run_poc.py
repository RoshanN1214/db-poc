# Import the logic from your .py file
import processor

# Create some dummy data
data = [("Quantum Task", 1), ("AI Task", 2), ("DevOps Task", 3)]
raw_df = spark.createDataFrame(data, ["TaskName", "Priority"])

# Execute the imported function
final_df = processor.run_transformation(raw_df)

# Show the result
display(final_df)
print("SUCCESS: Modular code imported and executed from Git Folder.")