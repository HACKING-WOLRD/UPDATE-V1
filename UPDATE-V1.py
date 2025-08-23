#!/usr/bin/env python3
# HACKING WORLD™ — Free Fire Diamond Top-Up (WORK / ROOT)
# VIP Neon Edition • Cookie → UID Flow • Non-Root
# NOTE: This is a WORK/simulation ONLY.  top-up diamonds.

import os, sys, time, random

# ---------- Colors ----------
R = '\033[1;31m'; G = '\033[1;32m'; Y = '\033[1;33m'
B = '\033[1;34m'; C = '\033[1;36m'; M = '\033[1;35m'
W = '\033[1;37m'; RESET = '\033[0m'

def clear(): os.system('clear' if os.name != 'nt' else 'cls')

def typewrite(text, delay=0.007):
    for ch in text:
        sys.stdout.write(ch); sys.stdout.flush(); time.sleep(delay)
    print()

def spinner(title, secs=3):
    frames = ['|','/','-','\\']
    sys.stdout.write(Y + title + " ")
    t0 = time.time(); i = 0
    while time.time() - t0 < secs:
        sys.stdout.write(frames[i % 4]); sys.stdout.flush()
        time.sleep(0.12); sys.stdout.write('\b'); i += 1
    print(G + "✓" + RESET)

def progress_bar(title, width=38, duration=2.2):
    print(C + title + RESET)
    steps = int(duration / 0.04)
    for i in range(steps + 1):
        filled = int(i / steps * width)
        bar = "█" * filled + "░" * (width - filled)
        percent = int(i / steps * 100)
        sys.stdout.write(M + f"[{bar}] {percent:3d}%\r" + RESET)
        sys.stdout.flush(); time.sleep(0.04)
    print()

def neon_banner():
    clear()
    lines = [
        f"{M}██████╗ ███████╗███████╗     ██╗██╗ ███████╗ ██████╗",
        f"{C}██╔══██╗██╔════╝██╔════╝     ██║██║ ██╔════╝██╔════╝",
        f"{B}██████╔╝█████╗  █████╗       ██║██║ █████╗  ██║     ",
        f"{G}██╔═══╝ ██╔══╝  ██╔══╝  ██   ██║██║ ██╔══╝  ██║     ",
        f"{Y}██║     ███████╗███████╗ ╚█████╔╝██║ ███████╗╚██████╗",
        f"{R}╚═╝     ╚══════╝╚══════╝  ╚════╝ ╚═╝ ╚══════╝ ╚═════╝{RESET}",
    ]
    for ln in lines: print(ln); time.sleep(0.02)
    print(W + "                 H A C K I N G   W O R L D™")
    print(C + "           Free Fire Diamond Panel • BD/WORK" + RESET)
    print(W + "────────────────────────────────────────────────────────\n")

def matrix_rain(rows=8, width=62, drops=95):
    glyphs = list("01▌▍▎▏✦✧⦿◉•+x")
    cols = [G,B,C,M,Y]
    for _ in range(rows):
        print("".join(random.choice(cols)+random.choice(glyphs)+RESET for _ in range(width)))
        time.sleep(0.02)
    columns = [random.randint(0,width-1) for _ in range(12)]
    for _ in range(drops):
        row = [" "] * width
        for j,c in enumerate(columns):
            ch = random.choice(["1","0","•","✦","x","+"])
            color = random.choice([G,B,C,Y,M])
            row[c] = color+ch+RESET
            if random.random()<0.18: columns[j]=random.randint(0,width-1)
        print("".join(row)); time.sleep(0.01)
    print()

def fake_cookie_check(cookie):
    # purely cosmetic checks (no real validation)
    score = 0
    if len(cookie) > 20: score += 1
    if any(x in cookie for x in ["session","_garena","auth","token","sid"]): score += 1
    if any(ch in cookie for ch in "=.:-_"): score += 1
    return score >= 2

def fake_logs(uid):
    nodes = ["bd-edge-1","sg-core-2","in-mum-3","eu-fr-1","us-va-2"]
    events = [
        "Negotiating TLS … OK",
        "Fingerprint Sync … OK",
        "Cookie Bind … OK",
        "UID Validation … OK",
        "Queue Ticket … GRANTED",
        "Wallet Bridge … READY",
        "Anti-Abuse Layer … PASSED"
    ]
    for ev in events:
        tag = random.choice(nodes)
        tk = hex(random.getrandbits(44))
        typewrite(C+f"[{tag}] {ev}  token={tk}  uid={uid}"+RESET, 0.006)
        time.sleep(0.06)

def choose_package():
    print(W+"\nSelect Diamond Package:"+RESET)
    packs = [("Lite", 520), ("Pro", 1060), ("Elite", 2190), ("Ultra", 5600)]
    for i,(n,v) in enumerate(packs,1):
        print(C+f"[{i}] {n:<5} → {v} Diamonds"+RESET)
    ch = input(Y+"Choose (1-4): "+W).strip()
    try: idx = max(1,min(4,int(ch)))
    except: idx = 2
    return packs[idx-1]

def simulate_topup(amount):
    steps = [
        "[#] Building secure tunnel",
        "[#] Allocating top-up window",
        "[#] Seeding wallet bridge",
        "[#] Streaming diamond packets",
        "[#] Verifying receipts",
        "[#] Clearing temp artifacts"
    ]
    for t in steps:
        progress_bar(t, 42, random.uniform(1.6, 2.3))
        if "Streaming" in t:
            # show flowing counter
            delivered = 0; target = amount
            bar_len = 44
            while delivered < target:
                inc = random.randint(max(1,amount//30), max(2,amount//15))
                delivered = min(target, delivered + inc)
                filled = int(delivered/target*bar_len)
                bar = G + "█"*filled + RESET + "░"*(bar_len-filled)
                sys.stdout.write(M+f"   → Sent: {W}{delivered:>5}/{target:<5}  {bar}\r"+RESET)
                sys.stdout.flush(); time.sleep(random.uniform(0.04,0.08))
            print()

def success_screen(uid, pkg_name, amount):
    clear(); neon_banner()
    conf = "✦"*60
    print(G+conf+RESET)
    print(G+" SUCCESS (Working): "+RESET+W+f"Queued {amount} Diamonds  "+C+f"[Package: {pkg_name}]"+RESET)
    print(C+"Target UID: "+W+uid+RESET)
    print(Y+"Note: "+W+"This is a simulation/real top-up occurs.\n"+RESET)
    print(G+conf+RESET)
    input(W+"\nPress Enter to exit…"+RESET)

def main():
    neon_banner()
    matrix_rain()

    # 1) Cookie first
    cookie = input(Y+"[+] Paste Garena/Free Fire Cookie: "+W).strip()
    print()
    spinner("[✓] Binding session cookie", 2)
    if not fake_cookie_check(cookie):
        print(R+"[✘] Invalid/Weak cookie pattern detected (work check)."+RESET)
        input(W+"Press Enter to exit…"+RESET)
        return

    # 2) Then UID
    uid = input(Y+"[+] Enter Free Fire UID: "+W).strip()
    if not uid:
        print(R+"UID required!"+RESET); time.sleep(1); return
    print()
    spinner("[✓] Connecting to Garena Network", 2)
    spinner("[✓] Verifying device fingerprint", 2)
    progress_bar("[#] Establishing secure control channel", 40, 1.9)
    print()
    fake_logs(uid)

    # 3) Choose package → simulate
    pkg_name, amount = choose_package()
    print()
    simulate_topup(amount)

    # 4) Final screen (work success)
    success_screen(uid, pkg_name, amount)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RESET+"\n\nInterrupted by user.\n")