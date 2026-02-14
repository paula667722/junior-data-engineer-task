import re
import pandas as pd

_LABEL_RE = re.compile(r"^[A-Za-z_]+$")
_ROLE_RE = re.compile(r"^\s*([A-Za-z_]+)\s*([+\-*])\s*([A-Za-z_]+)\s*$")


def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    if not isinstance(df, pd.DataFrame) or not isinstance(role, str) or not isinstance(new_column, str):
        return pd.DataFrame([])

    # new_column musi być OK
    if not _LABEL_RE.fullmatch(new_column):
        return pd.DataFrame([])

    # wszystkie kolumny w df muszą być OK
    if any((not isinstance(c, str)) or (not _LABEL_RE.fullmatch(c)) for c in df.columns):
        return pd.DataFrame([])

    # role musi być w formie: kol1 op kol2
    m = _ROLE_RE.fullmatch(role)
    if not m:
        return pd.DataFrame([])

    left, op, right = m.group(1), m.group(2), m.group(3)

    # kolumny muszą istnieć
    if left not in df.columns or right not in df.columns:
        return pd.DataFrame([])

    out = df.copy()
    if op == "+":
        out[new_column] = out[left] + out[right]
    elif op == "-":
        out[new_column] = out[left] - out[right]
    elif op == "*":
        out[new_column] = out[left] * out[right]
    else:
        return pd.DataFrame([])

    return out
