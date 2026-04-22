<!-- HEADER -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=120&section=header&animation=fadeIn" width="100%"/>

```
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   S A F A L   G U P T A                                          ║
║   Systems · AI Infrastructure · Quantitative Engineering         ║
║                                                                  ║
║   "I don't build features. I build the substrate others         ║
║    build features on."                                           ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&pause=1200&color=A78BFA&center=true&vCenter=true&width=700&lines=Systems+Engineer+%7C+AI+Infrastructure;Quant+Research+%7C+Low-Latency+Systems;Building+things+that+scale+to+the+edge+of+reason;VIT+Vellore+%E2%86%92+Next%3A+Jane+Street+%2F+DeepMind+%2F+Own+Fund" alt="Typing SVG" />
</a>

<br/>

[![Profile Views](https://komarev.com/ghpvc/?username=safalgupta&style=for-the-badge&color=7c3aed&labelColor=0d0d0d)]((https://github.com/alphasafal))
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-7c3aed?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0d0d0d)](https://www.linkedin.com/in/safal-gupta/)
[![Email](https://img.shields.io/badge/Email-Reach_Out-7c3aed?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0d0d0d)](mailto:safallovetocode@gmail.com)

</div>

---

## The Orientation

I am a third-year Computer Science student at VIT Vellore, building at the intersection of **AI systems**, **quantitative modeling**, and **high-performance infrastructure**. I do not chase frameworks — I study the mechanics beneath them.

My thinking is shaped by one constraint: **systems that work at 10x scale should have been designed that way from day one**. This forces a level of architectural clarity that most engineers never reach because they never need to.

I work on problems where the interesting part is not *what* to build — but *how* the underlying abstractions determine whether the thing survives contact with reality.

---

## Engineering Philosophy

> *Most engineers optimize for feature delivery. I optimize for the surface area of change — the fewer places a system has to be touched when requirements shift, the more correct its design was to begin with.*

Three principles I hold without compromise:

**1. Abstraction is a debt instrument.**
Every abstraction you introduce is a loan against future complexity. If you cannot name the exact invariant an abstraction preserves, you have not earned the right to introduce it.

**2. Latency is a design decision, not a performance problem.**
Systems that are slow were designed to be slow. By the time you are profiling, you have already lost. The bottleneck is architectural, and you should have seen it in the data flow diagram.

**3. Intelligence without interpretability is liability.**
An ML model in production that cannot be reasoned about under distribution shift is not an asset — it is a time bomb. I build systems where behavior is explainable by construction, not by post-hoc inspection.

---

## Active Research Interests

```
┌─────────────────────────────────────────────────────────────────┐
│  DOMAIN                   SPECIFIC QUESTION                      │
├─────────────────────────────────────────────────────────────────┤
│  Market Microstructure    When does order book imbalance carry   │
│                           predictive signal vs. noise injection? │
├─────────────────────────────────────────────────────────────────┤
│  ML Systems               How do you design serving infra for    │
│                           models with heterogeneous latency SLAs?│
├─────────────────────────────────────────────────────────────────┤
│  Distributed Systems      What is the minimal coordination cost  │
│                           for consensus in geo-distributed writes?│
├─────────────────────────────────────────────────────────────────┤
│  Reinforcement Learning   Can RL agents learn stable policies    │
│                           in non-stationary reward landscapes    │
│                           without reward model retraining?       │
└─────────────────────────────────────────────────────────────────┘
```

---

## High-Impact Projects

> Each project here solves a problem that was genuinely hard. The test I apply: *would removing any component of this system cause a non-obvious failure?* If no, the architecture is too shallow.

---

### `ARCA` — Adaptive Regime-Conditioned Allocation Engine
**[Status: Active Development]**

A quantitative portfolio management system that models market regimes as latent states and dynamically reweights allocation strategies based on real-time regime probability. Not a prediction model — a **decision engine** that degrades gracefully under uncertainty.

- Regime detection via Hidden Markov Models + online Bayesian updates
- Multi-strategy blending with Sharpe-normalized weights
- Execution layer with slippage modeling and transaction cost awareness
- Backtested on 10+ years of equity/futures data with walk-forward validation

`Python` `C++ (execution core)` `PyTorch` `Kafka` `TimescaleDB`

---

### `NEXUS` — Low-Latency ML Inference Router
**[Status: Design Phase]**

Production inference infrastructure that routes requests across heterogeneous model backends (GPU clusters, CPU inference, quantized edge models) based on real-time latency budgets and confidence thresholds. The insight: **not every request deserves a 70B parameter model**.

- Sub-millisecond routing decisions using a lightweight classifier
- Cascaded inference: fast model first, escalate on low-confidence
- gRPC-based inter-service communication with custom load balancing
- Observable by design: every routing decision is logged with reason

`Go` `C++` `ONNX Runtime` `gRPC` `Prometheus` `Kubernetes`

---

### `KIRA` — Kernel-Level Intrusion Response Agent
**[Status: Research Prototype]**

A behavioral anomaly detection system that instruments Linux kernel syscall traces to detect zero-day intrusions without signature databases. The model learns normal process behavior at the syscall graph level and flags structural deviations.

- eBPF-based syscall tracing with minimal overhead (< 2% CPU)
- Graph neural network on process interaction graphs
- Real-time alert generation with kill-chain attribution

`Rust` `eBPF` `PyTorch Geometric` `Linux Kernel` `Redis`

---

### `LOOM` — Distributed Feature Store for Online ML
**[Status: Open Source]**

A feature computation and serving platform designed for teams running ML models where **feature freshness directly impacts revenue**. Handles the hard problems: point-in-time correctness, backfilling, and online/offline consistency.

- Dual-write architecture for low-latency online serving and batch training
- Time-travel queries for reproducible training data
- Schema registry with backward-compatible evolution

`Python` `Apache Flink` `Redis` `PostgreSQL` `Avro`

---

## Technical Stack

```
SYSTEMS LAYER
├── Languages       C++17/20 · Rust · Go · Python 3.11+
├── Concurrency     POSIX Threads · Tokio · std::async
├── Networking      TCP/IP internals · gRPC · ZeroMQ · RDMA (learning)
└── OS              Linux (eBPF, cgroups, namespaces) · NUMA-aware design

AI / ML LAYER
├── Frameworks      PyTorch · JAX · scikit-learn
├── Serving         TorchServe · ONNX Runtime · TensorRT
├── Research        Transformers · RL (PPO, SAC) · GNNs · Bayesian methods
└── MLOps           MLflow · DVC · Weights & Biases

QUANT LAYER
├── Modeling        Time-series analysis · HMM · Stochastic processes
├── Execution       Order book modeling · Market impact · Slippage estimation
└── Backtesting     Walk-forward validation · Monte Carlo simulation

INFRASTRUCTURE LAYER
├── Cloud           AWS (EC2, EKS, SageMaker, Kinesis) · GCP (GKE)
├── Orchestration   Kubernetes · Terraform · Helm
├── Data            Kafka · Flink · TimescaleDB · Redis · S3
└── Observability   Prometheus · Grafana · OpenTelemetry
```

---

## GitHub Activity

<div align="center">

<img height="180em" src="https://github-readme-stats.vercel.app/api?username=safalgupta&show_icons=true&theme=midnight-purple&include_all_commits=true&count_private=true&hide_border=true&bg_color=0d0d0d&title_color=a78bfa&icon_color=7c3aed&text_color=c4b5fd"/>

<img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=safalgupta&layout=compact&theme=midnight-purple&hide_border=true&bg_color=0d0d0d&title_color=a78bfa&text_color=c4b5fd&langs_count=8"/>

</div>

<div align="center">

<img src="https://github-readme-streak-stats.herokuapp.com/?user=safalgupta&theme=midnight-purple&hide_border=true&background=0d0d0d&stroke=7c3aed&ring=a78bfa&fire=c4b5fd&currStreakLabel=a78bfa&sideNums=c4b5fd&sideLabels=7c3aed&dates=555555"/>

</div>

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=safalgupta&theme=react-dark&bg_color=0d0d0d&color=a78bfa&line=7c3aed&point=c4b5fd&hide_border=true"/>

</div>

---

## Principles of Work

I operate by a small set of non-negotiable standards that determine how I engage with any technical problem:

**Read the source, not the docs.**
Documentation describes intended behavior. Source code describes actual behavior. For anything that matters, I read the implementation.

**Benchmark before you claim.**
A performance claim without numbers is a story. I measure, plot, and question the measurement before I state it as fact.

**Design for the failure mode, not the happy path.**
The happy path is the least interesting thing about a system. The most important question in any design review is: *what does this look like when it breaks, and is that failure recoverable?*

**Finish what you start.**
A half-built system with clean architecture is worth less than a working system with rough edges. Shipping is a skill. Polish is a skill. The combination is rare.

---

## Currently

- Building `ARCA` — regime-conditioned allocation engine
- Reading: *Designing Data-Intensive Applications* (Kleppmann) · *The Elements of Statistical Learning* · Lamport's distributed systems papers
- Exploring: eBPF internals · JAX autodiff mechanics · FPGA basics for HFT pipelines
- Target: Research internship / quant role (Summer 2025) — open to conversations

---

## Contact

Reach me if you are working on something genuinely difficult in AI systems, quantitative research, or distributed infrastructure. I am not interested in adding features to CRUDs — I am interested in problems where the design space is not obvious.

`safal[at]domain.com` · [LinkedIn]((https://www.linkedin.com/in/safal-gupta/)) · [Twitter/X](https://x.com/safalgupta)

<br/>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=80&section=footer" width="100%"/>
</div>
