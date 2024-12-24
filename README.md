
# Filesize Guard

**Filesize Guard** is a lightweight GitHub Action designed to prevent bloating your repository or downloadable app size by introducing large assets. It ensures assets exceeding a specified size limit are flagged, encouraging optimization or offloading to a CDN.

---

## 🚀 Features
- Prevents large assets from being unintentionally added to the repository.
- Configurable size limit (default: 100 kB).
- Supports `.gitignore`-like syntax to exclude specific files or directories.

---

## 🛠️ Usage

### 1. **Create an Ignore File**
Add a `filesize_guard.ignore` file to the root of your repository to define patterns for files or directories to exclude from size checks. The syntax follows `.gitignore` conventions.

**Example `filesize_guard.ignore`:**
```gitignore
test/*
logs/*
*.log
```

---

### 2. **Add the GitHub Action**
Create a GitHub Actions workflow in `.github/workflows/filesize_guard.yml`:

```yaml
name: Filesize Guard
on:
  pull_request:
    branches:
      - master
  workflow_dispatch:

jobs:
  filesize_guard:
    runs-on: ubuntu-latest
    steps:
      - name: Filesize Guard
        uses: chris-rutkowski/filesize-guard@v1.0.0
```

---

## ⚙️ Configuration

### **Change the File Size Limit**
By default, the file size limit is set to **100 kB**. You can customize this by passing the `max_size_kb` input:

```yaml
steps:
  - name: Filesize Guard
    uses: chris-rutkowski/filesize-guard@v1.0.0
      with:
        max_size_kb: 50
```

### **Specify a Custom Ignore File Path**
If your `filesize_guard.ignore` file is not in the root directory, specify its location using the `ignore_file` input:

```yaml
steps:
  - name: Filesize Guard
    uses: chris-rutkowski/filesize-guard@v1.0.0
      with:
        ignore_file: ./my/path/my_filesize_guard.ignore
```

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).
