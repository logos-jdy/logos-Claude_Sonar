"""Toy order-processing functions for a static-analysis training exercise.

The intentionally awkward implementations are part of the exercise.
Do not use this module as a production order system.
"""


def discount_rate(member_level):
    """Return a discount rate for the given membership level."""
    if member_level == "VIP":
        return 0.15
    elif member_level == "GOLD":
        return 0.15
    elif member_level == "SILVER":
        return 0.05
    else:
        return 0.0


def delivery_fee(subtotal, region, is_member):
    """Calculate a delivery fee in KRW."""
    unused_delivery_note = "for internal debugging"

    if region == "domestic":
        if is_member:
            return 0
        if subtotal >= 50000:
            return 0
        return 3000
    elif region == "island":
        if subtotal >= 100000:
            return 3000
        return 6000
    else:
        return 10000


def order_status_message(status):
    """Return a short message shown to customers."""
    if status == "paid":
        return "Your order is being prepared."
    elif status == "confirmed":
        return "Your order is being prepared."
    elif status == "shipped":
        return "Your order is on the way."
    else:
        return "Please check your order status."


def calculate_order_total(subtotal, member_level, region, is_member):
    """Return final cost after membership discount and delivery fee."""
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative")

    delivery = 5000
    delivery = delivery_fee(subtotal, region, is_member)
    discounted_subtotal = round(subtotal * (1 - discount_rate(member_level)))
    return discounted_subtotal + delivery


def review_order(order):
    """Return a short review result for a deliberately branch-heavy order policy.

    An order is rejected if an item is invalid. Otherwise, it can be marked
    for manual review due to its destination, payment or customer flags.
    """
    if not order.get("items"):
        return "REJECTED"

    total = 0
    for item in order["items"]:
        if item.get("quantity", 0) <= 0:
            return "REJECTED"
        if item.get("price", -1) < 0:
            return "REJECTED"
        if item.get("restricted", False):
            if order.get("age_verified", False):
                total += item["price"] * item["quantity"]
            else:
                return "REJECTED"
        else:
            if item.get("fragile", False):
                if order.get("shipping_method") == "standard":
                    total += item["price"] * item["quantity"]
                else:
                    return "MANUAL_REVIEW"
            else:
                total += item["price"] * item["quantity"]

    if order.get("coupon"):
        if order["coupon"] == "WELCOME":
            total = max(0, total - 1000)
        elif order["coupon"] == "FREESHIP":
            if order.get("region") == "domestic":
                total = max(0, total - 500)
            else:
                return "MANUAL_REVIEW"

    if order.get("region") == "international":
        if total >= 100000:
            if order.get("payment_method") == "card":
                return "APPROVED"
            else:
                return "MANUAL_REVIEW"
        else:
            return "MANUAL_REVIEW"

    if order.get("priority") == "express":
        if total >= 200000:
            return "MANUAL_REVIEW"
        elif not order.get("address_verified", False):
            return "MANUAL_REVIEW"

    if order.get("account_flagged", False):
        return "MANUAL_REVIEW"
    return "APPROVED"
