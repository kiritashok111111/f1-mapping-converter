import customtkinter as ctk
from tkinter import StringVar

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# ─────────────────────────────────────────────
#  DATA
# ─────────────────────────────────────────────

F125 = {
    "xbox": dict(throttle="RT", brake="LT", steer_l="Left stick ←", steer_r="Left stick →",
                 gear_up="A", gear_down="B", drs="Y", ers="X", kers="N/A",
                 handbrake="RB", pit_limiter="LB + RB",
                 mfd_toggle="View", mfd_up="D-pad ↑", mfd_down="D-pad ↓",
                 mfd_left="D-pad ←", mfd_right="D-pad →",
                 look_back="RS click", camera="RS",
                 flashback="LB + Menu", radio="Menu", neutral="LS click"),
    "ps":   dict(throttle="R2", brake="L2", steer_l="Left stick ←", steer_r="Left stick →",
                 gear_up="Cross", gear_down="Circle", drs="Triangle", ers="Square", kers="N/A",
                 handbrake="R1", pit_limiter="L1 + R1",
                 mfd_toggle="Touchpad", mfd_up="D-pad ↑", mfd_down="D-pad ↓",
                 mfd_left="D-pad ←", mfd_right="D-pad →",
                 look_back="RS click", camera="RS",
                 flashback="L1 + Options", radio="Options", neutral="LS click"),
}

LX = dict(throttle="RT", brake="LT", steer_l="Left stick ←", steer_r="Left stick →",
          gear_up="A", gear_down="X", drs="N/A", ers="N/A", kers="N/A",
          handbrake="RB", pit_limiter="B",
          mfd_toggle="Back", mfd_up="D-pad ↑", mfd_down="D-pad ↓",
          mfd_left="D-pad ←", mfd_right="D-pad →",
          look_back="RS click", camera="RS",
          flashback="LB + Start", radio="Start", neutral="LS click")
LP = dict(throttle="R2", brake="L2", steer_l="Left stick ←", steer_r="Left stick →",
          gear_up="Cross", gear_down="Square", drs="N/A", ers="N/A", kers="N/A",
          handbrake="R1", pit_limiter="Circle",
          mfd_toggle="Select", mfd_up="D-pad ↑", mfd_down="D-pad ↓",
          mfd_left="D-pad ←", mfd_right="D-pad →",
          look_back="RS click", camera="RS",
          flashback="L1 + Start", radio="Start", neutral="LS click")

MX = dict(throttle="RT", brake="LT", steer_l="Left stick ←", steer_r="Left stick →",
          gear_up="A", gear_down="B", drs="Y", ers="X", kers="N/A",
          handbrake="RB", pit_limiter="LB + RB",
          mfd_toggle="View", mfd_up="D-pad ↑", mfd_down="D-pad ↓",
          mfd_left="D-pad ←", mfd_right="D-pad →",
          look_back="RS click", camera="RS",
          flashback="LB + Menu", radio="Menu", neutral="LS click")
MP = dict(throttle="R2", brake="L2", steer_l="Left stick ←", steer_r="Left stick →",
          gear_up="Cross", gear_down="Circle", drs="Triangle", ers="Square", kers="N/A",
          handbrake="R1", pit_limiter="L1 + R1",
          mfd_toggle="Touchpad", mfd_up="D-pad ↑", mfd_down="D-pad ↓",
          mfd_left="D-pad ←", mfd_right="D-pad →",
          look_back="RS click", camera="RS",
          flashback="L1 + Options", radio="Options", neutral="LS click")

GAMES = {
    "F1 2011": dict(era="PS3 / Xbox 360",
        note="No DRS button — DRS wasn't in the game. Gear down = X / Square. Back/Start used instead of View/Menu.",
        xbox={**LX, "drs":"N/A"}, ps={**LP, "drs":"N/A"}),
    "F1 2012": dict(era="PS3 / Xbox 360",
        note="DRS added (Y / Triangle). KERS auto-deployed — no manual button. Gear down = X / Square.",
        xbox={**LX, "drs":"Y"}, ps={**LP, "drs":"Triangle"}),
    "F1 2013": dict(era="PS3 / Xbox 360",
        note="Manual KERS button added on X / Square. Gear down moved to B / Circle.",
        xbox={**LX, "drs":"Y", "kers":"X", "gear_down":"B"},
        ps={**LP,  "drs":"Triangle", "kers":"Square", "gear_down":"Circle"}),
    "F1 2014": dict(era="PS3 / Xbox 360",
        note="KERS replaced by ERS on X / Square. Gear down = B / Circle. Still on Back/Start.",
        xbox={**LX, "drs":"Y", "ers":"X", "gear_down":"B"},
        ps={**LP,  "drs":"Triangle", "ers":"Square", "gear_down":"Circle"}),
    "F1 2015": dict(era="PS4 / Xbox One (first)",
        note="First PS4/Xbox One game. Same buttons as 2014 but Back→View and Start→Menu/Options.",
        xbox={**LX, "drs":"Y", "ers":"X", "gear_down":"B", "mfd_toggle":"View", "flashback":"LB + Menu", "radio":"Menu"},
        ps={**LP,  "drs":"Triangle", "ers":"Square", "gear_down":"Circle", "mfd_toggle":"Touchpad", "flashback":"L1 + Options", "radio":"Options"}),
    "F1 2016": dict(era="PS4 / Xbox One",
        note="Fully settled modern layout. Gear up=A/Cross, Gear down=B/Circle, DRS=Y/Triangle, ERS=X/Square.",
        xbox=dict(MX), ps=dict(MP)),
    "F1 2017": dict(era="PS4 / Xbox One", note="Same default layout as F1 2016.", xbox=dict(MX), ps=dict(MP)),
    "F1 2018": dict(era="PS4 / Xbox One", note="Same default layout as F1 2016/2017.", xbox=dict(MX), ps=dict(MP)),
    "F1 2019": dict(era="PS4 / Xbox One", note="Same layout as F1 2016–2018.", xbox=dict(MX), ps=dict(MP)),
    "F1 2020": dict(era="PS4 / Xbox One", note="Same layout as F1 2016–2019.", xbox=dict(MX), ps=dict(MP)),
    "F1 2021": dict(era="PS4 / PS5 / Xbox", note="Codemasters' final F1 game. Same layout as 2016–2020.", xbox=dict(MX), ps=dict(MP)),
    "F1 22":   dict(era="PS5 / Xbox Series", note="First EA Sports title. Same layout as F1 2021.", xbox=dict(MX), ps=dict(MP)),
    "F1 23":   dict(era="PS5 / Xbox Series", note="Same default layout as F1 22.", xbox=dict(MX), ps=dict(MP)),
    "F1 24":   dict(era="PS5 / Xbox Series", note="Same default layout as F1 22/23.", xbox=dict(MX), ps=dict(MP)),
}

SECTIONS = [
    ("🏎  Driving", [
        ("gear_up",    "Gear up"),
        ("gear_down",  "Gear down"),
        ("throttle",   "Throttle"),
        ("brake",      "Brake"),
        ("steer_l",    "Steer left"),
        ("steer_r",    "Steer right"),
        ("handbrake",  "Handbrake"),
        ("neutral",    "Neutral"),
    ]),
    ("⚡  Car systems", [
        ("drs",         "DRS"),
        ("ers",         "ERS overtake"),
        ("kers",        "KERS (2013 only)"),
        ("pit_limiter", "Pit limiter"),
    ]),
    ("📡  MFD & camera", [
        ("mfd_toggle", "MFD / settings toggle"),
        ("mfd_up",     "MFD up"),
        ("mfd_down",   "MFD down"),
        ("mfd_left",   "MFD left / previous"),
        ("mfd_right",  "MFD right / next"),
        ("look_back",  "Look back"),
        ("camera",     "Camera change"),
    ]),
    ("⚙  Other", [
        ("flashback",  "Flashback / rewind"),
        ("radio",      "Radio / team comms"),
    ]),
]

# ─────────────────────────────────────────────
#  COLOURS
# ─────────────────────────────────────────────
BG         = "#0f0f0f"
SURFACE    = "#1a1a1a"
SURFACE2   = "#222222"
SURFACE3   = "#2a2a2a"
BORDER     = "#333333"
TEXT       = "#f0f0f0"
TEXT2      = "#aaaaaa"
TEXT3      = "#555555"
RED        = "#e8002d"
AMBER      = "#ff8700"
GREEN_TEAL = "#00d2be"
CHANGED_BG = "#2a1c00"
SAME_BG    = "#1a1a1a"

BTN_COLORS = {
    "a":        ("#1a3d1a", "#44dd44"),
    "b":        ("#3d1a1a", "#ff6060"),
    "x":        ("#1a2a4a", "#66aaff"),
    "y":        ("#3d3000", "#ddcc44"),
    "cross":    ("#1a2a4a", "#5599ff"),
    "circle":   ("#3d1a1a", "#ff5555"),
    "square":   ("#3a1a35", "#ee77cc"),
    "triangle": ("#0d3327", "#44ddaa"),
    "trigger":  ("#2a1a4a", "#bb88ff"),
    "bumper":   ("#0f2e4a", "#55aaff"),
    "stick":    ("#252525", "#aaaaaa"),
    "dpad":     ("#202020", "#999999"),
    "system":   ("#1e1e1e", "#777777"),
    "na":       ("#111111", "#444444"),
}

def btn_style(label):
    if not label or label == "N/A":
        return BTN_COLORS["na"]
    b = label.lower()
    if b == "a":        return BTN_COLORS["a"]
    if b == "b":        return BTN_COLORS["b"]
    if b == "x":        return BTN_COLORS["x"]
    if b == "y":        return BTN_COLORS["y"]
    if b == "cross":    return BTN_COLORS["cross"]
    if b == "circle":   return BTN_COLORS["circle"]
    if b == "square":   return BTN_COLORS["square"]
    if b == "triangle": return BTN_COLORS["triangle"]
    if any(b.startswith(p) for p in ("rt","lt","r2","l2")): return BTN_COLORS["trigger"]
    if any(b.startswith(p) for p in ("rb","lb","r1","l1")): return BTN_COLORS["bumper"]
    if "stick" in b or "ls " in b or "rs " in b: return BTN_COLORS["stick"]
    if "d-pad" in b or "dpad" in b: return BTN_COLORS["dpad"]
    return BTN_COLORS["system"]

# ─────────────────────────────────────────────
#  APP
# ─────────────────────────────────────────────
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("F1 Controller Mapping — 2011 to 25")
        self.geometry("860x720")
        self.minsize(720, 580)
        self.configure(fg_color=BG)

        self._game_var = StringVar(value="F1 23")
        self._ctrl_var = StringVar(value="xbox")
        self._filter_var = StringVar(value="all")

        self._build_header()
        self._build_sidebar()
        self._build_main()
        self.render()

    # ── HEADER ──────────────────────────────
    def _build_header(self):
        hdr = ctk.CTkFrame(self, fg_color=SURFACE, corner_radius=0, height=52)
        hdr.pack(fill="x", side="top")
        hdr.pack_propagate(False)

        inner = ctk.CTkFrame(hdr, fg_color="transparent")
        inner.pack(fill="both", expand=True, padx=20)

        badge = ctk.CTkFrame(inner, fg_color=RED, corner_radius=6, width=34, height=34)
        badge.pack(side="left", pady=9)
        badge.pack_propagate(False)
        ctk.CTkLabel(badge, text="F1", font=("Segoe UI", 13, "bold"), text_color="white").pack(expand=True)

        title_col = ctk.CTkFrame(inner, fg_color="transparent")
        title_col.pack(side="left", padx=12)
        ctk.CTkLabel(title_col, text="Controller Mapping Converter",
                     font=("Segoe UI", 14, "bold"), text_color=TEXT).pack(anchor="w")
        ctk.CTkLabel(title_col, text="F1 2011 – F1 25  ·  Xbox & PlayStation",
                     font=("Segoe UI", 11), text_color=TEXT3).pack(anchor="w")

        pill = ctk.CTkLabel(inner, text="→ F1 25",
                            font=("Segoe UI", 11, "bold"), text_color=RED,
                            fg_color="#3a0010", corner_radius=12)
        pill.pack(side="right", pady=16, ipadx=10, ipady=3)

    # ── SIDEBAR ─────────────────────────────
    def _build_sidebar(self):
        self._sidebar = ctk.CTkScrollableFrame(self, width=190, fg_color=SURFACE,
                                               corner_radius=0, scrollbar_button_color=SURFACE3)
        self._sidebar.pack(side="left", fill="y", padx=0, pady=0)

        eras = [
            ("PS3 / Xbox 360", ["F1 2011","F1 2012","F1 2013","F1 2014","F1 2015"]),
            ("PS4 / Xbox One",  ["F1 2016","F1 2017","F1 2018","F1 2019","F1 2020","F1 2021"]),
            ("PS5 / Xbox Series", ["F1 22","F1 23","F1 24"]),
        ]

        self._game_buttons = {}
        for era_label, games in eras:
            ctk.CTkLabel(self._sidebar, text=era_label.upper(),
                         font=("Segoe UI", 9, "bold"), text_color=TEXT3,
                         anchor="w").pack(fill="x", padx=14, pady=(14,4))
            sep = ctk.CTkFrame(self._sidebar, fg_color=BORDER, height=1)
            sep.pack(fill="x", padx=14, pady=(0,6))

            for g in games:
                btn = ctk.CTkButton(
                    self._sidebar, text=g,
                    font=("Segoe UI", 12),
                    fg_color="transparent", hover_color=SURFACE3,
                    text_color=TEXT2, anchor="w",
                    corner_radius=6, height=30,
                    command=lambda gm=g: self._select_game(gm)
                )
                btn.pack(fill="x", padx=10, pady=2)
                self._game_buttons[g] = btn

        self._highlight_game("F1 23")

    def _select_game(self, game):
        self._game_var.set(game)
        self._highlight_game(game)
        self.render()

    def _highlight_game(self, game):
        for g, btn in self._game_buttons.items():
            if g == game:
                btn.configure(fg_color=RED, text_color="white")
            else:
                btn.configure(fg_color="transparent", text_color=TEXT2)

    # ── MAIN PANEL ──────────────────────────
    def _build_main(self):
        self._main = ctk.CTkFrame(self, fg_color=BG, corner_radius=0)
        self._main.pack(side="left", fill="both", expand=True)

        # Controls row
        ctrl_row = ctk.CTkFrame(self._main, fg_color="transparent")
        ctrl_row.pack(fill="x", padx=20, pady=(16,0))

        # Controller type
        c1 = ctk.CTkFrame(ctrl_row, fg_color="transparent")
        c1.pack(side="left", padx=(0,16))
        ctk.CTkLabel(c1, text="CONTROLLER", font=("Segoe UI", 9, "bold"),
                     text_color=TEXT3).pack(anchor="w")
        ctk.CTkSegmentedButton(c1, values=["xbox","ps"], variable=self._ctrl_var,
                               font=("Segoe UI", 12),
                               fg_color=SURFACE, selected_color=RED,
                               selected_hover_color="#c0001f",
                               unselected_color=SURFACE, unselected_hover_color=SURFACE3,
                               text_color=TEXT2, text_color_disabled=TEXT3,
                               command=lambda _: self.render()).pack(pady=(4,0))

        # Filter
        c2 = ctk.CTkFrame(ctrl_row, fg_color="transparent")
        c2.pack(side="left")
        ctk.CTkLabel(c2, text="SHOW", font=("Segoe UI", 9, "bold"),
                     text_color=TEXT3).pack(anchor="w")
        ctk.CTkSegmentedButton(c2, values=["all","changed","same"], variable=self._filter_var,
                               font=("Segoe UI", 12),
                               fg_color=SURFACE, selected_color=SURFACE3,
                               selected_hover_color=BORDER,
                               unselected_color=SURFACE, unselected_hover_color=SURFACE3,
                               text_color=TEXT2, text_color_disabled=TEXT3,
                               command=lambda _: self.render()).pack(pady=(4,0))

        # Summary bar
        self._summary = ctk.CTkFrame(self._main, fg_color=SURFACE, corner_radius=8, height=42)
        self._summary.pack(fill="x", padx=20, pady=(12,0))
        self._summary.pack_propagate(False)
        self._summary_label = ctk.CTkLabel(self._summary, text="",
                                            font=("Segoe UI", 12), text_color=TEXT2)
        self._summary_label.pack(side="left", padx=14)

        # Note bar
        self._note_frame = ctk.CTkFrame(self._main, fg_color="#1a1400",
                                         corner_radius=8, border_width=1, border_color="#332800")
        self._note_label = ctk.CTkLabel(self._note_frame, text="", wraplength=580,
                                         font=("Segoe UI", 11), text_color=TEXT2,
                                         justify="left", anchor="w")
        self._note_label.pack(padx=12, pady=8, fill="x")

        # Scrollable mapping area
        self._scroll = ctk.CTkScrollableFrame(self._main, fg_color=BG,
                                               scrollbar_button_color=SURFACE3)
        self._scroll.pack(fill="both", expand=True, padx=20, pady=(10,16))

    # ── RENDER ──────────────────────────────
    def render(self):
        game = self._game_var.get()
        ctrl = self._ctrl_var.get()
        filt = self._filter_var.get()
        gd = GAMES[game]
        src = gd[ctrl]
        dst = F125[ctrl]

        # Note
        note = gd.get("note","")
        if note:
            self._note_label.configure(text=f"ℹ  {note}")
            self._note_frame.pack(fill="x", padx=20, pady=(8,0))
        else:
            self._note_frame.pack_forget()

        # Count changes
        all_keys = [k for sec in SECTIONS for k,_ in sec[1]]
        comparable = [(k,l) for sec in SECTIONS for k,l in sec[1]
                      if not (src.get(k,"N/A")=="N/A" and dst.get(k,"N/A")=="N/A")]
        changed_count = sum(1 for k,_ in comparable if src.get(k,"N/A") != dst.get(k,"N/A"))
        same_count = len(comparable) - changed_count

        # Summary
        if changed_count == 0:
            self._summary_label.configure(
                text=f"✓  No button changes — {game} layout carries straight over to F1 25!",
                text_color=GREEN_TEAL)
        else:
            self._summary_label.configure(
                text=f"⚠  {changed_count} input{'s' if changed_count>1 else ''} changed  ·  "
                     f"{same_count} unchanged  ·  {gd['era']}",
                text_color=AMBER)

        # Clear scroll area
        for w in self._scroll.winfo_children():
            w.destroy()

        # Render sections
        for sec_label, actions in SECTIONS:
            visible = []
            for key, label in actions:
                sv = src.get(key, "N/A")
                dv = dst.get(key, "N/A")
                if sv == "N/A" and dv == "N/A":
                    continue
                changed = sv != dv
                if filt == "changed" and not changed: continue
                if filt == "same" and changed: continue
                visible.append((key, label, sv, dv, changed))

            if not visible:
                continue

            # Section header
            sec_hdr = ctk.CTkFrame(self._scroll, fg_color="transparent")
            sec_hdr.pack(fill="x", pady=(12,4))
            ctk.CTkLabel(sec_hdr, text=sec_label,
                         font=("Segoe UI", 11, "bold"), text_color=TEXT3,
                         anchor="w").pack(side="left")
            changed_in_sec = sum(1 for _,_,sv,dv,ch in visible if ch)
            if changed_in_sec:
                ctk.CTkLabel(sec_hdr, text=f"{changed_in_sec} changed",
                             font=("Segoe UI", 10), text_color=AMBER).pack(side="right")
            sep = ctk.CTkFrame(self._scroll, fg_color=BORDER, height=1)
            sep.pack(fill="x", pady=(0,4))

            # Column headers
            col_hdr = ctk.CTkFrame(self._scroll, fg_color="transparent")
            col_hdr.pack(fill="x", padx=4, pady=(0,2))
            for txt, w, side in [("Input", 200, "left"), (game, 180, "left"),
                                   ("", 30, "left"), ("F1 25", 180, "left")]:
                ctk.CTkLabel(col_hdr, text=txt, width=w, anchor="w",
                             font=("Segoe UI", 9, "bold"), text_color=TEXT3).pack(side=side)

            # Rows
            for key, label, sv, dv, changed in visible:
                row_bg = CHANGED_BG if changed else SAME_BG
                row = ctk.CTkFrame(self._scroll, fg_color=row_bg, corner_radius=6, height=36)
                row.pack(fill="x", pady=2)
                row.pack_propagate(False)

                inner = ctk.CTkFrame(row, fg_color="transparent")
                inner.pack(fill="both", expand=True, padx=8)

                # Action label
                ctk.CTkLabel(inner, text=label, width=200, anchor="w",
                             font=("Segoe UI", 12), text_color=TEXT2).pack(side="left")

                # Source button chip
                self._chip(inner, sv).pack(side="left", padx=(0,8))

                # Arrow
                arrow = "→" if changed else "="
                ctk.CTkLabel(inner, text=arrow, width=24, anchor="center",
                             font=("Segoe UI", 14), text_color=TEXT3).pack(side="left")

                # Dest button chip
                self._chip(inner, dv).pack(side="left", padx=(8,0))

                # Changed badge
                if changed:
                    badge = ctk.CTkLabel(inner, text="changed",
                                         font=("Segoe UI", 9, "bold"),
                                         text_color=AMBER, fg_color="#2a1800",
                                         corner_radius=10)
                    badge.pack(side="right", ipadx=6, ipady=2)

    def _chip(self, parent, label):
        if label == "N/A":
            return ctk.CTkLabel(parent, text="N/A", width=120, anchor="w",
                                font=("Segoe UI", 11, "italic"), text_color=TEXT3,
                                fg_color="transparent")
        bg, fg = btn_style(label)
        return ctk.CTkLabel(parent, text=label, width=120, anchor="w",
                            font=("Segoe UI", 11, "bold"), text_color=fg,
                            fg_color=bg, corner_radius=10)


if __name__ == "__main__":
    App().mainloop()
