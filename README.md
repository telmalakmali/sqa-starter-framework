# 🚀 Lean QA Starter Kit for Software Startups (Minimal Framework)

## 📌 Overview
Startups move fast. Speed is the priority. But when QA is skipped or kept informal, teams often face bugs, unstable releases, technical debt, and communication gaps as the product grows.

This repository provides a **lightweight QA starter kit** to introduce **basic structure** without slowing development.  
It is intentionally **minimal for now**, with **room for growth** as the team and product mature.

---

## ✨ What’s Included

### 🐍 1) Python Automation Scripts
- 🔍 **Repository Change Tracker**
  - Tracks changes in a target repository (latest commit vs stored reference)
  - Outputs a list of changed files so testing can focus on impacted areas

- ✅ **Entry & Exit Criteria Generator**
  - Generates an editable QA workbook (Excel) with:
    - 🧾 Summary tab (release info + sign-off fields)
    - 🚦 Entry Criteria (Dev readiness + QA readiness)
    - 🏁 Exit Criteria (QA completion checks before release)

---

### 📄 2) QA Templates
- 📝 **Test Plan Template**
  - Lightweight planning structure (scope, risks, assumptions, environments, schedule)

- 🧪 **Test Audit / QA Maturity Checklist Template**
  - Simple checklist for QA process self-review and continuous improvement

---

### 🧩 3) Process Visualisation
- 🗺️ **UML Activity Diagram**
  - High-level QA workflow showing change awareness → readiness → testing → release decision

---

## 🎯 Why This Kit Exists
This kit supports startups shifting from:
- ⚡ **Ad-hoc testing → Repeatable checks**
- 🤷 **Unclear readiness → Clear entry/exit gates**
- 🔥 **Reactive QA → Lightweight governance**

It is not an enterprise-heavy QA system.  
It is a **“start small, scale later”** approach.

---

## 🗂️ Recommended Folder Structure (Optional)
You can keep the repository organised like this:

startup-qa-kit/
├── automation/
│ ├── change_tracker.py
│ └── criteria_generator.py
├── templates/
│ ├── test_plan_template.docx
│ └── test_audit_checklist.xlsx
├── diagrams/
│ └── qa_workflow_uml.png
└── README.md



---

# ⚙️ How to Use (Quick Steps)
1. 📥 Clone this repository  
2. 🔑 Configure the change tracker script:
   - Target repository name
   - Branch name
   - GitHub token (recommended via GitHub Actions secret)
3. ▶️ Run scripts locally **or** integrate into CI
4. 📌 Use templates and checklists as your starting QA foundation

---

## 🚫 What’s Not Included (By Design)
This kit does **not** include company-specific checklists (for example: smoke testing, feature testing, or regression checklists) because those often depend heavily on the product and internal workflow.

✅ However, **generic versions of those templates can be added later** as the kit grows.

---

# 🛣️ Future Improvements (Growth Ideas)
This kit is minimal, but it has room for a lot of growth. Possible next steps:

- 🧾 Add a **Requirements Traceability Matrix (RTM)** template  
  *(Requirement → Test Case → Coverage → Status)*

- 📊 Add basic quality metrics:
  - coverage %
  - pass rate
  - defect trend tracking

- 🧰 Add more QA templates:
  - generic smoke checklist
  - generic feature checklist
  - generic regression checklist

- 🔗 Integrate free / lightweight tooling (optional):
  - ⚙️ GitHub Actions improvements (reporting + validation)
  - 🧹 Linters / static checks (e.g., ruff, flake8)
  - 🧪 Unit test setup (e.g., pytest)
  - 🧾 Simple CI summaries (markdown reports)

---

# 🤝 Contribution / Reuse
This repository is designed as a **starter framework**. Anyone can:
- 🔧 fine-tune the scripts
- 📄 add new templates
- 🧠 improve the framework
- 🚀 adapt it for their own startup QA process

If you extend it, try to keep the same principle:
✅ **simple, lightweight, scalable**

---

## 👤 Author
**Telma Lakmali**  
📍 Auckland, New Zealand  
🔗 GitHub: https://github.com/telmalakmali/sqa-starter-framework 
🔗 LinkedIn: https://www.linkedin.com/in/telma-lakmali-qalife999/

---

## 📜 License
Choose one:
- ✅ MIT License (common for open sharing)
- ✅ Apache 2.0 (also common)
- 🔒 Or keep private / unlicensed if you prefer

