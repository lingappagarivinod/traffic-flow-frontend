def optimize_traffic(ns_traffic, ew_traffic):
    """
    Decide traffic signal based on traffic density
    """

    if ns_traffic > ew_traffic:
        return "NS Green Signal (North–South traffic is higher)"
    elif ew_traffic > ns_traffic:
        return "EW Green Signal (East–West traffic is higher)"
    else:
        return "Equal Traffic → Signals will alternate"
