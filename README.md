# 🛒 Ecommerce Selenium Test Framework

This is a robust automation testing framework built using **Python**, **Selenium**, **unittest**, and **Page Object Model (POM)** design pattern. It tests key features of an e-commerce website and generates **detailed HTML reports** and **screenshots on failure**.

---

## 🚀 Features

- ✅ Python 3 + Selenium 4
- ✅ Structured using unittest framework
- ✅ Page Object Model for better maintainability
- ✅ HTML test reports with timestamps
- ✅ Automatic screenshots on test failure
- ✅ Cross-browser support ready (easy to extend)
- ✅ Shell script to run tests with one command

---

## 📁 Project Structure

ecommerce-selenium-test/
│
├── pages/ # Page classes (HomePage, ProductPage, etc.)
├── tests/ # Test cases using unittest
├── screenshots/ # Captured on failure
├── reports/ # HTML reports
│
├── run_tests.sh # Script to execute tests & generate report
├── requirements.txt # All dependencies
└── README.md # Project documentation


---

## 🧪 Sample Test Cases

- **Verify logo visibility** on homepage
- **Add product to cart** and verify the cart

---

## 📸 Reports & Screenshots

After running the tests, you’ll find:

- 📄 HTML reports inside `reports/`
- 🖼️ Screenshots (on failure) in `screenshots/`

---

## 🛠️ How to Run the Tests

Create Virtual Environment & Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Run Tests with Report

chmod +x run_tests.sh
./run_tests.sh



