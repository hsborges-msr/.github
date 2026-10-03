import math


def vein(ax, ay, bx, by, left, right, ts):
    """Faceted vein polygon along A->B; left/right are half-widths at each t in ts."""
    dx, dy = bx - ax, by - ay
    length = math.hypot(dx, dy)
    nx, ny = -dy / length, dx / length
    pts_l = [(ax + dx * t + nx * w, ay + dy * t + ny * w) for t, w in zip(ts, left)]
    pts_r = [(ax + dx * t - nx * w, ay + dy * t - ny * w) for t, w in zip(ts, right)]
    pts = pts_l + pts_r[::-1]
    return "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts) + " Z"
