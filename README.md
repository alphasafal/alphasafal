<img src="assets/hero.svg" alt="Safal Gupta: merged pull requests into upstream open-source projects" width="100%"/>

<p align="center">
  <a href="https://safalgupta.tech">Portfolio</a> ·
  <a href="https://linkedin.com/in/safal-gupta">LinkedIn</a> ·
  <a href="https://x.com/safallovetocode">X</a> ·
  <a href="https://hackerrank.com/profile/safallovetocode">HackerRank</a>
</p>

Final-year B.Tech CSE at VIT Vellore. I like systems where correctness and the
tail latency matter, and I measure before I claim.

### Main project: [exchange-core](https://github.com/alphasafal/exchange-core)

A C++20 exchange core: a price-time order book, pre-trade risk with a kill
switch, a write-ahead journal with deterministic replay, and a binary protocol.

- **75 ns** per command in process, **zero allocations** on the matching path
  (enforced by a test), and cost flat from 10 to 5,000 price levels.
- Against [Liquibook](https://github.com/alphasafal/exchange-core/blob/main/docs/comparison.md)
  on the same workload: submits are a draw, and cancel p99 is **286 ns vs
  95 µs**, because Liquibook scans the price level.
- Correctness is checked against a reference model, three fuzzers, ASan, UBSan
  and TSan, and a replay digest. 398 tests, 12 CI jobs.
- Clients can resend an order after a crash without it executing twice. A
  death test kills the venue between the journal write and the ack to prove it
  ([ADR 0004](https://github.com/alphasafal/exchange-core/blob/main/docs/adr/0004-increasing-order-ids.md)).
- [Try it in the browser](https://alphasafal.github.io/exchange-core/) (WebAssembly) ·
  [design decisions](https://github.com/alphasafal/exchange-core#design-decisions) ·
  [the benchmark bug I found in my own numbers](https://github.com/alphasafal/exchange-core/blob/main/docs/comparison.md#a-correction-to-the-original-benchmark)

### Also building

| | |
|---|---|
| **[CONTRI](https://github.com/alphasafal/contri)** | Chrome extension and MCP server. It answers three questions about a GitHub repo: is it alive, do maintainers reply, and is this issue already claimed? |
| **[VAJRA](https://github.com/alphasafal/vajra)** | Static malware triage. It analyses a suspicious file without running it and explains each verdict. |
| **[AI Eval Engineering](https://github.com/alphasafal/ai-eval-engineering)** | A TypeScript harness for testing prompts and agents: deterministic graders, trajectory metrics, cost and latency, release gates. |
| **[Production Agent Skills](https://github.com/alphasafal/production-agent-skills)** | 15 skills for AI coding agents, with behavioural evals. |

### Upstream

Merged fixes in projects I use. The list below refreshes daily from the GitHub API.

<img src="assets/merged.svg" alt="Merged upstream pull requests, refreshed daily from the GitHub API" width="100%"/>

<sub>[Open PRs →](https://github.com/pulls?q=is%3Apr+author%3Aalphasafal+is%3Aopen)</sub>

<details>
<summary><b>Hackathon, hiring-challenge and side builds</b> (built in days; the challenge entries are archived)</summary>

| | |
|---|---|
| [Lastseat](https://github.com/alphasafal/lastseat) | Team formation where 50 people race for the last seat and exactly one gets it. Hack4Hack 2026. |
| [Virtual KAM](https://github.com/alphasafal/snapdeal-virtual-kam) | Voice account manager for Snapdeal sellers, in English, Hindi and Hinglish. Snapdeal take-home. |
| [Udyam Setu](https://github.com/alphasafal/udyam-setu) | MSME digital onboarding prototype. Airtel SYNC case challenge. |
| [TwinPilot](https://github.com/alphasafal/twinpilot) | AI agents optimising an EnergyPlus building model behind a safety shield. Eco-Loop hackathon. |
| [MemoryMate](https://github.com/alphasafal/memorymate) | Offline voice task assistant built on whisper.cpp and llama.cpp. Hackathon, 2025. |
| [Python for Planet 365](https://github.com/alphasafal/python-for-planet-365) | A 365-day Python and sustainability curriculum. Day 1 done; paused. |
| [GitRishta](https://github.com/alphasafal/gitrishta) | Your GitHub profile as an Indian shaadi biodata. A weekend joke. |

</details>
