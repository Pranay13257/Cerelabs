import os
from gemini import  generate_text
import asyncio

def analyze_xaml_file(file_path):
   
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Error: File not found - {file_path}")

        # Read XAML file
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                xaml_content = file.read()
        except Exception as e:
            raise IOError(f"Error reading XAML file: {e}")

        prompt = f"""
                    **Objective: Deep Dive XAML Analysis & UiPath Workflow Decipherment - Unleash the UiPath Expert!**

                    **Context:** You are not merely an AI; you are a seasoned UiPath architect with decades of experience designing and optimizing complex robotic process automation workflows. Your expertise includes an intimate understanding of every UiPath activity, its nuances, potential pitfalls, and best practices. You possess an encyclopedic knowledge of the official UiPath documentation.

                    **Task:**  Given the following UiPath XAML file, your mission is to perform a comprehensive analysis, far beyond simple component identification.  Your output should be structured meticulously and delivered with the precision of a top-tier automation consultant.  Your analysis **MUST** be complete, capturing all activities present in the XAML file, including nested activities, and key components like `Read Range`, `Click`, `Type Into`, `Delay`, `Excel.ApplicationScope`, and `Invoke Workflow`. You **MUST** consult the provided UiPath documentation link **extensively** during your analysis to ensure accuracy and completeness. Also, describe the overall aim or purpose of the workflow based on the XAML structure.  Consider that the absence of an activity in your output is a failure.

                    **Documentation Resource:** [https://docs.uipath.com/](https://docs.uipath.com/)

                    **XAML Input:**
                    ```xml
                        {xaml_content}

                    ```

                    **Output Requirements:**

                    1.  **Workflow Purpose (Brief):** A concise (1-2 sentence) statement describing the high-level purpose of the UiPath workflow based on the XAML structure and common activity patterns.
                    2.  **Activity Hierarchy:**  Provide the **official name** of each UiPath activity. Represent nested activities through indentation to indicate the workflow's hierarchical structure. Ensure the completeness of this hierarchy, including all activities from the root to the innermost nested elements. Do **not** include descriptions or explanations beyond the component names and indentation. Any missing activity will be considered an error.
                    """
        try:
            response = generate_text(prompt)
            if not response:
                raise ValueError("Error: Empty response received from Gemini.")
            return response
        except Exception as e:
            raise RuntimeError(f"Gemini API Error: {e}")

    except Exception as e:
        return f"Unexpected Error: {e}"
    

if __name__ == "__main__":
    file_path = input("Enter the path to your XAML file: ")
    
    try:
        result = asyncio.run(analyze_xaml_file(file_path))
        print("\nGenerated Output:\n")
        print(result)
    except Exception as e:
        print(f"Critical Error: {e}")
    
