def computepay(h, r):
    if h > 40:
        overtime_hours = h - 40
        regular_pay = 40 * r
        overtime_pay = overtime_hours * (r * 1.5)
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = h * r
    return total_pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
hrs = float(hrs)
rate = float(rate)
p = computepay(hrs, rate)
print("Pay", p)