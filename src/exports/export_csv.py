import os
import io
import pandas as pd

def export_combined_csv(df_ip: pd.DataFrame, df_dom: pd.DataFrame, df_em: pd.DataFrame) -> bytes:
    parts = []
    if df_ip is not None and not df_ip.empty:
        df_ip = df_ip.copy()
        df_ip["source"] = "ip"
        parts.append(df_ip)
    if df_dom is not None and not df_dom.empty:
        df_dom = df_dom.copy()
        df_dom["source"] = "domain"
        parts.append(df_dom)
    if df_em is not None and not df_em.empty:
        df_em = df_em.copy()
        df_em["source"] = "email"
        parts.append(df_em)

    combined = pd.concat(parts, ignore_index=True, sort=False) if parts else pd.DataFrame(columns=["source"])
    combined["exported_at"] = pd.Timestamp.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")

    os.makedirs("data", exist_ok=True)
    combined.to_csv("data/combined_report.csv", index=False)

    buf = io.StringIO()
    combined.to_csv(buf, index=False)
    return buf.getvalue().encode("utf-8")
