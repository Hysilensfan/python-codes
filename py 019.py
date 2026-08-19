# First method
for _ in range(9):
    n: str =  input()
    tT = tL = 0 # Default counting total value is 0
    if n == "Tiger":
        tT += 1
    else:
        tL += 1
print("Tiger" if tT > tL else "Lion")
# Second method
print("Tiger" if sum(input()=="Tiger" for _ in range(9)) > 4 else "Lion")
"""
Logic clearly version,just judges the "Tiger"'s appeared dights greater than the "Lion"'s appeared dights.
"""

# Third method
log: list = [input() for _ in range(9)]
print("Tiger" log.counter("Tiger") > 4 else  "Lion")
