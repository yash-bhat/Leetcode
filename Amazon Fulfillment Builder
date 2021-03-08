def total(parts,tot):
    while(parts):
        if len(parts) == 1:
            return tot
        parts.sort()
        print(parts)
        s = parts.pop(0) + parts.pop(0)
        tot += s
        parts.append(s)
        print(parts)
    return tot
