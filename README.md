# 🚀 Python API Automation Framework – Reqres API

This is a complete API automation framework built using modern Python tools and structured for professional use.

---

## ✅ Tech Stack

- 🧪 **Pytest** – lightweight test runner
- 🔗 **Requests** – HTTP client library
- 📊 **Allure** – advanced test reporting
- 🧬 **Pydantic** – response schema validation
- 🔒 **python-dotenv** – environment config
- 🔁 **pytest-rerunfailures** – auto-retries for flaky tests
- 🌐 **GitHub Actions** – CI/CD pipeline

---

## 📁 Folder Structure

```
api-automation-framework/
├── .github/workflows/         # CI configuration
├── config/                    # Environment variables
├── reports/                   # HTML & Allure reports
├── tests/                     # Test suites: unit, e2e, advanced
├── utils/                     # API client, schema models
├── requirements.txt
├── pytest.ini
├── README.md
└── .env
```

---

## 🧩 Supported Test Types

| Category     | Description                               |
|--------------|-------------------------------------------|
| `@smoke`     | Quick validation tests                    |
| `@regression`| Functional coverage tests                 |
| `@advanced`  | Auth, schema, retry-based flows           |
| `@e2e`       | Full user lifecycle tests                 |

---

## 🧪 Sample Test: Create User

```python
@pytest.mark.regression
def test_create_user():
    payload = {"name": "morpheus", "job": "leader"}
    response = client.post("/users", json=payload)
    assert response.status_code == 201
    parsed = CreateUserResponse(**response.json())
    assert parsed.name == "morpheus"
```

---

## ✅ Sample E2E Test

```python
@pytest.mark.e2e
def test_user_lifecycle():
    # Create ➝ Login ➝ Update ➝ Delete
    ...
```

This simulates a full lifecycle of a user, suitable for real-world workflows.

---

## 🔁 Allure + HTML Reports

- All tests generate Allure results in `reports/allure-results`:
  ```bash
  allure serve reports/allure-results
  ```

- Also generates self-contained HTML:
  ```bash
  open reports/report.html
  ```

---

## ☁️ GitHub Actions CI

- Automatically runs on push/PR to `main`
- Staged execution: `smoke → regression → advanced → e2e`
- Retry logic for advanced tests
- Allure reports uploaded as build artifacts

---

## 📦 Setup Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Add environment config
`config/.env`:
```
BASE_URL=https://reqres.in/api
```

### 3. Run tests locally
```bash
pytest
```

---

## 🏁 Test by category
```bash
pytest -m smoke
pytest -m regression
pytest -m advanced
pytest -m e2e
pytest -m auth
```

---

> ⭐ Star this repository if you find it helpful to kickstart your API testing portfolio.
