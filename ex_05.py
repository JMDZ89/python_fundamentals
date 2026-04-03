def computepay(h, r):
    if h > 40:
        overtimerates = r * 1.50
        regularhours = 40 * r
        overtimehours = (h - 40) * overtimerates 
        totalpay = regularhours + overtimehours
    else: 
        h <= 40
        totalpay = regularhours + overtimehours
    return totalpay

hrs = input("Enter Hours:")
rate = input("Enter Rate")
hrs = float(hrs)
rate = float(rate)
p = computepay(hrs, rate)
print("Pay", p)