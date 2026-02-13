# Chocolate Game - Detailed Version

# Taking input from user
n = int(input("Enter number of rows (n): "))
m = int(input("Enter number of columns (m): "))

# Step 1: Calculate total pieces
total_pieces = n * m

# Step 2: Calculate total possible cuts
total_cuts = total_pieces - 1

# Step 3: Check who makes the last cut
if total_cuts % 2 != 0:
    result = "Yes"   # First player wins
else:
    result = "No"    # Second player wins

# Step 4: Print result
print("Total Pieces:", total_pieces)
print("Total Cuts Possible:", total_cuts)
print("Will first player win?", result)

