import os

TEXT = (
    "Day1: enter 2 free make.fun code bounties/day x30d (60 entries, "
    "$0 fees). Keep $100 for API/hosting + paid entries. ~1 in 6 "
    "places top-50 (avg $18) = ~$180 EV; top-10 adds $50+. Edge: "
    "sponsors pay, zero marketing; agent codes 24/7. Reinvest wins "
    "into paid pools."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
