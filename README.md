# CV and Cover Letter Tailoring System

This project provides an automated system to tailor your CV and cover letter based on job descriptions using OpenAI's API. The system analyzes your existing documents and the job description, then generates customized versions that highlight relevant skills and experiences.

## Project Structure

```
cv_tailoring_project/
├── data/                   # Directory for storing CV and cover letter templates
│   ├── Cover Letter.docx
│   └── Resume_Template_ATS.docx
├── notebooks/              # Jupyter notebooks for interactive usage
│   └── cv_tailoring_system.ipynb
├── output/                 # Directory for storing generated documents
├── src/                    # Source code
│   ├── parsers/            # Document parsing modules
│   │   └── document_parser.py
│   ├── updaters/           # Document updating modules
│   │   └── document_updater.py
│   └── utils/              # Utility modules
│       └── openai_integration.py
└── README.md               # Project documentation
```

## Features

- Parse and analyze Word document CV and cover letter templates
- Extract sections, personal information, and content structure
- Analyze job descriptions using OpenAI's API
- Generate tailored CV with updated profile summary, skills, and experience highlights
- Create customized cover letter that addresses specific job requirements
- Interactive Jupyter notebook interface for easy usage
- Support for batch processing multiple job applications

## Requirements

- Python 3.6+
- python-docx
- openai
- Jupyter Notebook/Lab
- OpenAI API key

## Getting Started

1. Clone this repository or download the project files
2. Install the required dependencies:
   ```
   pip install python-docx openai jupyter
   ```
3. Place your CV and cover letter templates in the `data` directory
4. Launch the Jupyter notebook:
   ```
   jupyter notebook notebooks/cv_tailoring_system.ipynb
   ```
5. Follow the step-by-step instructions in the notebook
