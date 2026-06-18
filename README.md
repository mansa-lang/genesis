# Mansa Genesis

> The Python bootstrap compiler that brought Mansa to life.

Genesis is **Stage 0** of the Mansa programming language — a Python-based
bootstrap compiler that takes Mansa from nothing to self-hosting. When
Mansa compiles itself for the first time, this repo is archived forever.

---

## What is Mansa?

Mansa is a systems programming language with Rust's memory safety,
near-ASM performance, and a syntax that gets out of your way.

Every design decision is measured against **PERFECT** — seven unbreakable
promises the language makes to every developer who uses it.

| Letter | Promise                                                 |
|--------|---------------------------------------------------------|
| **P**  | Productivity   — effortless to write and maintain       |
| **E**  | Efficiency     — zero-overhead, routinely beats C       |
| **R**  | Reliability    — memory safe, no UB in safe mode        |
| **F**  | Flexibility    — metaprogramming, multi-paradigm        |
| **E**  | Expressiveness — say more with less                     |
| **C**  | Correctness    — exhaustive types + formal verification |
| **T**  | Timeliness     — millisecond feedback, builds that fly  |

---

## Development Stack

- **Language:** Python 3.14+
- **Parser:** Lark (PEG Grammar)
- **Codegen:** llvmlite (LLVM IR)
- **Tests:** pytest
- **Target:** Linux x86_64 first, then `macOS` + `Windows`

---

## License

MIT — see [LICENSE](LICENSE)

When genesis is archived at v1.0, the production compiler continues at
[mansa-lang/mansa](https://github.com/mansa-lang/mansa) under Apache 2.0.

---

*Genesis ends when Mansa compiles itself. That's the whole point.*
