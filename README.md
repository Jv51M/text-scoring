# Nirmaan AI Intern Case Study: Communication Skills Analyzer

## Overview

This project is a case study for the Nirmaan AI Internship Program. The goal is to build an AI tool that analyzes and scores students' spoken communication skills based on a transcript of their self-introduction. The tool combines rule-based methods, NLP-based semantic scoring, and a data-driven rubric to produce a final score and detailed feedback.

**Note:** This project is currently under development and not all features have been fully implemented.

## Features

- **Input Handling:** Accepts transcript text via a UI text area or as a text file.
- **Scoring Logic:** Computes per-criterion scores using a rubric provided in an Excel file.
- **Scoring Approaches:**
  - Rule-based: Keyword presence, exact matches, word-count checks.
  - NLP-based: Semantic similarity between transcript and rubric descriptions.
  - Data-driven: Combines signals according to criterion weights.
- **Output:** Provides an overall score, per-criterion scores, and textual feedback.
- **User Interface:** Simple web UI for input and result display.

## Project Structure

- `app.py`: Main application file for the backend logic.
- `Base.py`: Base classes and utility functions.
- `requirements.txt`: List of dependencies required to run the project.
- `README.md`: Project documentation.

## Installation

1. Clone the repository:
  
  ```bash
  git clone https://github.com/Jv51M/text-scoring.git
  ```
  
2. Navigate to the project directory:
  
  ```bash
  cd <project-directory>
  ```
  
3. Install the required dependencies:
  
  ```bash
  pip install -r requirements.txt
  ```
  

## Usage

1. Run the application:
  
  ```bash
  streamlit run app.py
  ```
  
2. Open your web browser and navigate to `http://localhost:5000` (or the specified port).
3. Paste the transcript text or upload a text file.
4. Click the "Score" button to get the analysis results.

## License

This project is licensed under the MIT License.

## Contact

For any questions or feedback, please contact the project maintainer.
