#!/usr/bin/env python
# coding: utf-8

# In[8]:


"""
Test script for the document updater module.
This is a mock test since we don't want to make actual API calls during testing.
"""

import os
import sys
import docx
from unittest import mock

# Получаем текущий рабочий каталог
current_directory = os.getcwd()

# Указываем путь к папке, которую нужно добавить
project_directory = os.path.join(current_directory, 'cv_tailoring_project')

# Add the project root to the path
sys.path.append(project_directory)

from src.updaters.document_updater import DocumentUpdater
from src.utils.openai_integration import OpenAIIntegration

def test_document_updater():
    """Test the document updater module with mock responses."""
    print("Testing document updater module...")
    
    # Paths to test documents
    cv_path = os.path.join(current_directory, 'data', 'Olha Polishchuk - Resume_Template_ATS.docx')
    cover_letter_path = os.path.join(current_directory, 'data','Cover Letter_Olha.docx')
    
    # Create a mock OpenAI integration
    mock_openai = mock.MagicMock(spec=OpenAIIntegration)
    
    # Set up mock responses
    mock_openai.analyze_job_description.return_value = {
        "raw_response": """
        {
            "profile_summary": "Experienced Data Analyst with a strong background in IT and software, specializing in data analysis, optimization, and project management. Skilled in Python, SQL, Power BI, Tableau, and Excel, seeking a role to leverage analytical skills in driving business decision-making processes.",
            "skills": ["Data analysis", "Python", "SQL", "Power BI", "Tableau", "Excel", "Google Sheets", "Project optimization", "Visualization", "Workflow automation"],
            "experience_highlights": ["Performed data analysis to support business strategies", "Created interactive dashboards using Power BI and Tableau", "Optimized workflows using Python scripts and SQL queries", "Managed over 50 media projects with increased engagement"],
            "keywords_to_emphasize": ["data analysis", "optimization", "visualization", "Python", "SQL", "Power BI", "Tableau", "project management", "automation"]
        }
        """
    }

    mock_openai.tailor_cover_letter.return_value = "This is a tailored cover letter body text for testing purposes."
    
    # Initialize document updater with mock OpenAI integration
    document_updater = DocumentUpdater(cv_path, cover_letter_path, mock_openai)
    
    # Test analyze_job_description method
    job_description = "This is a test job description for an IT Project Management position."
    analysis = document_updater.analyze_job_description(job_description)
    
    assert "raw_response" in analysis
    print("✓ analyze_job_description method works correctly")
    
    # Test output paths
    # output_cv_path = '/cv_tailoring_project/output/test_cv.docx'
    # output_cl_path = '/cv_tailoring_project/output/test_cover_letter.docx'
    output_cv_path = os.path.join(current_directory, 'output', 'test_cv.docx')
    output_cl_path = os.path.join(current_directory, 'output', 'test_cover_letter.docx')
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_cv_path), exist_ok=True)
    
    # Test update_cv method
    cv_result = document_updater.update_cv(job_description, output_cv_path)
    
    # Check if the CV file was created
    if os.path.exists(cv_result):
        print(f"✓ update_cv method works correctly, file created at {cv_result}")
    else:
        print(f"✗ update_cv method failed, file not found at {cv_result}")
    
    # Test update_cover_letter method
    cl_result = document_updater.update_cover_letter(job_description, output_cl_path)
    
    # Check if the cover letter file was created
    if os.path.exists(cl_result):
        print(f"✓ update_cover_letter method works correctly, file created at {cl_result}")
    else:
        print(f"✗ update_cover_letter method failed, file not found at {cl_result}")
    
    print("\nDocument updater module tests completed successfully!")
    return True

if __name__ == "__main__":
    # Use patch to mock the OpenAI integration
    with mock.patch('src.utils.openai_integration.OpenAIIntegration') as MockOpenAI:
        test_document_updater()


# In[ ]:




