<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00F7FF,100:7B2FFF&height=220&section=header&text=Lalith%20Krish&fontSize=55&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Daily%20LeetCode%20Grinder%20%7C%20Java%20%7C%20DSA&descAlignY=55&descSize=18" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=26&pause=1000&color=00F7FF&center=true&vCenter=true&width=650&lines=Solving+1+Problem+a+Day;Building+Strong+DSA+Foundations;Consistency+%3E+Motivation;Java+%7C+Data+Structures+%7C+Algorithms" alt="Typing SVG" />

<br/>

![Profile Views](https://komarev.com/ghpvc/?username=Lalithkrish06&color=00F7FF&style=for-the-badge&label=PROFILE+VIEWS)
![Repo Stars](https://img.shields.io/github/stars/Lalithkrish06/leetcode-solutions?color=FFD700&style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/Lalithkrish06/leetcode-solutions?color=00e676&style=for-the-badge)
![Made with Java](https://img.shields.io/badge/MADE%20WITH-JAVA-orange?style=for-the-badge&logo=openjdk)

</div>

<br/>

## 🧠 About This Repository

This is my personal **LeetCode problem-solving journal** — every problem I solve, every pattern I learn, and every mistake I fix, tracked here.

> 🎯 **Goal:** Solve at least 1 problem a day, master core DSA patterns, and stay interview-ready.

Everything below — the chart, the streak, the snake — **updates itself automatically** through GitHub Actions. Solve a problem, log it, push. That's it.

<br/>

## 📊 LeetCode Stats

<div align="center">
<img src="https://leetcode-stats-card.vercel.app/api?username=LALITH_KRISH&theme=dark&border_radius=10&background=0d1117" alt="LeetCode Stats" />
</div>

> ⚠️ Swap `LALITH_KRISH` for your **exact** LeetCode username (check `leetcode.com/u/your-exact-id/` — no spaces allowed).

<br/>

## 📈 Auto-Visualized Daily Progress

<div align="center">
<img src="assets/progress_chart.png" alt="Daily Solve Progress Chart" width="750"/>
<br/>
<sub>🔄 Regenerated every day at 00:00 UTC by <code>.github/workflows/update-stats.yml</code></sub>
</div>

This chart isn't static — `scripts/generate_stats.py` reads `data/solved.json`, rebuilds a cumulative-solves + difficulty-breakdown chart, and commits it straight back to the repo. Nothing to touch by hand.

<br/>

## 🐍 Contribution Snake (Live Animation)

<div align="center">
<img src="https://raw.githubusercontent.com/Lalithkrish06/leetcode-solutions/output/github-contribution-grid-snake.svg" alt="Contribution Snake" width="100%"/>
</div>

Your GitHub contribution graph, eaten by an animated snake, regenerated daily by `.github/workflows/snake.yml`. Purely cosmetic, purely satisfying.

<br/>

## 🔥 Current Streak

<div align="center">
<img src="https://streak-stats.demolab.com?user=Lalithkrish06&theme=dark&border_radius=10&background=0D1117&ring=00F7FF&fire=FFD700&currStreakLabel=00F7FF" alt="Streak Stats"/>
</div>

<br/>

## 🏆 GitHub Trophies

<div align="center">
<img src="https://github-profile-trophy.vercel.app/?username=Lalithkrish06&theme=darkhub&no-frame=true&column=7&margin-w=8&margin-h=8" alt="Trophies"/>
</div>

<br/>

## 🗂️ Problems Solved

| # | Problem | Difficulty | Category | Language | Solution |
|---|---------|------------|----------|----------|----------|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | 🟢 Easy | Array / HashMap | Java | [Solution](./solutions/0001-two-sum/) |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | 🟡 Medium | Linked List | Java | [Solution](./solutions/0002-add-two-numbers/) |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | 🟢 Easy | Stack | Java | [Solution](./solutions/0020-valid-parentheses/) |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | 🟢 Easy | Array / DP | Java | [Solution](./solutions/0121-best-time-to-buy-and-sell-stock/) |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | 🟡 Medium | Sliding Window | Java | [Solution](./solutions/0003-longest-substring/) |

> 📌 Add a new row every time you solve a problem — or fold the log straight into `data/solved.json` and let the automation handle the rest.

<br/>

## 📁 Repository Structure

```
leetcode-solutions/
├── solutions/
│   ├── 0001-two-sum/
│   │   ├── Solution.java
│   │   └── notes.md
│   └── 0002-add-two-numbers/
│       ├── Solution.java
│       └── notes.md
├── data/
│   └── solved.json               # log of every problem solved (date, id, difficulty)
├── scripts/
│   └── generate_stats.py         # builds the progress chart
├── assets/
│   └── progress_chart.png        # auto-generated, don't edit by hand
├── .github/
│   └── workflows/
│       ├── update-stats.yml      # daily chart automation
│       └── snake.yml             # daily contribution-snake animation
└── README.md
```

<br/>

## 🛠️ Tech Stack

<div align="center">

![Java](https://img.shields.io/badge/-Java-007396?style=for-the-badge&logo=openjdk&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/-GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Python](https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/-Git-F05032?style=for-the-badge&logo=git&logoColor=white)

</div>

<br/>

## ⚙️ How the Automation Works

1. Solve a problem → add one line to `data/solved.json`:
   ```json
   { "date": "2026-07-26", "id": 5, "title": "Longest Palindromic Substring", "difficulty": "Medium" }
   ```
2. Push (or wait — both workflows also run on a daily schedule).
3. `update-stats.yml` runs `generate_stats.py`, rebuilds `assets/progress_chart.png`, commits it back.
4. `snake.yml` regenerates the contribution snake SVG on an `output` branch and commits it back.
5. The README always reflects the **latest** state automatically.

<br/>

## 🤝 Connect

<div align="center">

[![GitHub](https://img.shields.io/badge/-Lalithkrish06-181717?style=for-the-badge&logo=github)](https://github.com/Lalithkrish06)
[![LeetCode](https://img.shields.io/badge/-LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/LALITH_KRISH/)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7B2FFF,100:00F7FF&height=120&section=footer" width="100%"/>

<div align="center">
<sub>⭐ If this repo motivates your own daily-solve journey, consider starring it!</sub>
</div>
