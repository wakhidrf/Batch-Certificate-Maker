# 🎓 College Batch Certificate Maker

This project is a Python-based tool designed to automate the process of generating personalized certificates for a college batch. It uses a data file to create individual certificates, ensuring a smooth and efficient workflow.

---

## 🚀 Features

* **`main.py`**: The core script for generating certificates. It reads data, applies a design, and outputs finished certificates.
* **`decapitalize.py`**: A helper script to convert names in your CSV file from all caps to standard capitalization.
* **`compare.py`**: A utility for comparing two CSV files to ensure data accuracy before certificate generation.
* **`convert.py`**: A script to convert the generated `.png` certificates into a single `.pdf` file.

---

## 📂 Project Structure

Your project directory should be set up as follows:

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


* **`data.csv`**: Contains the names and other details for each certificate.
* **`input/design.png`**: The background image or template for your certificates.
* **`font/font.ttf`**: The font file used for writing text on the certificates.
* **`output/`**: The directory where all generated certificates will be saved.

---

## 🛠️ Installation

1.  Clone this repository:

    ```bash
    git clone [https://github.com/your-username/your-project-name.git](https://github.com/your-username/your-project-name.git)
    cd your-project-name
    ```

2.  Install the necessary Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

---

## 🏃 Usage

### 1. Preparing Your Files

* Make sure your **`data.csv`** file is in the root directory.
* Place your certificate template, **`design.png`**, in the `input` folder.
* Place your font file, **`font.ttf`**, in the `font` folder.

### 2. Running the Scripts

* **Generate Certificates**:

    ```bash
    python main.py
    ```

* **Decapitalize Names**:
    Use this if your names in `data.csv` are in all caps.

    ```bash
    python decapitalize.py
    ```

* **Compare Data**:
    Use this to compare two CSVs for quality control.

    ```bash
    python compare.py
    ```

* **Convert to PDF**:
    This will convert all `.png` files in the `output` folder into a single PDF.

    ```bash
    python convert.py
    ```

---

## 📜 Requirements

The project dependencies are listed in `requirements.txt`. Make sure to install them before running any of the scripts.

---

## 👨‍💻 Contributing

If you'd like to contribute, please feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.