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
| **P**  | **Productivity:** effortless to write and maintain      |
| **E**  | **Efficiency:** zero-overhead, routinely beats C        |
| **R**  | **Reliability:** memory safe, no UB in safe mode        |
| **F**  | **Flexibility:** metaprogramming, multi-paradigm        |
| **E**  | **Expressiveness:** say more with less                  |
| **C**  | **Correctness:** exhaustive types + formal verification |
| **T**  | **Timeliness:** millisecond feedback, builds that fly   |

See [Issue #2](https://github.com/mansa-lang/genesis/issues/2) for the full living definition of **PERFECT**

---

## Roadmap

Genesis exists to complete three stages then disappear.

| Stage       | Description                              | Status         |
|-------------|------------------------------------------|----------------|
| **Stage 0** | Python bootstrap — genesis               | 🔨 In progress |
| **Stage 1** | Rewrite compiler in Mansa                | ⏳ Pending     |
| **Stage 2** | Self-hosting — Python gone               | ⏳ Pending     |
| **v0.1**    | Genesis archived, mansa-lang/mansa opens | ⏳ Pending     |

---

### Version milestones

| Version | Name      | Milestone                       |
|---------|-----------|---------------------------------|
| v0.0.1  | Spark     | Lexer + parser exist            |
| v0.0.2  | Kindling  | Real code compiles              |
| v0.0.3  | Shape     | Type system working             |
| v0.0.4  | Ownership | Memory safety enters (MOM)      |
| v0.0.5  | Survive   | Error handling + collections    |
| v0.0.6  | Iron      | Native binaries ship            |
| v0.0.7  | Proven    | Stage 0 complete                |
| v0.0.8  | Mirror    | Compiler rewrites itself        |
| v0.0.9  | Resolve   | Resolver + typechecker in Mansa |
| v0.0.10 | Emit      | Full rewrite complete           |
| v0.0.11 | Ouroboros | Self-hosting achieved           |
| v0.0.12 | Hardened  | Production internals            |
| v0.1.0  | Genesis   | **This repo is archived**       |

---

## Development Stack

| Name          | Value                                        |
|---------------|----------------------------------------------|
| **Language:** | Python 3.15+                                 |
| **Parser:**   | Lark (PEG Grammar)                           |
| **Codegen:**  | llvmlite (LLVM IR)                           |
| **Tests:**    | pytest                                       |
| **Target:**   | Linux x86_64 first, then `macOS` + `Windows` |

---

## Repository structure

```dir
genesis/
  grammar/        # Mansa PEG grammar definition
  src/            # compiler source
  tests/          # test suite
  docs/           # language reference + design notes
  examples/       # example Mansa programs
  stdlib/         # Mansa standard library (Python stage)
```

---

## License

MIT — see [LICENSE](LICENSE)

When genesis is archived at v1.0, the production compiler continues at
[mansa-lang/mansa](https://github.com/mansa-lang/mansa) under Apache 2.0.

---

*Genesis ends when Mansa compiles itself. That's the whole point.*
