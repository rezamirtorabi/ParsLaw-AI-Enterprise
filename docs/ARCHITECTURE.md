# معماری اولیه

```text
UI (PySide6)
   |
Application Services
   |
Domain / Rules / Analysis
   |
Repositories
   |
SQLAlchemy
   |
SQLite (desktop) / PostgreSQL (future)
```

ماژول‌های AI و RAG از طریق interface جدا خواهند شد تا وابستگی به یک ارائه‌دهنده هوش مصنوعی ایجاد نشود.
