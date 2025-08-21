# 🎓 Batch Certificate Maker

This project is a Python-based tool designed to automate the process of generating personalized certificates in bulk.

---

## 🚀 Features

### Core Scripts
* **`main.py`**: The primary script that reads data, applies a design template, and generates individual certificates.
* **`convert.py`**: A utility to merge all generated `.png` certificates into a single `.pdf` file.

### Helper Utilities
* **`decapitalize.py`**: A script to convert names in your CSV file from all caps to standard capitalization.
* **`compare.py`**: A tool for comparing two CSV files to ensure data consistency and accuracy before generation.

---

## 📂 Project Structure

The project directory is organized as follows:

```
.
├── main.py
├── decapitalize.py
├── compare.py
├── convert.py
├── requirements.txt
├── data.csv
├── input/
│   └── design.png
├── font/
│   └── font.ttf
└── output/
```

- **`data.csv`**: Contains the names and other details for each certificate.
- **`input/`**: Holds your certificate template (`design.png`).
- **`font/`**: Stores the font file (`font.ttf`) used for text on the certificates.
- **`output/`**: The destination directory for all generated certificates.

---

## 🛠️ Getting Started

### Installation
1.  Clone the repository and navigate into the project directory:
    ```bash
    git clone [https://github.com/wakhidrf/Batch-Certificate-Maker](https://github.com/wakhidrf/Batch-Certificate-Maker)
    cd Batch-Certificate-Maker
    ```
2.  Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

### Usage
1.  **Prepare your files**: Place `data.csv` in the root directory, your certificate template (`design.png`) in the `input` folder, and your font file (`font.ttf`) in the `font` folder.
2.  **Generate certificates**:
    ```bash
    python main.py
    ```
3.  **Convert to PDF** (optional):
    ```bash
    python convert.py
    ```
4.  **Helper scripts** (optional):
    -   To clean up names in `data.csv`:
        ```bash
        python decapitalize.py
        ```
    -   To compare two CSV files for quality control:
        ```bash
        python compare.py
        ```

---

## 🤝 Contributing

We welcome contributions! Please feel free to fork the repository and submit a pull request.